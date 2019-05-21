import time
from PyQt5.QtCore import QThread, pyqtSignal

class Worker(QThread):
    sinOut = pyqtSignal(str)

    def __init__(self):
        super(Worker, self).__init__()
        self.num = 0
        self.__running = True

    def run(self):
        while self.__running:
            self.num += 1
            self.sinOut.emit('test:' + str(self.num))
            time.sleep(3)