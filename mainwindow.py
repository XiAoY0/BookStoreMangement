import sys
import os
import csv
import pymysql
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QFileDialog, QMainWindow, QMessageBox , QLineEdit,QApplication,QPushButton, QVBoxLayout, QWidget, QDialog,QLabel,QTableWidgetItem
from UI.Ui_insert_Employ import Ui_Insert_E
from UI.Ui_insert import Ui_Insert
from UI.Ui_Login import Ui_Login
from UI.Ui_register import Ui_Register
from UI.Ui_forget_widget import Ui_forget_widget
from UI.Ui_mainwindow import Ui_MainWindow
from UI.Ui_Employee import Ui_MainWindow_E
from UI.Ui_insert_Customer import Ui_Insert_C
from UI.Ui_insert_Admin import Ui_Insert_Admin
class InsertForm_Admin(QWidget,Ui_Insert_Admin):
    def __init__(self,parent_window):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)#隐藏边框
        self.setAttribute(Qt.WA_TranslucentBackground)#透明背景
        self.setupUi(self)
        self.parent_window=parent_window
        self.pushButton_2.clicked.connect(self.Insertquit_clicked)#取消插入
        self.pushButton_3.clicked.connect(self.InsertClear_clicked)#重置插入页面
        self.pushButton.clicked.connect(self.InsertMakesure_clicked)#重置插入页面
    def InsertMakesure_clicked(self):
        print('Make sure insert')
        self.adID=self.lineEdit.text()
        self.adName=self.lineEdit_2.text()
        self.adpass=self.lineEdit_3.text()
        
        self.Insert_data_customer = (self.adID, self.adName, self.adpass)
        insert_data('admin_info',self.Insert_data_customer)
        # 插入数据后更新界面显示
        self.parent_window.AdminWindowShow()
        
    def Insertquit_clicked(self):
        print('Insertquit cilcked')
        self.close()
    def InsertClear_clicked(self):
        print('InsertClear clicked')
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
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
class InsertForm_C(QWidget,Ui_Insert_C):
    def __init__(self,parent_window):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)#隐藏边框
        self.setAttribute(Qt.WA_TranslucentBackground)#透明背景
        self.setupUi(self)
        self.parent_window=parent_window
        self.pushButton_2.clicked.connect(self.Insertquit_clicked)#取消插入
        self.pushButton_3.clicked.connect(self.InsertClear_clicked)#重置插入页面
        self.pushButton.clicked.connect(self.InsertMakesure_clicked)#重置插入页面
    def InsertMakesure_clicked(self):
        print('Make sure insert')
        self.CustomerID=self.lineEdit.text()
        self.CustomerName=self.lineEdit_2.text()
        self.CustomerFrom=self.lineEdit_3.text()
        self.Customermajor=self.lineEdit_7.text()
        self.Customerconnect=self.lineEdit_6.text()
        
        self.Insert_data_customer = (self.CustomerID, self.CustomerName, self.CustomerFrom, self.Customermajor, self.Customerconnect)
        insert_data('会员',self.Insert_data_customer)
        # 插入数据后更新界面显示
        self.parent_window.CustomerWindowShow()
        
    def Insertquit_clicked(self):
        print('Insertquit cilcked')
        self.close()
    def InsertClear_clicked(self):
        print('InsertClear clicked')
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_6.clear()
        self.lineEdit_7.clear()
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
class InsertForm_E(QWidget,Ui_Insert_E):
    def __init__(self,parent_window):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)#隐藏边框
        self.setAttribute(Qt.WA_TranslucentBackground)#透明背景
        self.setupUi(self)
        self.parent_window=parent_window
        self.pushButton_2.clicked.connect(self.Insertquit_clicked)#取消插入
        self.pushButton_3.clicked.connect(self.InsertClear_clicked)#重置插入页面
        self.pushButton.clicked.connect(self.InsertMakesure_clicked)#重置插入页面
    def InsertMakesure_clicked(self):
        print('Make sure insert')
        self.employID=self.lineEdit.text()
        self.employName=self.lineEdit_2.text()
        self.employFrom=self.lineEdit_3.text()
        self.employPrice=self.lineEdit_7.text()
        self.employAuthor=self.lineEdit_6.text()
        self.employMajor=self.lineEdit_5.text()
        self.employCount=self.lineEdit_8.text()
        self.Insert_data_employ = (self.employID, self.employName, self.employFrom, self.employPrice, self.employAuthor, self.employMajor, self.employCount)
        insert_data('工作人员',self.Insert_data_employ)
        # 插入数据后更新界面显示
        self.parent_window.EmployWindowShow()
        
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
        self.lineEdit_8.clear()
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
class InsertForm1(QWidget,Ui_Insert):
    def __init__(self,parent_window):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)#隐藏边框
        self.setAttribute(Qt.WA_TranslucentBackground)#透明背景
        self.setupUi(self)
        self.parent_window=parent_window
        self.pushButton_2.clicked.connect(self.Insertquit_clicked)#取消插入
        self.pushButton_3.clicked.connect(self.InsertClear_clicked)#重置插入页面
        self.pushButton.clicked.connect(self.InsertMakesure_clicked)#重置插入页面
    def InsertMakesure_clicked(self):
        print('Make sure insert')
        self.bookID=self.lineEdit.text()
        self.bookName=self.lineEdit_2.text()
        self.bookFrom=self.lineEdit_3.text()
        self.bookPrice=self.lineEdit_7.text()
        self.bookAuthor=self.lineEdit_6.text()
        self.bookMajor=self.lineEdit_5.text()
        self.bookCount=self.spinBox.value()
        self.Insert_data_book = (self.bookID, self.bookName, self.bookFrom, self.bookPrice, self.bookAuthor, self.bookMajor, self.bookCount)
        insert_data('图书',self.Insert_data_book)
        # 插入数据后更新界面显示
        self.parent_window.BookWindowShow()
        
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

        # 查询表的列名
        cursor.execute(f"SHOW COLUMNS FROM {table_name}")
        columns = [column[0] for column in cursor.fetchall()]

        # 构建插入语句
        columns_str = ', '.join(columns)
        placeholders = ', '.join(['%s'] * len(columns))
        query = f"INSERT INTO {table_name} ({columns_str}) VALUES ({placeholders})"

        # 将数据插入数据库
        cursor.execute(query, data)
        # 提交事务
        conn.commit()

        print("数据插入成功")
        msgBox = QMessageBox()
        msgBox.setWindowTitle("提示")
        msgBox.setText("插入成功")
        msgBox.exec()
        return
    except Exception as e:
        print(f"数据插入失败: {str(e)}")
        msgBox = QMessageBox()
        msgBox.setWindowTitle("提示")
        msgBox.setText(f"数据插入失败: {str(e)}")
        msgBox.exec()
        # 如果发生异常，回滚事务
        conn.rollback()

    finally:
        # 关闭游标和数据库连接
        cursor.close()
        conn.close()
