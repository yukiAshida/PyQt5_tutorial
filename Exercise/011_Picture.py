from PyQt5.QtWidgets import QLabel,QProgressBar,QTextEdit,QWidget,QApplication,QLineEdit,QPushButton,QVBoxLayout,QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import sys

class MyWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        
        

    def initUI(self):

        #画像をラベルに設置
        label=QLabel(self)
        pixmap=QPixmap(r"image/sky.jpg")
        label.setPixmap(pixmap)

        #配置
        hBox=QHBoxLayout()
        hBox.addWidget(label)
        self.setLayout(hBox)

        self.setGeometry(50,150,400,100)
        self.show()

if __name__=="__main__":
    app=QApplication(sys.argv)
    window=MyWidget()
    sys.exit(app.exec_())

