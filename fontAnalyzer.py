# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QFileDialog, QApplication, QDesktopWidget
from PyQt5.QtWidgets import QDialog, QTextEdit, QPushButton, QLabel
from datetime import datetime, timedelta
from fontTools.ttLib import TTFont
from PyQt5.QtGui import QIcon
from functools import partial
from PyQt5.uic import loadUi
import selftools
import sys
import os


class MainWindow(QMainWindow):
    # 初始化
    def __init__(self):
        super(MainWindow, self).__init__()
        self.version = '0.00'  # 设置版本号
        # self.setupUi(self)  # 加载Ui
        loadUi("fontAnalyzer.ui", self)  # 加载Ui文件
        self.setWindowTitle("fontAnalyzer_v{}".format(self.version))  # 设置主窗口标题
        # self.setWindowIcon(QIcon(selftools.get_icon(selftools.mainIcon)))  # 设置图标

        # 初始化固有参数
        self.cwd = os.getcwd()  # 记录当前工作目录
        self.fontPath = None
        self.fontFile = None

        self.adv_commands()  # 执行预指令

    # 程序初始化预执行步骤
    def adv_commands(self):
        # self.labelVersion.setText('Version:{}'.format(self.version))  # 设定版本号
        self.setFixedSize(1261, 846)  # 设定窗口尺寸(固定尺寸)
        screenSize = QDesktopWidget().screenGeometry()  # 获取屏幕尺寸
        selfSize = self.geometry()  # 获取程序窗口尺寸
        newLeft = int((screenSize.width() - selfSize.width()) / 2)
        newTop = int((screenSize.height() - selfSize.height()) / 2)
        self.move(newLeft, newTop)  # 移动到居中位置
        # 预执行所有绑定函数
        self.bind()

    # 绑定按钮
    def bind(self):
        pass

    # 绑定鼠标双击事件
    def mouseDoubleClickEvent(self, event):
        pass

    # 关闭窗口时弹出确认消息
    def closeEvent(self, event):
        replyA = QMessageBox.question(self, 'Warning', '确认退出？', QMessageBox.Yes, QMessageBox.No)
        if replyA == QMessageBox.Yes:  # 接收到确认关闭信号之后关闭窗口
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    # 创建QApplication类的实例
    app = QApplication(sys.argv)
    # 实例化一个窗口类
    main_window = MainWindow()
    # 显示窗口
    main_window.show()
    # 进入程序主循环 通过exit函数确保主循环安全结束
    sys.exit(app.exec_())
