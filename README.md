# pyunihan

pyunihan is a Python program that converts the Unicode Consortium's Unihan database from its native text format to SQLite. 

It exposes the command-line tool `unihan`, which by default downloads [Unihan.zip](https://unicode.org/Public/UNIDATA/Unihan.zip) from the UNIDATA repository, unzips it, and reads and parses the files it contains to create an SQLite database with a set of tables corresponding to the Unihan properties described in [Unicode® Standard Annex #38](https://www.unicode.org/reports/tr38/index.html).

## Installation

You can install this package with `pip` or [`uv`](https://docs.astral.sh/uv/). Use the following steps:

1. `git clone https://github.com/sandbach/pyunihan`
2. `cd pyunihan`
3. `pipx .` or `uvx .`

## Usage

Use the shell command `unihan`.

By default, pyunihan stores all its files at [`$XDG_DATA_HOME`](https://specifications.freedesktop.org/basedir/latest/)`/pyunihan`. You can select different directories with arguments to `unihan`. Run `unihan --help` to see the available options.
