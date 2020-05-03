import sys
from PyQt5.QtWidgets import QMainWindow, QWidget, QPushButton, QApplication, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QPixmap


class FirstWin(QMainWindow):
    def __init__(self):
        super(FirstWin, self).__init__()

        self.setWindowTitle('FirstTitle')
        self.resize(300, 500)

        self.button1 = QPushButton('out')
        self.button1.clicked.connect(self.onClick_button)

        self.lable1 = QLabel('<a href="www.baidu.com">百度一下</a>')
        self.lable1.setAutoFillBackground(True)

        palette2 = QPalette()
        palette2.setColor(QPalette.Window, Qt.white)
        self.lable1.setPalette(palette2)

        self.lable2 = QLabel()
        self.lable2.setToolTip("这是张图片哦")
        self.lable2.setPixmap(QPixmap("C:/Users/Administrator/Desktop/wuli.png"))

        self.lable1.setOpenExternalLinks(True)
        self.lable1.setAlignment(Qt.AlignCenter)

        layout = QVBoxLayout()
        # 添加小部件
        layout.addWidget(self.button1)
        layout.addWidget(self.lable1)
        layout.addWidget(self.lable2)

        mainFrame = QWidget()
        mainFrame.setLayout(layout)

        self.setCentralWidget(mainFrame)

    def onClick_button(self):
        # 工作区域
        print('x = %d' % self.x())
        print('y = %d' % self.y())
        # 整个区域
        # print('x2 = %d' % self.geometry().x())
        # print('y2 = %d' % self.geometry().y())
        print('*********************************************')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    first = FirstWin()
    first.show()
    sys.exit(app.exec_())