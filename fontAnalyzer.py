# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QApplication, QDesktopWidget, QListWidgetItem
from PyQt5.QtGui import QIcon, QPixmap, QFontDatabase, QFont
from subModule import baseInfo, extendInfo, charsPreview
from fontAnalyzerUI import Ui_MainWindow
from PyQt5.QtCore import Qt, QPoint
from fontTools.ttLib import TTFont
from functools import partial
import fontAnalyzer_rc
import selfFontools
import selfTools
import sys
import os


class MainWindow(Ui_MainWindow, QMainWindow):
    # 初始化
    def __init__(self):
        super(MainWindow, self).__init__()
        self.version = '0.00'  # 设置版本号
        self.setupUi(self)  # 加载Ui
        # loadUi("fontAnalyzer.ui", self)  # 加载Ui文件
        self.setWindowTitle("fontAnalyzer_v{}".format(self.version))  # 设置主窗口标题
        self.setWindowIcon(QIcon('./iconFile/logoPin.ico'))  # 设置图标

        self.setWindowFlags(Qt.FramelessWindowHint)  # 隐藏主窗口边界
        self.setAttribute(Qt.WA_TranslucentBackground)  # 隐藏背景（透明化

        # 初始化固有参数
        self.cwd = os.getcwd()  # 记录当前工作目录
        self.fontPath = None
        self.fontFile = None
        # 鼠标移动窗口事件参数
        self.startPos = None
        self.endPos = None
        self.isTracking = None

        # 初始化所有子模块
        self.baseInfo = baseInfo.BaseInfo(self)
        self.extendInfo = extendInfo.ExtendInfo(self)
        self.adv_commands()  # 执行预指令

    # 程序初始化预执行步骤
    def adv_commands(self):
        self.setFixedSize(1024, 786)  # 设定窗口尺寸(固定尺寸)
        screenSize = QDesktopWidget().screenGeometry()  # 获取屏幕尺寸
        selfSize = self.geometry()  # 获取程序窗口尺寸
        newLeft = int((screenSize.width() - selfSize.width()) / 2)
        newTop = int((screenSize.height() - selfSize.height()) / 2)
        self.move(newLeft, newTop)  # 移动到居中位置
        self.pages.setCurrentIndex(0)  # 默认显示初始page

        # 添加自定义字体
        fontDb = QFontDatabase()
        fontDb.addApplicationFont(":resources/fontFile/霞骛文楷.ttf")
        # print(fontDb.applicationFontFamilies(fontDb.addApplicationFont(":resources/fontFile/霞骛文楷.ttf")))
        self.setFont(QFont('LXGW WenKai'))

        # 预执行所有绑定函数
        self.bind()

    # 绑定主界面基础按钮
    def bind(self):
        self.buttonClose.clicked.connect(self.close_window)  # 关闭按钮
        self.buttonMinimize.clicked.connect(self.minimize_window)  # 最小化按钮
        self.buttonUpload.clicked.connect(self.upload_font)  # 上传按钮
        self.buttonReset.clicked.connect(self.reset)  # 重置按钮
        self.listMenu.itemClicked.connect(self.page_change)  # 点击列表项切换菜单栏页面

    # 上传字体函数
    def upload_font(self):
        defaultDir = os.path.join(os.path.expanduser('~'), "Desktop")  # 获取桌面路径
        fontPath, _ = QFileDialog.getOpenFileName(self, "选择字体文件", defaultDir, "类型({})".format("*.ttf *.otf"))
        if fontPath:
            # 初始化字体数据
            self.fontPath = fontPath
            self.lineUpload.setText(os.path.basename(self.fontPath))  # 显示字体名
            self.baseInfo.set_base_info()  # 填充BaseInfo界面
            self.set_extend_info()  # 填充ExtendInfo界面

    # 切换页面
    def page_change(self, item: QListWidgetItem):
        if item.text() == "BaseInfo":
            self.pages.setCurrentIndex(1)
        elif item.text() == "ExtendInfo":
            self.pages.setCurrentIndex(2)
        elif item.text() == "CharsPreview":
            self.pages.setCurrentIndex(3)
        else:
            pass

    # 重置界面
    def reset(self):
        # 设置所有列表项为未选中
        for i in range(self.listMenu.count()):
            self.listMenu.item(i).setSelected(False)
        self.lineUpload.clear()  # 清空字体名
        self.pages.setCurrentIndex(0)  # 返回初始页面
        self.baseInfo.reset_base_info()  # 重置BaseInfo界面

    # 关闭界面
    def close_window(self):
        self.window().close()

    # 最小化界面
    def minimize_window(self):
        self.window().showMinimized()

    # 鼠标按下事件
    def mousePressEvent(self, event):
        # 根据鼠标按下时的位置判断是否在顶部菜单栏内
        if self.childAt(event.x(), event.y()).objectName() == "labelBGTop":
            if event.button() == Qt.LeftButton:  # 判断鼠标按下的是左键
                self.startPos = QPoint(event.x(), event.y())  # 记录初始位置
                self.isTracking = True

    # 鼠标松开事件
    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.isTracking = False
            self.startPos = None
            self.endPos = None

    # 鼠标移动事件
    def mouseMoveEvent(self, event):
        if self.startPos:
            self.endPos = event.pos() - self.startPos
            self.move(self.pos() + self.endPos)  # 移动窗口

    # TODO：编写拖入事件：从外部直接拖入字体包可以等效于上传操作


if __name__ == '__main__':
    app = QApplication(sys.argv)  # 创建QApplication类的实例
    main_window = MainWindow()  # 实例化一个窗口类
    main_window.show()  # 显示窗口
    sys.exit(app.exec_())  # 进入程序主循环 通过exit函数确保主循环安全结束
