import sys
import os
import pymysql
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QFileDialog, QMainWindow, QMessageBox , QLineEdit,QApplication,QPushButton, QVBoxLayout, QWidget, QDialog,QLabel,QTableWidgetItem
from Ui_insert import Ui_Insert
from Ui_Login import Ui_Login
from Ui_register import Ui_Register
from Ui_forget_widget import Ui_forget_widget
from Ui_mainwindow import Ui_MainWindow
from Ui_Employee import Ui_MainWindow_E
class InsertForm1(QWidget,Ui_Insert):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)#隐藏边框
        self.setAttribute(Qt.WA_TranslucentBackground)#透明背景
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.Insertquit_clicked)#取消插入
        self.pushButton_3.clicked.connect(self.InsertClear_clicked)#重置插入页面
        self.pushButton.clicked.connect(self.InsertMakesure_clicked)#重置插入页面
    def InsertMakesure_clicked(self):
        print('Make sure insert')
    def Insertquit_clicked(self):
        print('Insertquit cilcked')
        self.close()
    def InsertClear_clicked(self):
        print('InsertClear clicked')
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_5.clear()
        self.lineEdit_6.clear()
        self.lineEdit_7.clear()
        self.spinBox.clear()
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

def insert_data(table_name, data):
    try:
        conn = pymysql.connect(host='localhost', user='root', passwd='110+120+z', database='bookmanage')
        cursor = conn.cursor()

        # 构建插入语句
        query = f"INSERT INTO {table_name} (列1, 列2, 列3, ...) VALUES (%s, %s, %s, ...)"
        # 将数据插入数据库
        cursor.execute(query, data)
        # 提交事务
        conn.commit()

        print("数据插入成功")

    except Exception as e:
        print(f"数据插入失败: {str(e)}")
        # 如果发生异常，回滚事务
        conn.rollback()

    finally:
        # 关闭游标和数据库连接
        cursor.close()
        conn.close()
# 要插入的数据
data_to_insert = ('值1', '值2', '值3', ...)  # 用实际的值替换 '值1', '值2', '值3', ...

