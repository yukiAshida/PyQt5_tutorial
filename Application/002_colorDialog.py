from PyQt5.QtWidgets import QWidget,QApplication,QPushButton,QHBoxLayout,QVBoxLayout,QLabel,QFrame
from PyQt5.QtGui import QColor
from PyQt5.Qt import QColorDialog
import sys

#from PyQt5.QtGui import *
#from PyQt5.Qt import *

class MyWidget(QWidget):

    def __init__(self):
        super().__init__()

        self.label = None
        self.frame = None

        self.initUI()
        
    def initUI(self):

        color_button = QPushButton('Select Color', self)
        color_button.clicked.connect(self.colorDialog)

        self.label = QLabel(self)
        self.frame = QFrame(self)

        # ボタンを設置
        vBox = QVBoxLayout()
        vBox.addWidget(color_button)

        # ラベル・フレームを設置
        hBox = QHBoxLayout()
        hBox.addWidget(self.label)
        hBox.addWidget(self.frame)
        vBox.addLayout(hBox)

        self.setLayout(vBox)
        self.show()
        

    def colorDialog(self,*e):

        # ダイアログを表示する
        getcolor = QColorDialog.getColor()
        
        # ラベルに色名を設定
        self.label.setText(getcolor.name())
        
        # フレームに色を設定
        style_color = "background-color: {0}".format(getcolor.name())
        self.frame.setStyleSheet("QWidget { "+style_color+" }")
        

if __name__ =='__main__':
    
    App = QApplication(sys.argv)
    window = MyWidget()
    sys.exit(App.exec_())