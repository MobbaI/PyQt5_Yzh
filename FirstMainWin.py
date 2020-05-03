import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QDesktopWidget, QPushButton, QWidget, QHBoxLayout
from PyQt5.QtGui import QIcon


class FirstMainWin(QMainWindow):
    def __init__(self):
        # 子类对象转为父类对象
        super(FirstMainWin, self).__init__()

        self.setWindowTitle('Hello World')
        # 屏幕尺寸
        self.resize(300, 300)

        # self.setWindowIcon(QIcon('E:/p1.ico'))
        '''
        self.status = self.statusBar()
        self.status.showMessage('5 seconds...', 5000)
        '''
        # 创建按钮
        self.button1 = QPushButton('退出')
        # 传递函数地址
        # self.button1.clicked.connect(self.onClick_Button)

        # 创建水平布局
        layout = QHBoxLayout()
        layout.addWidget(self.button1)

        # 创建框架
        mainFrame = QWidget()
        mainFrame.setLayout(layout)

        self.setCentralWidget(mainFrame)
    '''
    def onClick_Button(self):
        sender = self.sender()
        print(sender.text() + '按钮被按下')
        app = QApplication.instance()
        app.quit()
    '''
    '''
    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        newLeft = (screen.width() - size.width()) / 2
        newTop = (screen.height() - size.height()) / 3
        self.move(newLeft, newTop)
    '''


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('E:/p1.ico'))
    main = FirstMainWin()
    # main.center()
    main.show()
    sys.exit(app.exec_())