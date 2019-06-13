from PyQt5.QtWidgets import QTextEdit,QWidget,QApplication,QLineEdit,QTextEdit,QPushButton,QVBoxLayout,QHBoxLayout
from PyQt5.QtCore import Qt
import sys

class MyWidget(QWidget):

    def __init__(self):
        super().__init__()
        
        self.line = None
        self.line_content = None
        self.text = None
        self.text_content = None

        self.initUI()

    def initUI(self):

        #ラインボックス
        self.line=QLineEdit(self)
        self.line.setText("initial line.")
        self.line.textChanged[str].connect(self.onChange)
        #line.setReadOnly(True)

        #テキストボックス
        self.text=QTextEdit(self)
        self.text.setText("initial text.")
        #text.setReadOnly(True)

        #送信ボタン
        button=QPushButton("送信")
        button.clicked.connect(self.onClick)

        #配置
        vBox = QVBoxLayout()
        vBox.addWidget(self.line)
        vBox.addWidget(self.text)
        vBox.addWidget(button)
        self.setLayout(vBox)

        self.show()

    def onChange(self, *e):
        print(e)

    def onClick(self, *e):
        
        l_extracted = self.line.text()
        t_extracted = self.text.toPlainText()

        print(l_extracted)
        print(t_extracted)


if __name__=="__main__":
    app=QApplication(sys.argv)
    window=MyWidget()
    sys.exit(app.exec_())

