# -*- coding: utf-8 -*-
from fontTools.ttLib import TTFont
from PyQt5.QtGui import QPixmap
import platform
import base64
import os


# 图标bytes转成pixmap
def get_icon(icon):
    icon_img = base64.b64decode(icon)  # 解码
    icon_pixmap = QPixmap()  # 新建QPixmap对象
    icon_pixmap.loadFromData(icon_img)  # 往QPixmap中写入数据
    return icon_pixmap


# 解析字体"name"数据表
def analyze_name_table(f_path):
    try:
        name = TTFont(f_path)["name"]
        info = dict()
        # 解析name字段
        for i in name.names:
            try:  # 事先捕获可能的编码报错
                iString = i.toStr()
            except UnicodeDecodeError:
                iString = "[Decode error]"
            # platformID解析
            if i.platformID == 0:   # unicode平台
                pass
            elif i.platformID == 1:  # mac平台
                pass
            elif i.platformID == 3:  # windows平台
                # win平台的languageID需要事先将十进制转换成十六进制
                langID = str(hex(i.langID)).replace("0x", "")
                if len(langID) == 3:
                    langID = "0" + langID
                if langID in Win_Language_IDs:
                    if Win_Language_IDs[langID] not in info:
                        info[Win_Language_IDs[langID]] = dict()
                    if str(i.nameID) in name_IDs:
                        info[Win_Language_IDs[langID]][name_IDs[str(i.nameID)]] = iString
            else:
                raise Exception("Invalid platformID")
        return info
    except Exception as e:
        raise Exception(e)


# 获取字体字形数和字符数
def get_glyph_num(f_path):
    try:
        font = TTFont(f_path)
        glyphs = font["maxp"].numGlyphs
        characters = len(font.getBestCmap())
        return glyphs, characters
    except Exception as e:
        raise Exception(e)


# 解析字体信息
def analyse_font(f_path):
    try:
        font_dict = dict()
        # 获取文件名
        font_dict["fileName"] = os.path.basename(f_path)
        # 解析字体基本信息
        font_info = analyze_name_table(f_path)['US']
        keys = ["Family", "Subfamily", "FullName"]
        for key in keys:
            font_dict[key] = font_info[key] if key in font_info else "[Miss]"
        # 解析字体字符数
        font_dict["Glyphs"], font_dict["Chars"] = get_glyph_num(f_path)
        # 转换成字符串列表
        info_list = [str('{}: {}'.format(x, y))for x, y in font_dict.items()]
        return info_list
    except Exception as e:
        raise Exception(e)


