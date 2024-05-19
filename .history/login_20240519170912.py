import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QFileDialog, QMainWindow, QMessageBox , QLineEdit,QApplication,QPushButton, QVBoxLayout, QWidget, QDialog
from Ui_Login import Ui_Login
from Ui_register import Ui_Register
from Ui_forget_widget import Ui_forget_widget

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
        print("btnLogin is clicked")

    def btnSignin_clicked(self):#注册窗口
        print("btnSign is clicked")
        self.close()  # 关闭主窗口
        print("btnSign is clicked")
        self.show()
        register_window = RegisterForm()  # 实例化注册窗口
        register_window.show()  # 显示注册窗口
        register_window.raise_()

    def btnLogin_2_clicked(self):#忘记 密码窗口
        print("btnForget is clicked")

    def Toggle_LogincheckBox(self):#是否显示密码 默认不显示
        print("check box clicked")
        if self.LogincheckBox.isChecked():
            self.txtPassword.setEchoMode(QLineEdit.Normal)
        else:
            self.txtPassword.setEchoMode(QLineEdit.Password)
    def btn_Close_clicked(self):
        print("btnClose is pushed")
        QCoreApplication.instance().quit()#关闭窗口

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

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = loginForm()
    window.show()
    sys.exit(app.exec_())