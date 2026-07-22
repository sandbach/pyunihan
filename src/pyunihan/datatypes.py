from collections.abc import Callable
from dataclasses import dataclass


@dataclass
class Basic:
    pass


# @dataclass
# class Variant(Basic):
#     pass


@dataclass
class Numeric(Basic):
    pass


@dataclass
class IRG_Source:
    pass


@dataclass
class Complex:
    columns: list
    parser_function: Callable


@dataclass
class Column:
    def __init__(self, name, column_type, nullable=False, primary_key_component=False):
        self.name = name
        self.column_type = column_type
        self.nullable = nullable
        self.primary_key_component = primary_key_component

    def nullable_string(self):
        if not self.nullable:
            return " NOT NULL"
        return ""


@dataclass
class Insertion:
    table_name: str
    values: list


@dataclass
class Entry:
    def __init__(self, code, property_name, value, database):
        self.code = code
        self.property_name = property_name
        self.value = value
        self.database = database
        self.category = self.database.property_category(self.property_name)
        self.table_name = f"{self.property_name}Table"
