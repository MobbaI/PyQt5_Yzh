from PyQt5.QtWidgets import *
import sys
from PyQt5.QtCore import Qt


class QlabelBuddy(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QlabelBuddy')
        self.initUI()

    def initUI(self):
        label1 = QLabel('&Name', self)
        label2 = QLabel('&Age', self)
        lineedit1 = QLineEdit(self)
        lineedit2 = QLineEdit(self)
        lineedit1.setPlaceholderText('输入名字')
        lineedit2.setPlaceholderText('输入年龄')

        label1.setBuddy(lineedit1)
        label2.setBuddy(lineedit2)

        button1 = QPushButton('确定', self)
        button2 = QPushButton('取消', self)

        mainlayout = QGridLayout()
        mainlayout.addWidget(label1, 0, 0)
        mainlayout.addWidget(label2, 1, 0, Qt.AlignRight)
        mainlayout.addWidget(lineedit1, 0, 1, 1, 2)
        mainlayout.addWidget(lineedit2, 1, 1, 1, 2)
        mainlayout.addWidget(button1, 2, 1)
        mainlayout.addWidget(button2, 2, 2)

        self.setLayout(mainlayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QlabelBuddy()
    main.show()
    sys.exit(app.exec_())