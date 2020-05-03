# 控件提示消息
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QDesktopWidget, QPushButton, QWidget, QHBoxLayout, QToolTip
from PyQt5.QtGui import QFont

class TooltipForm(QWidget):
    def __int__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        Q