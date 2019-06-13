from PyQt5.QtWidgets import QSizePolicy,QHBoxLayout,QWidget,QApplication,QPushButton,QCheckBox,QGridLayout,QSizePolicy
import sys

class MyWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):

        #ボタン1は縦方向伸縮可能
        button1=QPushButton("button1",self)
        button1.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Expanding)

        #ボタン2は横方向伸縮可能
        button2=QPushButton("button2",self)
        button2.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Fixed)

        hBox=QHBoxLayout()
        hBox.addWidget(button1)
        hBox.addWidget(button2)
        self.setLayout(hBox)

        self.show()

if __name__=="__main__":
    app=QApplication(sys.argv)
    window=MyWidget()
    sys.exit(app.exec_())

