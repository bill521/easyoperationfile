
import datetime
from PyQt5 import QtCore

class LoggerThread(QtCore.QThread):
    log_signal = QtCore.pyqtSignal(str)

    def __init__(self, state, message):
        super().__init__()
        self.state = state
        self.message = message

    def run(self):
        # 获取当前时间并格式化
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"{self.state} [{current_time}] {self.message}"
        self.log_signal.emit(log_message)