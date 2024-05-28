import sys
import os
import pymysql
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QFileDialog, QMainWindow, QMessageBox , QLineEdit,QApplication,QPushButton, QVBoxLayout, QWidget, QDialog,QLabel,QTableWidgetItem
from Ui_Login import Ui_Login
from Ui_register import Ui_Register
from Ui_forget_widget import Ui_forget_widget
from Ui_mainwindow import Ui_MainWindow
from Ui_Employee import Ui_MainWindow_E

# #自定义label的鼠标单击事件
# class ClickableLabel(QLabel):
#     def __init__(self, parent=None):
#         super().__init__(parent)

#     def mousePressEvent(self, event):
#         self.clicked.emit()

#     clicked = QtCore.pyqtSignal()

class MainwindowForm(QMainWindow,Ui_MainWindow):
    # clicked = QtCore.pyqtSignal()
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)#隐藏边框
        self.setAttribute(Qt.WA_TranslucentBackground)#透明背景
        self.setupUi(self)
        #self.adminWindow()#不能加self作为参数
        # self.Mysql_admin()
        # self.Mysql_employ()
        self.setFixedSize(1152,648)
        #槽函数绑定 主要是标签点击切换显示界面
        self.btn_Close.clicked.connect(self.btnClose_clicked)#关闭窗口函数
        self.pushButton_3.clicked.connect(self.btnInsert_clicked)#插入数据
        self.pushButton_5.clicked.connect(self.btnInsertLot_clicked)#批量导入数据
        self.pushButton_4.clicked.connect(self.btnOut_clicked)#导出数据
        self.pushButton_2.clicked.connect(self.btnDelete_clicked)#删除数据

        self.label_8.setOpenExternalLinks(False)
        self.label_8.linkActivated.connect(self.AdminWindowShow)
        self.label_13.setOpenExternalLinks(False)
        self.label_13.linkActivated.connect(self.EmployWindowShow)
        self.label_5.setOpenExternalLinks(False)
        self.label_5.linkActivated.connect(self.CustomerWindowShow)
        self.label_12.setOpenExternalLinks(False)
        self.label_12.linkActivated.connect(self.BookWindowShow)
        self.label_11.setOpenExternalLinks(False)
        self.label_11.linkActivated.connect(self.BookBuyWindowShow)
        self.label_14.setOpenExternalLinks(False)
        self.label_14.linkActivated.connect(self.BookBackWindowShow)
    # def Mysql_admin(self):#连接数据库
    #     conn = pymysql.Connect(host='localhost',user='root',passwd='110+120+z',database='bookmanage')
    #     cursor = conn.cursor()
    #     cursor.execute("select * from admin_info")
    #     data = cursor.fetchall()
    #     self.tableWidget_Admin.setRowCount(len(data))
    #     self.tableWidget_Admin.setColumnCount(len(data[0]))  # Assuming the number of columns is the same for all rows

    #     for row_index, row_data in enumerate(data):
    #         for col_index, col_data in enumerate(row_data):
    #             self.tableWidget_Admin.setItem(row_index, col_index, QTableWidgetItem(str(col_data)))
    #     cursor.close()
    #     conn.close()
    # def Mysql_employ(self):

    def btnInsertLot_clicked(self):
        print('Lots of logs to insert')
    def btnOut_clicked(self):
        print('btnOut is clicked')
    def btnDelete_clicked(self):
        print('btnDelete is clicked')
    def BookBackWindowShow(self):#退书记录
        print('BookBackWindowShow')
        conn = pymysql.Connect(host='localhost',user='root',passwd='110+120+z',database='bookmanage')
        cursor = conn.cursor()
        cursor.execute("select * from 退书记录")
        data = cursor.fetchall()
        self.tableWidget_Admin.setRowCount(len(data))
        self.tableWidget_Admin.setColumnCount(len(data[0]))  # Assuming the number of columns is the same for all rows

        for row_index, row_data in enumerate(data):
            for col_index, col_data in enumerate(row_data):
                self.tableWidget_Admin.setItem(row_index, col_index, QTableWidgetItem(str(col_data)))
        cursor.close()
        conn.close()
    def BookBuyWindowShow(self):# 购书记录
        print('BookBuyWindowShow')
        conn = pymysql.Connect(host='localhost',user='root',passwd='110+120+z',database='bookmanage')
        cursor = conn.cursor()
        cursor.execute("select * from 购买记录")
        data = cursor.fetchall()
        self.tableWidget_Admin.setRowCount(len(data))
        self.tableWidget_Admin.setColumnCount(len(data[0]))  # Assuming the number of columns is the same for all rows

        for row_index, row_data in enumerate(data):
            for col_index, col_data in enumerate(row_data):
                self.tableWidget_Admin.setItem(row_index, col_index, QTableWidgetItem(str(col_data)))
        cursor.close()
        conn.close()
    def BookWindowShow(self):# 图书
        print('BookWindowShow')
        conn = pymysql.Connect(host='localhost',user='root',passwd='110+120+z',database='bookmanage')
        cursor = conn.cursor()
        cursor.execute("select * from 图书")
        data = cursor.fetchall()
        self.tableWidget_Admin.setRowCount(len(data))
        self.tableWidget_Admin.setColumnCount(len(data[0]))  # Assuming the number of columns is the same for all rows

        for row_index, row_data in enumerate(data):
            for col_index, col_data in enumerate(row_data):
                self.tableWidget_Admin.setItem(row_index, col_index, QTableWidgetItem(str(col_data)))
        cursor.close()
        conn.close()
    def CustomerWindowShow(self):# 会员界面
        print('CustomerWindowShow')
        conn = pymysql.Connect(host='localhost',user='root',passwd='110+120+z',database='bookmanage')
        cursor = conn.cursor()
        cursor.execute("select * from 会员")
        data = cursor.fetchall()
        self.tableWidget_Admin.setRowCount(len(data))
        self.tableWidget_Admin.setColumnCount(len(data[0]))  # Assuming the number of columns is the same for all rows

        for row_index, row_data in enumerate(data):
            for col_index, col_data in enumerate(row_data):
                self.tableWidget_Admin.setItem(row_index, col_index, QTableWidgetItem(str(col_data)))
        cursor.close()
        conn.close()
    def EmployWindowShow(self): # 职工界面   
        print('EmployWindowShow')
        conn = pymysql.Connect(host='localhost',user='root',passwd='110+120+z',database='bookmanage')
        cursor = conn.cursor()
        cursor.execute("select * from 工作人员")
        data = cursor.fetchall()
        self.tableWidget_Admin.setRowCount(len(data))
        self.tableWidget_Admin.setColumnCount(len(data[0]))  # Assuming the number of columns is the same for all rows

        for row_index, row_data in enumerate(data):
            for col_index, col_data in enumerate(row_data):
                self.tableWidget_Admin.setItem(row_index, col_index, QTableWidgetItem(str(col_data)))
        cursor.close()
        conn.close()
    def AdminWindowShow(self):    #管理员界面
        print('AdminWindowShow')
        conn = pymysql.Connect(host='localhost',user='root',passwd='110+120+z',database='bookmanage')
        cursor = conn.cursor()
        cursor.execute("select * from admin_info")
        data = cursor.fetchall()
        self.tableWidget_Admin.setRowCount(len(data))
        self.tableWidget_Admin.setColumnCount(len(data[0]))  # Assuming the number of columns is the same for all rows

        for row_index, row_data in enumerate(data):
            for col_index, col_data in enumerate(row_data):
                self.tableWidget_Admin.setItem(row_index, col_index, QTableWidgetItem(str(col_data)))
        cursor.close()
        conn.close()
    def btnInsert_clicked(self):#插入数据
        print('Insert is clicked')
    def btnClose_clicked(self):# 红点退出
        print("mainwindow quit")
        QCoreApplication.instance().quit()      
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

class MainwindowForm_E(QMainWindow,Ui_MainWindow_E):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)#隐藏边框
        self.setAttribute(Qt.WA_TranslucentBackground)#透明背景
        self.setupUi(self)
        self.setFixedSize(1152,648)
        self.btn_Close.clicked.connect(self.btnClose_clicked)#关闭窗口函数

    def btnClose_clicked(self):
        print("mainwindow quit")
        QCoreApplication.instance().quit()      
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
    window = MainwindowForm()
    #TODO:加一个判断 显示不同界面 分为管理员（MainwindowForm_E）和职工（MainwindowForm）
    window.show()
    sys.exit(app.exec_())