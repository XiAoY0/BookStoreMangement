import sys
import os
import pymysql
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QFileDialog, QMainWindow, QMessageBox , QLineEdit,QApplication,QPushButton, QVBoxLayout, QWidget, QDialog,QTableWidgetItem
from UI.Ui_Login import Ui_Login
from UI.Ui_register import Ui_Register
from UI.Ui_forget_widget import Ui_forget_widget
from UI.Ui_fluent_test import Ui_MainWindow

class MainwindowForm(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()  
        self.setupUi(self,)
        self.adminWindow()#不能加self作为参数
        
        #self.setFixedSize(1152,648)
        self.Mysql_admin()
        self.btn_Close.clicked.connect(self.btnClose_clicked)#关闭窗口函数
    def adminWindow(self):
        self.tableWidget_Admin = QtWidgets.QTableWidget(self.frame)
        self.tableWidget_Admin.setGeometry(QtCore.QRect(220, 50, 771, 351))
        self.tableWidget_Admin.setObjectName("tableWidget_Admin")
        self.tableWidget_Admin.setColumnCount(0)
        self.tableWidget_Admin.setRowCount(0)                      
    def Mysql_admin(self):#连接数据库
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

        
    def btnClose_clicked(self):
        print("mainwindow quit")
        QCoreApplication.instance().quit()      
    

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainwindowForm()
    window.show()
    sys.exit(app.exec_())