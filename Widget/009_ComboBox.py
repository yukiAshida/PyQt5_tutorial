from PyQt5.QtWidgets import QComboBox,QSplitter,QFrame,QLabel,QProgressBar,QTextEdit,QWidget,QApplication,QLineEdit,QPushButton,QVBoxLayout,QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import sys

class MyWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        
        

    def initUI(self):
        
        #コンボボックスを生成
        combo = QComboBox(self)
        combo.activated[str].connect(self.onActivate)

        for item in ["first","second","third","more"]:
            combo.addItem(item)

        #配置
        hBox=QHBoxLayout()
        hBox.addWidget(combo)
        self.setLayout(hBox)

        self.setGeometry(50,150,400,100)
        self.show()
    
    def onActivate(self, *e):
        """
        e: (str,)
            選択したアイテム名
        """
        
        print(e)

if __name__=="__main__":
    app=QApplication(sys.argv)
    window=MyWidget()
    sys.exit(app.exec_())

