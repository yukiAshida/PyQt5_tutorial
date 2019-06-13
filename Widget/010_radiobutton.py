from PyQt5.QtWidgets import QWidget,QApplication,QPushButton,QVBoxLayout,QHBoxLayout,QRadioButton,QButtonGroup
import sys

class MyWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        
        

    def initUI(self):

        #性別用のラジオボタンを生成
        sex_man=QRadioButton("男",self)
        sex_woman=QRadioButton("女",self)
        sex_man.clicked.connect(lambda e: self.onClick(e,"man"))
        sex_woman.clicked.connect(lambda e: self.onClick(e,"woman"))

        #性別ボタンをグループ化
        sex_group=QButtonGroup()
        sex_group.addButton(sex_man)
        sex_group.addButton(sex_woman)

        #年齢用のラジオボタンを生成
        age_young=QRadioButton("20歳未満",self)
        age_senior=QRadioButton("20歳以上",self)
        age_young.clicked.connect(lambda e: self.onClick(e,"under20"))
        age_senior.clicked.connect(lambda e: self.onClick(e,"over20"))

        #年齢ボタンをグループ化
        age_group=QButtonGroup()
        age_group.addButton(age_young)
        age_group.addButton(age_senior)

        #ラジオボタンを配置( ラジオグループを配置するわけではないので注意 )
        hBox1=QHBoxLayout()
        hBox1.addWidget(sex_man)
        hBox1.addWidget(sex_woman)

        hBox2=QHBoxLayout()
        hBox2.addWidget(age_young)
        hBox2.addWidget(age_senior)

        vBox=QVBoxLayout()
        vBox.addLayout(hBox1)
        vBox.addLayout(hBox2)
        self.setLayout(vBox)

        self.show()    

    def onClick(self, *e):
        """
        e: (bool,)
            なんか常にTrueが返ってくる
            識別用の値をlambdaで渡すべし
        """
        
        print(e)

if __name__=="__main__":
    app=QApplication(sys.argv)
    window=MyWidget()
    sys.exit(app.exec_())




