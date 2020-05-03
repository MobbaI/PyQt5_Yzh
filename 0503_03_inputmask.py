import sys
from PyQt5.QtWidgets import *


class InputMask(QWidget):
    def __init__(self):
        super(InputMask, self).__init__()
        self.initUI()

    def initUI(self):
        lineedit1 = QLineEdit()
        lineedit2 = QLineEdit()
        lineedit3 = QLineEdit()
        lineedit4 = QLineEdit()
        lineedit5 = QLineEdit()

        lineedit1.setInputMask('000.000.000.000;_')
        lineedit2.setInputMask('HH:HH:HH:HH:HH:HH:HH;_')
        lineedit3.setInputMask('0000-00-00')
        lineedit4.setInputMask('>AAAA-AAAA-AAAA-AAAA-AAAA;#')

        lineedit5.textChanged.connect(self.textChange)

        formlayout = QFormLayout()
        formlayout.addRow('数字掩码', lineedit1)
        formlayout.addRow('MAC掩码', lineedit2)
        formlayout.addRow('日期掩码', lineedit3)
        formlayout.addRow('许可证掩码', lineedit4)
        formlayout.addRow('文本变化', lineedit5)

        self.setLayout(formlayout)

    # Yzh：默认传入文本，无参也可
    def textChange(self, text):
        print('传入文本：' + text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    inputmask = InputMask()
    inputmask.show()
    sys.exit(app.exec_())