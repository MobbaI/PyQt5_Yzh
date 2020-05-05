import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt


class Spinbox(QWidget):
    def __init__(self):
        super(Spinbox, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QSpinBox')
        self.resize(200, 100)
        self.label = QLabel('当前数值：')
        self.sb = QSpinBox()
        self.sb.setValue(66)
        self.sb.setRange(66, 88)
        # self.sb.setSingleStep(3)
        self.sb.valueChanged.connect(self.valueChange)

        vlayout = QVBoxLayout()
        vlayout.addWidget(self.label)
        vlayout.addWidget(self.sb)
        self.setLayout(vlayout)

    def valueChange(self):
        self.label.setText('当前数值：' + str(self.sb.value()))
        print(self.sb.value())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    spinwin = Spinbox()
    spinwin.show()
    sys.exit(app.exec_())