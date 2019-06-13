from PyQt5.QtWidgets import QWidget,QApplication
import sys

class MyWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):

        #(x,y)の位置に幅width、高さheightのウインドウを表示
        x = 400
        y = 100
        width = 500
        height = 500
        self.setGeometry(x,y,width,height)
        
        self.show()

if __name__=="__main__":
    app=QApplication(sys.argv)
    window=MyWidget()
    sys.exit(app.exec_())

