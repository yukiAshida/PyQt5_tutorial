"""
ウインドウを出すだけ
"""

from PyQt5.QtWidgets import QWidget,QApplication
import sys

class MyWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
    
    #初期化処理
    def initUI(self):
        self.show()

if __name__=="__main__":
    app=QApplication(sys.argv)
    window=MyWidget()
    sys.exit(app.exec_())

