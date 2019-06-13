from PyQt5.QtWidgets import QSlider,QProgressBar,QWidget,QApplication,QVBoxLayout,QHBoxLayout
from PyQt5.QtCore import Qt
import sys

class MyWidget(QWidget):

    def __init__(self):
        super().__init__()
        
        self.progress_bar = None
        
        self.initUI()
        
        

    def initUI(self):

        #プログレスバー生成
        self.progress_bar=QProgressBar(self)
        
        #スライダーバー
        slider = QSlider(Qt.Horizontal,self)
        slider.valueChanged.connect(self.onChange)

        #配置
        vBox = QVBoxLayout()
        vBox.addWidget(self.progress_bar)
        vBox.addWidget(slider)
        self.setLayout(vBox)

        self.show()

    def onChange(self,*e):
    
        self.progress_bar.setValue(e[0])

if __name__=="__main__":
    app=QApplication(sys.argv)
    window=MyWidget()
    sys.exit(app.exec_())

