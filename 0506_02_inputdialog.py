import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt, QRegExp


class Inputdialog(QWidget):
    def __init__(self):
        super(Inputdialog, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Inputdialog')

        self.button1 = QPushButton('语言')
        self.button2 = QPushButton('字符')
        self.button3 = QPushButton('整数')
        self.button4 = QPushButton('自定义')

        self.lineedit1 = QLineEdit()
        self.lineedit1.setReadOnly(True)
        self.lineedit2 = QLineEdit()
        self.lineedit3 = QLineEdit()
        self.lineedit3.setReadOnly(True)

        self.button1.clicked.connect(self.getItem)
        self.button2.clicked.connect(self.getText)
        self.button3.clicked.connect(self.getInt)
        self.button4.clicked.connect(self.getTwo)

        flayout = QFormLayout()
        flayout.addRow(self.button1, self.lineedit1)
        flayout.addRow(self.button2, self.lineedit2)
        flayout.addRow(self.button3, self.lineedit3)
        flayout.addRow(self.button4)

        self.setLayout(flayout)

    def getItem(self):
        items = ['C', 'Java', 'Python']
        getitem = QInputDialog()
        # 能否编辑默认是True
        item, ok = getitem.getItem(self, '请选择语言', '语言列表', items, editable=False)
        getitem.setComboBoxEditable(False)
        if ok and item:
            self.lineedit1.setText(item)

    def getText(self):
        text, ok = QInputDialog.getText(self, '文本输入框', '输入字符')
        if ok and text:
            self.lineedit2.setText(text)

    def getInt(self):
        num, ok = QInputDialog.getInt(self, '整数输入框', '输入整数')
        if ok and num:
            self.lineedit3.setText(str(num))

    def getTwo(self):
        dl = QDialog()
        dl.setWindowTitle('自定义窗口')
        lab1 = QLabel('日期：')
        lab2 = QLabel('月：')
        lab3 = QLabel('日：')
        linee1 = QSpinBox()
        linee1.setRange(1, 12)

        # 怎么使用正则不能输入0开头？
        # regvalidator = QRegExpValidator(self)
        # reg = QRegExp("^[1-9]")
        # regvalidator.setRegExp(reg)

        linee2 = QSpinBox()
        # 暂时用下
        linee2.setRange(1, 31)
        button = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.No, Qt.Horizontal)
        flayout2 = QFormLayout(dl)
        flayout2.addRow(lab1)
        flayout2.addRow(lab2, linee1)
        flayout2.addRow(lab3, linee2)
        flayout2.addRow(button)
        dl.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwin = Inputdialog()
    mainwin.show()
    sys.exit(app.exec_())