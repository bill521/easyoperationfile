
from PyQt5 import QtCore

class WorkerThread(QtCore.QThread):
    """工作线程类"""
    def __init__(self, excel_utils_class):
        super(WorkerThread, self).__init__()
        self.excel_utils_class = excel_utils_class

    def run(self):
        self.excel_utils_class.console()

    def stop(self):
        # 停止工作线程
        self.stop()