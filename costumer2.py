import sys
import os
import csv
import mysql
import pymysql
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QFileDialog, QMainWindow, QMessageBox , QLineEdit,QCheckBox,QApplication,QPushButton, QVBoxLayout, QWidget, QDialog,QLabel,QTableWidgetItem
from UI.Ui_Costumer import Ui_MainWindow_Customer
class Customer(QMainWindow,Ui_MainWindow_Customer):
    def __init__(self,username):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)#隐藏边框
        self.setAttribute(Qt.WA_TranslucentBackground)#透明背景
        self.setupUi(self)
        self.username = username
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
    
    def Pay(self):
        print("pay the book")
        try:
            # 连接到数据库
            with pymysql.connect(host='localhost', user='root', passwd='110+120+z', database='bookmanage') as conn:
                cursor = conn.cursor()
                total_price = 0  # 初始化总价格

                # 遍历表格行
                for row in range(self.tableWidget_Admin.rowCount()):
                    checkbox = self.tableWidget_Admin.cellWidget(row, 0)
                    if checkbox and checkbox.isChecked():
                        book_id = self.tableWidget_Admin.item(row, 1).text()
                        book_name = self.tableWidget_Admin.item(row, 2).text()
                        unit_price = float(self.tableWidget_Admin.item(row, 4).text())
                        quantity = int(self.tableWidget_Admin.item(row, 7).text())  # 获取购买数量

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

                # 提交事务
                conn.commit()

            # 显示结算成功信息和总价格
            QMessageBox.information(self, "提示", f"结算成功！总价格为：{total_price:.2f} 元")

        except Exception as e:
            # 提示出现错误
            QMessageBox.critical(self, "错误", f"结算时发生错误: {str(e)}")
    
    def IntotheStar(self):
        print("into the star")
        conn = pymysql.connect(host='localhost', user='root', passwd='123456', database='bookmanage')
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

    def IntotheCart(self):
        print("Into the cart")
        conn = pymysql.connect(host='localhost', user='root', passwd='123456', database='bookmanage')
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
    def DeleteBookinfo(self):
        print("Delete book info")
    def SearchThebook(self):
        print("search the book")
    def Cartshow(self):
        print("cart show")
        conn = pymysql.Connect(host='localhost', user='root', passwd='123456', database='bookmanage')
        cursor = conn.cursor()
        query = "SELECT * FROM 购物车 WHERE 会员编号 = %s"
        cursor.execute(query, (self.username,))
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
                header_text = self.tableWidget_Admin.horizontalHeaderItem(col_index).text()
                if header_text == '数量':  # 设置数量列可编辑
                    item.setFlags(item.flags() | Qt.ItemIsEditable)
                else:
                    item.setFlags(item.flags() & ~Qt.ItemIsEditable)
                self.tableWidget_Admin.setItem(row_index, col_index, item)
        self.tableWidget_Admin.cellChanged.connect(self.updateTotalPrice)
        cursor.close()
        conn.close()
    def updateTotalPrice(self, row, col):
        quantity_col = None
        price_col = None
        total_price_col = None

        # 根据列名获取对应的列索引
        for index in range(self.tableWidget_Admin.columnCount()):
            header_text = self.tableWidget_Admin.horizontalHeaderItem(index).text()
            if header_text == '数量':
                quantity_col = index
            elif header_text == '图书单价':
                price_col = index
            elif header_text == '图书总价':
                total_price_col = index

        if quantity_col is None or price_col is None or total_price_col is None:
            QMessageBox.warning(self, "错误", "列名设置有误")
            return

        if col == quantity_col:
            try:
                quantity_item = self.tableWidget_Admin.item(row, quantity_col)
                price_item = self.tableWidget_Admin.item(row, price_col)
                total_price_item = self.tableWidget_Admin.item(row, total_price_col)

                if quantity_item and price_item:
                    quantity = int(quantity_item.text())
                    price = float(price_item.text())
                    total_price = quantity * price

                    if total_price_item is None:
                        total_price_item = QTableWidgetItem(str(total_price))
                        self.tableWidget_Admin.setItem(row, total_price_col, total_price_item)
                    else:
                        total_price_item.setText(str(total_price))

                    # 更新数据库中的总价
                    conn = pymysql.connect(host='localhost', user='root', passwd='110+120+z', database='bookmanage')
                    cursor = conn.cursor()
                    update_query = "UPDATE 购物车 SET 图书总价 = %s, 数量 = %s WHERE 会员编号 = %s AND 图书名称 = %s"
                    cursor.execute(update_query, (total_price, quantity, self.username, self.tableWidget_Admin.item(row, 1).text()))
                    conn.commit()
                    cursor.close()
                    conn.close()
            except ValueError:
                QMessageBox.warning(self, "输入错误", "数量和单价必须是有效数字")
    def Myinfoshow(self,include_checkboxes=False):
        conn = pymysql.connect(host='localhost', user='root', passwd='123456', database='bookmanage')
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
        conn = pymysql.connect(host='localhost', user='root', passwd='123456', database='bookmanage')
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
    def Starshow(self):
        print("star ")
        conn = pymysql.connect(host='localhost', user='root', passwd='123456', database='bookmanage')
        cursor = conn.cursor()
        query = "SELECT * FROM 收藏夹 WHERE 会员编号 = %s"
        cursor.execute(query, (self.username,))
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
    def History(self):
        print("History show")
        conn = pymysql.Connect(host='localhost',user='root',passwd='123456',database='bookmanage')
        cursor = conn.cursor()
        query="select * from 购买记录 where 会员编号 = %s"
        cursor.execute(query,(self.username,))
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

#if __name__ == "__main__":
#   app = QtWidgets.QApplication(sys.argv)
#   window = Customer(username)
#   window.show()
#   sys.exit(app.exec_()) 