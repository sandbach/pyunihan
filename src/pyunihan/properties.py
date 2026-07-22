from pyunihan.datatypes import Basic, Numeric, Complex, Column
from pyunihan import parsers

properties = {
    "kAccountingNumeric": Numeric(),
    "kAlternateTotalStrokes": Complex(
        [
            Column("code", "integer", primary_key_component=True),
            Column("kAlternateTotalStrokes", "integer", nullable=True),
            Column("IRGSourceSpecifier", "text", nullable=True),
        ],
        parsers.kAlternateTotalStrokes_parser,
    ),
    "kBigFive": Basic(),
    "kCangjie": Basic(),
    "kCantonese": Basic(),
    "kCCCII": Basic(),
    "kCheungBauer": Complex(
        [
            Column("code", "integer", primary_key_component=True),
            Column("kangxiRadicalNumber", "integer", primary_key_component=True),
            Column("strokeCount", "integer", primary_key_component=True),
            Column("cangjie", "text", nullable=True),
            Column("cantoneseReading", "text", primary_key_component=True),
        ],
        parsers.kCheungBauer_parser,
    ),
    "kCheungBauerIndex": Complex(
        [
            Column("code", "integer", primary_key_component=True),
            Column("pageNumber", "integer", primary_key_component=True),
            Column("positionNumber", "integer", primary_key_component=True),
        ],
        parsers.page_position_parser,
    ),
    "kCihaiT": Complex(
        [
            Column("code", "integer", primary_key_component=True),
            Column("pageNumber", "integer", primary_key_component=True),
            Column("rowNumber", "integer", primary_key_component=True),
            Column("positionOnRow", "integer", primary_key_component=True),
        ],
        parsers.kCihaiT_parser,
    ),
    "kCNS1986": Basic(),
    "kCNS1992": Basic(),
    "kCompatibilityVariant": Complex(
        [
            Column("code", "integer", primary_key_component=True),
            Column("variantCode", "integer"),
        ],
        parsers.variant_parser,
    ),
    "kCowles": Basic(),
    "kDaeJaweon": Complex(
        [
            Column("code", "integer", primary_key_component=True),
            Column("pageNumber", "integer", primary_key_component=True),
            Column("positionNumber", "integer", primary_key_component=True),
            Column("virtual", "integer", primary_key_component=True),
        ],
        parsers.kDaeJaweon_parser,
    ),
    "kDefinition": Basic(),
    "kEACC": Basic(),
    "kFanqie": Complex(
        [
            Column("code", "integer", primary_key_component=True),
            Column("onsetCharacter", "text", primary_key_component=True),
            Column("finalCharacter", "text", primary_key_component=True),
        ],
        parsers.kFanqie_parser,
    ),
    "kFenn": Complex(
        [
            Column("code", "integer", primary_key_component=True),
            Column("soothillNumber", "integer", primary_key_component=True),
            Column(
                "frequencyIndication", "text", primary_key_component=True, nullable=True
            ),
            Column("phonetic", "integer"),
            Column("present", "integer"),
        ],
        parsers.kFenn_parser,
    ),
    "kFennIndex": Complex(
        [
            Column("code", "integer", primary_key_component=True),
            Column("pageNumber", "integer", primary_key_component=True),
            Column("positionNumber", "integer", primary_key_component=True),
        ],
        parsers.kFennIndex_parser,
    ),
    "kFourCornerCode": Complex(
        [
            Column("code", "integer", primary_key_component=True),
            Column("fourCornerCode", "text", primary_key_component=True),
            Column("fifthDigit", "integer", primary_key_component=True, nullable=True),
        ],
        parsers.kFourCornerCode_parser,
    ),
    "kGB0": Basic(),
    "kGB1": Basic(),
    "kGB3": Basic(),
    "kGB5": Basic(),
    "kGB8": Basic(),
    "kGradeLevel": Numeric(),
    "kGSR": Complex(
        [
            Column("code", "integer", primary_key_component=True),
            Column("setNumber", "integer", primary_key_component=True),
            Column("entryLabel", "text", primary_key_component=True),
        ],
        parsers.kGSR_parser,
    ),
    "kHangul": Complex(
        [
            Column("code", "integer", primary_key_component=True),
            Column("hangul", "text", primary_key_component=True),
            Column("source", "text", primary_key_component=True),
        ],
        parsers.kHangul_parser,
    ),
    "kHanYu": Complex(
        [
            Column("code", "integer", primary_key_component=True),
            Column("volumeNumber", "integer", primary_key_component=True),
            Column("pageNumber", "integer", primary_key_component=True),
            Column("ideographNumber", "integer", primary_key_component=True),
            Column("virtual", "integer", primary_key_component=True),
        ],
        parsers.kHanYu_parser,
    ),
    "kHanyuPinlu": Complex(
        [
            Column("code", "integer", primary_key_component=True),
            Column("pinyin", "text", primary_key_component=True),
            Column("frequency", "integer"),
        ],
        parsers.kHanyuPinlu_parser,
    ),
    "kHanyuPinyin": Complex(
        [
            Column("code", "integer", primary_key_component=True),
            Column("volumeNumber", "integer", primary_key_component=True),
            Column("pageNumber", "integer", primary_key_component=True),
            Column("ideographNumber", "integer", primary_key_component=True),
            Column("virtual", "integer", primary_key_component=True),
            Column("pinyin", "text", primary_key_component=True),
            Column("priority", "integer", primary_key_component=True),
        ],
        parsers.kHanyuPinyin_parser,
    ),
    "kHDZRadBreak": Complex(
        [
            Column("code", "integer", primary_key_component=True),
            Column("radical", "text"),
            Column("radicalCode", "integer"),
            Column("volumeNumber", "integer", primary_key_component=True),
            Column("pageNumber", "integer", primary_key_component=True),
            Column("ideographNumber", "integer", primary_key_component=True),
            Column("virtual", "integer", primary_key_component=True),
        ],
        parsers.kHDZRadBreak_parser,
    ),
    "kHKGlyph": Numeric(),
    "kIBMJapan": Basic(),
    "kIICore": Complex(
        [
            Column("code", "integer", primary_key_component=True),
            Column("priorityValue", "text"),
            Column("IRGSourceSpecifier", "text"),
        ],
        parsers.kIICore_parser,
    ),
    "kIRGDaeJaweon": Complex(
        [
            Column("code", "integer", primary_key_component=True),
            Column("pageNumber", "integer", primary_key_component=True),
            Column("positionNumber", "integer", primary_key_component=True),
            Column("virtual", "integer", primary_key_component=True),
        ],
        parsers.kDaeJaweon_parser,
    ),
    "kIRGHanyuDaZidian": Complex(
        [
            Column("code", "integer", primary_key_component=True),
            Column("volumeNumber", "integer", primary_key_component=True),
            Column("pageNumber", "integer", primary_key_component=True),
            Column("ideographNumber", "integer", primary_key_component=True),
            Column("virtual", "integer", primary_key_component=True),
        ],
        parsers.kHanYu_parser,
    ),
    "kIRGKangXi": Complex(
        [
            Column("code", "integer", primary_key_component=True),
            Column("pageNumber", "integer", primary_key_component=True),
            Column("positionNumber", "integer", primary_key_component=True),
            Column("virtual", "integer", primary_key_component=True),
        ],
        parsers.kKangXi_parser,
    ),
    "kJapanese": Complex(
        [
            Column("code", "integer", primary_key_component=True),
            Column("reading", "text", primary_key_component=True),
            Column("priority", "integer", primary_key_component=True),
        ],
        parsers.string_splitter,
    ),
    "kJapaneseKun": Complex(
        [
            Column("code", "integer", primary_key_component=True),
            Column("reading", "text", primary_key_component=True),
            Column("priority", "integer", primary_key_component=True),
        ],
        parsers.string_splitter,
    ),
    "kJapaneseOn": Complex(
        [
            Column("code", "integer", primary_key_component=True),
            Column("reading", "text", primary_key_component=True),
            Column("priority", "integer", primary_key_component=True),
        ],
        parsers.string_splitter,
    ),
    "kJinmeiyoKanji": Complex(
        [
            Column("code", "integer", primary_key_component=True),
            Column("year", "integer"),
            Column("standardFormCode", "integer", nullable=True),
        ],
        parsers.kJinmeiyoKanji_parser,
    ),
    "kJIS0213": Complex(
        [
            Column("code", "integer", primary_key_component=True),
            Column("plane", "integer"),
            Column("row", "integer"),
            Column("cell", "integer"),
        ],
        parsers.kJIS0213_parser,
    ),
    "kJis0": Complex(
        [
            Column("code", "integer", primary_key_component=True),
            Column("row", "integer"),
            Column("cell", "integer"),
        ],
        parsers.row_cell_parser,
    ),
    "kJis1": Complex(
        [
            Column("code", "integer", primary_key_component=True),
            Column("row", "integer"),
            Column("cell", "integer"),
        ],
        parsers.row_cell_parser,
    ),
    "kJoyoKanji": Complex(
        [
            Column("code", "integer", primary_key_component=True),
            Column("year", "integer", nullable=True),
            Column("variantCode", "integer", nullable=True),
        ],
        parsers.kJoyoKanji_parser,
    ),
    "kKangXi": Complex(
        [
            Column("code", "integer", primary_key_component=True),
            Column("pageNumber", "integer", primary_key_component=True),
            Column("positionNumber", "integer", primary_key_component=True),
            Column("virtual", "integer", primary_key_component=True),
        ],
        parsers.kKangXi_parser,
    ),
    "kKarlgren": Complex(
        [
            Column("code", "integer", primary_key_component=True),
            Column("indexNumber", "text"),
            Column("interpolated", "integer"),
        ],
        parsers.kKarlgren_parser,
    ),
    "kKorean": Complex(
        [
            Column("code", "integer", primary_key_component=True),
            Column("reading", "text", primary_key_component=True),
            Column("priority", "integer", primary_key_component=True),
        ],
        parsers.string_splitter,
    ),
    "kKoreanEducationHanja": Numeric(),
    "kKoreanName": Numeric(),
    "kLau": Complex(
        [
            Column("code", "integer", primary_key_component=True),
            Column("indexNumber", "integer", primary_key_component=True),
        ],
        parsers.integer_splitter,
    ),
    "kMainlandTelegraph": Basic(),
    "kMandarin": Complex(
        [
            Column("code", "integer", primary_key_component=True),
            Column("reading", "text"),
            Column("languageTag", "text", primary_key_component=True),
        ],
        parsers.kMandarin_parser,
    ),
    "kMatthews": Basic(),
    "kMeyerWempe": Basic(),
    "kMojiJoho": Complex(
        [
            Column("code", "integer", primary_key_component=True),
            Column("serialNumber", "text", primary_key_component=True),
            Column(
                "variationSelector", "text", primary_key_component=True, nullable=True
            ),
        ],
        parsers.kMojiJoho_parser,
    ),
    "kMorohashi": Complex(
        [
            Column("code", "integer", primary_key_component=True),
            Column("indexNumber", "text", primary_key_component=True),
            Column(
                "variationSelector", "text", primary_key_component=True, nullable=True
            ),
        ],
        parsers.kMorohashi_parser,
    ),
    "kNelson": Complex(
        [
            Column("code", "integer", primary_key_component=True),
            Column("indexNumber", "integer", primary_key_component=True),
        ],
        parsers.integer_splitter,
    ),
    "kOtherNumeric": Numeric(),
    "kPhonetic": Complex(
        [
            Column("code", "integer", primary_key_component=True),
            Column("phoneticClass", "integer", primary_key_component=True),
            Column(
                "subsidiaryClass", "text", nullable=True, primary_key_component=True
            ),
            Column("explicitlyIncluded", "integer"),
        ],
        parsers.kPhonetic_parser,
    ),
    "kPrimaryNumeric": Complex(
        [
            Column("code", "integer", primary_key_component=True),
            Column("numericValue", "integer"),
            Column("priority", "integer", primary_key_component=True),
        ],
        parsers.kPrimaryNumeric_parser,
    ),
    "kPseudoGB1": Numeric(),
    "kRSAdobe_Japan1_6": Complex(
        [
            Column("code", "integer", primary_key_component=True),
            Column("variant", "integer", primary_key_component=True),
            Column("characterId", "integer", primary_key_component=True),
            Column("kangxiRadicalNumber", "integer", primary_key_component=True),
            Column("strokesInRadical", "integer", primary_key_component=True),
            Column("strokesInResidue", "integer", primary_key_component=True),
        ],
        parsers.kRSAdobe_Japan1_6_parser,
    ),
    "kRSUnicode": Complex(
        [
            Column("code", "integer", primary_key_component=True),
            Column("kangxiRadicalNumber", "integer", primary_key_component=True),
            Column("additionalStrokes", "integer", primary_key_component=True),
            Column("zhSimp", "integer", primary_key_component=True),
            Column("nonZhSimp", "integer", primary_key_component=True),
            Column("secondNonZhSimp", "integer", primary_key_component=True),
        ],
        parsers.kRSUnicode_parser,
    ),
    "kSBGY": Complex(
        [
            Column("code", "integer", primary_key_component=True),
            Column("pageNumber", "integer", primary_key_component=True),
            Column("ideographNumber", "integer", primary_key_component=True),
        ],
        parsers.kSBGY_parser,
    ),
    "kSemanticVariant": Complex(
        [
            Column("code", "integer", primary_key_component=True),
            Column("variantCode", "integer", primary_key_component=True),
            Column("property", "text", primary_key_component=True, nullable=True),
            Column("same", "text"),
            Column("improper", "text"),
            Column("preferred", "text"),
            Column("traditional", "text"),
            Column("simplified", "text"),
        ],
        parsers.kSemanticVariant_parser,
    ),
    "kSimplifiedVariant": Complex(
        [
            Column("code", "integer", primary_key_component=True),
            Column("variantCode", "integer", primary_key_component=True),
        ],
        parsers.variant_parser,
    ),
    "kSMSZD2003Index": Complex(
        [
            Column("code", "integer", primary_key_component=True),
            Column("pageNumber", "integer", primary_key_component=True),
            Column("positionNumber", "integer", primary_key_component=True),
        ],
        parsers.page_position_parser,
    ),
    "kSMSZD2003Readings": Complex(
        [
            Column("code", "integer", primary_key_component=True),
            Column("mandarin", "text", primary_key_component=True),
            Column("cantonese", "text", primary_key_component=True),
            Column("definitionPriority", "integer", primary_key_component=True),
            Column("readingPriority", "integer", primary_key_component=True),
        ],
        parsers.kSMSZD2003Readings_parser,
    ),
    "kSpecializedSemanticVariant": Complex(
        [
            Column("code", "integer", primary_key_component=True),
            Column("variantCode", "integer", primary_key_component=True),
            Column("property", "text", primary_key_component=True, nullable=True),
            Column("same", "text"),
            Column("improper", "text"),
            Column("preferred", "text"),
            Column("traditional", "text"),
            Column("simplified", "text"),
        ],
        parsers.kSemanticVariant_parser,
    ),
    "kSpoofingVariant": Complex(
        [
            Column("code", "integer", primary_key_component=True),
            Column("variantCode", "integer", primary_key_component=True),
        ],
        parsers.variant_parser,
    ),
    "kStrange": Complex(
        [
            Column("code", "integer", primary_key_component=True),
            Column("category", "text", primary_key_component=True),
            Column(
                "referenceCode", "integer", primary_key_component=True, nullable=True
            ),
        ],
        parsers.kStrange_parser,
    ),
    "kTaiwanTelegraph": Complex(
        [
            Column("code", "integer", primary_key_component=True),
            Column("telegraphCode", "integer", primary_key_component=True),
        ],
        parsers.integer_splitter,
    ),
    "kTang": Complex(
        [
            Column("code", "integer", primary_key_component=True),
            Column("reading", "text", primary_key_component=True),
            Column("frequent", "integer", primary_key_component=True),
        ],
        parsers.kTang_parser,
    ),
    "kTayNumeric": Numeric(),
    "kTGH": Complex(
        [
            Column("code", "integer", primary_key_component=True),
            Column("year", "integer"),
            Column("indexNumber", "integer"),
        ],
        parsers.kTGH_parser,
    ),
    "kTGHZ2013": Complex(
        [
            Column("code", "integer", primary_key_component=True),
            Column("pageNumber", "integer", primary_key_component=True),
            Column("positionNumber", "integer", primary_key_component=True),
            Column("entryType", "integer", primary_key_component=True),
            Column("reading", "text"),
        ],
        parsers.kTGHZ2013_parser,
    ),
    "kTotalStrokes": Numeric(),
    "kTraditionalVariant": Complex(
        [
            Column("code", "integer", primary_key_component=True),
            Column("variantCode", "integer", primary_key_component=True),
        ],
        parsers.variant_parser,
    ),
    "kUnihanCore2020": Basic(),
    "kVietnamese": Complex(
        [
            Column("code", "integer", primary_key_component=True),
            Column("reading", "text", primary_key_component=True),
            Column("priority", "integer", primary_key_component=True),
        ],
        parsers.string_splitter,
    ),
    "kVietnameseNumeric": Numeric(),
    "kZhuangNumeric": Numeric(),
    "kZVariant": Complex(
        [
            Column("code", "integer", primary_key_component=True),
            Column("variantCode", "integer", primary_key_component=True),
        ],
        parsers.variant_parser,
    ),
    "kXerox": Complex(
        [
            Column("code", "integer", primary_key_component=True),
            Column("charSetCode", "integer"),
            Column("char8Code", "integer"),
        ],
        parsers.kXerox_parser,
    ),
    "kXHC1983": Complex(
        [
            Column("code", "integer", primary_key_component=True),
            Column("pageNumber", "integer", primary_key_component=True),
            Column("positionNumber", "integer", primary_key_component=True),
            Column("entryType", "integer", primary_key_component=True),
            Column("unifiableVariant", "integer", primary_key_component=True),
            Column("reading", "text"),
            Column("priority", "integer"),
        ],
        parsers.kXHC1983_parser,
    ),
    "kZhuang": Complex(
        [
            Column("code", "integer", primary_key_component=True),
            Column("reading", "text"),
            Column("standardZhuang", "integer"),
        ],
        parsers.kZhuang_parser,
    ),
    "kStrange_strokes": Numeric(),
}

