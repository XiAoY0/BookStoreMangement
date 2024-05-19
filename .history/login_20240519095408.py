import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QFileDialog, QMainWindow, QMessageBox , QLineEdit,QApplication,QPushButton, QVBoxLayout, QWidget, QDialog
from Ui_Login import Ui_Login

class loginForm(QDialog, Ui_Login):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setupUi(self)
    def mouseMoveEvent(self, e: QMouseEvent):  # 重写移动事件
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