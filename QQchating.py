# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QQchating.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from socket import *
import threading


class Ui_MainWindow(object):

    def recv_thead(self,s):
        buffsize = 1024
        def recv():
            while True:
                recvdata =s.recv(buffsize).decode('utf-8')
                self.textBrowser.append(recvdata + "\n" + "\n")
        re = threading.Thread(target=recv)  # 创建线程
        re.start()


    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(771, 588)
        self.MainWindow.setMinimumSize(QtCore.QSize(771, 585))
        self.MainWindow.setMaximumSize(QtCore.QSize(771, 588))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("image/QQicon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MainWindow.setWindowIcon(icon)
        self.MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 241, 571))
        self.frame.setStyleSheet("background-image: url(image/qqchatbk.jpg);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.listWidget = QtWidgets.QListWidget(self.frame)
        self.listWidget.setGeometry(QtCore.QRect(0, 50, 241, 521))
        self.listWidget.setIconSize(QtCore.QSize(40, 40))
        self.listWidget.setGridSize(QtCore.QSize(40, 40))
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("image/chatbk.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon1)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("image/qqchat.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon2)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setIcon(icon)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setIcon(icon)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("image/qqlogin.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon3)
        self.listWidget.addItem(item)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 10, 241, 31))
        self.label.setObjectName("label")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(240, 49, 531, 531))
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.frame_2)
        self.textBrowser.setGeometry(QtCore.QRect(10, 11, 511, 311))
        self.textBrowser.setObjectName("textBrowser")
        self.textEdit = QtWidgets.QTextEdit(self.frame_2)
        self.textEdit.setGeometry(QtCore.QRect(10, 340, 511, 131))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(354, 482, 91, 31))
        self.pushButton.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.pushButton.setObjectName("pushButton")
        #self.pushButton.clicked.connect(self.send)

        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setGeometry(QtCore.QRect(60, 480, 81, 31))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.pushButton_2.setObjectName("pushButton_2")

        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(240, 0, 531, 51))
        self.frame_3.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setGeometry(QtCore.QRect(220, 15, 101, 21))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        #MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        #MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.MainWindow.setWindowTitle(_translate("MainWindow", "QQ群聊"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "小伟"))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "one"))
        item = self.listWidget.item(2)
        item.setText(_translate("MainWindow", "hacker"))
        item = self.listWidget.item(3)
        item.setText(_translate("MainWindow", "perl"))
        item = self.listWidget.item(4)
        item.setText(_translate("MainWindow", "葱"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("MainWindow", "群聊人员："))
        self.pushButton.setText(_translate("MainWindow", "发送"))
        self.pushButton_2.setText(_translate("MainWindow", "关闭"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">TCP群聊</span></p></body></html>"))

    def dj_send(self,s,wename,user):
        def send():
            we_text=['wechat']
            we_text.append(wename)
            we_text.append(user)
            text=self.textEdit.toPlainText()
            if text!='':
                we_text.append(text)
                we_text=' '.join(we_text)
                s.send(we_text.encode())
            else:
                QtWidgets.QMessageBox.information(self.MainWindow, '警告', '输入消息为空！', QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Close, QtWidgets.QMessageBox.Close)
            self.textEdit.clear()

        self.pushButton.clicked.connect(send)

    def dj_quit(self,ui2):
        def quit():
            ui2.close()
        self.pushButton_2.clicked.connect(quit)


#import frist_rc

'''if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui = Ui_MainWindow()
    ui.setupUi(widget)
    widget.show()
    #ui.tcp_start()

    sys.exit(app.exec_())'''
