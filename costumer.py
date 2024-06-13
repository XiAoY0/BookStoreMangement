import sys
import os
import csv
import mysql
import pymysql
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QFileDialog, QMainWindow, QMessageBox , QLineEdit,QCheckBox,QApplication,QPushButton, QVBoxLayout, QWidget, QDialog,QLabel,QTableWidgetItem,QInputDialog
from UI.Ui_Costumer import Ui_MainWindow_Customer
class Customer(QMainWindow,Ui_MainWindow_Customer):
    def __init__(self,username):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)#隐藏边框
        self.setAttribute(Qt.WA_TranslucentBackground)#透明背景
        self.setupUi(self)
        self.username = username
        self.searchFlag=0
        # 槽函数连接 左侧界面选择
        #购物车
        self.label_11.setOpenExternalLinks(False)
        self.label_11.linkActivated.connect(self.Cartshow)
        #我的信息
        self.label_8.setOpenExternalLinks(False)
        self.label_8.linkActivated.connect(self.Myinfoshow)
        #购书界面
        self.label_12.setOpenExternalLinks(False)
        self.label_12.linkActivated.connect(self.Buythebook)
        #收藏夹
        self.label_14.setOpenExternalLinks(False)
        self.label_14.linkActivated.connect(self.Starshow)
        #历史购书
        self.label_13.setOpenExternalLinks(False)
        self.label_13.linkActivated.connect(self.History)
        #槽函数连接 按钮事件
        #退书按钮
        self.pushButton_6.clicked.connect(self.ReturnBook)
        #结算
        self.pushButton_5.clicked.connect(self.Pay)
        #添加到收藏夹
        self.pushButton_4.clicked.connect(self.IntotheStar)
        #添加到购物车
        self.pushButton_3.clicked.connect(self.IntotheCart)
        #删除
        self.pushButton_2.clicked.connect(self.DeleteBookinfo)
        #查询
        self.pushButton.clicked.connect(self.SearchThebook)
        #关闭窗口函数
        self.btn_Close.clicked.connect(self.btnClose_clicked)

    def setupTableHeaders(self, cursor, include_checkboxes=False):
        # 设置表头，包括复选框列（如果需要）
        column_headers = ["Select"] if include_checkboxes else []
        column_headers += [description[0] for description in cursor.description]
        self.tableWidget_Admin.setColumnCount(len(column_headers))
        for col_index, header in enumerate(column_headers):
            header_item = QTableWidgetItem(header)
            self.tableWidget_Admin.setHorizontalHeaderItem(col_index, header_item)

    def ReturnBook(self):
        print("Return book")
        try:
            # 弹出选择框选择办理人
            with pymysql.connect(host='localhost', user='root', passwd='110+120+z', database='bookmanage') as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT 员工编号, 员工姓名 FROM 工作人员")
                employees = cursor.fetchall()
                employee_dict = {f"{employee[1]} ({employee[0]})": employee[0] for employee in employees}
                if not employee_dict:
                    raise Exception("无可用员工办理。")
                items = list(employee_dict.keys())
                item, ok = QInputDialog.getItem(self, "选择办理人", "请选择办理人:", items, 0, False)
                if not ok or not item:
                    raise Exception("未选择办理人。")
                employee_id = employee_dict[item]

                # 查询会员信息
                cursor.execute("SELECT 会员联系方式, 会员姓名, 会员类别 FROM 会员 WHERE 会员编号 = %s", (self.username,))
                member_info = cursor.fetchone()
                if not member_info:
                    raise Exception("会员信息未找到。")
                member_contact, member_name, member_category = member_info

                # 遍历表格行
                for row in range(self.tableWidget_Admin.rowCount()):
                    checkbox = self.tableWidget_Admin.cellWidget(row, 0)
                    if checkbox and checkbox.isChecked():
                        headers = [self.tableWidget_Admin.horizontalHeaderItem(col).text() for col in range(self.tableWidget_Admin.columnCount())]

                        book_id_col = headers.index('图书编号')
                        book_name_col = headers.index('图书名称')
                        #unit_price_col = headers.index('图书价格')
                        #quantity_col = headers.index('数量')

                        book_id = self.tableWidget_Admin.item(row, book_id_col).text()
                        book_name = self.tableWidget_Admin.item(row, book_name_col).text()
                        #quantity = int(self.tableWidget_Admin.item(row, quantity_col).text())

                        # 检查购买记录是否存在
                        cursor.execute("SELECT 购买记录编号 FROM 购买记录 WHERE 会员编号 = %s AND 图书编号 = %s", (self.username, book_id))
                        purchase_record = cursor.fetchone()
                        if not purchase_record:
                            raise Exception(f"没有找到图书 '{book_name}' 的购买记录。")
                        purchase_record_id = purchase_record[0]

                        # 删除购买记录
                        cursor.execute("DELETE FROM 购买记录 WHERE 购买记录编号 = %s", (purchase_record_id,))

                        # 增加退书记录
                        cursor.execute("""
                            INSERT INTO 退书记录 (退款时间, 会员编号, 会员联系方式, 会员姓名, 图书编号, 图书名称, 办理人)
                            VALUES (NOW(), %s, %s, %s, %s, %s, %s)
                        """, (self.username, member_contact, member_name, book_id, book_name, employee_id))

                        # 更新库存数量
                        cursor.execute("SELECT 图书库存数量 FROM 图书 WHERE 图书编号 = %s", (book_id,))
                        current_stock = cursor.fetchone()
                        if not current_stock:
                            raise Exception(f"没有找到图书 '{book_name}' 的库存信息。")
                        new_stock = current_stock[0] + 1

                        cursor.execute("""
                            UPDATE 图书
                            SET 图书库存数量 = %s
                            WHERE 图书编号 = %s
                        """, (new_stock, book_id))

                # 提交事务
                conn.commit()

            # 显示退书成功信息
            QMessageBox.information(self, "提示", f"退书成功！办理人：{item}")
            self.History()
        except Exception as e:
            # 提示出现错误
            QMessageBox.critical(self, "错误", f"退书时发生错误: {str(e)}")   
    def Pay(self):
        print("pay the book")
        try:
            # 弹出选择框选择办理人
            with pymysql.connect(host='localhost', user='root', passwd='110+120+z', database='bookmanage') as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT 员工编号, 员工姓名 FROM 工作人员")
                employees = cursor.fetchall()
                employee_dict = {f"{employee[1]} ({employee[0]})": employee[0] for employee in employees}
                if not employee_dict:
                    raise Exception("无可用员工办理。")
                items = list(employee_dict.keys())
                item, ok = QInputDialog.getItem(self, "选择办理人", "请选择办理人:", items, 0, False)
                if not ok or not item:
                    raise Exception("未选择办理人。")
                employee_id = employee_dict[item]
                total_price = 0  # 初始化总价格
                # 查询会员信息
                cursor.execute("SELECT 会员联系方式, 会员姓名, 会员类别 FROM 会员 WHERE 会员编号 = %s", (self.username,))
                member_info = cursor.fetchone()
                if not member_info:
                    raise Exception("会员信息未找到。")
                member_contact, member_name, member_category = member_info                
                # 遍历表格行
                for row in range(self.tableWidget_Admin.rowCount()):
                    checkbox = self.tableWidget_Admin.cellWidget(row, 0)
                    if checkbox and checkbox.isChecked():
                        headers = [self.tableWidget_Admin.horizontalHeaderItem(col).text() for col in range(self.tableWidget_Admin.columnCount())]
                        
                        book_id_col = headers.index('图书编号')
                        book_name_col = headers.index('图书名称')
                        unit_price_col = headers.index('图书价格')
                        quantity_col = headers.index('数量')

                        book_id = self.tableWidget_Admin.item(row, book_id_col).text()
                        book_name = self.tableWidget_Admin.item(row, book_name_col).text()
                        unit_price = float(self.tableWidget_Admin.item(row, unit_price_col).text())
                        quantity = int(self.tableWidget_Admin.item(row, quantity_col).text())  # 获取购买数量

                        total_price += unit_price * quantity  # 累加总价格

                        # 检查库存是否充足
                        cursor.execute("SELECT 图书库存数量 FROM 图书 WHERE 图书编号 = %s", (book_id,))
                        result = cursor.fetchone()
                        if result is None or result[0] < quantity:
                            raise Exception(f"书籍 '{book_name}' 库存不足或不存在。")

                        # 更新库存数量
                        cursor.execute("""
                            UPDATE 图书
                            SET 图书库存数量 = 图书库存数量 - %s
                            WHERE 图书编号 = %s
                        """, (quantity, book_id))
                        # 写入购书记录
                        cursor.execute("""
                            INSERT INTO 购买记录 (购买时间, 会员编号, 会员联系方式, 会员姓名, 会员类别,图书编号,图书名称,办理人)
                            VALUES (NOW(),%s, %s, %s, %s, %s, %s, %s)
                        """,  (self.username, member_contact, member_name, member_category, book_id, book_name, employee_id))

                # 提交事务
                conn.commit()

            # 显示结算成功信息和总价格
            QMessageBox.information(self, "提示", f"结算成功！总价格为：{total_price:.2f} 元，办理人：{item}")
        except Exception as e:
            # 提示出现错误
            QMessageBox.critical(self, "错误", f"结算时发生错误: {str(e)}")       
    def IntotheStar(self):
        print("into the star")
        if self.searchFlag==1:
            conn = pymysql.connect(host='localhost', user='root', passwd='110+120+z', database='bookmanage')
            cursor = conn.cursor()
            for row in range(self.tableWidget_Admin.rowCount()):
                checkbox = self.tableWidget_Admin.cellWidget(row, 0)
                if checkbox and checkbox.isChecked():
                    book_id = self.tableWidget_Admin.item(row, 1).text()
                    book_name = self.tableWidget_Admin.item(row, 2).text()
                    unit_price = float(self.tableWidget_Admin.item(row, 4).text())

                    cursor.execute("""
                        INSERT INTO 收藏夹 (会员编号, 图书编号, 图书名称, 图书价格)
                        VALUES (%s, %s, %s, %s)
                    """, (self.username, book_id, book_name, unit_price))
            conn.commit()
            cursor.close()
            conn.close()
            QMessageBox.information(self, "提示", "成功添加到收藏夹！")
        else:
            QMessageBox.warning(self,"warning","本界面内容不能添加至收藏夹！请检查！")

    def IntotheCart(self):
        print("Into the cart")
        if self.searchFlag==1:
            conn = pymysql.connect(host='localhost', user='root', passwd='110+120+z', database='bookmanage')
            cursor = conn.cursor()
            for row in range(self.tableWidget_Admin.rowCount()):
                checkbox = self.tableWidget_Admin.cellWidget(row, 0)
                if checkbox and checkbox.isChecked():
                    book_id = self.tableWidget_Admin.item(row, 1).text()
                    book_name = self.tableWidget_Admin.item(row, 2).text()
                    unit_price = float(self.tableWidget_Admin.item(row, 4).text())
                    quantity = 1  # 可以根据需求设置数量
                    total_price = unit_price * quantity

                    cursor.execute("""
                        INSERT INTO 购物车 (会员编号, 图书编号, 图书名称, 图书价格, 数量, 图书总价)
                        VALUES (%s, %s, %s, %s, %s, %s)
                    """, (self.username, book_id, book_name, unit_price, quantity, total_price))
            conn.commit()
            cursor.close()
            conn.close()
            QMessageBox.information(self, "提示", "成功添加到购物车！")
        else:
            QMessageBox.warning(self,"warning","本界面内容不能添加至收藏夹！请检查！")
    def DeleteBookinfo(self,table_name):
        if self.searchFlag==2:
            table_name="购物车"
        elif self.searchFlag==3:
            table_name="收藏夹"
        else:
            QMessageBox.warning(self,"warning","你没有删除的权限！")
        print("Delete book info")
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
                    if self.searchFlag == 2:
                        self.Cartshow()
                    elif self.searchFlag == 3:
                        self.Starshow()
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
    def SearchThebook(self,include_checkboxes=True):
        print("search the book")
        self.Searchtext=self.lineEdit.text()#输入框内容
        print(self.Searchtext)
        if self.searchFlag==1: 
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
            # 增加一个复选框列
            self.tableWidget_Admin.setRowCount(len(data))
            self.setupTableHeaders(cursor, include_checkboxes)  # 调用设置表头的函数
            #TODO：复选框的显示有问题
            # 
            for row_index, row_data in enumerate(data):
                if include_checkboxes:
                    checkbox = QCheckBox()
                    self.tableWidget_Admin.setCellWidget(row_index, 0, checkbox)  

                for col_index, col_data in enumerate(row_data):
                    item = QTableWidgetItem(str(col_data))
                    item.setFlags(item.flags() & ~Qt.ItemIsEditable)  # 设置单元格不可编辑
                    self.tableWidget_Admin.setItem(row_index, col_index + (1 if include_checkboxes else 0), item) 

            cursor.close()
            conn.close()
        else:
            QMessageBox.warning(self,"warning","错误，请检查操作！")
    def Cartshow(self,include_checkboxes=True):
        print("cart show")
        self.searchFlag = 2
        conn = pymysql.connect(host='localhost', user='root', passwd='110+120+z', database='bookmanage')
        cursor = conn.cursor()
        query = "SELECT * FROM 购物车 WHERE 会员编号 = %s"
        cursor.execute(query, (self.username,))
        data = cursor.fetchall()

        self.tableWidget_Admin.setRowCount(len(data))
        self.setupTableHeaders(cursor, include_checkboxes)  # 调用设置表头的函数

        # 填充表格数据
        for row_index, row_data in enumerate(data):
            if include_checkboxes:
                checkbox = QCheckBox()
                self.tableWidget_Admin.setCellWidget(row_index, 0, checkbox)  # 在第一列添加复选框

            for col_index, col_data in enumerate(row_data):
                item = QTableWidgetItem(str(col_data))
                header_text = self.tableWidget_Admin.horizontalHeaderItem(col_index + (1 if include_checkboxes else 0)).text()
                if header_text == '数量':  # 设置数量列可编辑
                    item.setFlags(item.flags() | Qt.ItemIsEditable)
                else:
                    item.setFlags(item.flags() & ~Qt.ItemIsEditable)
                self.tableWidget_Admin.setItem(row_index, col_index + (1 if include_checkboxes else 0), item)  # 复选框列后移一位

        cursor.close()
        conn.close()

    def Myinfoshow(self,include_checkboxes=False):
        
        conn = pymysql.connect(host='localhost', user='root', passwd='110+120+z', database='bookmanage')
        cursor = conn.cursor()
        query = "SELECT * FROM 会员 WHERE 会员编号 = %s"
        cursor.execute(query, (self.username,))
        data = cursor.fetchall()

        if data:
            self.tableWidget_Admin.setRowCount(len(data))
            self.setupTableHeaders(cursor, include_checkboxes)  # 调用设置表头的函数

            for row_index, row_data in enumerate(data):
                if include_checkboxes:
                    checkbox = QCheckBox()
                    self.tableWidget_Admin.setCellWidget(row_index, 0, checkbox)  # Adding the checkbox to the first column

                for col_index, col_data in enumerate(row_data):
                    item = QTableWidgetItem(str(col_data))
                    if col_index == 0:  # 如果是第一列
                        item.setFlags(item.flags() & ~Qt.ItemIsEditable)  # 设置第一列单元格不可编辑
                    else:
                        item.setFlags(item.flags() | Qt.ItemIsEditable)  # 设置其他单元格可编辑
                    self.tableWidget_Admin.setItem(row_index, col_index + (1 if include_checkboxes else 0), item)  # Shift by one for checkbox column
        else:
            print("No data found for the given username.")

        cursor.close()
        conn.close()
    def Buythebook(self, include_checkboxes=True):
        print("buy the book")
        self.searchFlag=1
        conn = pymysql.connect(host='localhost', user='root', passwd='110+120+z', database='bookmanage')
        cursor = conn.cursor()
        cursor.execute("select * from 图书")
        data = cursor.fetchall()

        # 增加一个复选框列
        self.tableWidget_Admin.setRowCount(len(data))
        self.setupTableHeaders(cursor, include_checkboxes)  # 调用设置表头的函数

        # Fill the table with data
        for row_index, row_data in enumerate(data):
            if include_checkboxes:
                checkbox = QCheckBox()
                self.tableWidget_Admin.setCellWidget(row_index, 0, checkbox)  # Adding the checkbox to the first column

            for col_index, col_data in enumerate(row_data):
                item = QTableWidgetItem(str(col_data))
                if col_index == 0:  # 如果是第一列
                    item.setFlags(item.flags() & ~Qt.ItemIsEditable)  # 设置第一列单元格不可编辑
                else:
                    item.setFlags(item.flags() | Qt.ItemIsEditable)  # 设置其他单元格可编辑
                self.tableWidget_Admin.setItem(row_index, col_index + (1 if include_checkboxes else 0), item)  # Shift by one for checkbox column

        cursor.close()
        conn.close()
    def Starshow(self,include_checkboxes=True):
        print("star ")
        self.searchFlag = 3
        conn = pymysql.connect(host='localhost', user='root', passwd='110+120+z', database='bookmanage')
        cursor = conn.cursor()
        query = "SELECT * FROM 收藏夹 WHERE 会员编号 = %s"
        cursor.execute(query, (self.username,))
        data = cursor.fetchall()

        self.tableWidget_Admin.setRowCount(len(data))
        self.setupTableHeaders(cursor, include_checkboxes)  # 调用设置表头的函数

        # 填充表格数据
        for row_index, row_data in enumerate(data):
            if include_checkboxes:
                checkbox = QCheckBox()
                self.tableWidget_Admin.setCellWidget(row_index, 0, checkbox)  # 在第一列添加复选框

            for col_index, col_data in enumerate(row_data):
                item = QTableWidgetItem(str(col_data))
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)  # 设置每个单元格不可编辑
                self.tableWidget_Admin.setItem(row_index, col_index + (1 if include_checkboxes else 0), item)  # 复选框列后移一位

        cursor.close()
        conn.close()
    def History(self):
        self.searchFlag=4
        conn = pymysql.Connect(host='localhost', user='root', passwd='110+120+z', database='bookmanage')
        cursor = conn.cursor()
        query = "select * from 购买记录 where 会员编号 = %s"
        cursor.execute(query, (self.username,))
        data = cursor.fetchall()
        
        # 设置行数和列数，列数比数据列数多1，用于复选框
        self.tableWidget_Admin.setRowCount(len(data))
        self.tableWidget_Admin.setColumnCount(len(data[0]) + 1)
        
        # 设置复选框列的表头
        header_item = QTableWidgetItem("")
        self.tableWidget_Admin.setHorizontalHeaderItem(0, header_item)
        
        # 设置其他列的表头
        column_headers = [description[0] for description in cursor.description]
        for col_index, header in enumerate(column_headers):
            header_item = QTableWidgetItem(header)
            self.tableWidget_Admin.setHorizontalHeaderItem(col_index + 1, header_item)
        
        # 为表格添加数据和复选框
        for row_index, row_data in enumerate(data):
            checkbox = QCheckBox()
            self.tableWidget_Admin.setCellWidget(row_index, 0, checkbox)
            for col_index, col_data in enumerate(row_data):
                item = QTableWidgetItem(str(col_data))
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)  # 设置每个单元格不可编辑
                self.tableWidget_Admin.setItem(row_index, col_index + 1, item)
        
        cursor.close()
        conn.close()       
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
# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     window = Customer(username)
#     window.show()
#     sys.exit(app.exec_())