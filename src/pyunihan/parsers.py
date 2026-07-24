import re

from pyunihan.datatypes import Numeric, Insertion
from pyunihan import utils


def basic_parser(entry):
    if isinstance(entry.category, Numeric):
        value = int(entry.value)
    else:
        value = entry.value
    return [Insertion(entry.table_name, [entry.code, value])]


def variant_parser(entry):
    variants = entry.value.split(" ")
    return [
        Insertion(entry.table_name, [entry.code, utils.usv_to_integer(variant)])
        for variant in variants
    ]


def string_splitter(entry):
    values = entry.value.split(" ")
    return [
        Insertion(entry.table_name, [entry.code, value, index + 1])
        for index, value in enumerate(values)
    ]


def integer_splitter(entry):
    values = entry.value.split(" ")
    return [Insertion(entry.table_name, [entry.code, value]) for value in values]


def row_cell_parser(entry):
    reg = re.compile(r"(\d\d)(\d\d)")
    match = reg.match(entry.value)
    values = [entry.code, int(match.group(1)), int(match.group(2))]
    return [Insertion(entry.table_name, values)]


def page_position_parser(entry):
    parts = entry.value.split(" ")
    insertions = []
    reg = re.compile(r"(\d+)\.(\d+)")
    for part in parts:
        match = reg.match(part)
        page = int(match.group(1))
        position = int(match.group(2))
        insertions.append(Insertion(entry.table_name, [entry.code, page, position]))
    return insertions


def hexadecimal_parser(entry):
    mapping = int(entry.value, 16)
    values = [entry.code, mapping]
    return [Insertion(entry.table_name, values)]


def kCNS_parser(entry):
    reg = re.compile(r"(\w+)-(\w\w)(\w\w)")
    match = reg.match(entry.value)
    set_number = int(match.group(1), 16)
    row_number = int(match.group(2), 16)
    column_number = int(match.group(3), 16)
    values = [entry.code, set_number, row_number, column_number]
    return [Insertion(entry.table_name, values)]


def kCowles_parser(entry):
    parts = entry.value.split(" ")
    insertions = []
    for part in parts:
        int_and_fractional = part.split(".")
        if len(int_and_fractional) == 1:
            values = [entry.code, int(int_and_fractional[0]), 0]
        else:
            values = [
                entry.code,
                int(int_and_fractional[0]),
                int(int_and_fractional[1]),
            ]
        insertions.append(Insertion(entry.table_name, values))
    return insertions


def kAlternateTotalStrokes_parser(entry):
    if entry.value == "-":
        values = [entry.code, None, None]
        return [Insertion(entry.table_name, values)]
    reg = re.compile(r"(\d+):(\w+)")
    match = reg.match(entry.value)
    values = [entry.code, int(match.group(1)), match.group(2)]
    return [Insertion(entry.table_name, values)]


def kCheungBauer_parser(entry):
    radical_stroke, cangjie, readings = entry.value.split(";")
    reg = re.compile(r"(\d+)/(\d+)")
    match = reg.match(radical_stroke)
    radical = int(match.group(1))
    stroke = int(match.group(2))
    readings = readings.split(",")
    insertions = [
        Insertion(entry.table_name, [entry.code, radical, stroke, cangjie, r])
        for r in readings
    ]
    return insertions


def kCihaiT_parser(entry):
    parts = entry.value.split(" ")
    insertions = []
    reg = re.compile(r"(\d+)\.(\d)(\d+)")
    for part in parts:
        match = reg.match(part)
        page = int(match.group(1))
        row = int(match.group(2))
        position_on_row = int(match.group(3))
        values = [entry.code, page, row, position_on_row]
        insertions.append(Insertion(entry.table_name, values))
    return insertions


def kDaeJaweon_parser(entry):
    reg = re.compile(r"(\d+)\.(\d\d)(\d)")
    match = reg.match(entry.value)
    page = int(match.group(1))
    position = int(match.group(2))
    virtual = int(match.group(3))
    values = [entry.code, page, position, virtual]
    return [Insertion(entry.table_name, values)]


def kFanqie_parser(entry):
    parts = entry.value.split(" ")
    insertions = []
    reg = re.compile("(.)(.)")
    for part in parts:
        match = reg.match(part)
        onset = match.group(1)
        final = match.group(2)
        values = [entry.code, onset, final]
        insertions.append(Insertion(entry.table_name, values))
    return insertions


def kFenn_parser(entry):
    parts = entry.value.split(" ")
    insertions = []
    reg = re.compile(r"(\d+)(.)")
    for part in parts:
        match = reg.match(part)
        soothill_number = int(match.group(1))
        final_char = match.group(2)
        phonetic = 1 if final_char == "P" else 0
        present = 1 if final_char != "*" else 0
        if (not phonetic) and present:
            frequency_indication = final_char
        else:
            frequency_indication = None
        values = [entry.code, soothill_number, frequency_indication, phonetic, present]
        insertions.append(Insertion(entry.table_name, values))
    return insertions