# 要插入的数据
#data_to_insert = ('值1', '值2', '值3', ...)  # 用实际的值替换 '值1', '值2', '值3', ...

# 调用函数插入数据
#insert_data('表名', data_to_insert)  # 用实际的表名替换 '表名'
class MainwindowForm(QMainWindow,Ui_MainWindow):
    # clicked = QtCore.pyqtSignal()
    def __init__(self,isAdmin=1):#多传一个状态参数
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)#隐藏边框
        self.setAttribute(Qt.WA_TranslucentBackground)#透明背景
        self.isAdmin=isAdmin
        self.setupUi(self)
        #self.setFixedSize(1152,680)
        #槽函数绑定 主要是标签点击切换显示界面
        self.btn_Close.clicked.connect(self.btnClose_clicked)#关闭窗口函数
        self.pushButton_3.clicked.connect(self.btnInsert_clicked)#插入数据
        self.pushButton_5.clicked.connect(self.btnInsertLot_clicked)#批量导入数据
        self.pushButton_4.clicked.connect(self.btnOut_clicked)#导出数据
        self.pushButton_2.clicked.connect(self.btnDelete_clicked)#删除数据
        self.pushButton.clicked.connect(self.btnSearch_clicked)#查询
        self.pushButton_6.clicked.connect(self.btnSaveChange_clicked)#保存修改
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
        if self.searchFlag==4:
            options = QFileDialog.Options()
            file_name, _ = QFileDialog.getOpenFileName(self,"选择CSV文件", "","CSV Files (*.csv)", options=options)
            if file_name:
                try:
                    conn = pymysql.Connect(host='localhost', user='root', passwd='110+120+z', database='bookmanage')
                    cursor = conn.cursor()
                    with open(file_name, 'r', encoding='utf-8') as file:
                        csv_reader = csv.reader(file)
                        next(csv_reader)  # 跳过标题行
                        for row in csv_reader:
                            # 插入数据的SQL语句
                            query = """
                            INSERT INTO 图书 (图书编号, 图书名称, 图书出版社, 图书价格, 图书作者, 图书类别, 图书库存数量)
                            VALUES (%s, %s, %s, %s, %s, %s, %s)
                            """
                            # 执行插入操作
                            cursor.execute(query, row)
                    # 提交事务
                    conn.commit()
                    QMessageBox.information(self, "提示", "批量导入成功")
                
                except Exception as e:
                    QMessageBox.warning(self, "错误", f"批量导入失败: {str(e)}")

                finally:
                    cursor.close()
                    conn.close()       
    def btnOut_clicked(self):
        print('btnOut is clicked')
        if self.searchFlag==1:
            print("导出管理员信息")
            # 创建文件对话框，让用户选择保存的文件路径
            file_dialog = QFileDialog()
            file_path, _ = file_dialog.getSaveFileName(self, "保存CSV文件", "", "CSV 文件 (*.csv)")

            if file_path:
                try:
                    conn = pymysql.Connect(host='localhost', user='root', passwd='110+120+z', database='bookmanage')
                    cursor = conn.cursor()

                    # 执行查询语句，获取数据库中的数据
                    cursor.execute("SELECT * FROM admin_info")
                    data = cursor.fetchall()

                    # 将数据写入CSV文件
                    with open(file_path, 'w', newline='', encoding='utf-8') as file:
                        csv_writer = csv.writer(file)
                        csv_writer.writerow([i[0] for i in cursor.description])  # 写入列名
                        csv_writer.writerows(data)  # 写入数据

                    print("数据已成功导出为CSV文件。")
                    msgBox = QMessageBox()
                    msgBox.setWindowTitle("提示")
                    msgBox.setText("已成功导出管理员信息！请妥善保管！")
                    msgBox.exec()
                    return

                except Exception as e:
                    print("导出失败:", e)
                    msgBox = QMessageBox()
                    msgBox.setWindowTitle("提示")
                    msgBox.setText(f"导出失败！{e}")
                    msgBox.exec()
                    return

                finally:
                    cursor.close()
                    conn.close()
        elif self.searchFlag==4:
            print("test")
            # 创建文件对话框，让用户选择保存的文件路径
            file_dialog = QFileDialog()
            file_path, _ = file_dialog.getSaveFileName(self, "保存CSV文件", "", "CSV 文件 (*.csv)")

            if file_path:
                try:
                    conn = pymysql.Connect(host='localhost', user='root', passwd='110+120+z', database='bookmanage')
                    cursor = conn.cursor()

                    # 执行查询语句，获取数据库中的数据
                    cursor.execute("SELECT * FROM 图书")
                    data = cursor.fetchall()

                    # 将数据写入CSV文件
                    with open(file_path, 'w', newline='', encoding='utf-8') as file:
                        csv_writer = csv.writer(file)
                        csv_writer.writerow([i[0] for i in cursor.description])  # 写入列名
                        csv_writer.writerows(data)  # 写入数据

                    print("数据已成功导出为CSV文件。")
                    msgBox = QMessageBox()
                    msgBox.setWindowTitle("提示")
                    msgBox.setText("已成功导出图书信息！")
                    msgBox.exec()
                    return

                except Exception as e:
                    print("导出失败:", e)
                    msgBox = QMessageBox()
                    msgBox.setWindowTitle("提示")
                    msgBox.setText(f"导出失败！{e}")
                    msgBox.exec()
                    return

                finally:
                    cursor.close()
                    conn.close()
        elif self.searchFlag==2:
            print("导出职工信息")
            # 创建文件对话框，让用户选择保存的文件路径
            file_dialog = QFileDialog()
            file_path, _ = file_dialog.getSaveFileName(self, "保存CSV文件", "", "CSV 文件 (*.csv)")

            if file_path:
                try:
                    conn = pymysql.Connect(host='localhost', user='root', passwd='110+120+z', database='bookmanage')
                    cursor = conn.cursor()

                    # 执行查询语句，获取数据库中的数据
                    cursor.execute("SELECT * FROM 工作人员")
                    data = cursor.fetchall()

                    # 将数据写入CSV文件
                    with open(file_path, 'w', newline='', encoding='utf-8') as file:
                        csv_writer = csv.writer(file)
                        csv_writer.writerow([i[0] for i in cursor.description])  # 写入列名
                        csv_writer.writerows(data)  # 写入数据

                    print("数据已成功导出为CSV文件。")
                    msgBox = QMessageBox()
                    msgBox.setWindowTitle("提示")
                    msgBox.setText("已成功导出职工信息！")
                    msgBox.exec()
                    return

                except Exception as e:
                    print("导出失败:", e)
                    msgBox = QMessageBox()
                    msgBox.setWindowTitle("提示")
                    msgBox.setText(f"导出失败！{e}")
                    msgBox.exec()
                    return

                finally:
                    cursor.close()
                    conn.close()
        elif self.searchFlag==3:
            print("导出顾客信息")
            # 创建文件对话框，让用户选择保存的文件路径
            file_dialog = QFileDialog()
            file_path, _ = file_dialog.getSaveFileName(self, "保存CSV文件", "", "CSV 文件 (*.csv)")

            if file_path:
                try:
                    conn = pymysql.Connect(host='localhost', user='root', passwd='110+120+z', database='bookmanage')
                    cursor = conn.cursor()

                    # 执行查询语句，获取数据库中的数据
                    cursor.execute("SELECT * FROM 会员")
                    data = cursor.fetchall()

                    # 将数据写入CSV文件
                    with open(file_path, 'w', newline='', encoding='utf-8') as file:
                        csv_writer = csv.writer(file)
                        csv_writer.writerow([i[0] for i in cursor.description])  # 写入列名
                        csv_writer.writerows(data)  # 写入数据

                    print("数据已成功导出为CSV文件。")
                    msgBox = QMessageBox()
                    msgBox.setWindowTitle("提示")
                    msgBox.setText("已成功导出会员信息！")
                    msgBox.exec()
                    return

                except Exception as e:
                    print("导出失败:", e)
                    msgBox = QMessageBox()
                    msgBox.setWindowTitle("提示")
                    msgBox.setText(f"导出失败！{e}")
                    msgBox.exec()
                    return

                finally:
                    cursor.close()
                    conn.close()
        elif self.searchFlag==5:
            print("test")
            # 创建文件对话框，让用户选择保存的文件路径
            file_dialog = QFileDialog()
            file_path, _ = file_dialog.getSaveFileName(self, "保存CSV文件", "", "CSV 文件 (*.csv)")

            if file_path:
                try:
                    conn = pymysql.Connect(host='localhost', user='root', passwd='110+120+z', database='bookmanage')
                    cursor = conn.cursor()

                    # 执行查询语句，获取数据库中的数据
                    cursor.execute("SELECT * FROM 购买记录")
                    data = cursor.fetchall()

                    # 将数据写入CSV文件
                    with open(file_path, 'w', newline='', encoding='utf-8') as file:
                        csv_writer = csv.writer(file)
                        csv_writer.writerow([i[0] for i in cursor.description])  # 写入列名
                        csv_writer.writerows(data)  # 写入数据

                    print("数据已成功导出为CSV文件。")
                    msgBox = QMessageBox()
                    msgBox.setWindowTitle("提示")
                    msgBox.setText("已成功导出购买记录！")
                    msgBox.exec()
                    return

                except Exception as e:
                    print("导出失败:", e)
                    msgBox = QMessageBox()
                    msgBox.setWindowTitle("提示")
                    msgBox.setText(f"导出失败！{e}")
                    msgBox.exec()
                    return

                finally:
                    cursor.close()
                    conn.close()
        elif self.searchFlag==6:
            print("test")
            # 创建文件对话框，让用户选择保存的文件路径
            file_dialog = QFileDialog()
            file_path, _ = file_dialog.getSaveFileName(self, "保存CSV文件", "", "CSV 文件 (*.csv)")

            if file_path:
                try:
                    conn = pymysql.Connect(host='localhost', user='root', passwd='110+120+z', database='bookmanage')
                    cursor = conn.cursor()

                    # 执行查询语句，获取数据库中的数据
                    cursor.execute("SELECT * FROM 退书记录")
                    data = cursor.fetchall()

                    # 将数据写入CSV文件
                    with open(file_path, 'w', newline='', encoding='utf-8') as file:
                        csv_writer = csv.writer(file)
                        csv_writer.writerow([i[0] for i in cursor.description])  # 写入列名
                        csv_writer.writerows(data)  # 写入数据

                    print("数据已成功导出为CSV文件。")
                    msgBox = QMessageBox()
                    msgBox.setWindowTitle("提示")
                    msgBox.setText("已成功导出退书记录！")
                    msgBox.exec()
                    return

                except Exception as e:
                    print("导出失败:", e)
                    msgBox = QMessageBox()
                    msgBox.setWindowTitle("提示")
                    msgBox.setText(f"导出失败！{e}")
                    msgBox.exec()
                    return

                finally:
                    cursor.close()
                    conn.close()
    def btnSaveChange_clicked(self):
        if self.searchFlag==1:
            table_name='admin_info'
            try:
            # 调用保存修改的函数，传入表名作为参数
                self.save_changes_to_database(table_name)
            except Exception as e:
                QMessageBox.critical(self, "错误", f"保存修改时发生异常：{str(e)}")
        elif self.searchFlag==2:
            table_name='工作人员'
            try:
            # 调用保存修改的函数，传入表名作为参数
                self.save_changes_to_database(table_name)
            except Exception as e:
                QMessageBox.critical(self, "错误", f"保存修改时发生异常：{str(e)}")            
        elif self.searchFlag==3:
            table_name='会员'
            try:
            # 调用保存修改的函数，传入表名作为参数
                self.save_changes_to_database(table_name)
            except Exception as e:
                QMessageBox.critical(self, "错误", f"保存修改时发生异常：{str(e)}")            
        elif self.searchFlag==4:
            table_name='图书'
            try:
            # 调用保存修改的函数，传入表名作为参数
                self.save_changes_to_database(table_name)
            except Exception as e:
                QMessageBox.critical(self, "错误", f"保存修改时发生异常：{str(e)}")            
        elif self.searchFlag==5:
            QMessageBox.information(self,"提示","购书记录由系统生成，不支持修改")
        elif self.searchFlag==6:
            QMessageBox.information(self,"提示","退书记录由系统生成，不支持修改")
        
    def save_changes_to_database(self,table_name):#修改函数执行
        conn = pymysql.Connect(host='localhost', user='root', passwd='110+120+z', database='bookmanage')
        cursor = conn.cursor()
        try:
            for row in range(self.tableWidget_Admin.rowCount()):
                values = []
                primary_key_value = self.tableWidget_Admin.item(row, 0).text()  # 第一列作为主键值
                primary_key_name = self.tableWidget_Admin.horizontalHeaderItem(0).text()  # 获取主键列的列名
                for column in range(self.tableWidget_Admin.columnCount()):
                    item = self.tableWidget_Admin.item(row, column)
                    if item is not None:
                        values.append(item.text())
                    else:
                        values.append('')
                    # 检查是否修改了主键列，如果是，则跳过当前行的更新
                    if column == 0 and primary_key_value != self.tableWidget_Admin.item(row, column).text():
                        QMessageBox.warning(self, "警告", "主键列不支持更新")
                        break
                else:
                    # 构建 UPDATE 语句
                    placeholders = ', '.join([f'{self.tableWidget_Admin.horizontalHeaderItem(column).text()} = %s' for column in range(1, self.tableWidget_Admin.columnCount())])  # 从第二列开始构建 SET 子句
                    cursor.execute(f"UPDATE {table_name} SET {placeholders} WHERE {primary_key_name} = %s", (values[1:] + [primary_key_value]))  # 使用主键列更新
            conn.commit()
            QMessageBox.information(self, "提示", "修改已生效")
        except Exception as e:
            conn.rollback()#回滚事务
            raise e#将异常重新抛出
        finally:
            cursor.close()
            conn.close()
    def deleteAllSelected(self, table_name):  # 执行删除操作
        selected_items = self.tableWidget_Admin.selectedItems()
        if selected_items:
            reply = QMessageBox.question(self, '确认删除', '确定要删除选中的行吗？', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                selected_rows = list(set(item.row() for item in selected_items))  # 获取所有选中的行号
                primary_key_column = self.tableWidget_Admin.horizontalHeaderItem(0).text()  # 假设主键列在第一列
                primary_key_values = [self.tableWidget_Admin.item(row, 0).text() for row in selected_rows]  # 获取所有选中行的主键值

                conn = pymysql.Connect(host='localhost', user='root', passwd='110+120+z', database='bookmanage')
                cursor = conn.cursor()
                try:
                    for primary_key_value in primary_key_values:
                        cursor.execute(f"DELETE FROM {table_name} WHERE {primary_key_column} = %s", (primary_key_value,))
                    conn.commit()
                    QMessageBox.information(self, "提示", "删除成功")
                    if self.searchFlag == 1:
                        self.AdminWindowShow()
                    elif self.searchFlag == 2:
                        self.EmployWindowShow()
                    elif self.searchFlag == 3:
                        self.CustomerWindowShow()
                    elif self.searchFlag == 4:
                        self.BookWindowShow()

                except Exception as e:
                    conn.rollback()  # 回滚事务
                    QMessageBox.warning(self, "警告", f"删除失败：{str(e)}")
                finally:
                    cursor.close()
                    conn.close()
            else:
                return
        else:
            QMessageBox.warning(self, "警告", "请先选择要删除的行")

    def btnDelete_clicked(self):
        print('btnDelete is clicked')
        if self.searchFlag==1:
            table_name='admin_info'
            try:
                self.deleteAllSelected(table_name)
            except Exception as e:
                QMessageBox.critical(self, "错误", f"删除时发生异常：{str(e)}")
        elif self.searchFlag==2:
            table_name='工作人员'
            try:
                self.deleteAllSelected(table_name)
            except Exception as e:
                QMessageBox.critical(self, "错误", f"删除时发生异常：{str(e)}")            
        elif self.searchFlag==3:
            table_name='会员'
            try:
                self.deleteAllSelected(table_name)
            except Exception as e:
                QMessageBox.critical(self, "错误", f"删除时发生异常：{str(e)}")            
        elif self.searchFlag==4:
            table_name='图书'
            try:
                self.deleteAllSelected(table_name)
            except Exception as e:
                QMessageBox.critical(self, "错误", f"删除时发生异常：{str(e)}")            
        elif self.searchFlag==5:
            QMessageBox.information(self,"提示","购书记录由系统生成，不支持删除")
        elif self.searchFlag==6:
            QMessageBox.information(self,"提示","退书记录由系统生成，不支持删除")
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
                item = QTableWidgetItem(str(col_data))
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)  # 设置每个单元格不可编辑
                self.tableWidget_Admin.setItem(row_index, col_index, item)
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
                item = QTableWidgetItem(str(col_data))
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)  # 设置每个单元格不可编辑
                self.tableWidget_Admin.setItem(row_index, col_index, item)
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
                item = QTableWidgetItem(str(col_data))
                if col_index == 0:  # 如果是第一列
                    item.setFlags(item.flags() & ~Qt.ItemIsEditable)  # 设置第一列单元格不可编辑
                else:
                    item.setFlags(item.flags() | Qt.ItemIsEditable)  # 设置其他单元格可编辑
                self.tableWidget_Admin.setItem(row_index, col_index, item)
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
                item = QTableWidgetItem(str(col_data))
                if col_index == 0:  # 如果是第一列
                    item.setFlags(item.flags() & ~Qt.ItemIsEditable)  # 设置第一列单元格不可编辑
                else:
                    item.setFlags(item.flags() | Qt.ItemIsEditable)  # 设置其他单元格可编辑
                self.tableWidget_Admin.setItem(row_index, col_index, item)
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
                item = QTableWidgetItem(str(col_data))
                if col_index == 0:  # 如果是第一列
                    item.setFlags(item.flags() & ~Qt.ItemIsEditable)  # 设置第一列单元格不可编辑
                else:
                    item.setFlags(item.flags() | Qt.ItemIsEditable)  # 设置其他单元格可编辑
                self.tableWidget_Admin.setItem(row_index, col_index, item)
        cursor.close()
        cursor.close()
        conn.close()
    def AdminWindowShow(self):    #管理员界面
        print('AdminWindowShow')
        self.searchFlag=1
        print(self.searchFlag)
        if self.isAdmin==1:
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
                    item = QTableWidgetItem(str(col_data))
                    if col_index == 0:  # 如果是第一列
                        item.setFlags(item.flags() & ~Qt.ItemIsEditable)  # 设置第一列单元格不可编辑
                    else:
                        item.setFlags(item.flags() | Qt.ItemIsEditable)  # 设置其他单元格可编辑
                    self.tableWidget_Admin.setItem(row_index, col_index, item)
            cursor.close()
            cursor.close()
            conn.close()
        else:
            QMessageBox.warning(self, "权限错误", "你不是管理员。无权查看此表")
    def btnInsert_clicked(self):#插入数据
        print('Insert is clicked')
         #TODO:根据flag判断是哪个界面弹出对应的插入窗口
        if self.searchFlag==4:
            self.Insert=InsertForm1(self)#传递父窗口
            self.Insert.show()
            self.Insert.raise_()
        elif self.searchFlag==2:
            self.Insert_e=InsertForm_E(self)
            self.Insert_e.show()
            self.Insert_e.raise_()
        elif self.searchFlag==3:
            self.Insert_c=InsertForm_C(self)
            self.Insert_c.show()
            self.Insert_c.raise_()
        elif self.searchFlag==1:
            self.Insert_Admin=InsertForm_Admin(self)
            self.Insert_Admin.show()
            self.Insert_Admin.raise_()
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
class MainwindowForm_E(QMainWindow,Ui_MainWindow_E):# 职工界面主界面
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
    #TODO:加一个判断 显示不同界面 分为管理员（MainwindowForm_E）和职工（MainwindowForm）职工界面相比管理员界面少了管理员和职工的显示 只显示图书、会员、退书记录、购书记录
    window.show()
    sys.exit(app.exec_())