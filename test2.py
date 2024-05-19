
import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QFileDialog, QMainWindow, QMessageBox , QLineEdit,QApplication,QPushButton, QVBoxLayout, QWidget, QDialog
from Ui_Login import Ui_Login
from Ui_register import Ui_Register
from Ui_forget_widget import Ui_forget_widget
# 在一个窗口中调用另一个窗口
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Main Window')
        self.setGeometry(100, 100, 400, 300)

        self.open_other_window_button = QPushButton('Open Other Window', self)
        self.open_other_window_button.clicked.connect(self.open_other_window)

    def open_other_window(self):
        other_window = OtherWindow()
        other_window.show()

class OtherWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Other Window')
        self.setGeometry(200, 200, 300, 200)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
