import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem
import pymysql

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.populateTable()

    def initUI(self):
        self.setWindowTitle("Database Table Display")
        self.setGeometry(100, 100, 600, 400)

        self.tableWidget = QTableWidget(self)
        self.tableWidget.setGeometry(50, 50, 500, 300)

    def populateTable(self):
        # Connect to MySQL database
        try:
            conn = pymysql.connect(host='localhost', user='root', passwd='110+120+z', database='bookmanage')
            cursor = conn.cursor()

            # Execute the SQL query
            cursor.execute("SELECT * FROM admin_info")  # Replace 'your_table_name' with the actual table name

            # Fetch all the data
            data = cursor.fetchall()

            # Display the data in the table widget
            self.tableWidget.setRowCount(len(data))
            self.tableWidget.setColumnCount(len(data[0]))  # Assuming the number of columns is the same for all rows

            for row_index, row_data in enumerate(data):
                for col_index, col_data in enumerate(row_data):
                    self.tableWidget.setItem(row_index, col_index, QTableWidgetItem(str(col_data)))

        except pymysql.Error as e:
            print("Error connecting to MySQL:", e)
        finally:
            cursor.close()
            conn.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
