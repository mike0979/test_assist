from PyQt5.QtCore import QThread, pyqtSignal

class WorkThread(QThread):
    def __init__(self):
        self.interval = None
        self.is_send = True
        super(WorkThread, self).__init__()
    def run(self):
        pass

class HttpThread(WorkThread):
    s = pyqtSignal(str)
    def __init__(self):
        self.token = None
        super(HttpThread, self).__init__()
    def run(self):
        while self.is_send:
            self.s.emit(self.token)
            self.sleep(int(self.interval))

class TcpThread(WorkThread):
    s = pyqtSignal()
    def __init__(self):
        self.token = None
        super(TcpThread, self).__init__()
    def run(self):
        while self.is_send:
            self.s.emit()
            self.sleep(int(self.interval))