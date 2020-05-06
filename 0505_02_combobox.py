import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt


class Combobox(QWidget):
    def __init__(self):
        super(Combobox, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QComboBox')
        self.resize(300, 120)
        vlayout = QVBoxLayout()
        self.label1 = QLabel('语言选择：')
        self.cb = QComboBox()
        self.cb.addItems(['C语言', 'Python', 'Java', 'Go'])
        self.cb.currentIndexChanged.connect(self.selectionChange)
        self.label2 = QLabel('感兴趣程度：')
        self.cb2 = QComboBox()
        # 能否编辑默认是False
        self.cb2.setEditable(True)
        self.cb2.addItems(['喜欢', '超爱', '无感', '厌恶'])

        vlayout.addWidget(self.label1)
        vlayout.addWidget(self.cb)
        vlayout.addWidget(self.label2)
        vlayout.addWidget(self.cb2)

        self.setLayout(vlayout)

    # 默认传入当前索引
    def selectionChange(self, i):
        newlabel1 = '语言选择：' + self.cb.currentText()
        self.label1.setText(newlabel1)
        # 根据内容自适应大小
        self.label1.adjustSize()
        for count in range(self.cb.count()):
            print('item' + str(count) + '=' + self.cb.itemText(count))
        print('当前索引：', i, '，编程：', self.cb.currentText())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    combowin = Combobox()
    combowin.show()
    sys.exit(app.exec_())