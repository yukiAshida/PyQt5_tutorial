from PyQt5.QtWidgets import QWidget,QApplication,QPushButton,QHBoxLayout
import sys

class MyWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):

        #ボタンの生成
        button = QPushButton("button",self)
        button.clicked.connect(self.onClick)
        
        #ボタンの配置
        hBox=QHBoxLayout()
        hBox.addWidget(button)
        self.setLayout(hBox)

        self.show()

    def onClick(self,*e):

        print("close.")
        self.close()

if __name__=="__main__":

    app=QApplication(sys.argv)
    window=MyWidget()
    app.exec_()

    print("Application continues ...")

