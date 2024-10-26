
import sys

from PyQt5.QtWidgets import QMainWindow, QApplication

from untitled import Ui_MainWindow  # 导入设计界面


class mainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(mainWindow, self).__init__()
        self.setupUi(self)  # 初始化窗口


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = mainWindow()
    ui.show()
    sys.exit(app.exec_())