# all_properties = [
#     "kAccountingNumeric",
#     "kAlternateTotalStrokes",
#     "kBigFive",
#     "kCangjie",
#     "kCantonese",
#     "kCCCII",
#     "kCheungBauer",
#     "kCheungBauerIndex",
#     "kCihaiT",
#     "kCNS1986",
#     "kCNS1992",
#     "kCompatibilityVariant",
#     "kCowles",
#     "kDaeJaweon",
#     "kDefinition",
#     "kEACC",
#     "kFanqie",
#     "kFenn",
#     "kFennIndex",
#     "kFourCornerCode",
#     "kGB0",
#     "kGB1",
#     "kGB3",
#     "kGB5",
#     "kGB8",
#     "kGradeLevel",
#     "kGSR",
#     "kHangul",
#     "kHanYu",
#     "kHanyuPinlu",
#     "kHanyuPinyin",
#     "kHDZRadBreak",
#     "kHKGlyph",
#     "kIBMJapan",
#     "kIICore",
#     "kIRG_GSource",
#     "kIRG_HSource",
#     "kIRG_JSource",
#     "kIRG_KPSource",
#     "kIRG_KSource",
#     "kIRG_MSource",
#     "kIRG_SSource",
#     "kIRG_TSource",
#     "kIRG_UKSource",
#     "kIRG_USource",
#     "kIRG_VSource",
#     "kIRGDaeJaweon",
#     "kIRGHanyuDaZidian",
#     "kIRGKangXi",
#     "kJapanese",
#     "kJapaneseKun",
#     "kJapaneseOn",
#     "kJinmeiyoKanji",
#     "kJis0",
#     "kJis1",
#     "kJIS0213",
#     "kJoyoKanji",
#     "kKangXi",
#     "kKarlgren",
#     "kKorean",
#     "kKoreanEducationHanja",
#     "kKoreanName",
#     "kLau",
#     "kMainlandTelegraph",
#     "kMandarin",
#     "kMatthews",
#     "kMeyerWempe",
#     "kMojiJoho",
#     "kMorohashi",
#     "kNelson",
#     "kOtherNumeric",
#     "kPhonetic",
#     "kPrimaryNumeric",
#     "kPseudoGB1",
#     "kRSAdobe_Japan1_6",
#     "kRSUnicode",
#     "kSBGY",
#     "kSemanticVariant",
#     "kSimplifiedVariant",
#     "kSMSZD2003Index",
#     "kSMSZD2003Readings",
#     "kSpecializedSemanticVariant",
#     "kSpoofingVariant",
#     "kStrange",
#     "kTaiwanTelegraph",
#     "kTang",
#     "kTayNumeric",
#     "kTGH",
#     "kTGHZ2013",
#     "kTotalStrokes",
#     "kTraditionalVariant",
#     "kUnihanCore2020",
#     "kVietnamese",
#     "kVietnameseNumeric",
#     "kXerox",
#     "kXHC1983",
#     "kZhuang",
#     "kZhuangNumeric",
#     "kZVariant",
# ]
