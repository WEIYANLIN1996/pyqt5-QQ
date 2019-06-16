# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.11.2

# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication,QMessageBox
#import login_rc
import sys
from socket import *
import threading




class Ui_MainWindow(object):

    def tcp_start(self):
        address = '127.0.0.1'
        port = 6337
        self.buffsize = 1024
        self.s = socket(AF_INET, SOCK_STREAM)
        self.s.connect((address, port))

    def setupUi(self, MainWindow):
        self.MainWindow=MainWindow
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(360, 340)
        self.MainWindow.setMinimumSize(QtCore.QSize(360, 340))
        self.MainWindow.setMaximumSize(QtCore.QSize(360, 340))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("image/QQicon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MainWindow.setWindowIcon(icon)
        #MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(100, 160, 191, 30))
        self.lineEdit.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setText("")
        self.lineEdit.setMaxLength(32767)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 210, 191, 31))
        self.lineEdit_2.setInputMask("")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setMaxLength(32767)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setCursorPosition(0)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(70, 260, 221, 41))
        self.pushButton.setStyleSheet("background-color: rgb(7, 85, 240);\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.login)



        self.formFrame = QtWidgets.QFrame(self.centralwidget)
        self.formFrame.setGeometry(QtCore.QRect(0, -1, 361, 151))
        self.formFrame.setStyleSheet("border-color: rgb(0, 85, 255);\n"
"background-image: url(image/loginicon.jpg);")
        self.formFrame.setObjectName("formFrame")
        self.formLayout = QtWidgets.QFormLayout(self.formFrame)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 170, 31, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 220, 31, 16))
        self.label_2.setObjectName("label_2")


        #MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        #MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(self.MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.MainWindow.setWindowTitle(_translate("MainWindow", "QQ登录"))
        self.pushButton.setText(_translate("MainWindow", "登录"))
        self.label.setText(_translate("MainWindow", "账号："))
        self.label_2.setText(_translate("MainWindow", "密码："))

    def login(self):
        login_info=['login']
        self.user=self.lineEdit.text()
        password=self.lineEdit_2.text()
        user_l=len(str(self.user))
        if self.user=='':
            QMessageBox.information(self.MainWindow,'提示','QQ账号不能为空!', QMessageBox.Ok | QMessageBox.Close, QMessageBox.Close)
        elif user_l<5 or user_l>10:
            QMessageBox.information(self.MainWindow, '提示', 'QQ账号长度不对!', QMessageBox.Ok | QMessageBox.Close, QMessageBox.Close)
        else:
            if password=='':
                QMessageBox.information(self.MainWindow, '提示', '密码不能为空!', QMessageBox.Ok | QMessageBox.Close, QMessageBox.Close)
            else:
                login_info.append(self.user)
                login_info.append(password)
                login_info=' '.join(login_info)
                print(login_info)
                self.s.send(str(login_info).encode())
                self.login_recv()



    def login_recv(self):
        recv_info=self.s.recv(self.buffsize).decode('utf-8')
        print(recv_info)
        if str(recv_info)=='true':
            QMessageBox.information(self.MainWindow, '登录成功', '登录成功!', QMessageBox.Ok | QMessageBox.Close, QMessageBox.Close)
            #QtCore.QCoreApplication.instance().quit()
            widget.hide()
            widget1.show()
            ui1.label.setText(self.user)
        elif str(recv_info)=='flase-user':
            QMessageBox.information(self.MainWindow, '失败', '登录失败，无此账号!!', QMessageBox.Ok | QMessageBox.Close,QMessageBox.Close)
        elif str(recv_info)=='flase-pw':
            QMessageBox.information(self.MainWindow, '失败', '登录失败，密码错误!!', QMessageBox.Ok | QMessageBox.Close,QMessageBox.Close)
        elif str(recv_info)=='flase-login':
            QMessageBox.information(self.MainWindow, '失败', '此账号已登录!', QMessageBox.Ok | QMessageBox.Close,QMessageBox.Close)



if __name__ == "__main__":

    import sys
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui = Ui_MainWindow()
    ui.setupUi(widget)
    ui.tcp_start()
    widget.show()
    import QQ
    widget1 = QtWidgets.QWidget()
    ui1 = QQ.Ui_MainWindowt(ui.s)
    ui1.setupUit(widget1)

    '''app = QtWidgets.QApplication(sys.argv)
    widget2 = QtWidgets.QWidget()
    ui2 = QQchating.Ui_MainWindow()
    ui2.setupUi(widget2)
    child = QDialog()
    child_ui = personal.Ui_Dialog()
    child_ui.setupUi(child)'''


    sys.exit(app.exec_())


