import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt


class Pushbutton(QWidget):
    def __init__(self):
        super(Pushbutton, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('PushButton')
        self.resize(300, 400)
        self.button1 = QPushButton('状态')
        self.button2 = QPushButton('图片Key_E')
        self.button3 = QPushButton('不可用')
        self.button4 = QPushButton('默认回车')
        self.button5 = QPushButton('热键（&H）')

        self.button1.setCheckable(True)
        # 点一下
        # self.button1.toggle()
        self.button1.clicked.connect(lambda: self.on_clicked_button(self.button1))
        self.button1.clicked.connect(self.buttonStatus)
        self.button2.setIcon(QIcon('E:/p1.ico'))
        # 大键盘是Return，小键盘才是Enter
        self.button2.setShortcut(Qt.Key_E)
        self.button2.clicked.connect(lambda: self.on_clicked_button(self.button2))
        self.button3.setEnabled(False)
        # 默认按钮，一个窗口一个
        # self.button4.setDefault(True)
        # self.button4.clicked.connect(lambda: self.on_clicked_button(self.button4))
        self.button5.clicked.connect(lambda: self.on_clicked_button(self.button5))

        vlayput = QVBoxLayout()
        vlayput.addWidget(self.button1)
        vlayput.addWidget(self.button2)
        vlayput.addWidget(self.button3)
        # vlayput.addWidget(self.button4)
        vlayput.addWidget(self.button5)

        self.setLayout(vlayput)

    def buttonStatus(self, btn):
        if self.button1.isChecked():
            print('状态：已按下')
        else:
            print('状态：未按下')

    def on_clicked_button(self, btn):
        print('被点击的按钮是：' + btn.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    pushwin = Pushbutton()
    pushwin.show()
    sys.exit(app.exec_())