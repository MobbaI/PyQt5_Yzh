import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt


class Messagebox(QWidget):
    def __init__(self):
        super(Messagebox, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Messagebox')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwin = Messagebox()
    mainwin.show()
    sys.exit(app.exec_())