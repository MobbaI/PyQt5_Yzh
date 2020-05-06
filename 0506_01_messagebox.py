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
        self.resize(300, 400)

        self.button1 = QPushButton('关于')
        self.button2 = QPushButton('消息')
        self.button3 = QPushButton('提问')
        self.button4 = QPushButton('错误')
        self.button5 = QPushButton('警告')
        self.button6 = QPushButton('自定义')

        # gif标签添加，想到就试试，够辣够下饭
        self.label = QLabel()
        self.movie = QMovie('E:\CS-害羞.gif')
        self.label.setMovie(self.movie)
        self.movie.start()

        self.button1.clicked.connect(self.openDialog)
        self.button2.clicked.connect(self.openDialog)
        self.button3.clicked.connect(self.openDialog)
        self.button4.clicked.connect(self.openDialog)
        self.button5.clicked.connect(self.openDialog)
        self.button6.clicked.connect(self.openDialog)

        vlayout = QVBoxLayout()
        vlayout.addWidget(self.button1)
        vlayout.addWidget(self.button2)
        vlayout.addWidget(self.button3)
        vlayout.addWidget(self.button4)
        vlayout.addWidget(self.button5)
        vlayout.addWidget(self.button6)
        vlayout.addWidget(self.label)

        self.setLayout(vlayout)

    def openDialog(self):
        text = self.sender().text()
        # 直接调用静态方法
        if text == '关于':
            QMessageBox.about(self, '关于', '这是一个关于对话框！')
        # 非静态调用，且修改提示框图标
        elif text == '消息':
            # QWidget parent, title, text, buttons, defaultButton
            temp = QMessageBox()
            temp.setWindowIcon(QIcon('E:\p1.ico'))
            temp.information(temp, '消息', '这是一个消息对话框', QMessageBox.No | QMessageBox.Yes, QMessageBox.No)
        elif text == '提问':
            QMessageBox.question(self, '提问', '这是一个提问对话框', QMessageBox.No | QMessageBox.Yes)
        elif text == '错误':
            QMessageBox.critical(self, '错误', '这是一个错误对话框', QMessageBox.No | QMessageBox.Yes)
        elif text == '警告':
            QMessageBox.warning(self, '警告', '这是一个警告对话框', QMessageBox.Ignore | QMessageBox.Abort)
        # 非静态，自定义提示框
        else:
            self.inform = QMessageBox()
            self.inform.setWindowTitle('hello_world')
            self.inform.setText('世界你好hahahahahahahahah')
            self.inform.addButton('取消', QMessageBox.NoRole)
            self.inform.addButton(QPushButton('确定'), QMessageBox.YesRole)
            # self.inform.setIcon(1)
            self.inform.setIconPixmap(QPixmap('E:\\旧时\\秀智\\0zHN-fyixhyw8009997.jpg'))
            self.inform.setWindowIcon(QIcon('E:\p1.ico'))
            self.inform.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwin = Messagebox()
    mainwin.show()
    sys.exit(app.exec_())