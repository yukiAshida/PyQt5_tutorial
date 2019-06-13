from PyQt5.QtWidgets import QWidget,QApplication,QSlider,QPushButton,QLabel,QHBoxLayout
from PyQt5.QtCore import Qt
import sys

class MyWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):

        #スライダーの生成
        slider = QSlider(Qt.Horizontal,self)
        #slider = QSlider(Qt.Vertical,self)
        
        slider.valueChanged.connect(self.onChange)

        #スライダーの配置
        hBox=QHBoxLayout()
        hBox.addWidget(slider)
        self.setLayout(hBox)

        self.show()

    def onChange(self,*e):
        """
        Parameters
        ------------
        e: (int,)
            スライダーの相対位置（0～99）
        """

        print("change")
        print(e)

if __name__=="__main__":
    app=QApplication(sys.argv)
    window=MyWidget()
    sys.exit(app.exec_())

