import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt, QRegExp


class Colordialog(QWidget):
    def __init__(self):
        super(Colordialog, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Colordialog')

        self.colorbutton = QPushButton('选择颜色')
        self.colorbackgroundbutton = QPushButton('选择背景')
        self.label = QLabel('测试字体')
        self.label.setAlignment(Qt.AlignCenter)

        self.colorbutton.clicked.connect(self.textColorChange)
        self.colorbackgroundbutton.clicked.connect(self.colorBackgroundChange)

        vlayout = QVBoxLayout()
        vlayout.addWidget(self.colorbutton)
        vlayout.addWidget(self.colorbackgroundbutton)
        vlayout.addWidget(self.label)

        self.setLayout(vlayout)

    # 怎么同时设置？
    def colorBackgroundChange(self):
        color = QColorDialog.getColor()
        p = QPalette()
        p.setColor(QPalette.Window, color)
        self.label.setAutoFillBackground(True)
        self.label.setPalette(p)

    def textColorChange(self):
        color = QColorDialog.getColor()
        p = QPalette()
        p.setColor(QPalette.WindowText, color)
        self.label.setPalette(p)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwin = Colordialog()
    mainwin.show()
    sys.exit(app.exec_())