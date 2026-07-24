# pyunihan

pyunihan is a Python program that converts the Unicode Consortium's Unihan database from its native text format to SQLite. 

It exposes the command-line tool `unihan`, which by default downloads [Unihan.zip](https://unicode.org/Public/UNIDATA/Unihan.zip) from the UNIDATA repository, unzips it, and reads and parses the files it contains to create an SQLite database with a set of tables corresponding to the Unihan properties described in [Unicode® Standard Annex #38](https://www.unicode.org/reports/tr38/index.html).

pyunihan has similar aims to [libUnihan](https://libunihan.sourceforge.net/index.html) and takes inspiration from it. pyunihan has the following advantages:

- It supports the most recent version of the Unihan database (Unicode 17.0.0).
- In the event of new properties being introduced in future versions of Unihan, it should be able to provide rudimentary support without changes to the source code.
- The design of the program is such that parser functions can be added or amended relatively simply.
- It is easy to install.

The documentation file [parsers.md](./docs/parsers.md) provides further information about parser functions with more complex behaviour.

## Installation

You can install this package with `pip` or [`uv`](https://docs.astral.sh/uv/). Use the following steps:

1. `git clone https://github.com/sandbach/pyunihan`
2. `cd pyunihan`
3. `pipx .` or `uvx .`

## Usage

Use the shell command `unihan`.

By default, pyunihan stores all its files at [`$XDG_DATA_HOME`](https://specifications.freedesktop.org/basedir/latest/)`/pyunihan`. You can select different directories for `Unihan.zip`, the extracted files, etc., with arguments to `unihan`. Run `unihan --help` to see the available options.
