import sys
import os
import mysql
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QFileDialog, QMainWindow, QMessageBox , QLineEdit,QApplication,QPushButton, QVBoxLayout, QWidget, QDialog
from UI.Ui_Login import Ui_Login
from UI.Ui_register import Ui_Register
from UI.Ui_forget_widget import Ui_forget_widget
import pymysql

#主登录界面 最开始显示的窗口 其余的登陆界面 在按钮点击后被显示
class loginForm(QDialog, Ui_Login):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)#隐藏边框
        self.setAttribute(Qt.WA_TranslucentBackground)#透明背景
        self.setupUi(self)
        self.btn_Close.clicked.connect(self.btn_Close_clicked)#关闭窗口槽函数
        self.btnLogin.clicked.connect(self.btnLogin_clicked)#登录槽函数
        self.btnSignin.clicked.connect(self.btnSignin_clicked)#注册槽函数
        self.btnLogin_2.clicked.connect(self.btnLogin_2_clicked)#找回密码槽函数
        self.LogincheckBox.stateChanged.connect(self.Toggle_LogincheckBox)#是否显示密码



    def btnLogin_clicked(self):#登录
        username = self.txtUserName.text()
        password = self.txtPassword.text()
        # 连接到MySQL数据库
        connection = pymysql.connect(host='localhost', user='root', password='123456', database='py')
        cursor = connection.cursor()
        try:
            # 查询会员表
            cursor.execute('SELECT * FROM vip WHERE Vnumber=%s AND Vpassword=%s', (username, password))
            member_result = cursor.fetchone()

            # 查询管理员表
            cursor.execute('SELECT * FROM manage WHERE Mnumber=%s AND Mpassword=%s', (username, password))
            admin_result = cursor.fetchone()

            if member_result:
                QMessageBox.information(self, '登录结果', '会员登录成功')
            elif admin_result:
                QMessageBox.information(self, '登录结果', '管理员登录成功')
            else:
                QMessageBox.warning(self, '登录结果', '用户名或密码错误')
        finally:
            # 关闭数据库连接
            cursor.close()
            connection.close()

    def btnSignin_clicked(self):#注册窗口
        print("btnSign is clicked")
        self.hide()
        self.register_window = RegisterForm()  # 实例化注册窗口
        self.register_window.show()  # 显示注册窗口
        self.register_window.raise_()



    def btnLogin_2_clicked(self):#忘记 密码窗口
        print("btnForget is clicked")
        self.hide()
        self.forget_window = ForgetForm()
        self.forget_window.show()
        self.forget_window.raise_()

    def Toggle_LogincheckBox(self):#是否显示密码 默认不显示
        print("check box clicked")
        if self.LogincheckBox.isChecked():
            self.txtPassword.setEchoMode(QLineEdit.Normal)
        else:
            self.txtPassword.setEchoMode(QLineEdit.Password)
    def btn_Close_clicked(self):
        print("btnClose is pushed")
        QCoreApplication.instance().quit()#关闭程序 结束整个事件循环

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
class ForgetForm(QWidget,Ui_forget_widget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)#隐藏边框
        self.setAttribute(Qt.WA_TranslucentBackground)#透明背景
        self.setupUi(self)
        self.cancel_pushButton.clicked.connect(self.btnCancel_clicked)#取消注册槽函数
        # 连接 MySQL 数据库
        self.cnx = pymysql.connect(
            host="localhost",
            user="root",
            password="123456",
            database="py"
        )
    def btnCancel_clicked(self):
        print("btnCancel clicked")
        self.close()
        window.show()

    def confirmChanges(self):
        username = self.acc_lineEdit.text()
        contact = self.email_lineEdit.text()
        password = self.pass_lineEdit.text()
        confirm_password = self.pass2_lineEdit.text()

        # 检查密码和确认密码是否一致
        if password != confirm_password:
            QMessageBox.warning(self, "Warning", "密码和确认密码不一致")
            return

        # 根据用户名和联系方式查找并修改数据库内容
        cursor = self.cnx.cursor()
        update_query = "UPDATE vip SET Vpassword = %s WHERE Vno = %s AND Vphone = %s"
        data = (password, username, contact)
        cursor.execute(update_query, data)
        self.cnx.commit()
        cursor.close()
        # 设置完毕后显示成功信息
        QMessageBox.information(self, "Success", "修改成功")

        # 清空输入框
        self.acc_lineEdit.clear()
        self.email_lineEdit.clear()
        self.pass_lineEdit.clear()
        self.pass2_lineEdit.clear()

        # 关闭窗口
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
class RegisterForm(QDialog,Ui_Register):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)#隐藏边框
        self.setAttribute(Qt.WA_TranslucentBackground)#透明背景
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.btnCancel_clicked)#取消注册槽函数
    def btnCancel_clicked(self):
        print("btnCancel clicked")
        self.close()
        window.show()
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
    window = loginForm()
    window.show()
    sys.exit(app.exec_())

