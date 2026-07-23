import pyunihan.parsers
import bisect
import re
import argparse
from pathlib import Path
import os
import logging
import sqlite3
import sys
import zipfile

import requests

from pyunihan.datatypes import Basic, Numeric, IRG_Source, Complex, Entry
from pyunihan.utils import usv_to_integer, bisect_index, find_unihan_files
from pyunihan import properties
from pyunihan import parsers


class Database:
    def __init__(self, args=None):
        self.args = args
        self.tables = {}
        self.character_codes = []
        try:
            self.data_dir = Path(os.environ["XDG_DATA_HOME"]) / "pyunihan"
        except KeyError:
            self.data_dir = Path.home() / ".local/share/pyunihan"
        if not self.data_dir.exists():
            os.makedirs(self.data_dir)
        self.logger = logging.getLogger(__name__)
        if self.args:
            self.setup_logger()

    def property_category(self, property_name, report_unknown=False):
        try:
            return properties.properties[property_name]
        except KeyError:
            if report_unknown:
                self.logger.warning("Unknown property: %s", property_name)
            return Basic()

    def create_table_statement(self, table_name):
        # table_name = self.table_name
        reg = re.compile("(.*)Table")
        column_name = reg.match(table_name).group(1)
        report_unknown = table_name != "utf8Table"
        category = self.property_category(column_name, report_unknown)
        column_type = "integer" if isinstance(category, Numeric) else "text"
        statement = (
            f"CREATE TABLE {table_name} (code integer NOT NULL, "
            f"{column_name} {column_type} NOT NULL, "
            "PRIMARY KEY (code));"
        )
        if isinstance(category, Basic):
            return statement
        if isinstance(category, Complex):
            columns = ", ".join(
                [
                    f"{c.name} {c.column_type}{c.nullable_string()}"
                    for c in category.columns
                ]
            )
            primary_key_components = ", ".join(
                [c.name for c in category.columns if c.primary_key_component]
            )
            statement = (
                f"CREATE TABLE {table_name} ( {columns}, "
                f"PRIMARY KEY ( {primary_key_components} ))"
            )
            return statement

    def create_index_statement(self, table_name):
        # TODO
        pass

    def read_unihan_files(self):
        unihan_dir_path = self.args.unihan_dir_path.expanduser()
        filenames = [
            unihan_dir_path / name for name in find_unihan_files(unihan_dir_path)
        ]
        line_count = 0
        for filename in filenames:
            with open(filename, "r") as file:
                self.logger.info("Reading %s", filename.absolute())
                lines = file.readlines()
                [self.process_entry(line.strip()) for line in lines]
                line_count += len(lines)
        self.logger.debug("%d lines read.", line_count)
        self.tables.update(
            {"utf8Table": [[code, chr(code)] for code in self.character_codes]}
        )

    def insertions(self, entry):
        if isinstance(entry.category, Complex):
            parser = entry.category.parser_function
        elif isinstance(entry.category, IRG_Source):
            parser = parsers.kIRG_source_parser
        else:
            parser = parsers.basic_parser
        insertions = parser(entry)
        return insertions

    def process_entry(self, line):
        if not line:
            return
        if line.startswith("#"):
            return
        unicode_scalar_value, property_name, value = line.split("\t")
        code = usv_to_integer(unicode_scalar_value)
        entry = Entry(code, property_name, value, self)
        try:
            bisect_index(self.character_codes, entry.code)
        except ValueError:
            bisect.insort(self.character_codes, entry.code)
        # insertions = entry.insertions()
        insertions = self.insertions(entry)
        for insertion in insertions:
            try:
                self.tables[insertion.table_name].append(insertion.values)
            except KeyError:
                self.tables.update({insertion.table_name: [insertion.values]})

    def build_sqlite(self):
        database_file = self.args.database_file.expanduser()
        if self.args.rebuild:
            os.remove(database_file)
        self.logger.info("Building database at %s", database_file.absolute())
        con = sqlite3.connect(database_file)
        cur = con.cursor()
        for table_name in self.tables:
            self.logger.debug("Creating table %s.", table_name)
            create_table_statement = self.create_table_statement(table_name)
            cur.execute(create_table_statement)
            qmarks = ", ".join("?" * len(self.tables[table_name][0]))
            self.logger.debug(
                "Inserting %d values into %s.", len(self.tables[table_name]), table_name
            )
            cur.executemany(
                f"INSERT INTO {table_name} VALUES({qmarks})", self.tables[table_name]
            )
        con.commit()
        con.close()

    def setup_logger(self):
        self.logger.setLevel(logging.DEBUG)
        console_handler = logging.StreamHandler()
        self.logger.addHandler(console_handler)
        file_handler = logging.FileHandler(
            self.data_dir / "pyunihan.log", mode="a", encoding="utf-8"
        )
        self.logger.addHandler(file_handler)
        formatter = logging.Formatter(
            "{asctime} {levelname}: {message}", style="{", datefmt="%Y-%m-%d %H:%M"
        )
        file_handler.setFormatter(formatter)
        formatter = logging.Formatter(
            "{levelname}: {message}", style="{", datefmt="%Y-%m-%d %H:%M"
        )
        console_handler.setFormatter(formatter)
        console_handler.setLevel(self.args.log_level)
        file_handler.setLevel("DEBUG")

    def download_unihan_zip(self):
        url = "https://unicode.org/Public/UNIDATA/Unihan.zip"
        zip_path = self.args.unihan_zip_path.expanduser()
        self.logger.info("Downloading Unihan.zip.")
        response = requests.get(url)
        with open(zip_path, "wb") as file:
            file.write(response.content)

    def extract_unihan_zip(self):
        zip_path = self.args.unihan_zip_path.expanduser()
        zip_file = zipfile.ZipFile(zip_path)
        dir_file = self.args.unihan_dir_path.expanduser()
        self.logger.info("Extracting %s to %s.", zip_path, dir_file)
        zip_file.extractall(self.args.unihan_dir_path.expanduser())

    def prepare_files(self):
        database_file = self.args.database_file.expanduser()
        if database_file.exists() and not self.args.rebuild:
            self.logger.critical("%s already exists.", database_file.absolute())
            self.logger.critical("Use --rebuild to rebuild.")
            sys.exit()
        if not database_file.parent.exists():
            self.logger.critical("%s does not exist.", database_file.parent.absolute())
            sys.exit()
        dir_path = self.args.unihan_dir_path.expanduser()
        if dir_path.parent == self.data_dir and not dir_path.exists():
            os.mkdir(dir_path)
        if not dir_path.exists():
            self.logger.critical("%s does not exist.", dir_path.absolute())
            sys.exit()
        else:
            unihan_files = find_unihan_files(dir_path)
            if unihan_files:
                self.logger.debug(
                    "Files found in dir %s: %s", dir_path.absolute(), unihan_files
                )
                return
            self.logger.debug("No `Unihan*.txt` files found in %s", dir_path.absolute())
        zip_file = self.args.unihan_zip_path.expanduser()
        if not zip_file.parent.exists():
            self.logger.critical("%s does not exist.", zip_file.parent.absolute())
            sys.exit()
        if zip_file.exists():
            self.extract_unihan_zip()
        else:
            self.download_unihan_zip()
            self.extract_unihan_zip()


def argument_parser():
    project_name = "pyunihan"
    parser = argparse.ArgumentParser()
    try:
        data_dir = Path(os.environ["XDG_DATA_HOME"]) / project_name
    except KeyError:
        data_dir = Path.home() / f".local/share/{project_name}"
    parser.add_argument("--unihan-zip-path", type=Path, default=data_dir / "Unihan.zip")
    parser.add_argument("--unihan-dir-path", type=Path, default=data_dir / "Unihan")
    parser.add_argument("--database-file", type=Path, default=data_dir / "Unihan.db")
    parser.add_argument(
        "--rebuild", action=argparse.BooleanOptionalAction, default=False
    )
    parser.add_argument(
        "--log-level",
        type=str,
        default="INFO",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
    )
    return parser


def main():
    argparser = argument_parser()
    args = argparser.parse_args()
    database = Database(args)
    database.prepare_files()
    # [database.process_entry(e) for e in TEST_ENTRIES]
    database.read_unihan_files()
    database.build_sqlite()
    # [print(s) for s in database.create_table_statements]
    # print(json.dumps(database.tables, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
