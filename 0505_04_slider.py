import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt


class Slider(QWidget):
    def __init__(self):
        super(Slider, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QSlider')
        self.resize(200, 100)
        self.label = QLabel('声音大小：50')
        self.sd = QSlider(Qt.Horizontal)
        self.sd.setValue(50)
        # 默认0到99
        # self.sd.setMinimum(3)
        # self.sd.setMaximum(1000)
        # self.sd.setRange(3, 1000)
        self.sd.setSingleStep(10)
        self.sd.setTickPosition(QSlider.TicksBelow)
        self.sd.valueChanged.connect(self.valueChange)

        vlayout = QVBoxLayout()
        vlayout.addWidget(self.label)
        vlayout.addWidget(self.sd)
        self.setLayout(vlayout)

    def valueChange(self):
        self.label.setText('声音大小：' + str(self.sd.value()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwin = Slider()
    mainwin.show()
    sys.exit(app.exec_())