import sys
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QPushButton, QLabel, QWidget, QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


class Restore(QMainWindow):
    def __init__(self):
        super(Restore, self).__init__()
        self.setUI()

    def setUI(self):
        self.setWindowTitle('hahaha')
        self.resize(300, 400)
        self.button1 = QPushButton('按钮')
        self.label1 = QLabel('标签')
        self.label1.setFont(QFont('HeiTi', 20))
        self.label1.setAlignment(Qt.AlignCenter)
        layout = QVBoxLayout()
        layout.addWidget(self.button1)
        layout.addWidget(self.label1)

        mainFrame = QWidget()
        mainFrame.setLayout(layout)

        self.setCentralWidget(mainFrame)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    restore = Restore()
    restore.show()
    sys.exit(app.exec_())