# mac平台语言ID对照表
Mac_Language_IDs = {
    "0": "En",
    "1": "French",
    "2": "German",
    "3": "Italian",
    "4": "Dutch",
    "5": "Swedish",
    "6": "Spanish",
    "7": "Danish",
    "8": "Portuguese",
    "9": "Norwegian",
    "10": "Hebrew",
    "11": "Japanese",
    "12": "Arabic",
    "13": "Finnish",
    "14": "Greek",
    "15": "Icelandic",
    "16": "Maltese",
    "17": "Turkish",
    "18": "Croatian",
    "19": "ChT",
    "20": "Urdu",
    "21": "Hindi",
    "22": "Thai",
    "23": "Korean",
    "24": "Lithuanian",
    "25": "Polish",
    "26": "Hungarian",
    "27": "Estonian",
    "28": "Latvian",
    "29": "Sami",
    "30": "Faroese",
    "31": "Farsi/Persian",
    "32": "Russian",
    "33": "Ch",
    "34": "Flemish",
    "35": "Irish Gaelic",
    "36": "Albanian",
    "37": "Romanian",
    "38": "Czech",
    "39": "Slovak",
    "40": "Slovenian",
    "41": "Yiddish",
    "42": "Serbian",
    "43": "Macedonian",
    "44": "Bulgarian",
    "45": "Ukrainian",
    "46": "Byelorussian",
    "47": "Uzbek",
    "48": "Kazakh",
    "49": "Azerbaijani(Cyrillic script)",
    "50": "Azerbaijani(Arabicsc ript)",
    "51": "Armenian",
    "52": "Georgian",
    "53": "Moldavian",
    "54": "Kirghiz",
    "55": "Tajiki",
    "56": "Turkmen",
    "57": "Mongolian(Mongolian script)",
    "58": "Mongolian(Cyrillic script)",
    "59": "Pashto",
    "60": "Kurdish",
    "61": "Kashmiri",
    "62": "Sindhi",
    "63": "Tibetan",
    "64": "Nepali",
    "65": "Sanskrit",
    "66": "Marathi",
    "67": "Bengali",
    "68": "Assamese",
    "69": "Gujarati",
    "70": "Punjabi",
    "71": "Oriya",
    "72": "Malayalam",
    "73": "Kannada",
    "74": "Tamil",
    "75": "Telugu",
    "76": "Sinhalese",
    "77": "Burmese",
    "78": "Khmer",
    "79": "Lao",
    "80": "Vietnamese",
    "81": "Indonesian",
    "82": "Tagalog",
    "83": "Malay(Roman script)",
    "84": "Malay(Arabic script)",
    "85": "Amharic",
    "86": "Tigrinya",
    "87": "Galla",
    "88": "Somali",
    "89": "Swahili",
    "90": "Kinyarwanda/Ruanda",
    "91": "Rundi",
    "92": "Nyanja/Chewa",
    "93": "Malagasy",
    "94": "Esperanto",
    "128": "Welsh",
    "129": "Basque",
    "130": "Catalan",
    "131": "Latin",
    "132": "Quechua",
    "133": "Guarani",
    "134": "Aymara",
    "135": "Tatar",
    "136": "Uighur",
    "137": "Dzongkha",
    "138": "Javanese(Roman script)",
    "139": "Sundanese(Roman script)",
    "140": "Galician",
    "141": "Afrikaans",
    "142": "Breton",
    "143": "Inuktitut",
    "144": "ScottishGaelic",
    "145": "ManxGaelic",
    "146": "IrishGaelic(with dot above)",
    "147": "Tongan",
    "148": "Greek(polytonic)",
    "149": "Greenlandic",
    "150": "Azerbaijani(Roman script)"
}
# win平台语言对照表
Win_Language_IDs = {
    "0436": "South Africa",
    "041C": "Albania",
    "0484": "France",
    "045E": "Ethiopia",
    "1401": "Algeria",
    "3C01": "Bahrain",
    "0C01": "Egypt",
    "0801": "Iraq",
    "2C01": "Jordan",
    "3401": "Kuwait",
    "3001": "Lebanon",
    "1001": "Libya",
    "1801": "Morocco",
    "2001": "Oman",
    "4001": "Qatar",
    "0401": "Saudi Arabia",
    "2801": "Syria",
    "1C01": "Tunisia",
    "3801": "U.A.E.",
    "2401": "Yemen",
    "042B": "Armenia",
    "044D": "India",
    "082C": "Azerbaijan",
    "042C": "Azerbaijan",
    "046D": "Russia",
    "042D": "Basque",
    "0423": "Belarus",
    "0845": "Bangladesh",
    "0445": "India",
    "201A": "Bosnia and Herzegovina",
    "141A": "Bosnia and Herzegovina",
    "047E": "France",
    "0402": "Bulgaria",
    "0403": "Catalan",
    "0C04": "HK",
    "1404": "Macao",
    "0804": "Ch",
    "1004": "Singapore",
    "0404": "TW",
    "0483": "France",
    "041A": "Croatia",
    "101A": "Bosnia and Herzegovina",
    "0405": "Czech Republic",
    "0406": "Denmark",
    "048C": "Afghanistan",
    "0465": "Maldives",
    "0813": "Belgium",
    "0413": "Netherlands",
    "0C09": "Australia",
    "2809": "Belize",
    "1009": "Canada",
    "2409": "Caribbean",
    "4009": "India",
    "1809": "Ireland",
    "2009": "Jamaica",
    "4409": "Malaysia",
    "1409": "New Zealand",
    "3409": "Republic of the Philippines",
    "4809": "Singapore",
    "1C09": "SouthAfrica",
    "2C09": "Trinidad and Tobago",
    "0809": "UK",
    "0409": "US",
    "3009": "Zimbabwe",
    "0425": "Estonia",
    "0438": "Faroe Islands",
    "0464": "Philippines",
    "040B": "Finland",
    "080C": "Belgium",
    "0C0C": "Canada",
    "040C": "France",
    "140c": "Luxembourg",
    "180C": "Principality of Monaco",
    "100C": "Switzerland",
    "0462": "Netherlands",
    "0456": "Galician",
    "0437": "Georgia",
    "0C07": "Austria",
    "0407": "Germany",
    "1407": "Liechtenstein",
    "1007": "Luxembourg",
    "0807": "Switzerland",
    "0408": "Greece",
    "046F": "Greenland",
    "0447": "India",
    "0468": "Nigeria",
    "040D": "Israel",
    "0439": "India",
    "040E": "Hungary",
    "040F": "Iceland",
    "0470": "Nigeria",
    "0421": "Indonesia",
    "045D": "Canada",
    "085D": "Canada",
    "083C": "Ireland",
    "0434": "South Africa",
    "0435": "South Africa",
    "0410": "Italy",
    "0810": "Switzerland",
    "0411": "Japan",
    "044B": "India",
    "043F": "Kazakhstan",
    "0453": "Cambodia",
    "0486": "Guatemala",
    "0487": "Rwanda",
    "0441": "Kenya",
    "0457": "India",
    "0412": "Korea",
    "0440": "Kyrgyzstan",
    "0454": "Lao P.D.R.",
    "0426": "Latvia",
    "0427": "Lithuania",
    "082E": "Germany",
    "046E": "Luxembourg",
    "042F": "North Macedonia",
    "083E": "Brunei Darussalam",
    "043E": "Malaysia",
    "044C": "India",
    "043A": "Malta",
    "0481": "New Zealand",
    "047A": "Chile",
    "044E": "India",
    "047C": "Mohawk",
    "0450": "Mongolia",
    "0850": "People’s Republic of China",
    "0461": "Nepal",
    "0414": "Norway",
    "0814": "Norway",
    "0482": "France",
    "0448": "India",
    "0463": "Afghanistan",
    "0415": "Poland",
    "0416": "Brazil",
    "0816": "Portugal",
    "0446": "India",
    "046B": "Bolivia",
    "086B": "Ecuador",
    "0C6B": "Peru",
    "0418": "Romania",
    "0417": "Switzerland",
    "0419": "Russia",
    "243B": "Finland",
    "103B": "Norway",
    "143B": "Sweden",
    "0C3B": "Finland",
    "043B": "Norway",
    "083B": "Sweden",
    "203B": "Finland",
    "183B": "Norway",
    "1C3B": "Sweden",
    "044F": "India",
    "1C1A": "Bosnia and Herzegovina",
    "0C1A": "Serbia",
    "181A": "Bosnia and Herzegovina",
    "081A": "Serbia",
    "046C": "South Africa",
    "0432": "South Africa",
    "045B": "Sri Lanka",
    "041B": "Slovakia",
    "0424": "Slovenia",
    "2C0A": "Argentina",
    "400A": "Bolivia",
    "340A": "Chile",
    "240A": "Colombia",
    "140A": "CostaRica",
    "1C0A": "Dominican Republic",
    "300A": "Ecuador",
    "440A": "El Salvador",
    "100A": "Guatemala",
    "480A": "Honduras",
    "080A": "Mexico",
    "4C0A": "Nicaragua",
    "180A": "Panama",
    "3C0A": "Paraguay",
    "280A": "Peru",
    "500A": "Puerto Rico",
    "0C0A": "Spain",
    "040A": "Spain",
    "540A": "United States",
    "380A": "Uruguay",
    "200A": "Venezuela",
    "081D": "Finland",
    "041D": "Sweden",
    "045A": "Syria",
    "0428": "Tajikistan",
    "085F": "Algeria",
    "0449": "India",
    "0444": "Russia",
    "044A": "India",
    "041E": "Thailand",
    "0451": "PRC",
    "041F": "Turkey",
    "0442": "Turkmenistan",
    "0480": "PRC",
    "0422": "Ukraine",
    "042E": "Germany",
    "0420": "Islamic Republic of Pakistan",
    "0843": "Uzbekistan",
    "0443": "Uzbekistan",
    "042A": "Vietnam",
    "0452": "United Kingdom",
    "0488": "Senegal",
    "0485": "Russia",
    "0478": "PRC",
    "046A": "Nigeria"
}

# name字段对照表
name_IDs = {
    "0": "Copyright",     # 版权公告
    "1": "Family",        # 字体家族名称用户看
    "2": "Subfamily",     # 字体子家族名称
    "3": "UniqueID",      # 唯一字体标识符
    "4": "FullName",      # 完整字体名
    "5": "Version",       # 版本字符串
    "6": "PostScript",    # PostScript名称
    "7": "Trademark",     # 商标
    "8": "Manufacturer",  # 制造商名称
    "9": "Designer",      # 设计师
    "10": "Description",  # 字体的描述
    "11": "URLVendor",    # 字体供应商的URL
    "12": "URLDesigner",  # 设计师的URL
    "13": "License",      # 许可证
    "14": "URLLicense"    # 许可证信息URL
}
