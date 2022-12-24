import selfFontools
import selfTools
import os


# “基础信息”模块
class ExtendInfo:
    def __init__(self, main_window):
        super(ExtendInfo, self).__init__()
        self.main_window = main_window
        # 设定初始参数

        # 预执行指
        self.adv_commands()
        self.bind()

    # 预执行步骤
    def adv_commands(self):
        pass

    # 绑定按钮
    def bind(self):
        pass

    # 填充ExtendInfo界面
    def set_extend_info(self):
        pass

