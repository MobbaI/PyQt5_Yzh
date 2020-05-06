import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt


class Dialog(QWidget):
    def __init__(self):
        super(Dialog, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QDialog')
        self.resize(400, 300)
        self.button = QPushButton('打开对话框', self)
        self.button.move(100, 100)
        self.button.clicked.connect(self.openDialog)

    # 刚开始没带self，只是临时变量，窗口一闪而过
    def openDialog(self):
        self.dialog = QDialog()
        self.dialog.setWindowTitle('对话框')
        self.dialog.resize(200, 150)
        button = QPushButton('关闭对话框', self.dialog)
        button.move(50, 50)
        button.clicked.connect(self.dialog.close)
        # exec方法默认为模态，堵塞线程
        # dialog.exec()
        # show方法默认为非模态，可以设置以下内容更改为模态
        self.dialog.setWindowModality(Qt.ApplicationModal)
        self.dialog.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwin = Dialog()
    mainwin.show()
    sys.exit(app.exec_())