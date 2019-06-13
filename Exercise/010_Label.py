from PyQt5.QtWidgets import QLabel,QProgressBar,QTextEdit,QWidget,QApplication,QLineEdit,QPushButton,QVBoxLayout,QHBoxLayout
from PyQt5.QtCore import Qt
import sys

class MyWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        
        

    def initUI(self):

        #ラベルの生成(文字列)
        self.label1=QLabel(self)
        self.label1.setText("abcdefg")
        
        #ラベルの生成(数値)
        self.label2=QLabel(self)
        self.label2.setNum(123456789)
        self.label2.setAlignment(Qt.AlignTop | Qt.AlignCenter)

        #ラベルの生成(文字の位置を右下に設定)
        self.label3=QLabel(self)
        self.label3.setText("ABCDEFG")
        self.label3.setAlignment(Qt.AlignBottom | Qt.AlignRight)

        #消去ボタン
        button = QPushButton("消去", self)
        button.clicked.connect(self.onClick)

        #配置
        vBox = QVBoxLayout()
        vBox.addWidget(self.label1)
        vBox.addWidget(self.label2)
        vBox.addWidget(self.label3)
        vBox.addWidget(button)
        self.setLayout(vBox)

        self.show()

    def onClick(self,*e):
        
        self.label1.clear()
        self.label2.clear()
        self.label3.clear()
        
if __name__=="__main__":
    app=QApplication(sys.argv)
    window=MyWidget()
    sys.exit(app.exec_())

