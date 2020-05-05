import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt


# 单选按钮
class Radiobutton(QWidget):
    def __init__(self):
        super(Radiobutton, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QRadioButton')
        self.button1 = QRadioButton('单选按钮A')
        self.button1.toggled.connect(self.buttonStatus)
        self.button2 = QRadioButton('单选按钮B')
        # 默认选择
        # self.button2.setChecked(True)
        self.button2.toggled.connect(self.buttonStatus)
        self.button3 = QRadioButton('单选按钮C')
        self.button3.toggled.connect(self.buttonStatus)

        vlayout = QHBoxLayout()
        vlayout.addWidget(self.button1)
        vlayout.addWidget(self.button2)
        vlayout.addWidget(self.button3)

        self.setLayout(vlayout)

    def buttonStatus(self):
        radioButton = self.sender()
        if radioButton.isChecked() == True:
            print( radioButton.text() + '被选中')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    radiowin = Radiobutton()
    radiowin.show()
    sys.exit(app.exec_())