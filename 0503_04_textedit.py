import sys
from PyQt5.QtWidgets import *


class Textedit(QWidget):
    def __init__(self):
        super(Textedit, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('TextEdit')
        self.resize(300, 400)

        self.textedit = QTextEdit()
        button1 = QPushButton('显示纯文本')
        button2 = QPushButton('显示HTML')
        button3 = QPushButton('获取纯文本')
        button4 = QPushButton('获取HTML')

        button1.clicked.connect(self.on_clicked_button1)
        button2.clicked.connect(self.on_clicked_button2)
        button3.clicked.connect(self.on_clicked_button3)
        button4.clicked.connect(self.on_clicked_button4)

        vlayout = QVBoxLayout()
        vlayout.addWidget(self.textedit)
        vlayout.addWidget(button1)
        vlayout.addWidget(button2)
        vlayout.addWidget(button3)
        vlayout.addWidget(button4)

        self.setLayout(vlayout)

    def on_clicked_button1(self):
        self.textedit.setPlainText('Hello PyQt5\nI\'m fine')

    def on_clicked_button2(self):
        self.textedit.setHtml('<font color="blue" size="20">Hello PyQt5\nI\'m fine</font>')

    def on_clicked_button3(self):
        print(self.textedit.toPlainText())

    def on_clicked_button4(self):
        print(self.textedit.toHtml())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    textwin = Textedit()
    textwin.show()
    sys.exit(app.exec_())