import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt, QRegExp


class Filedialog(QWidget):
    def __init__(self):
        super(Filedialog, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Filedialog')

        self.button1 = QPushButton('加载图片')
        self.button1.clicked.connect(self.loadimage)
        self.label = QLabel()

        self.button2 = QPushButton('显示内容')
        self.button2.clicked.connect(self.loadtext)
        self.textedit = QTextEdit()
        self.textedit.setReadOnly(True)

        vlayout = QVBoxLayout()
        vlayout.addWidget(self.button1)
        vlayout.addWidget(self.label)
        vlayout.addWidget(self.button2)
        vlayout.addWidget(self.textedit)

        self.setLayout(vlayout)

    def loadimage(self):
        # 标题，默认路径，文件类型规定，返回路径和类型规定
        # 打开文件窗口，类型选项里怎么设置下拉？
        fname, _ = QFileDialog.getOpenFileName(self, '打开图片', 'E:/', '图像文件(*.jpg *.png *.gif)')
        if fname.endswith('.gif'):
            movie = QMovie(fname)
            self.label.setMovie(movie)
            movie.start()
        else:
            self.label.setPixmap(QPixmap(fname))

    def loadtext(self):
        fdialog = QFileDialog()
        # 不太懂奥
        # 设置打开任何文件
        # fdialog.setFileMode(QFileDialog.AnyFile)
        # fdialog.setFilter(QDir.Files)

        if fdialog.exec_():
            filenames = fdialog.selectedFiles()
            f = open(filenames[0], 'r')
            with f:
                data = f.read()
                self.textedit.setText(data)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwin = Filedialog()
    mainwin.show()
    sys.exit(app.exec_())