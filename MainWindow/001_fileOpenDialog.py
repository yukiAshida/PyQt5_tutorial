# import sys
# from PyQt5.QtWidgets import *
# from PyQt5.QtGui import QIcon

from PyQt5.QtWidgets import QWidget,QApplication,QPushButton,QVBoxLayout,QTextEdit,QFileDialog,QAction,QMainWindow
from PyQt5.QtGui import QIcon
import sys


class MyWidget(QMainWindow):

    def __init__(self):
        super().__init__()

        self.text = None

        self.initUI()


    def initUI(self):

        
        self.text = QTextEdit()
        
        self.setCentralWidget(self.text)
        
        self.statusBar()

        # ファイルオープンアクションを生成
        openFile = QAction(QIcon('open.png'), '開く', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('新しいファイルを開く')
        openFile.triggered.connect(self.showDialog)

        # メニューバーにファイルオープンタブを追加
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&ファイル')
        fileMenu.addAction(openFile)

        self.show()


    def showDialog(self):

        fname = QFileDialog.getOpenFileName(self,'Open file', '/', filter="Image Files (*.csv *.txt *.html *.xml *.py *.pyw)")[0]


if __name__ == '__main__':

    App = QApplication(sys.argv)
    window = MyWidget()
    sys.exit(App.exec_())