from PyQt5.QtWidgets import QWidget,QApplication,QPushButton,QHBoxLayout,QVBoxLayout
import sys

class MyWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):

        # ボタンを生成
        # buttons = {
        #   "L":  [Button, Button, ...],
        #   "CL": [...],
        #   "C":  [...]
        #   ...
        # }

        buttons = {}
        for name in ("L","CL","C","CR","R"):
            buttons[name] = [ QPushButton(name+"_"+str(i),self) for i in range(4) ]  
        
        # レイアウトウィジェット
        hBox = QHBoxLayout()
        vBoxes = {}
        
        # 各列に対してボタンを設置し，
        for name in ("L","CL","C","CR","R"):

            # vBoxレイアウトウィジェットの生成
            vBoxes[name] = QVBoxLayout()

            # ボタンを縦に4つvBoxにセット
            for i in range(4):
                vBoxes[name].addWidget(buttons[name][i])

            # vBoxをhBoxにセット
            hBox.addLayout(vBoxes[name])
            
            # vBox間にスペースを入れる
            if name!="R":
                hBox.addSpacing(10)

            # CLとCの間に伸縮スペースを入れる            
            if name=="CL":
                hBox.addStretch(100)

        self.setLayout(hBox) #vBoxをMyWidgetに追加

        self.show()

if __name__=="__main__":
    app=QApplication(sys.argv)
    window=MyWidget()
    sys.exit(app.exec_())

