# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'personal.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import threading


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(525, 556)
        #Dialog.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(525, 556))
        Dialog.setMaximumSize(QtCore.QSize(525, 556))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("image/QQicon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 0, 531, 41))
        self.frame.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(200, 10, 101, 20))
        self.label.setStyleSheet("font: 12pt \"Agency FB\";\n"
"color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(494, 0, 31, 23))
        self.pushButton_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(460, 0, 31, 23))
        self.pushButton_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(10, 390, 361, 91))
        self.textEdit.setObjectName("textEdit")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(10, 80, 361, 291))
        self.textBrowser.setObjectName("textBrowser")
        self.frame_2 = QtWidgets.QFrame(Dialog)
        self.frame_2.setGeometry(QtCore.QRect(380, 40, 151, 521))
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(10, 60, 124, 251))
        self.frame_3.setStyleSheet("background-image: url(image/qqman2.jpg);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(10, 500, 81, 31))
        self.pushButton.setStyleSheet("background-color: rgb(255, 170, 127);\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 500, 91, 31))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 170, 127);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog)
        self.pushButton_4.clicked.connect(Dialog.showMinimized)
        self.pushButton_3.clicked.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "聊天"))
        self.label.setText(_translate("Dialog", "perl"))
        self.pushButton_3.setText(_translate("Dialog", "关闭"))
        self.pushButton_4.setText(_translate("Dialog", "隐藏"))
        self.pushButton.setText(_translate("Dialog", "关闭"))
        self.pushButton_2.setText(_translate("Dialog", "发送"))

    def pel_send(self,s,sendname,recvname):
        def send():
            send_list=['personal']
            send_list.append(sendname)
            send_list.append(recvname)
            sendtext=self.textEdit.toPlainText()
            if sendtext!=' ':
                send_list.append(sendtext)
                textsend=' '.join(send_list)
                s.send(textsend.encode())
            self.textEdit.clear()
        self.pushButton_2.clicked.connect(send)

    def pel_recv(self,s):
        buffsize = 1024
        def recv():
            while True:
                recvtext=s.recv(buffsize).decode('utf-8')
                self.textBrowser.append(recvtext + "\n")
                print(recvtext)
        re = threading.Thread(target=recv)  # 创建线程
        re.start()

    def quit(self,Dlog):
        def quit():
            Dlog.close()
        self.pushButton.clicked.connect(quit)


