# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\code\mysql\BookStore\insert_Employ.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Insert_E(object):
    def setupUi(self, Insert):
        Insert.setObjectName("Insert")
        Insert.resize(381, 435)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Insert.sizePolicy().hasHeightForWidth())
        Insert.setSizePolicy(sizePolicy)
        self.frame = QtWidgets.QFrame(Insert)
        self.frame.setGeometry(QtCore.QRect(0, 10, 201, 411))
        self.frame.setStyleSheet("QFrame{\n"
"background-color: rgb(121, 121, 121);\n"
"border-radius:20px  ;\n"
"}\n"
"QLineEdit{\n"
"border-radius:6px  ;\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(242, 255, 210);\n"
"background-color: rgb(255, 170, 255);\n"
"font: 290 9pt \"Microsoft YaHei UI\";    \n"
"border-radius:3px  ;\n"
"}")
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(23)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setText("")
        self.lineEdit_2.setClearButtonEnabled(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setClearButtonEnabled(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout.addWidget(self.lineEdit_3)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_7.setInputMask("")
        self.lineEdit_7.setClearButtonEnabled(True)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.verticalLayout.addWidget(self.lineEdit_7)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_6.setClearButtonEnabled(True)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.verticalLayout.addWidget(self.lineEdit_6)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_5.setClearButtonEnabled(True)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.verticalLayout.addWidget(self.lineEdit_5)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_8.setClearButtonEnabled(True)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.verticalLayout.addWidget(self.lineEdit_8)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)

        self.retranslateUi(Insert)
        QtCore.QMetaObject.connectSlotsByName(Insert)

    def retranslateUi(self, Insert):
        _translate = QtCore.QCoreApplication.translate
        Insert.setWindowTitle(_translate("Insert", "Dialog"))
        self.lineEdit.setPlaceholderText(_translate("Insert", "员工编号"))
        self.lineEdit_2.setPlaceholderText(_translate("Insert", "员工姓名"))
        self.lineEdit_3.setPlaceholderText(_translate("Insert", "员工性别"))
        self.lineEdit_7.setPlaceholderText(_translate("Insert", "员工身份证号"))
        self.lineEdit_6.setPlaceholderText(_translate("Insert", "员工职位"))
        self.lineEdit_5.setPlaceholderText(_translate("Insert", "员工工资"))
        self.lineEdit_8.setPlaceholderText(_translate("Insert", "密码"))
        self.pushButton.setText(_translate("Insert", "录入"))
        self.pushButton_3.setText(_translate("Insert", "重置"))
        self.pushButton_2.setText(_translate("Insert", "取消"))
