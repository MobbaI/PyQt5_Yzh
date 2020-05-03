import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIntValidator, QDoubleValidator, QRegExpValidator
from PyQt5.QtCore import QRegExp


class Qvalidator(QWidget):
    def __init__(self):
        super(Qvalidator, self).__init__()
        self.initUI()

    def initUI(self):
        lineedit1 = QLineEdit()
        lineedit2 = QLineEdit()
        lineedit3 = QLineEdit()

        # 整数验证
        intValidator = QIntValidator(self)
        # 如何1到111?
        intValidator.setRange(1, 99)

        # 正则验证
        regvalidator = QRegExpValidator(self)
        reg = QRegExp("^[A-Z][0-9]{2}$")
        regvalidator.setRegExp(reg)

        # 浮点型验证
        doubleValidator = QDoubleValidator(self)
        doubleValidator.setRange(-99, 99)
        # 作用是什么
        doubleValidator.setNotation(QDoubleValidator.StandardNotation)
        doubleValidator.setDecimals(2)

        lineedit1.setValidator(intValidator)
        lineedit2.setValidator(regvalidator)
        lineedit3.setValidator(doubleValidator)

        lineedit2.setPlaceholderText('字母数字数字')

        formlayout = QFormLayout()
        formlayout.addRow('数字', lineedit1)
        formlayout.addRow('正则', lineedit2)
        formlayout.addRow('两位小数', lineedit3)

        self.setLayout(formlayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    qvalidator = Qvalidator()
    qvalidator.show()
    sys.exit(app.exec_())