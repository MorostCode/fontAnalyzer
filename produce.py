import os

name = "fontAnalyzer"

# ui文件转py
os.system("python -m PyQt5.uic.pyuic {0}.ui -o {0}UI.py".format(name))
print("{0}.ui已转为{0}UI.py".format(name))
# # qrc文件转py
# os.system("pyrcc5 {0}.qrc -o {0}_rc.py".format(name))
# print("{0}.ico已转为{0}_rc.py".format(name))
# # 打包生产(单文件)
# os.system("pyinstaller -w -F -i logoPin.ico {}.py".format(name))
# print("{}.exe文件已生成".format(name))
# os.system("pyinstaller -w -i ZhLogo.ico ZHunTools.py")  # 打包生产(多文件)
# print("{}程序包已生成".format(name))
