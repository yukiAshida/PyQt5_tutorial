from PyQt5.QtWidgets import QWidget,QApplication,QPushButton,QCheckBox,QGridLayout,QSizePolicy,QTextEdit
import sys

class MyWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):

        #===グリッドを生成・設置
        grid=QGridLayout()

        # テキストボックスを配置
        # addWidget( Widget, x, y, height, widget )
        grid.addWidget(QTextEdit(),0,0)
        grid.addWidget(QTextEdit(),0,1)
        grid.addWidget(QTextEdit(),0,2)
        grid.addWidget(QTextEdit(),1,0,2,3)
        grid.addWidget(QTextEdit(),0,3,3,4)

        # setColumnStretch(row, stretch_rate)
        grid.setColumnStretch(0, 1)
        grid.setColumnStretch(1, 2)
        grid.setColumnStretch(2, 1)
        
        # setColumnStretch(column, stretch_rate)
        grid.setRowStretch(0, 2)
        grid.setRowStretch(1, 3)
        
        
            
        self.setLayout(grid)

        self.show()

if __name__=="__main__":
    app=QApplication(sys.argv)
    window=MyWidget()
    sys.exit(app.exec_())

