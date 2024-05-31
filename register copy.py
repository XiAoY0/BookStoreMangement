import re
import sys
import os
import pymysql
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QFileDialog, QMainWindow, QMessageBox , QLineEdit,QApplication,QPushButton, QVBoxLayout, QWidget, QDialog
from UI.Ui_Login import Ui_Login
from UI.Ui_register import Ui_Register
from UI.Ui_forget_widget import Ui_forget_widget

class RegisterForm(QDialog,Ui_Register):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)#隐藏边框
        self.setAttribute(Qt.WA_TranslucentBackground)#透明背景
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.btnCancel_clicked)#取消注册槽函数
        # 连接MySQL数据库
        self.connection = pymysql.connect(
            host="localhost",
            user="root",
            password="110+120+z",
            database="bookmanage"
        )
        self.cursor = self.connection.cursor()
    def registerUser(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        confirm_password = self.lineEdit_3.text()
        contact = self.lineEdit_4.text()

        # 验证密码确认
        if password != confirm_password:
            QMessageBox.warning(self, "Error", "密码输入不一致")
            return

        # 检查重复用户名
        self.cursor.execute("SELECT * FROM vip WHERE  Vno=?", (username,))
        existing_user = self.cursor.fetchone()
        if existing_user:
            QMessageBox.warning(self, "Error", "用户名已存在")
            return

        # 验证联系方式格式
        if not re.match(r'^[1-9]\d{10}$', contact):  # 简单验证手机号格式
            QMessageBox.warning(self, "Error", "联系方式格式不正确")
            return

        # 在这里执行插入数据库的逻辑
        try:
            self.cursor.execute("INSERT INTO vip (Vno, Vpassword, Vphone) VALUES (?, ?, ?)",
                                (username, password, contact))
            self.connection.commit()
            QMessageBox.information(self, "Success", "用户注册成功")
            self.close()  # 注册成功后关闭对话框
        except Exception as e:
            print("用户注册失败:", e)
            QMessageBox.warning(self, "Error", "用户注册失败")

    def closeEvent(self, event):
        # 关闭数据库连接
        if self.connection.is_connected():
            self.cursor.close()
            self.connection.close()

    def btnCancel_clicked(self):
        print("btnCancel clicked")
        self.close()
    # 重写移动，点击事件 使能够拖动透明背景移动 不要删
    def mouseMoveEvent(self, e: QMouseEvent):  
        if self._tracking:
            self._endPos = e.pos() - self._startPos
            self.move(self.pos() + self._endPos)
    def mousePressEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._startPos = QPoint(e.x(), e.y())
            self._tracking = True
    def mouseReleaseEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._tracking = False
            self._startPos = None
            self._endPos = None
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = RegisterForm()
    window.show()
    sys.exit(app.exec_())      