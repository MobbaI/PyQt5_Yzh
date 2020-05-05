import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt


class Checkbox(QWidget):
    def __init__(self):
        super(Checkbox, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QCheckBox')
        hlayout = QHBoxLayout()

        self.button1 = QCheckBox('未选中')
        # 也可这样设置两种状态
        # self.button1.setCheckState(Qt.Checked)
        self.button2 = QCheckBox('选中')
        self.button2.setChecked(True)
        self.button3 = QCheckBox('半选中')
        # 允许半选中状态，设置三态
        self.button3.setTristate(True)
        # 设置默认半选中
        self.button3.setCheckState(Qt.PartiallyChecked)

        self.button3.stateChanged.connect(lambda: self.buttonstate(self.button3))
        self.button1.stateChanged.connect(lambda: self.buttonstate(self.button1))
        self.button2.stateChanged.connect(lambda: self.buttonstate(self.button2))

        hlayout.addWidget(self.button1)
        hlayout.addWidget(self.button2)
        hlayout.addWidget(self.button3)

        self.setLayout(hlayout)

    def buttonstate(self, btn):
        print(btn.text() + '：' + str(btn.checkState()))
        print(self.button3.text() + '：' + str(self.button3.checkState()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    checkwin = Checkbox()
    checkwin.show()
    sys.exit(app.exec_())