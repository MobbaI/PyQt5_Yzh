import sys
from PyQt5.QtWidgets import QApplication, QVBoxLayout,QHBoxLayout, QFormLayout, QPushButton, QLineEdit, QWidget,\
    QTextEdit, QLabel, QFileDialog
from PyQt5.QtGui import QIntValidator
import openpyxl
import os

class DeleteExcel(QWidget):
    def __init__(self):
        super(DeleteExcel, self).__init__()
        self.fname = ''
        # self.minrow = ''
        # self.maxrow = ''
        # self.mincol = ''
        # self.maxcol = ''
        # self.sheetname = ''
        self.initUI()

    def initUI(self):
        self.setWindowTitle('DeleteExcel')

        h1widget = QWidget()
        h2widget = QWidget()
        fwidget = QWidget()
        v1widget = QWidget()

        self.label1 = QLabel('路径：')
        self.lineedit1 = QLineEdit()
        self.lineedit1.setReadOnly(True)
        self.button1 = QPushButton('...')

        self.button1.clicked.connect(self.on_click_button1)

        h1layout = QHBoxLayout(h1widget)
        h1layout.addWidget(self.label1)
        h1layout.addWidget(self.lineedit1)
        h1layout.addWidget(self.button1)

        self.lineedit2 = QLineEdit()
        self.lineedit3 = QLineEdit()
        self.lineedit4 = QLineEdit()
        self.lineedit5 = QLineEdit()
        self.lineedit6 = QLineEdit()
        intvalidator = QIntValidator()
        self.lineedit3.setValidator(intvalidator)
        self.lineedit4.setValidator(intvalidator)
        self.lineedit5.setValidator(intvalidator)
        self.lineedit5.setPlaceholderText('暂时没做奥')
        self.lineedit6.setValidator(intvalidator)
        self.lineedit6.setPlaceholderText('暂时没做奥')
        flayout = QFormLayout(fwidget)
        flayout.addRow('表单名：', self.lineedit2)
        flayout.addRow('开始行：', self.lineedit3)
        flayout.addRow('结束行：', self.lineedit4)
        flayout.addRow('开始列：', self.lineedit5)
        flayout.addRow('结束列：', self.lineedit6)

        self.textedit = QTextEdit()
        self.textedit.setReadOnly(True)
        self.button2 = QPushButton('运行')
        self.button2.clicked.connect(self.on_click_button2)
        v1layout = QVBoxLayout(v1widget)
        v1layout.addWidget(self.textedit)
        v1layout.addWidget(self.button2)

        h2layout = QHBoxLayout(h2widget)
        h2layout.addWidget(fwidget)
        h2layout.addWidget(v1widget)

        v2layout = QVBoxLayout()
        v2layout.addWidget(h1widget)
        v2layout.addWidget(h2widget)

        self.setLayout(v2layout)

    def on_click_button1(self):
        self.fname, _ = QFileDialog.getOpenFileName(self, '选择Excel文件', '.', '*.xlsx')
        self.lineedit1.setText(self.fname)

    def on_click_button2(self):
        _sheetname = self.lineedit2.text()
        _minrow = self.lineedit3.text()
        _maxrow = self.lineedit4.text()
        self.deleterow(_sheetname, _minrow, _maxrow)

    def deleterow(self, sheetname, minrow, maxrow):
        if self.fname:
            wb = openpyxl.load_workbook(self.fname)
            try:
                ws = wb[sheetname]
            except KeyError:
                self.textedit.setPlainText('表单名(Sheet)不存在')
                return
            if minrow and maxrow and int(maxrow) >= int(minrow):
                rows = int(maxrow) - int(minrow) + 1
                ws.delete_rows(int(minrow), rows)
                fname = self.fname.rstrip('.xlsx')
                wb.save('{}_new.xlsx'.format(fname))
                self.textedit.setPlainText('运行完成')
                os.startfile(os.path.dirname(self.fname))
            else:
                self.textedit.setPlainText('请正确输入行数')
        else:
            self.textedit.setPlainText('请选择Excel文件')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demain = DeleteExcel()
    demain.show()
    sys.exit(app.exec_())