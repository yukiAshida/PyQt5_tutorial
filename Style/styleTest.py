from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.Qt import *
import sys
from ui_mainwindow import Ui_MainWindow

class StyleTest(QMainWindow):
    def __init__(self, parent=None):
        super(StyleTest, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.loadStyleSheet('coffee')

    def loadStyleSheet(self, sheetName):
        file = QFile('%s.qss' % sheetName.lower())
        file.open(QFile.ReadOnly)

        styleSheet = file.readAll()
        styleSheet = str(styleSheet, encoding='utf8')

        print(styleSheet)
        QApplication.instance().setStyleSheet(styleSheet)

if __name__ == '__main__':


    app = QApplication(sys.argv)

    button = StyleTest()
    button.show()
    sys.exit(app.exec_())