def kFennIndex_parser(entry):
    parts = entry.value.split(" ")
    reg = re.compile(r"(\d+)\.(\d+)")
    insertions = []
    for part in parts:
        match = reg.match(part)
        page = int(match.group(1))
        position = int(match.group(2))
        values = [entry.code, page, position]
        insertions.append(Insertion(entry.table_name, values))
    return insertions


def kFourCornerCode_parser(entry):
    parts = entry.value.split(" ")
    reg = re.compile(r"(\d+)(\.(\d))?")
    insertions = []
    for part in parts:
        match = reg.match(part)
        four_corner_code = match.group(1)
        if match.group(3):
            fifth_digit = match.group(3)
        else:
            fifth_digit = None
        values = [entry.code, four_corner_code, fifth_digit]
        insertions.append(Insertion(entry.table_name, values))
    return insertions


def kGSR_parser(entry):
    parts = entry.value.split(" ")
    reg = re.compile(r"(\d+)(\w'?)")
    insertions = []
    for part in parts:
        match = reg.match(part)
        set_number = match.group(1)
        entry_label = match.group(2)
        values = [entry.code, set_number, entry_label]
        insertions.append(Insertion(entry.table_name, values))
    return insertions


def kHangul_parser(entry):
    parts = entry.value.split(" ")
    reg = re.compile(r"(.+):(.+)")
    insertions = []
    for part in parts:
        match = reg.match(part)
        hangul = match.group(1)
        source = match.group(2)
        values = [entry.code, hangul, source]
        insertions.append(Insertion(entry.table_name, values))
    return insertions


def kHanYu_parser(entry):
    parts = entry.value.split(" ")
    insertions = []
    for part in parts:
        values = [entry.code] + utils.hanyu_da_zidian_values(part)
        insertions.append(Insertion(entry.table_name, values))
    return insertions


def kHanyuPinlu_parser(entry):
    parts = entry.value.split(" ")
    reg = re.compile(r"(\w+)\((\d+)\)")
    all_values = []
    insertions = []
    for part in parts:
        match = reg.match(part)
        values = [entry.code, match.group(1), int(match.group(2))]
        if values not in all_values:
            all_values.append(values)
            insertions.append(Insertion(entry.table_name, values))
    return insertions


def kHanyuPinyin_parser(entry):
    parts = entry.value.split(" ")
    insertions = []
    for part in parts:
        locations, readings = part.split(":")
        locations = locations.split(",")
        readings = readings.split(",")
        for location in locations:
            location_values = utils.hanyu_da_zidian_values(location)
            for index, reading in enumerate(readings):
                values = [entry.code] + location_values + [reading, index + 1]
                insertions.append(Insertion(entry.table_name, values))
    return insertions


def kHDZRadBreak_parser(entry):
    reg = re.compile(r"(.)\[(.*)\]:(.+)")
    match = reg.match(entry.value)
    radical = match.group(1)
    usv = match.group(2)
    position = match.group(3)
    radical_code = utils.usv_to_integer(usv)
    position_values = utils.hanyu_da_zidian_values(position)
    values = [entry.code, radical, radical_code] + position_values
    return [Insertion(entry.table_name, values)]


def kIICore_parser(entry):
    priority_value = entry.value[0]
    irg_source_specifier = entry.value[1:]
    return [
        Insertion(entry.table_name, [entry.code, priority_value, irg_source_specifier])
    ]


def kIRG_source_parser(entry):
    source_name, source_mapping = entry.value.split("-")
    values = [entry.code, source_name, source_mapping]
    return [Insertion("IRG_SourceMappingTable", values)]


def kKangXi_parser(entry):
    parts = entry.value.split(" ")
    reg = re.compile(r"(\d+)\.(\d\d)(\d)")
    insertions = []
    for part in parts:
        match = reg.match(part)
        page = match.group(1)
        position = match.group(2)
        virtual = match.group(3)
        values = [entry.code, page, position, virtual]
        insertions.append(Insertion(entry.table_name, values))
    return insertions


def kJinmeiyoKanji_parser(entry):
    reg = re.compile(r"(\d+)(:(.+))?")
    match = reg.match(entry.value)
    year = int(match.group(1))
    if match.group(3):
        standard_form_code = utils.usv_to_integer(match.group(3))
    else:
        standard_form_code = None
    values = [entry.code, year, standard_form_code]
    return [Insertion(entry.table_name, values)]


