from PyQt5.QtWidgets import QSplitter,QFrame,QLabel,QProgressBar,QTextEdit,QWidget,QApplication,QLineEdit,QPushButton,QVBoxLayout,QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import sys

class MyWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        
        

    def initUI(self):
        
        #テキストボックスを生成
        text={}
        text["L"]=QTextEdit(self)
        text["C"]=QTextEdit(self)
        text["R"]=QTextEdit(self)
        
        #スプリッターを生成
        splitter = QSplitter(Qt.Horizontal)
        for lcr in ("L","C","R"):
            splitter.addWidget(text[lcr])
        
        #配置
        hBox=QHBoxLayout()
        hBox.addWidget(splitter)
        self.setLayout(hBox)

        self.show()

if __name__=="__main__":
    app=QApplication(sys.argv)
    window=MyWidget()
    sys.exit(app.exec_())

