import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QToolTip, QLabel
from PyQt5.QtGui import QFont, QPalette, QPixmap
# Qt包含一些常量
from PyQt5.QtCore import Qt


def onClick_button1():
    print('Hello World!')

def linkHovered():
    print('划过')

def linkClicked():
    print('点击')


app = QApplication(sys.argv)
main = QMainWindow()
QToolTip.setFont(QFont('KaiTi', 50))
# 为控件添加提示消息
main.setToolTip('这是工作区')
button1 = QPushButton(main)
button1.setText('按钮')
button1.setToolTip('这是按钮')
button1.move(100, 100)
button1.resize(100, 100)  # 工作区尺寸
button1.clicked.connect(onClick_button1)


lable1 = QLabel(main)
lable1.setText('<a href="www.baidu.com">百度一下</a>')
lable1.move(100, 230)
lable1.resize(100, 50)
lable1.setFont(QFont('SongTi', 14))
# 打开外部链接（跳转网页和触发事件二者选其一）
# lable1.setOpenExternalLinks(True)
lable1.setAlignment(Qt.AlignCenter)
# 允许填充背景
lable1.setAutoFillBackground(True)
palette = QPalette()
palette.setColor(QPalette.Window, Qt.green)
lable1.setPalette(palette)
lable1.linkActivated.connect(linkClicked)
lable1.linkHovered.connect(linkHovered)

lable2 = QLabel(main)
lable2.setAlignment(Qt.AlignCenter)
lable2.setPixmap(QPixmap("C:/Users/Administrator/Desktop/wuli.png"))
# lable2.linkActivated.connect(linkClicked)

main.resize(300, 300)
main.setWindowTitle('标题')
main.show()
sys.exit(app.exec_())