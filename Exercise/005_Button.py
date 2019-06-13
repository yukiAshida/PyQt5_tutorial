"""
* ボタンを設置する
* イベントを設定する
"""

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
        
        #トグルボタン
        toggle = QPushButton("toggle",self)
        toggle.clicked.connect(self.onClick)
        toggle.setCheckable(True)

        #ボタンの配置
        hBox=QHBoxLayout()
        hBox.addWidget(button)
        hBox.addWidget(toggle)
        self.setLayout(hBox)

        self.show()

    def onClick(self,*e):
        """
        Parameters
        -----------
        e: (bool,)
            押した後のボタンの状態（true=押されてる, flase=押されてない）
            普通のボタンの場合は常にfalseが返る
            トグルボタンの場合は
        """

        print("clicked.")
        print(e)

if __name__=="__main__":
    app=QApplication(sys.argv)
    window=MyWidget()
    sys.exit(app.exec_())

