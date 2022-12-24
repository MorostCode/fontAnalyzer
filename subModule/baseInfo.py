import selfFontools
import selfTools
import os


# “基础信息”模块
class BaseInfo:
    def __init__(self, main_window):
        super(BaseInfo, self).__init__()
        self.main_window = main_window
        # 设定初始参数

        # 预执行指令
        self.adv_commands()
        self.bind()

    # 预执行步骤
    def adv_commands(self):
        pass

    # 绑定按钮
    def bind(self):
        pass

    # 填充BaseInfo界面
    def set_base_info(self):
        try:
            # 如果仍处于初始页面，则自动跳转到BaseInfo界面
            if self.main_window.pages.currentIndex() == 0:
                self.main_window.pages.setCurrentIndex(1)
            # 获取信息
            fileName = os.path.basename(self.main_window.fontPath)  # 文件名
            fileSize = selfTools.get_size(self.main_window.fontPath)  # 文件大小
            glyphs, chars = selfFontools.get_glyph_num(self.main_window.fontPath)  # 字形数，字符数
            createdTime, modifiedTime = selfFontools.get_time(self.main_window.fontPath)  # 创建日期，修改日期
            baseDict = selfFontools.get_font_base_info(self.main_window.fontPath)  # 其他基础信息
            # 设置文件基础信息
            self.main_window.labelFileName2.setText(fileName)
            self.main_window.labelFileSize2.setText(fileSize)
            self.main_window.labelGlyphs2.setText(str(glyphs))
            self.main_window.labelCharacters2.setText(str(chars))
            self.main_window.labelCreatedTime2.setText(createdTime)
            self.main_window.labelModifiedTime2.setText(modifiedTime)
            # 设置字体基础信息（取自win平台US语言）
            self.main_window.labelFontFamily2.setText(baseDict["Family"])
            self.main_window.labelFontSubfamily2.setText(baseDict["Subfamily"])
            self.main_window.labelUniqueFontID2.setText(baseDict["UniqueID"])
            self.main_window.labelFullFontName2.setText(baseDict["FullName"])
            self.main_window.labelVersion2.setText(baseDict["Version"])
            self.main_window.labelPostScript2.setText(baseDict["PostScript"])
        except Exception as e:
            print(e)

    # 重置BaseInfo界面
    def reset_base_info(self):
        self.main_window.labelFileName2.clear()
        self.main_window.labelFileSize2.clear()
        self.main_window.labelGlyphs2.clear()
        self.main_window.labelCharacters2.clear()
        self.main_window.labelCreatedTime2.clear()
        self.main_window.labelModifiedTime2.clear()
        self.main_window.labelFontFamily2.clear()
        self.main_window.labelFontSubfamily2.clear()
        self.main_window.labelUniqueFontID2.clear()
        self.main_window.labelFullFontName2.clear()
        self.main_window.labelVersion2.clear()
        self.main_window.labelPostScript2.clear()
