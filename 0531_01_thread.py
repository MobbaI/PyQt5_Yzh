import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class DemoThread(QWidget):
    def __init__(self):
        super(DemoThread, self).__init__()
        self.setWindowTitle('Thread')
        self.initUI()

    def initUI(self):
        self.thread = RunThread()

        self.button = QPushButton('开始')
        self.listw = QListWidget()

        vlayout = QVBoxLayout()
        vlayout.addWidget(self.listw)
        vlayout.addWidget(self.button)

        self.button.clicked.connect(self.buttonClicked)
        self.thread.sinOut.connect(self.listAdd)

        self.setLayout(vlayout)

    def listAdd(self, file_inf):
        self.listw.addItem(file_inf)
        if file_inf == 'Hello World 6':
            self.button.setEnabled(True)

    def buttonClicked(self):
        self.button.setEnabled(False)
        self.thread.start()


class RunThread(QThread):
    sinOut = pyqtSignal(str)

    def __init__(self):
        super(RunThread, self).__init__()
    #     self.working = True
    #
    # def __del__(self):
    #     self.working = False
    #     self.wait()

    def run(self):
        num = 0
        while num < 7:
            file_str = 'Hello World {}'.format(num)
            num += 1
            self.sinOut.emit(file_str)
            self.sleep(1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainw = DemoThread()
    mainw.show()
    sys.exit(app.exec_())