# 调用函数插入数据
insert_data('表名', data_to_insert)  # 用实际的表名替换 '表名'
class MainwindowForm(QMainWindow,Ui_MainWindow):
    # clicked = QtCore.pyqtSignal()
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)#隐藏边框
        self.setAttribute(Qt.WA_TranslucentBackground)#透明背景
        self.setupUi(self)
        self.setFixedSize(1152,680)
        #槽函数绑定 主要是标签点击切换显示界面
        self.btn_Close.clicked.connect(self.btnClose_clicked)#关闭窗口函数
        self.pushButton_3.clicked.connect(self.btnInsert_clicked)#插入数据
        self.pushButton_5.clicked.connect(self.btnInsertLot_clicked)#批量导入数据
        self.pushButton_4.clicked.connect(self.btnOut_clicked)#导出数据
        self.pushButton_2.clicked.connect(self.btnDelete_clicked)#删除数据
        self.pushButton.clicked.connect(self.btnSearch_clicked)#查询
        #用于查询标记 不同界面设为不同值 同样用于插入导出导入标记
        self.searchFlag=0

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
    def btnSearch_clicked(self):
        print('Search button is clicked')
        self.Searchtext=self.lineEdit.text()#输入框内容
        print(self.Searchtext)
        if self.searchFlag==0: 
            msgBox = QMessageBox()
            msgBox.setWindowTitle("提示")
            msgBox.setText("请点击界面后查询")
            msgBox.exec()
            return
        # if not self.Searchtext:
        # # 如果 self.Searchtext 为空，显示消息框提示用户输入查询信息
        #     msgBox = QMessageBox()
        #     msgBox.setWindowTitle("提示")
        #     msgBox.setText("请输入查询信息")
        #     msgBox.exec()
        #     return
        elif self.searchFlag==1: 
            conn = pymysql.Connect(host='localhost', user='root', passwd='110+120+z', database='bookmanage')
            cursor = conn.cursor()
            query = """
            SELECT * FROM admin_info 
            WHERE 
                ad_name LIKE %s OR
                ad_id LIKE %s  
            """
            # 将查询条件绑定到查询语句中
            cursor.execute(query, (f"%{self.Searchtext}%",  f"%{self.Searchtext}%"))

            data = cursor.fetchall()
            if not data:
                QMessageBox.warning(self, "提示", "未找到匹配的数据")
                return
            self.tableWidget_Admin.setRowCount(len(data))
            self.tableWidget_Admin.setColumnCount(len(data[0]))  # Assuming the number of columns is the same for all rows
            column_headers = [description[0] for description in cursor.description]
            for col_index, header in enumerate(column_headers):
                header_item = QTableWidgetItem(header)
                self.tableWidget_Admin.setHorizontalHeaderItem(col_index, header_item)
            for row_index, row_data in enumerate(data):
                for col_index, col_data in enumerate(row_data):
                    self.tableWidget_Admin.setItem(row_index, col_index, QTableWidgetItem(str(col_data)))
            cursor.close()
            conn.close()
        elif self.searchFlag==2: 
            conn = pymysql.Connect(host='localhost', user='root', passwd='110+120+z', database='bookmanage')
            cursor = conn.cursor()
            query = """
            SELECT * FROM 工作人员 
            WHERE 
                员工姓名 LIKE %s OR
                员工编号 = %s OR
                员工身份证号 LIKE %s OR
                员工职位 LIKE %s 
                
            """
            # 将查询条件绑定到查询语句中
            cursor.execute(query, (f"%{self.Searchtext}%", self.Searchtext,  f"%{self.Searchtext}%", f"%{self.Searchtext}%"))

            data = cursor.fetchall()
            if not data:
                QMessageBox.warning(self, "提示", "未找到匹配的数据")
                return
            self.tableWidget_Admin.setRowCount(len(data))
            self.tableWidget_Admin.setColumnCount(len(data[0]))  # Assuming the number of columns is the same for all rows
            column_headers = [description[0] for description in cursor.description]
            for col_index, header in enumerate(column_headers):
                header_item = QTableWidgetItem(header)
                self.tableWidget_Admin.setHorizontalHeaderItem(col_index, header_item)
            for row_index, row_data in enumerate(data):
                for col_index, col_data in enumerate(row_data):
                    self.tableWidget_Admin.setItem(row_index, col_index, QTableWidgetItem(str(col_data)))
            cursor.close()
            conn.close()
        elif self.searchFlag==3: 
            conn = pymysql.Connect(host='localhost', user='root', passwd='110+120+z', database='bookmanage')
            cursor = conn.cursor()
            query = """
            SELECT * FROM 会员 
            WHERE 
                会员类别 LIKE %s OR
                会员编号 = %s OR
                会员联系方式 LIKE %s OR
                会员姓名 LIKE %s 
                
            """
            # 将查询条件绑定到查询语句中
            cursor.execute(query, (f"%{self.Searchtext}%", self.Searchtext, f"%{self.Searchtext}%", f"%{self.Searchtext}%"))

            data = cursor.fetchall()
            if not data:
                QMessageBox.warning(self, "提示", "未找到匹配的数据")
                return
            self.tableWidget_Admin.setRowCount(len(data))
            self.tableWidget_Admin.setColumnCount(len(data[0]))  # Assuming the number of columns is the same for all rows
            column_headers = [description[0] for description in cursor.description]
            for col_index, header in enumerate(column_headers):
                header_item = QTableWidgetItem(header)
                self.tableWidget_Admin.setHorizontalHeaderItem(col_index, header_item)
            for row_index, row_data in enumerate(data):
                for col_index, col_data in enumerate(row_data):
                    self.tableWidget_Admin.setItem(row_index, col_index, QTableWidgetItem(str(col_data)))
            cursor.close()
            conn.close()
        elif self.searchFlag==4: 
            conn = pymysql.Connect(host='localhost', user='root', passwd='110+120+z', database='bookmanage')
            cursor = conn.cursor()
            query = """
            SELECT * FROM 图书 
            WHERE 
                图书名称 LIKE %s OR
                图书编号 = %s OR
                图书出版社 LIKE %s OR
                图书作者 LIKE %s OR
                图书类别 LIKE %s 
            """
            # 将查询条件绑定到查询语句中
            cursor.execute(query, (f"%{self.Searchtext}%", self.Searchtext,  f"%{self.Searchtext}%", f"%{self.Searchtext}%", f"%{self.Searchtext}%", ))

            data = cursor.fetchall()
            if not data:
                QMessageBox.warning(self, "提示", "未找到匹配的数据")
                return
            self.tableWidget_Admin.setRowCount(len(data))
            self.tableWidget_Admin.setColumnCount(len(data[0]))  # Assuming the number of columns is the same for all rows
            column_headers = [description[0] for description in cursor.description]
            for col_index, header in enumerate(column_headers):
                header_item = QTableWidgetItem(header)
                self.tableWidget_Admin.setHorizontalHeaderItem(col_index, header_item)
            for row_index, row_data in enumerate(data):
                for col_index, col_data in enumerate(row_data):
                    self.tableWidget_Admin.setItem(row_index, col_index, QTableWidgetItem(str(col_data)))
            cursor.close()
            conn.close()
        elif self.searchFlag==5: 
            conn = pymysql.Connect(host='localhost', user='root', passwd='110+120+z', database='bookmanage')
            cursor = conn.cursor()
            query = """
            SELECT * FROM 购书记录 
            WHERE 
                图书名称 LIKE %s OR
                图书编号 = %s OR
                购书记录编号 = %s OR
                购买时间 LIKE %s OR
                会员编号 = %s OR
                会员联系方式 LIKE %s OR
                会员姓名 LIKE %s OR
                办理人 LIKE %s
            """
            # 将查询条件绑定到查询语句中
            cursor.execute(query, (f"%{self.Searchtext}%", self.Searchtext, self.Searchtext, f"%{self.Searchtext}%",self.Searchtext, f"%{self.Searchtext}%", f"%{self.Searchtext}%", f"%{self.Searchtext}%"))

            data = cursor.fetchall()
            if not data:
                QMessageBox.warning(self, "提示", "未找到匹配的数据")
                return
            self.tableWidget_Admin.setRowCount(len(data))
            self.tableWidget_Admin.setColumnCount(len(data[0]))  # Assuming the number of columns is the same for all rows
            column_headers = [description[0] for description in cursor.description]
            for col_index, header in enumerate(column_headers):
                header_item = QTableWidgetItem(header)
                self.tableWidget_Admin.setHorizontalHeaderItem(col_index, header_item)
            for row_index, row_data in enumerate(data):
                for col_index, col_data in enumerate(row_data):
                    self.tableWidget_Admin.setItem(row_index, col_index, QTableWidgetItem(str(col_data)))
            cursor.close()
            conn.close()
        elif self.searchFlag==6: 
            conn = pymysql.Connect(host='localhost', user='root', passwd='110+120+z', database='bookmanage')
            cursor = conn.cursor()
            query = """
            SELECT * FROM 退书记录 
            WHERE 
                图书名称 LIKE %s OR
                图书编号 = %s OR
                退款记录编号 = %s OR
                退款时间 LIKE %s OR
                会员编号 = %s OR
                会员联系方式 LIKE %s OR
                会员姓名 LIKE %s OR
                办理人 LIKE %s
            """
            # 将查询条件绑定到查询语句中
            cursor.execute(query, (f"%{self.Searchtext}%", self.Searchtext, self.Searchtext, f"%{self.Searchtext}%",self.Searchtext, f"%{self.Searchtext}%", f"%{self.Searchtext}%", f"%{self.Searchtext}%"))

            data = cursor.fetchall()
            if not data:
                QMessageBox.warning(self, "提示", "未找到匹配的数据")
                return
            self.tableWidget_Admin.setRowCount(len(data))
            self.tableWidget_Admin.setColumnCount(len(data[0]))  # Assuming the number of columns is the same for all rows
            column_headers = [description[0] for description in cursor.description]
            for col_index, header in enumerate(column_headers):
                header_item = QTableWidgetItem(header)
                self.tableWidget_Admin.setHorizontalHeaderItem(col_index, header_item)
            for row_index, row_data in enumerate(data):
                for col_index, col_data in enumerate(row_data):
                    self.tableWidget_Admin.setItem(row_index, col_index, QTableWidgetItem(str(col_data)))
            cursor.close()
            conn.close()
    def btnInsertLot_clicked(self):
        print('Lots of logs to insert')
        
    def btnOut_clicked(self):
        print('btnOut is clicked')
    def btnDelete_clicked(self):
        print('btnDelete is clicked')
    def BookBackWindowShow(self):#退书记录
        print('BookBackWindowShow')
        self.searchFlag=6
        print(self.searchFlag)
        conn = pymysql.Connect(host='localhost',user='root',passwd='110+120+z',database='bookmanage')
        cursor = conn.cursor()
        cursor.execute("select * from 退书记录")
        data = cursor.fetchall()
        self.tableWidget_Admin.setRowCount(len(data))
        self.tableWidget_Admin.setColumnCount(len(data[0]))  # Assuming the number of columns is the same for all rows
        column_headers = [description[0] for description in cursor.description]
        for col_index, header in enumerate(column_headers):
            header_item = QTableWidgetItem(header)
            self.tableWidget_Admin.setHorizontalHeaderItem(col_index, header_item)
        for row_index, row_data in enumerate(data):
            for col_index, col_data in enumerate(row_data):
                self.tableWidget_Admin.setItem(row_index, col_index, QTableWidgetItem(str(col_data)))
        cursor.close()
        conn.close()
    def BookBuyWindowShow(self):# 购书记录
        print('BookBuyWindowShow')
        self.searchFlag=5
        print(self.searchFlag)
        conn = pymysql.Connect(host='localhost',user='root',passwd='110+120+z',database='bookmanage')
        cursor = conn.cursor()
        cursor.execute("select * from 购买记录")
        data = cursor.fetchall()
        self.tableWidget_Admin.setRowCount(len(data))
        self.tableWidget_Admin.setColumnCount(len(data[0]))  # Assuming the number of columns is the same for all rows
        column_headers = [description[0] for description in cursor.description]
        for col_index, header in enumerate(column_headers):
            header_item = QTableWidgetItem(header)
            self.tableWidget_Admin.setHorizontalHeaderItem(col_index, header_item)
        for row_index, row_data in enumerate(data):
            for col_index, col_data in enumerate(row_data):
                self.tableWidget_Admin.setItem(row_index, col_index, QTableWidgetItem(str(col_data)))
        cursor.close()
        conn.close()
    def BookWindowShow(self):# 图书
        print('BookWindowShow')
        self.searchFlag=4
        print(self.searchFlag)
        conn = pymysql.Connect(host='localhost',user='root',passwd='110+120+z',database='bookmanage')
        cursor = conn.cursor()
        cursor.execute("select * from 图书")
        data = cursor.fetchall()
        self.tableWidget_Admin.setRowCount(len(data))
        self.tableWidget_Admin.setColumnCount(len(data[0]))  # Assuming the number of columns is the same for all rows
        column_headers = [description[0] for description in cursor.description]
        for col_index, header in enumerate(column_headers):
            header_item = QTableWidgetItem(header)
            self.tableWidget_Admin.setHorizontalHeaderItem(col_index, header_item)
        for row_index, row_data in enumerate(data):
            for col_index, col_data in enumerate(row_data):
                self.tableWidget_Admin.setItem(row_index, col_index, QTableWidgetItem(str(col_data)))
        cursor.close()
        conn.close()
    def CustomerWindowShow(self):# 会员界面
        print('CustomerWindowShow')
        self.searchFlag=3
        print(self.searchFlag)
        conn = pymysql.Connect(host='localhost',user='root',passwd='110+120+z',database='bookmanage')
        cursor = conn.cursor()
        cursor.execute("select * from 会员")
        data = cursor.fetchall()
        self.tableWidget_Admin.setRowCount(len(data))
        self.tableWidget_Admin.setColumnCount(len(data[0]))  # Assuming the number of columns is the same for all rows
        column_headers = [description[0] for description in cursor.description]
        for col_index, header in enumerate(column_headers):
            header_item = QTableWidgetItem(header)
            self.tableWidget_Admin.setHorizontalHeaderItem(col_index, header_item)
        for row_index, row_data in enumerate(data):
            for col_index, col_data in enumerate(row_data):
                self.tableWidget_Admin.setItem(row_index, col_index, QTableWidgetItem(str(col_data)))
        cursor.close()
        conn.close()
    def EmployWindowShow(self): # 职工界面   
        print('EmployWindowShow')
        self.searchFlag=2
        print(self.searchFlag)
        conn = pymysql.Connect(host='localhost',user='root',passwd='110+120+z',database='bookmanage')
        cursor = conn.cursor()
        cursor.execute("select * from 工作人员")
        data = cursor.fetchall()
        self.tableWidget_Admin.setRowCount(len(data))
        self.tableWidget_Admin.setColumnCount(len(data[0]))  # Assuming the number of columns is the same for all rows
        # 插入表头
        column_headers = [description[0] for description in cursor.description]
        for col_index, header in enumerate(column_headers):
            header_item = QTableWidgetItem(header)
            self.tableWidget_Admin.setHorizontalHeaderItem(col_index, header_item)
        for row_index, row_data in enumerate(data):
            for col_index, col_data in enumerate(row_data):
                self.tableWidget_Admin.setItem(row_index, col_index, QTableWidgetItem(str(col_data)))
        cursor.close()
        conn.close()
    def AdminWindowShow(self):    #管理员界面
        print('AdminWindowShow')
        self.searchFlag=1
        print(self.searchFlag)
        conn = pymysql.Connect(host='localhost',user='root',passwd='110+120+z',database='bookmanage')
        cursor = conn.cursor()
        cursor.execute("select * from admin_info")
        data = cursor.fetchall()
        self.tableWidget_Admin.setRowCount(len(data))
        self.tableWidget_Admin.setColumnCount(len(data[0]))  # Assuming the number of columns is the same for all rows
        column_headers = [description[0] for description in cursor.description]
        for col_index, header in enumerate(column_headers):
            header_item = QTableWidgetItem(header)
            self.tableWidget_Admin.setHorizontalHeaderItem(col_index, header_item)
        for row_index, row_data in enumerate(data):
            for col_index, col_data in enumerate(row_data):
                self.tableWidget_Admin.setItem(row_index, col_index, QTableWidgetItem(str(col_data)))
        cursor.close()
        conn.close()
    def btnInsert_clicked(self):#插入数据
        print('Insert is clicked')
         #TODO:根据flag判断是哪个界面弹出对应的插入窗口
        self.Insert=InsertForm1()
        self.Insert.show()
        self.Insert.raise_()
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