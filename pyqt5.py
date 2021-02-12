import sys
from PyQt5.QtWidgets import QApplication, QWidget

class MyApp(QWidget):
    def __init__(self):
        super().__init__() # 기반 클래스(QWidget) 초기화
        """
         __init__없으면 기반 클래스 초기화는 자동으로 수행하지만 
         지금처럼 수동으로 정의할 때에는 기반 클래스 초기화를 위해 
         별도의 지정이 필요하다
        """
        self.initUI()

    def initUI(self):
        self.setWindowTitle('My First Application')
        self.move(300,300)
        self.resize(400,200)
        self.show()


app = QApplication(sys.argv)
ex = MyApp()
sys.exit(app.exec_())