def kJIS0213_parser(entry):
    reg = re.compile(r"(\d+),(\d+),(\d+)")
    match = reg.match(entry.value)
    plane = int(match.group(1))
    row = int(match.group(2))
    cell = int(match.group(3))
    values = [entry.code, plane, row, cell]
    return [Insertion(entry.table_name, values)]


def kJoyoKanji_parser(entry):
    if entry.value.startswith("U"):
        year = None
        variant_code = utils.usv_to_integer(entry.value)
    else:
        year = int(entry.value)
        variant_code = None
    values = [entry.code, year, variant_code]
    return [Insertion(entry.table_name, values)]


def kKarlgren_parser(entry):
    reg = re.compile(r"(\w+)(\*?)")
    match = reg.match(entry.value)
    index = match.group(1)
    interpolated = 1 if match.group(2) else 0
    values = [entry.code, index, interpolated]
    return [Insertion(entry.table_name, values)]


def kMandarin_parser(entry):
    # The third value is a BCP 47 language tag.
    # https://developer.mozilla.org/en-US/docs/Glossary/BCP_47_language_tag
    readings = entry.value.split(" ")
    if len(readings) == 1:
        values = [entry.code, readings[0], "zh"]
        return [Insertion(entry.table_name, values)]
    insertions = []
    tags = ["zh-Hans-CN", "zh-Hant-TW"]
    for reading, tag in zip(readings, tags):
        values = [entry.code, reading, tag]
        insertions.append(Insertion(entry.table_name, values))
    return insertions


def kMojiJoho_parser(entry):
    parts = entry.value.split(" ")
    reg = re.compile(r"(MJ\d+)(:(.*))?")
    insertions = []
    for part in parts:
        match = reg.match(part)
        serial_number = match.group(1)
        variation_selector = match.group(3)
        values = [entry.code, serial_number, variation_selector]
        insertions.append(Insertion(entry.table_name, values))
    return insertions


def kMorohashi_parser(entry):
    parts = entry.value.split(" ")
    reg = re.compile(r"(\w+)(:(.+))?")
    insertions = []
    for part in parts:
        match = reg.match(part)
        index_number = match.group(1)
        variation_selector = match.group(3)
        values = [entry.code, index_number, variation_selector]
        insertions.append(Insertion(entry.table_name, values))
    return insertions


def kPhonetic_parser(entry):
    parts = entry.value.split(" ")
    reg = re.compile(r"(\d+)([A-D]?)(\*?)")
    insertions = []
    for part in parts:
        match = reg.match(part)
        phonetic_class = int(match.group(1))
        subsidiary_class = match.group(2)
        explicitly_included = 0 if match.group(3) else 1
        values = [entry.code, phonetic_class, subsidiary_class, explicitly_included]
        insertions.append(Insertion(entry.table_name, values))
    return insertions


def kPrimaryNumeric_parser(entry):
    parts = entry.value.split(" ")
    return [
        Insertion(entry.table_name, [entry.code, int(part), index + 1])
        for index, part in enumerate(parts)
    ]


def kRSAdobe_Japan1_6_parser(entry):
    parts = entry.value.split(" ")
    reg = re.compile(r"(C|V)\+(\d+)\+(\d+)\.(\d+)\.(\d+)")
    insertions = []
    for part in parts:
        match = reg.match(part)
        variant = 1 if match.group(1) == "V" else 0
        cid = int(match.group(2))
        kangxi_radical_number = int(match.group(3))
        strokes_in_radical = int(match.group(4))
        strokes_in_residue = int(match.group(5))
        values = [
            entry.code,
            variant,
            cid,
            kangxi_radical_number,
            strokes_in_radical,
            strokes_in_residue,
        ]
        insertions.append(Insertion(entry.table_name, values))
    return insertions


def kRSUnicode_parser(entry):
    parts = entry.value.split(" ")
    reg = re.compile(r"(\d+)('*)\.(-?\d+)")
    insertions = []
    for part in parts:
        match = reg.match(part)
        radical_number = int(match.group(1))
        apostrophes = match.group(2)
        zh_simp = 1 if len(apostrophes) == 1 else 0
        non_zh_simp = 1 if len(apostrophes) == 2 else 0
        second_non_zh_simp = 1 if len(apostrophes) == 3 else 0
        additional_strokes = int(match.group(3))
        values = [
            entry.code,
            radical_number,
            additional_strokes,
            zh_simp,
            non_zh_simp,
            second_non_zh_simp,
        ]
        insertions.append(Insertion(entry.table_name, values))
    return insertions


def kSBGY_parser(entry):
    parts = entry.value.split(" ")
    reg = re.compile(r"(\d+)\.(\d+)")
    insertions = []
    for part in parts:
        match = reg.match(part)
        page = int(match.group(1))
        number = int(match.group(2))
        values = [entry.code, page, number]
        insertions.append(Insertion(entry.table_name, values))
    return insertions


