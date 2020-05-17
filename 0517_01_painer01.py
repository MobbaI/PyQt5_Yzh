import sys
import math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class PainterPi(QWidget):
    def __init__(self):
        super(PainterPi, self).__init__()
        self.resize(300, 300)
        self.setWindowTitle('绘图')

    def paintEvent(self, QPaintEvent):
        painter = QPainter()
        painter.begin(self)
        painter.setPen(Qt.darkMagenta)
        size = self.size()

        for i in range(1000):
            x = size.width()/3 * math.sin(-1 * math.pi + math.pi * 2.0 * (i/1000)) + size.width()/2
            y = size.height()/6 * math.cos(-1 * math.pi + math.pi * 2.0 * (i/1000)) + size.height()/2
            painter.drawPoint(x, y)

        painter.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwin = PainterPi()
    mainwin.show()
    sys.exit(app.exec_())