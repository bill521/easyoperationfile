import datetime
import sys
from PyQt5.QtCore import pyqtSignal, QObject
from pyqt5_plugins.examplebuttonplugin import QtGui


class ExceptionHandler(QObject):

    error_occurred = pyqtSignal(str)  # 定义一个信号，参数类型为str

    def __init__(self, parent=None):
        super().__init__(parent)
        self.error_occurred.connect(self.handle_error)  # 连接信号到槽


    def handle_error(self, message, model, listView):

        # 获取当前时间并格式化
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # 创建带有时间戳的日志信息
        log_message = f"[{current_time}] {message}"

        # 将日志信息添加到 QListView
        item = QtGui.QStandardItem(log_message)
        model.appendRow(item)
        # 滚动到最新的日志
        listView.scrollToBottom()