def kSemanticVariant_parser(entry):
    parts = entry.value.split(" ")
    reg = re.compile(r"(U\+[0-9A-F]+)(<(.+))?")
    insertions = []
    for part in parts:
        match = reg.match(part)
        usv = utils.usv_to_integer(match.group(1))
        if not match.group(3):
            values = [entry.code, usv, None, 0, 0, 0, 0, 0]
            insertions.append(Insertion(entry.table_name, values))
            continue
        sources = match.group(3).split(",")
        for source in sources:
            new_reg = re.compile(r"(\w+)(:(\w+))?")
            new_match = new_reg.match(source)
            name = new_match.group(1)
            tbzfj = str(new_match.group(3))
            same = 1 if "T" in tbzfj else 0
            improper = 1 if "B" in tbzfj else 0
            preferred = 1 if "Z" in tbzfj else 0
            traditional = 1 if "F" in tbzfj else 0
            simplified = 1 if "J" in tbzfj else 0
            values = [
                entry.code,
                usv,
                name,
                same,
                improper,
                preferred,
                traditional,
                simplified,
            ]
            insertions.append(Insertion(entry.table_name, values))
    return insertions


def kSMSZD2003Readings_parser(entry):
    parts = entry.value.split(" ")
    reg = re.compile(r"(.+)粵(.+)")
    insertions = []
    for def_index, part in enumerate(parts):
        match = reg.match(part)
        m_readings = match.group(1).split(",")
        c_readings = match.group(2).split(",")
        if len(m_readings) > len(c_readings):
            c_readings *= len(m_readings)
        elif len(c_readings) > len(m_readings):
            m_readings *= len(c_readings)
        for read_index, (m_reading, c_reading) in enumerate(
            zip(m_readings, c_readings)
        ):
            values = [entry.code, m_reading, c_reading, def_index + 1, read_index + 1]
            insertions.append(Insertion(entry.table_name, values))
    return insertions


def kStrange_parser(entry):
    parts = entry.value.split(" ")
    insertions = []
    for part in parts:
        letter, *rest = part.split(":")
        if letter == "S":
            values = [entry.code, int(rest[0])]
            insertions.append(Insertion("kStrange_strokesTable", values))
            continue
        if not rest:
            values = [entry.code, letter, None]
            insertions.append(Insertion(entry.table_name, values))
        for usv in rest:
            ref_code = utils.usv_to_integer(usv)
            values = [entry.code, letter, ref_code]
            insertions.append(Insertion(entry.table_name, values))
    return insertions


def kTang_parser(entry):
    parts = entry.value.split(" ")
    reg = re.compile(r"(\*)?(.+)")
    insertions = []
    for part in parts:
        match = reg.match(part)
        frequent = 1 if match.group(1) else 0
        reading = match.group(2)
        values = [entry.code, reading, frequent]
        insertions.append(Insertion(entry.table_name, values))
    return insertions


def kTGH_parser(entry):
    year, index_number = entry.value.split(":")
    values = [entry.code, int(year), int(index_number)]
    return [Insertion(entry.table_name, values)]


def kTGHZ2013_parser(entry):
    parts = entry.value.split(" ")
    insertions = []
    for part in parts:
        locations, reading = part.split(":")
        for location in locations.split(","):
            reg = re.compile(r"(\d\d\d)\.(\d\d)(\d)")
            match = reg.match(location)
            page = int(match.group(1))
            position = int(match.group(2))
            entry_type = int(match.group(3))
            values = [entry.code, page, position, entry_type, reading]
            insertions.append(Insertion(entry.table_name, values))
    return insertions


def kXerox_parser(entry):
    char_set_code, char_8_code = entry.value.split(":")
    values = [entry.code, int(char_set_code, 8), int(char_8_code, 8)]
    return [Insertion(entry.table_name, values)]


def kXHC1983_parser(entry):
    parts = entry.value.split(" ")
    insertions = []
    for index, part in enumerate(parts):
        locations, reading = part.split(":")
        for location in locations.split(","):
            reg = re.compile(r"(\d\d\d\d).(\d\d)(\d)(\*)?")
            match = reg.match(location)
            page = int(match.group(1))
            position = int(match.group(2))
            entry_type = int(match.group(3))
            unifiable_variant = 1 if match.group(4) else 0
            values = [
                entry.code,
                page,
                position,
                entry_type,
                unifiable_variant,
                reading,
                index + 1,
            ]
            insertions.append(Insertion(entry.table_name, values))
    return insertions


def kZhuang_parser(entry):
    reg = re.compile(r"(\w+)(\*)?")
    match = reg.match(entry.value)
    reading = match.group(1)
    standard = 0 if match.group(2) else 1
    values = [entry.code, reading, standard]
    return [Insertion(entry.table_name, values)]
