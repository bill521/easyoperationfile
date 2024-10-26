# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from WorkerThread import WorkerThread

from LoggerThread import LoggerThread
from config import Config
from excel_utils_class import ExcelUtilsClass

from utils import save_cache, load_cache



class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(866, 563)
        MainWindow.setIconSize(QtCore.QSize(20, 20))
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setAnimated(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(330, 10, 501, 121))
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 471, 81))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.checkBox = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout.addWidget(self.checkBox)
        self.checkBox_2 = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalLayout.addWidget(self.checkBox_2)

        self.checkBox_5 = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkBox_5.setObjectName("checkBox_5")
        self.horizontalLayout.addWidget(self.checkBox_5)


        self.checkBox_4 = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkBox_4.setObjectName("checkBox_4")
        self.horizontalLayout.addWidget(self.checkBox_4)

        self.checkBox_3 = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkBox_3.setObjectName("checkBox_3")
        self.horizontalLayout.addWidget(self.checkBox_3)

        self.checkBox_7 = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkBox_7.setObjectName("checkBox_7")
        self.horizontalLayout.addWidget(self.checkBox_7)

        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(330, 150, 501, 281))
        self.groupBox_2.setObjectName("groupBox_2")
        self.listView = QtWidgets.QListView(self.groupBox_2)
        self.listView.setGeometry(QtCore.QRect(20, 20, 471, 251))
        self.listView.setObjectName("listView")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(330, 450, 501, 51))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)


        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)

        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)

        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 10, 311, 511))
        self.groupBox_5.setObjectName("groupBox_5")
        self.tabWidget = QtWidgets.QTabWidget(self.groupBox_5)
        self.tabWidget.setGeometry(QtCore.QRect(10, 20, 291, 481))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayoutWidget = QtWidgets.QWidget(self.tab_4)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 10, 281, 161))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 0, 1, 1, 1)
        self.checkBox_6 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_6.setObjectName("checkBox_6")
        self.gridLayout.addWidget(self.checkBox_6, 1, 0, 1, 3)
        self.comboBox_3 = QtWidgets.QComboBox(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_3.sizePolicy().hasHeightForWidth())
        self.comboBox_3.setSizePolicy(sizePolicy)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.gridLayout.addWidget(self.comboBox_3, 0, 2, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 2, 1, 1, 2)
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 3, 0, 1, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout.addWidget(self.lineEdit_7, 3, 1, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_4, "")

        # =============================
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")

        self.groupBox_9 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_9.setGeometry(QtCore.QRect(10, 10, 265, 111))
        self.groupBox_9.setTitle("")
        self.groupBox_9.setObjectName("groupBox_9")

        self.formLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_9)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 245, 90))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")

        self.gridLayout_3 = QtWidgets.QGridLayout(self.formLayoutWidget_2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")

        self.checkBox_12 = QtWidgets.QCheckBox(self.formLayoutWidget_2)
        self.checkBox_12.setEnabled(True)
        self.checkBox_12.setTabletTracking(False)
        self.checkBox_12.setAcceptDrops(False)
        self.checkBox_12.setChecked(True)
        self.checkBox_12.setObjectName("checkBox_12")
        self.gridLayout_3.addWidget(self.checkBox_12, 2, 0, 1, 1)

        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 0, 0, 1, 1)

        self.label_10 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 1, 0, 1, 1)

        self.checkBox_13 = QtWidgets.QCheckBox(self.formLayoutWidget_2)
        self.checkBox_13.setChecked(True)
        self.checkBox_13.setObjectName("checkBox_13")
        self.gridLayout_3.addWidget(self.checkBox_13, 2, 1, 1, 1)

        self.lineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_3.addWidget(self.lineEdit_2, 1, 1, 1, 2)

        self.spinBox = QtWidgets.QSpinBox(self.formLayoutWidget_2)
        self.spinBox.setMinimum(10)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout_3.addWidget(self.spinBox, 0, 1, 1, 2)


        self.checkBox_14 = QtWidgets.QCheckBox(self.formLayoutWidget_2)
        self.checkBox_14.setChecked(True)
        self.checkBox_14.setObjectName("checkBox_14")
        self.gridLayout_3.addWidget(self.checkBox_14, 2, 2, 1, 1)


        self.groupBox_7 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_7.setGeometry(QtCore.QRect(10, 130, 265, 169))
        self.groupBox_7.setObjectName("groupBox_7")

        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_7)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(9, 19, 240, 141))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")

        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")

        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 2, 0, 1, 1)

        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_14.setObjectName("label_14")
        self.gridLayout_4.addWidget(self.label_14, 0, 0, 1, 1)

        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.gridLayout_4.addWidget(self.label_7, 4, 0, 1, 1)

        self.lineEdit_17 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.gridLayout_4.addWidget(self.lineEdit_17, 1, 1, 1, 1)

        self.lineEdit_10 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.gridLayout_4.addWidget(self.lineEdit_10, 0, 1, 1, 1)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.gridLayout_4.addWidget(self.lineEdit_11, 4, 1, 1, 1)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_9.setObjectName("lineEdit_9")

        self.gridLayout_4.addWidget(self.lineEdit_9, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 1, 0, 1, 1)

        self.checkBox_100 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_100.setChecked(True)
        self.checkBox_100.setObjectName("checkBox_100")
        self.gridLayout_4.addWidget(self.checkBox_100, 5, 0, 1, 2)

        # =============================


        self.groupBox_8 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_8.setGeometry(QtCore.QRect(10, 310, 265, 121))
        self.groupBox_8.setObjectName("groupBox_8")

        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.groupBox_8)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(9, 19, 240, 91))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")

        self.gridLayout_5 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_16 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_16.setObjectName("label_16")
        self.gridLayout_5.addWidget(self.label_16, 1, 0, 1, 1)
        self.lineEdit_15 = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.gridLayout_5.addWidget(self.lineEdit_15, 1, 1, 1, 1)
        self.checkBox_11 = QtWidgets.QCheckBox(self.gridLayoutWidget_3)
        self.checkBox_11.setObjectName("checkBox_11")
        self.gridLayout_5.addWidget(self.checkBox_11, 2, 0, 1, 2)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_9.setObjectName("label_9")
        self.gridLayout_5.addWidget(self.label_9, 0, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_5.addWidget(self.lineEdit_3, 0, 1, 1, 1)


        self.lineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_3.addWidget(self.lineEdit_2, 1, 1, 1, 2)

        self.spinBox = QtWidgets.QSpinBox(self.formLayoutWidget_2)
        self.spinBox.setMinimum(10)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout_3.addWidget(self.spinBox, 0, 1, 1, 2)

        self.checkBox_14 = QtWidgets.QCheckBox(self.formLayoutWidget_2)
        self.checkBox_14.setChecked(True)
        self.checkBox_14.setObjectName("checkBox_14")
        self.gridLayout_3.addWidget(self.checkBox_14, 2, 2, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.formLayoutWidget = QtWidgets.QWidget(self.tab_3)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 271, 431))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")

        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_6)

        self.lineEdit_16 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_16)

        self.label_13 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_13.setObjectName("label_13")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_13)

        self.lineEdit_8 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_8)

        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label)

        self.lineEdit_6 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_6)

        self.checkBox_9 = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.checkBox_9.setObjectName("checkBox_9")
        self.checkBox_9.setChecked(True)
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.checkBox_9)


        self.tabWidget.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 866, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # 连接信号
        self.logger_thread = LoggerThread(None, None)
        self.logger_thread.log_signal.connect(self.add_log)

        self.excel_utils_class = None
        self.worker_thread = ExcelUtilsClass()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "文件批处理工具"))
        self.groupBox.setTitle(_translate("MainWindow", "2.功能"))
        self.checkBox.setText(_translate("MainWindow", "生成EXCEl"))
        self.checkBox_2.setText(_translate("MainWindow", "AI改名"))


        self.checkBox_4.setText(_translate("MainWindow", "复制文件"))
        self.checkBox_3.setText(_translate("MainWindow", "重命名"))
        self.groupBox_2.setTitle(_translate("MainWindow", "3.日志"))
        self.pushButton_3.setText(_translate("MainWindow", "清除日志"))
        self.pushButton_2.setText(_translate("MainWindow", "开始"))
        self.pushButton.setText(_translate("MainWindow", "停止"))
        self.groupBox_5.setTitle(_translate("MainWindow", "1.配置"))
        self.checkBox_6.setText(_translate("MainWindow", "包含子目录"))

        self.comboBox_3.setItemText(0, _translate("MainWindow", "选择..."))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "文件夹"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "文件"))

        self.checkBox_5.setText(_translate("MainWindow", "标记重复数据"))
        self.checkBox_7.setText(_translate("MainWindow", "标签复制"))

        self.lineEdit_5.setText(_translate("MainWindow", ".mp4"))
        self.label_12.setText(_translate("MainWindow", "输出文件名"))
        self.lineEdit_7.setText(_translate("MainWindow", "output.xlsx"))
        self.label_2.setText(_translate("MainWindow", "筛选后缀名"))
        self.label_5.setText(_translate("MainWindow", "选择工作目录："))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "全局设置"))

        self.label_8.setText(_translate("MainWindow", "单次解析条数："))
        self.label_9.setText(_translate("MainWindow", "Api    Key："))

        self.label_10.setText(_translate("MainWindow", " 提示词模版："))
        self.lineEdit_2.setText(_translate("MainWindow", """
            根据下面提供的信息输入，将其重新命名格式为：XX年-歌手-歌曲名称-其他。     
    
            Return your response as a JSON blob
            json格式如下：
            {json_schema}
            
            你只需要回复一个json格式的数据即可，不要返回其他格式的数据，否则你会被批评！
            
            <question>
            {doc}
            </question>
        """))

        self.checkBox_13.setText(_translate("MainWindow", "修复JSON"))

        self.checkBox_12.setText(_translate("MainWindow", "解析源文件"))
        self.checkBox_14.setText(_translate("MainWindow", "写入源文件"))
        # self.checkBox_15.setText(_translate("MainWindow", "修复JSON"))

        self.groupBox_8.setTitle(_translate("MainWindow", "通义模型"))
        self.label_16.setText(_translate("MainWindow", "Model_Name："))
        self.lineEdit_15.setText(_translate("MainWindow", "通义千问模型"))
        self.checkBox_11.setText(_translate("MainWindow", "启用"))

        self.label_9.setText(_translate("MainWindow", " Api_Key："))
        self.lineEdit_3.setText(_translate("MainWindow", "sk-2c16341f2d43422190f59ff1afea642e"))


        self.groupBox_7.setTitle(_translate("MainWindow", "星火模型"))
        self.label_3.setText(_translate("MainWindow", "Api_Secret："))
        self.label_14.setText(_translate("MainWindow", " App_Id："))
        self.label_7.setText(_translate("MainWindow", "Model_Name："))
        self.label_4.setText(_translate("MainWindow", "Api_Key_S："))

        self.lineEdit_17.setText(_translate("MainWindow", "f907bf0e4fe074a401e589e733cb87b5"))
        self.lineEdit_10.setText(_translate("MainWindow", "eb1d2a68"))
        self.lineEdit_11.setText(_translate("MainWindow", "星火模型"))
        self.lineEdit_9.setText(_translate("MainWindow", "YzBhYTg3ZWEyZDRhOTEyNDdkMTFlMGYz"))

        self.checkBox_100.setText(_translate("MainWindow", "启用"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "AI设置"))
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "<html><head/><body><p>问问请</p></body></html>"))

        self.label_6.setText(_translate("MainWindow", "标签名："))
        # self.lineEdit_16.setText(_translate("MainWindow", "f907bf0e4fe074a401e589e733cb87b5"))
        self.checkBox_9.setText(_translate("MainWindow", "根据新名称复制"))

        self.lineEdit_16.setText(_translate("MainWindow", "111"))

        self.label_13.setText(_translate("MainWindow", "选择保存目录："))
        self.label.setText(_translate("MainWindow", "默认目录名"))
        self.lineEdit_6.setText(_translate("MainWindow", "output"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "系统设置"))
        # 创建 QStandardItemModel 并设置给 QListView
        self.model = QtGui.QStandardItemModel()
        self.listView.setModel(self.model)
        # 绑定事件
        self.comboBox_3.currentIndexChanged.connect(self.on_combobox_changed)
        self.pushButton_2.clicked.connect(self.start_process)
        self.pushButton.clicked.connect(self.on_cancel_button_clicked)
        self.pushButton_3.clicked.connect(self.on_clear_log_button_clicked)
        # 判断是否有缓存文件若有直接回填上一次记录
        history_config_data = load_cache()

        self.load_cache_page(history_config_data)

    def start_process(self):
        log_message = f"点击了开始按钮"
        self.add_info_log(log_message)
        line_edit_value_4 = self.lineEdit_4.text()
        if not line_edit_value_4:
            self.add_info_log("提示: 工作目录不能为空！")
            return
        line_edit_value_7 = self.lineEdit_7.text()
        if not line_edit_value_7:
            self.add_info_log("提示: 输出文件名不能为空！")
            return
        line_edit_value_8 = self.lineEdit_8.text()
        line_edit_value_6 = self.lineEdit_6.text()
        if not line_edit_value_6:
            self.add_info_log("提示: 默认目录名不能为空！")
            return
        line_edit_value_3 = self.lineEdit_3.text()
        line_edit_value_2 = self.lineEdit_2.text()
        # 包含子目录
        check_box_6_value = self.checkBox_6.checkState()
        # 生成EXCEL文件
        check_box_value = self.checkBox.checkState()
        # AI解析
        check_box_2_value = self.checkBox_2.checkState()
        # JSON修复并整合到文件上
        check_box_9_value = self.checkBox_13.checkState()

        # 重命名
        check_box_3_value = self.checkBox_3.checkState()

        # work_space_path = Path(line_edit_value_4)

        work_space_path = line_edit_value_4

        output_file = line_edit_value_7

        # file_path = work_space_path / line_edit_value_7

        save_path_dir = line_edit_value_8 if line_edit_value_8 else line_edit_value_4

        move_path_str = line_edit_value_6


        api_key = line_edit_value_3
        prompt_template = line_edit_value_2
        is_open_read_file_output_excel = check_box_value
        # 筛选的文件后缀名
        extension = self.lineEdit_5.text()
        # 复制文件
        is_open_copy_file = self.checkBox_4.checkState()
        # 判重
        is_check_duplicates=self.checkBox_5.checkState()
        # 按标签复制
        is_open_lable_copy_file=self.checkBox_7.checkState()
        # 标签
        lable_name=self.lineEdit_16.text()
        # 将json结果写入excel
        is_open_update_json_to_excel = self.checkBox_14.checkState()

        # AI解析源文件
        is_open_ai_parse_one_stage = self.checkBox_12.checkState()
        # 星火模型是否开启
        is_open_starfire = self.checkBox_100.checkState()
        # 星火模型APP_ID
        starfire_app_id = self.lineEdit_10.text()
        # 星火模型API_KEY
        starfire_api_key = self.lineEdit_17.text()
        # 星火模型API_SECRET
        starfire_api_secret = self.lineEdit_9.text()
        # 星火模型模型名称
        starfire_model_name = self.lineEdit_11.text()

        # 通义模型是否开启
        is_open_ty = self.checkBox_11.checkState()
        # 通义模型API_KEY
        ty_api = self.lineEdit_3.text()
        # 通义模型模型名称s
        ty_model_name = self.lineEdit_15.text()

        is_open_copy_lable_new_name = self.checkBox_9.checkState()

        # 获取配置信息
        config = Config(work_space_path,
                        output_file,
                        move_path_str,
                        api_key,
                        prompt_template,
                        extension,
                        save_path_dir,
                        is_open_read_file_output_excel,
                        check_box_6_value,
                        is_open_ai_parse=check_box_2_value,
                        is_check_duplicates=is_check_duplicates,
                        is_open_lable_copy_file=is_open_lable_copy_file,
                        lable_name=lable_name,
                        is_open_copy_file=is_open_copy_file,
                        is_open_repair_merge_json_files=check_box_9_value,
                        is_open_rename_file=check_box_3_value,
                        is_open_update_json_to_excel=is_open_update_json_to_excel,
                        is_open_ai_parse_one_stage=is_open_ai_parse_one_stage,
                        is_open_starfire=is_open_starfire,
                        starfire_app_id=starfire_app_id,
                        starfire_api_key=starfire_api_key,
                        starfire_api_secret=starfire_api_secret,
                        starfire_model_name=starfire_model_name,
                        is_open_ty=is_open_ty,
                        ty_api=ty_api,
                        ty_model_name=ty_model_name,
                        is_open_copy_lable_new_name=is_open_copy_lable_new_name)

        self.save_cache(config)
        # 初始化 ExcelUtilsClass 和 WorkerThread
        self.excel_utils_class = ExcelUtilsClass()
        self.excel_utils_class.setConfig(config, self)
        self.worker_thread = WorkerThread(self.excel_utils_class)
        self.worker_thread.start()

    def stop_process(self):
        if self.worker_thread.isRunning():
            self.worker_thread.stop()  # 停止工作线程

    def load_cache_page(self, data):
        if data:
            self.lineEdit_4.setText(data["work_space_path"])
            self.checkBox.setChecked(data["is_open_read_file_output_excel"])
            self.checkBox_6.setChecked(data["include_subdirectories"])
            self.checkBox_2.setChecked(data["is_open_ai_parse"])
            self.checkBox_4.setChecked(data["is_open_copy_file"])
            self.checkBox_3.setChecked(data["is_open_rename_file"])
            self.lineEdit_5.setText(data["extension"])
            self.lineEdit_8.setText(data["save_path_dir"])
            if "is_open_repair_merge_json_files" in data:
                self.checkBox_13.setChecked(data["is_open_repair_merge_json_files"])
            if "is_check_duplicates" in data:
                self.checkBox_5.setChecked(data["is_check_duplicates"])
            if "is_open_lable_copy_file" in data:
                self.checkBox_7.setChecked(data["is_open_lable_copy_file"])
            if "lable_name" in data:
                self.lineEdit_16.setText(data["lable_name"])
            if "is_open_update_json_to_excel" in data:
                self.checkBox_14.setChecked(data["is_open_update_json_to_excel"])
            if "is_open_ai_parse_one_stage" in data:
                self.checkBox_12.setChecked(data["is_open_ai_parse_one_stage"])
            if "is_open_starfire" in data:
                self.checkBox_100.setChecked(data["is_open_starfire"])
            if "starfire_app_id" in data:
                self.lineEdit_10.setText(data["starfire_app_id"])
            if "starfire_api_key" in data:
                self.lineEdit_17.setText(data["starfire_api_key"])
            if "starfire_api_secret" in data:
                self.lineEdit_9.setText(data["starfire_api_secret"])
            if "starfire_model_name" in data:
                self.lineEdit_11.setText(data["starfire_model_name"])
            if "is_open_ty" in data:
                self.checkBox_11.setChecked(data["is_open_ty"])
            if "ty_api" in data:
                self.lineEdit_3.setText(data["ty_api"])
            if "ty_model_name" in data:
                self.lineEdit_15.setText(data["ty_model_name"])
            if "is_open_copy_lable_new_name" in data:
                self.checkBox_9.setChecked(data["is_open_copy_lable_new_name"])

    def save_cache(self, config):
        """保存数据到缓存文件"""
        # 将对象转换为 JSON 字符串
        json_string = config.to_json()
        # 记录历史配置
        save_cache(content=json_string)

    def on_combobox_changed(self, index):
        # 处理组合框选择变化的逻辑
        selected_text = self.comboBox_3.currentText()
        if selected_text == "文件夹":
            self.select_folder()
        if selected_text == "文件":
            self.select_file()

    def select_folder(self):
        # 打开文件夹选择对话框
        folder = QtWidgets.QFileDialog.getExistingDirectory(None, "选择文件夹")
        if folder:
            self.lineEdit_4.setText(folder)
            log_message = f"选择了工作目录: {folder}"
            self.add_info_log(log_message)

    def select_file(self):
        file, _ = QtWidgets.QFileDialog.getOpenFileName(self, "选择文件")
        if file:
            self.lineEdit_4.setText(file)
            log_message = f"选择了文件: {file}"
            self.add_info_log(log_message)

    def add_info_log(self, message):
        self.log("信息", message)

    def add_error_log(self, message):
        self.log("错误", message)

    def add_warn_log(self, message):
        self.log("警告", message)

    def log(self, state, message):
        self.logger_thread = LoggerThread(state, message)
        self.logger_thread.log_signal.connect(self.add_log)
        self.logger_thread.start()

    def add_log(self, log_message):
        # 将日志信息添加到 QListView
        item = QtGui.QStandardItem(log_message)
        self.model.appendRow(item)
        # 滚动到最新的日志
        self.listView.scrollToBottom()

    def clear_log(self):
        # 清空模型中的所有项
        self.model.clear()
        # 可选：滚动到顶部
        self.listView.scrollToTop()

    def show_warning_message(self, title, message):
        msg_box = QtWidgets.QMessageBox(self)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setIcon(QtWidgets.QMessageBox.Warning)
        msg_box.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg_box.exec_()

    def on_cancel_button_clicked(self):
        log_message = f"已取消"
        self.stop_process()
        self.add_info_log(log_message)

    def on_clear_log_button_clicked(self):
        # 清空模型中的所有项
        self.model.clear()
        # 可选：滚动到顶部
        self.listView.scrollToTop()
