import re
import bisect
import os


def usv_to_integer(usv):
    reg = re.compile(r"U\+([23]?[0-9A-F]{4})")
    return int(reg.match(usv).group(1), 16)


def bisect_index(sorted_list, item):
    """Return the index of `item` in `sorted_list` with a binary search."""
    index = bisect.bisect_left(sorted_list, item)
    if index != len(sorted_list) and sorted_list[index] == item:
        return index
    raise ValueError


def hanyu_da_zidian_values(string):
    reg = re.compile(r"(\d)(\d+)\.(\d\d)(\d)")
    match = reg.match(string)
    volume = int(match.group(1))
    page = int(match.group(2))
    ideograph = int(match.group(3))
    virtual = int(match.group(4))
    return [volume, page, ideograph, virtual]


def find_unihan_files(dir_path):
    files = os.listdir(dir_path)
    reg = re.compile(r"Unihan.*\.txt")
    filtered = filter(lambda f: reg.match(f), files)
    return list(filtered)
