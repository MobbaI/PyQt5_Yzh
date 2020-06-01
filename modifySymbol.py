import sys
from PyQt5.QtWidgets import QApplication, QVBoxLayout,QHBoxLayout, QPushButton, QLineEdit, QWidget, QLabel, \
    QCheckBox, QFileDialog, QMessageBox
from PyQt5.QtCore import QThread, pyqtSignal
import openpyxl
import os
import re


class DeleteNot(QWidget):
    def __init__(self):
        super(DeleteNot, self).__init__()
        self.fname = ''
        self.initUI()

    def initUI(self):
        self.setWindowTitle('修改标识符')
        self.setFixedSize(350, 120)

        hwidget_1 = QWidget()
        hwidget_2 = QWidget()

        self.lineedit = QLineEdit()
        self.lineedit.setReadOnly(True)
        self.button_1 = QPushButton('...')

        self.button_1.clicked.connect(self.on_click_button_1)

        hlayout_1 = QHBoxLayout(hwidget_1)
        hlayout_1.addWidget(self.lineedit)
        hlayout_1.addWidget(self.button_1)
        # hlayout_1.setStretch(0, 10)
        # hlayout_1.setStretch(1, 1)

        self.checkbox1 = QCheckBox('运行')
        self.checkbox2 = QCheckBox('UI')
        self.checkbox3 = QCheckBox('模型')
        self.checkbox4 = QCheckBox('场景')
        self.checkbox1.setCheckState(2)
        self.checkbox2.setCheckState(2)
        self.checkbox3.setCheckState(2)
        self.checkbox4.setCheckState(2)
        self.button_2 = QPushButton('运行')

        self.button_2.clicked.connect(self.on_click_button_2)

        hlayout_2 = QHBoxLayout(hwidget_2)
        hlayout_2.addWidget(self.checkbox1)
        hlayout_2.addWidget(self.checkbox2)
        hlayout_2.addWidget(self.checkbox3)
        hlayout_2.addWidget(self.checkbox4)
        hlayout_2.addWidget(self.button_2)

        vlayout = QVBoxLayout()
        vlayout.addWidget(hwidget_1)
        vlayout.addWidget(hwidget_2)

        self.setLayout(vlayout)

    def on_click_button_1(self):
        self.fname, _ = QFileDialog.getOpenFileName(self, '选择Excel文件', '.', '*.xlsx')
        self.lineedit.setText(os.path.basename(self.fname))

    def on_click_button_2(self):
        if not(self.fname) or (self.checkbox1.checkState() == 0 and self.checkbox2.checkState() == 0 and
                               self.checkbox3.checkState() == 0 and self.checkbox4.checkState() == 0):
            QMessageBox.information(self, '提示', '请选择')
        else:
            self.button_1.setEnabled(False)
            self.button_2.setEnabled(False)
            wb = openpyxl.load_workbook(self.fname)
            try:
                ws = wb['测试记录']
            except:
                pass
            self.modify1 = ModifySymbol('U', self.checkbox1.checkState())
            self.modify2 = ModifySymbol('W', self.checkbox2.checkState())
            self.modify3 = ModifySymbol('X', self.checkbox3.checkState())
            self.modify4 = ModifySymbol('Y', self.checkbox4.checkState())


class ModifySymbol(QThread):
    sinOut = pyqtSignal(int)

    def __init__(self, column, checkbox_state):
        super(ModifySymbol, self).__init__()
        self.column = column
        self.checkbox_state = checkbox_state

    def run(self):



if __name__ == '__main__':
    app = QApplication(sys.argv)
    deletenot = DeleteNot()
    deletenot.show()
    sys.exit(app.exec_())