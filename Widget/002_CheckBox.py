from PyQt5.QtWidgets import QWidget,QApplication,QCheckBox,QHBoxLayout
import sys

class MyWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):

        #チェックボックスの生成
        check = QCheckBox("check",self)
        check.stateChanged.connect(self.onChange)
        check.toggle()

        #チェックボックスの配置
        hBox=QHBoxLayout()
        hBox.addWidget(check)
        self.setLayout(hBox)
        
        self.show()

    def onChange(self,*e):
        """
        Parameters
        ------------
        e: (int,)
            2=チェックが付いている
            0=チェックが付いていない
        """

        print("change.")
        print(e)

if __name__=="__main__":
    app=QApplication(sys.argv)
    window=MyWidget()
    sys.exit(app.exec_())

