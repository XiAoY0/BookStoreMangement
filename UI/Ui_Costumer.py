# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\code\mysql\BookStore - 副本\UI_Source\Costumer.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_Customer(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1300, 758)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 1291, 651))
        self.frame.setStyleSheet("/*??*/\n"
"QWidget\n"
"{\n"
"color: rgb(50,76,108);  /*????*/\n"
"background-color: rgb(206,220,237); /*???*/\n"
"\n"
"}\n"
"QWidget#Contents\n"
"{\n"
"    color: rgb(50,76,108);  /*????*/\n"
"    background-color: rgb(206,220,237); /*???*/\n"
"}\n"
"/*??????*/\n"
"QPushButton#btnLogin,#btnLogout,#btnHide,#btnUpdate,#btnSure,#btnAdd,#btnDel\n"
"{\n"
"    background-color:rgba(189,209,233);/*???*/\n"
"    min-height:30px; /*????*/\n"
"    min-width:180px; /*????*/\n"
"    border-style:solid;/*???? solid?? none??? inset/outset 3D??*/\n"
"    border-width:4px; /*??????*/\n"
"    border-radius:10px;/*????????*/\n"
"    border-color:rgba(127,154,184);/*????*/\n"
"    font-size:12pt;/*?? ????*/\n"
"    color: rgb(50,76,108);/*????*/\n"
"    padding:6px; /*??*/\n"
"}\n"
"/*??????*/\n"
"QPushButton:pressed\n"
"{\n"
"    background-color:rgba(192,240,255);/*???*/\n"
"    border-color:rgba(127,154,184);/*????*/\n"
"    border-style:solid;/*???? solid?? none??? inset/outset 3D??*/\n"
"    color: rgb(50,76,108);/*????*/\n"
"}\n"
"/*??????*/\n"
"QPushButton#btnLogin:hover,#btnLogout:hover,#btnHide:hover,#btnUpdate:hover,#btnSure:hover,#btnAdd:hover,#btnDel:hover\n"
"{\n"
"    background-color:rgba(192,221,244);/*???*/\n"
"    border-color:rgba(127,154,184);/*????*/\n"
"    color: rgb(50,76,108);/*????*/\n"
"}\n"
"QLineEdit\n"
"{\n"
"    background-color:rgb(206,220,237);/*???*/\n"
"    min-height:30px; /*????*/\n"
"    min-width:180px; /*????*/\n"
"    border-style:solid;/*???? solid?? none??? inset/outset 3D??*/\n"
"    border-width:4px; /*??????*/\n"
"    border-radius:10px;/*????????*/\n"
"    border-color:rgba(127,154,184);/*????*/\n"
"    font-size:12pt;/*?? ????*/\n"
"    color: rgb(50,76,108);/*????*/\n"
"    padding:6px;/*??*/\n"
"}\n"
"QCheckBox\n"
"{\n"
"    color:rgb(50,76,108);/*????*/\n"
"    background-color:rgb(206,220,237);/*???*/\n"
"}\n"
"QComboBox\n"
"{\n"
"    background-color:rgb(206,220,237);\n"
"    color:rgb(50,76,108);/*????*/\n"
"    border-style:solid;/*???? solid?? none??? inset/outset 3D??*/\n"
"    border-width:4px;/*??????*/\n"
"    border-radius:10px;/*????????*/\n"
"    border-color:rgba(127,154,184);/*????*/\n"
"    min-height:35px; /*????*/\n"
"    font-size:12pt;\n"
"}\n"
"/*??????????*/\n"
"QComboBox::drop-down\n"
"{\n"
"     width:20px;\n"
"     border:none;\n"
"     background:transparent;\n"
" }\n"
"/*????????*/\n"
"QComboBox::down-arrow\n"
"{\n"
"    image:url(:/image/array_down.png);\n"
"}\n"
"/*??????????*/\n"
"QComboBox QAbstractItemView\n"
"{\n"
" background-color: rgb(206,220,237); /*???*/\n"
"    color: rgb(50,76,108);/*????*/\n"
"outline:none;\n"
"}\n"
"/*??????item*/\n"
"QComboBox QAbstractItemView::item\n"
"{\n"
"    height:30px;\n"
"    color:rgb(50,76,108);/*????*/\n"
"}\n"
"/*???item??*/\n"
"QComboBox QAbstractItemView::item:selected\n"
"{\n"
"    background-color:rgb(206,220,237); /*???*/\n"
"    color:rgb(50,76,108);/*????*/\n"
"}\n"
"QLabel\n"
"{\n"
"    color:rgb(50,76,108);/*????*/\n"
"font-size:12pt;\n"
"border:none;/*????*/\n"
"}\n"
"QTabWidget\n"
"{\n"
"    background-color: rgb(206,220,237); /*???*/\n"
"    color:rgb(50,76,108);/*????*/\n"
"}\n"
"QTabBar::tab\n"
"{\n"
"    background-color:rgb(206,220,237); /*???*/\n"
"    color:rgb(50,76,108);/*????*/\n"
"    font-size:12pt;/*????*/\n"
"    height:30px; /*??*/\n"
"    min-width:100px;/*??*/\n"
"    border-top-left-radius:4px;/*??????????*/\n"
"    border-top-right-radius:4px;/*??????????*/\n"
"    margin-right: 5px;/*???  ????*/\n"
"    padding-left:5px;/*???--????*/\n"
"    padding-right:5px;/*???--????*/\n"
"}\n"
"QTabBar::tab:hover\n"
"{\n"
"    background-color: rgb(206,220,237); /*???*/\n"
"}\n"
"QTabBar::tab:selected\n"
"{\n"
"    background-color: rgb(189,209,233); /*???*/\n"
"}\n"
"QTableView,QTableWidget{\n"
"    background-color:rgb(206,220,237); /*???*/\n"
"    color:rgb(50,76,108);/*????*/\n"
"    selection-background-color:rgba(192,221,244);/*???*/;/*??????*/\n"
"    border:1px solid #E0DDDC;/*???1?????*/\n"
"    gridline-color:lightgray;/*????????????????*/\n"
"    font:bold 12pt;/*?? ????*/\n"
"}\n"
"/*??????*/\n"
"QHeaderView::section{\n"
"    background-color:rgb(206,220,237); /*???*/\n"
"    border:0px solid #E0DDDC;/*????????0??????????*/\n"
"    border-bottom:1px solid #E0DDDC;/*??????????????????????Table?????????2px?????*/\n"
"    min-height:30px;;/*????*/\n"
"    font-size:12pt;/*????*/\n"
"}\n"
"QTreeWidget,QTreeView\n"
"{\n"
"    background-color:rgb(206,220,237); /*???*/\n"
"    color:rgb(50,76,108);/*????*/\n"
"    selection-background-color:rgba(5,23,200);/*??????*/\n"
"    font-size:12pt;/*????*/\n"
"}\n"
"/*????*/\n"
"QTreeWidget::branch:has-children:!has-siblings:closed,\n"
"QTreeWidget::branch:closed:has-children:has-siblings {\n"
"    border-image: none;\n"
"    image: url(:/image/add-line_horizontal.png);\n"
"}\n"
"/*????*/\n"
"QTreeWidget::branch:open:has-children:!has-siblings,\n"
"QTreeWidget::branch:open:has-children:has-siblings  {\n"
"    border-image: none;\n"
"    image: url(:/image/array_down.png);\n"
"}\n"
"/*????*/\n"
"QTreeView::branch:has-children:!has-siblings:closed,\n"
"QTreeView::branch:closed:has-children:has-siblings {\n"
"    border-image: none;\n"
"    image: url(:/image/add-line_horizontal.png);\n"
"}\n"
"/*????*/\n"
"QTreeView::branch:open:has-children:!has-siblings,\n"
"QTreeView::branch:open:has-children:has-siblings  {\n"
"    border-image: none;\n"
"    image: url(:/image/array_down.png);\n"
"}\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.btn_Close = QtWidgets.QPushButton(self.frame)
        self.btn_Close.setEnabled(True)
        self.btn_Close.setGeometry(QtCore.QRect(1270, 10, 20, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_Close.sizePolicy().hasHeightForWidth())
        self.btn_Close.setSizePolicy(sizePolicy)
        self.btn_Close.setMinimumSize(QtCore.QSize(20, 20))
        self.btn_Close.setMaximumSize(QtCore.QSize(20, 20))
        self.btn_Close.setStyleSheet("QPushButton\n"
"{\n"
"background:#FF6694;\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background:#FF0000;\n"
"}\n"
"\n"
"")
        self.btn_Close.setText("")
        self.btn_Close.setObjectName("btn_Close")
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 20, 137, 621))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setStyleSheet("\n"
"QLabel::hover{\n"
"    color: rgb(255, 102, 148);\n"
"}")
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget)
        self.label_12.setStyleSheet("\n"
"QLabel::hover{\n"
"    color: rgb(255, 102, 148);\n"
"}")
        self.label_12.setObjectName("label_12")
        self.verticalLayout.addWidget(self.label_12)
        self.label_13 = QtWidgets.QLabel(self.layoutWidget)
        self.label_13.setStyleSheet("\n"
"QLabel::hover{\n"
"    color: rgb(255, 102, 148);\n"
"}")
        self.label_13.setObjectName("label_13")
        self.verticalLayout.addWidget(self.label_13)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget)
        self.label_11.setStyleSheet("\n"
"QLabel::hover{\n"
"    color: rgb(255, 102, 148);\n"
"}")
        self.label_11.setObjectName("label_11")
        self.verticalLayout.addWidget(self.label_11)
        self.label_14 = QtWidgets.QLabel(self.layoutWidget)
        self.label_14.setStyleSheet("\n"
"QLabel::hover{\n"
"    color: rgb(255, 102, 148);\n"
"}")
        self.label_14.setObjectName("label_14")
        self.verticalLayout.addWidget(self.label_14)
        self.tableWidget_Admin = QtWidgets.QTableWidget(self.frame)
        self.tableWidget_Admin.setGeometry(QtCore.QRect(180, 80, 1101, 551))
        self.tableWidget_Admin.setStyleSheet("")
        self.tableWidget_Admin.setObjectName("tableWidget_Admin")
        self.tableWidget_Admin.setColumnCount(0)
        self.tableWidget_Admin.setRowCount(0)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(1180, 20, 61, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(200, 19, 431, 52))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(1060, 20, 115, 51))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_3.addWidget(self.pushButton_3)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(950, 20, 100, 51))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_4.addWidget(self.pushButton_4)
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(780, 20, 166, 51))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_5.addWidget(self.pushButton_6)
        self.pushButton_5 = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_5.addWidget(self.pushButton_5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1300, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_8.setText(_translate("MainWindow", "<a href='http://baidu.com'><html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">我的信息</span></p></body></html></a>"))
        self.label_12.setText(_translate("MainWindow", "<a href='http://baidu.com'><html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">购书界面</span></p></body></html></a>"))
        self.label_11.setText(_translate("MainWindow", "<a href='http://baidu.com'><html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">购物车</span></p></body></html></a>"))
        self.label_14.setText(_translate("MainWindow", "<a href='http://baidu.com'><html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">收藏夹</span></p></body></html></a>"))
        self.label_13.setText(_translate("MainWindow", "<a href='http://baidu.com'><html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">历史购书</span></p></body></html></a>"))
        self.pushButton_2.setText(_translate("MainWindow", "删除"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "输入查询内容"))
        self.pushButton.setText(_translate("MainWindow", "查询"))
        self.pushButton_3.setText(_translate("MainWindow", "添加到购物车"))
        self.pushButton_4.setText(_translate("MainWindow", "添加到收藏夹"))
        self.pushButton_6.setText(_translate("MainWindow", "退书"))
        self.pushButton_5.setText(_translate("MainWindow", "结算"))
