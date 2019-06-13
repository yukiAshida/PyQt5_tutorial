from PyQt5.QtWidgets import QHBoxLayout,QSizePolicy,QWidget,QApplication,QPushButton,QCheckBox,QGridLayout,QSizePolicy
import sys

class MyWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):

        button1=QPushButton("button1",self)
        button2=QPushButton("button2",self)

        #ボタンからサイズポリシーを取り出す
        sizePolicy1=button1.sizePolicy()
        sizePolicy2=button2.sizePolicy()

        #サイズポリシーを2:3に設定
        sizePolicy1.setHorizontalStretch(2)
        sizePolicy2.setHorizontalStretch(3)

        #ボタンにサイズポリシーを再設定
        button1.setSizePolicy(sizePolicy1)
        button2.setSizePolicy(sizePolicy2)

        hBox=QHBoxLayout()
        hBox.addWidget(button1)
        hBox.addWidget(button2)
        self.setLayout(hBox)

        self.show()

if __name__=="__main__":
    app=QApplication(sys.argv)
    window=MyWidget()
    sys.exit(app.exec_())

