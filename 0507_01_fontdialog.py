import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt, QRegExp


class Fontdialog(QWidget):
    def __init__(self):
        super(Fontdialog, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Fontdialog')

        self.fontbutton = QPushButton('选择字体')
        self.label = QLabel('测试字体')
        self.label.setAlignment(Qt.AlignCenter)

        self.fontbutton.clicked.connect(self.fontChange)

        vlayout = QVBoxLayout()
        vlayout.addWidget(self.fontbutton)
        vlayout.addWidget(self.label)

        self.setLayout(vlayout)

    def fontChange(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.label.setFont(font)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwin = Fontdialog()
    mainwin.show()
    sys.exit(app.exec_())