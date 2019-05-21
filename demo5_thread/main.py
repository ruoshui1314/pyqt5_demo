import sys 	
from PyQt5.QtWidgets import QApplication , QMainWindow
from Ui_MainFrame import Ui_MainWindow

from worker import Worker

class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):    
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.worker = Worker()
        self.worker.sinOut.connect(self.updateText)
        self.worker.start()

    def updateText(self, txt):
        self.label.setText(txt)

if __name__=="__main__":  
    app = QApplication(sys.argv)  
    myWin = MyMainWindow()  
    myWin.show()  
    sys.exit(app.exec_())  