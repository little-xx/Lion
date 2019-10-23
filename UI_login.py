from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Ui_loginWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_loginWindow, self).__init__()
        self.resize(1048, 600)
        self.setWindowTitle("Lion")
        self.btn = QtWidgets.QPushButton("Start", self)
        self.btn.setGeometry(QtCore.QRect(100, 100, 141, 71))
        self.btn.setStyleSheet("QPushButton{color:black}"
                               "QPushButton:hover{color:red}"
                               "QPushButton{background-color:rgb(78,255,255)}"
                               "QPushButton{border:0px}"
                               "QPushButton{border-radius:10px}"
                               "QPushButton{padding:2px 4px}"
                               )
        self.setStyleSheet("background-image:url(background.png)")

        self.show()
        self.center()



    def center(self):
        qr = self.frameGeometry()
        # 获得屏幕中心点
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        # 显示到屏幕中心
        qr.moveCenter(cp)
        self.move(qr.topLeft())


class Ui_login(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_login, self).__init__()
        self.setObjectName('Custom_Dialog')
        self.resize(480, 400)
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
        self.initUi()

    def initUi(self):
        self.widget = QtWidgets.QWidget(self)
        self.widget.resize(480, 400)
        self.setWindowTitle("login")
        self.setWindowFlags(QtCore.Qt.Popup)
        self.widget.setStyleSheet("border-radius:5px;background-color:#36393e;")

        self.lab1 = QtWidgets.QLabel("Welcome!", self)
        self.lab1.setFont(QtGui.QFont('SansSerif'))
        self.lab1.setStyleSheet("color:white;font-size:30px; font:comic sans ms;")
        self.lab1.setGeometry(165, 10, 150, 100)

        self.lab2 = QtWidgets.QLabel("USER", self)
        self.lab2.move(90, 100)
        self.lab2.setStyleSheet("color:#8f9297;font-size:12px")

        self.login_user = QtWidgets.QLineEdit(self)
        self.login_user.setGeometry(90, 130, 290, 35)
        self.login_user.setStyleSheet("background-color:#303338; border-radius:5px; border:1px solid #191818; color:white; ")

        self.lab3 = QtWidgets.QLabel("PASSWORD", self)
        self.lab3.move(90, 190)
        self.lab3.setStyleSheet("color:#8f9297;font-size:12px")

        self.login_password = QtWidgets.QLineEdit(self)
        self.login_password.setGeometry(90, 220, 290, 35)
        self.login_password.setStyleSheet("background-color:#303338; border-radius:5px; border:1px solid #191818; color:white")
        self.login_password.setEchoMode(QtWidgets.QLineEdit.Password)

        self.btn = QtWidgets.QPushButton("Login", self)
        self.btn.setGeometry(90, 295, 290, 40)
        self.btn.setStyleSheet("background-color:#758ad4; color:white;border-radius:5px; font-size:14px;")
        self.btn.setShortcut("return")
        self.btn.clicked.connect(self.login)

        self.center()

    def center(self):
        qr = self.frameGeometry()
        # 获得屏幕中心点
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        # 显示到屏幕中心
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def handle_click(self):
        self.show()

    def handle_close(self):
        self.close()

    def login(self):
        text_user = self.login_user.text()
        text_password = self.login_password.text()
        if text_user == 'wlz' and text_password == 'wlz123':
            self.handle_close()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    loginw = Ui_loginWindow()
    login = Ui_login()
    loginw.btn.clicked.connect(login.handle_click)
    sys.exit(app.exec())
