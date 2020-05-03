import sys
from PyQt5.QtWidgets import *


class QlineEditEchoMode(QWidget):
    def __init__(self):
        super(QlineEditEchoMode, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('文本输入框的回显模式')

        formlayout = QFormLayout()

        lineedit1 = QLineEdit(self)
        lineedit2 = QLineEdit(self)
        lineedit3 = QLineEdit(self)
        lineedit4 = QLineEdit(self)

        # 表单布局
        formlayout.addRow('Normal', lineedit1)
        formlayout.addRow('Echo', lineedit2)
        formlayout.addRow('Password', lineedit3)
        formlayout.addRow('PasswordEchoOnEdit', lineedit4)

        lineedit1.setPlaceholderText('Normal')
        lineedit2.setPlaceholderText('Echo')
        lineedit3.setPlaceholderText('Password')
        lineedit4.setPlaceholderText('PasswordEchoOnEdit')

        lineedit1.setEchoMode(QLineEdit.Normal)
        lineedit2.setEchoMode(QLineEdit.NoEcho)
        lineedit3.setEchoMode(QLineEdit.Password)
        lineedit4.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.setLayout(formlayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    lineeditechomode = QlineEditEchoMode()
    lineeditechomode.show()
    sys.exit(app.exec_())