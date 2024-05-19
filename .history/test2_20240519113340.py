import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QCheckBox

class PasswordWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Password Show/Hide')
        self.setGeometry(300, 300, 250, 150)

        layout = QVBoxLayout()

        self.passwordEdit = QLineEdit()
        self.passwordEdit.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.passwordEdit)

        self.showPasswordCheckBox = QCheckBox('Show Password')
        self.showPasswordCheckBox.stateChanged.connect(self.togglePassword)
        layout.addWidget(self.showPasswordCheckBox)

        self.setLayout(layout)

    def togglePassword(self, state):
        if self.showPasswordCheckBox.isChecked():
            self.passwordEdit.setEchoMode(QLineEdit.Normal)
        else:
            self.passwordEdit.setEchoMode(QLineEdit.Password)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PasswordWidget()
    window.show()
    sys.exit(app.exec_())
