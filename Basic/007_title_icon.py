"""
ウインドウを出すだけ
"""

from PyQt5.QtWidgets import QWidget,QApplication
from PyQt5.QtGui import QIcon
import sys

class MyWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
    
    #初期化処理
    def initUI(self):

        # タイトル
        self.setWindowTitle("Application Title")

        # アイコン
        self.setWindowIcon(QIcon(r"image/python.png"))
        
        self.show()

if __name__=="__main__":
    app=QApplication(sys.argv)
    window=MyWidget()
    sys.exit(app.exec_())

