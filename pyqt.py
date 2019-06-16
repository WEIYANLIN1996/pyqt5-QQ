#-*-coding:utf-8-*-

import sys
from PyQt5.QtWidgets import (QApplication,QWidget,QPushButton,QMessageBox, QPlainTextEdit,QTextEdit, QTextBrowser)
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore


class QQ(QWidget):
    def __init__(self):
        super().__init__()
        self.init()

    def init(self):
        self.setGeometry(100,50,800,550)
        self.setWindowTitle('QQ聊天室')
        self.setWindowIcon(QIcon('image/QQicon.ico'))
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)


        self.bt1=QPushButton('发送',self)
        self.bt1.move(20,500)


        self.brower=QTextBrowser(self)
        self.brower.move(10,50)
        self.bt1.clicked.connect(self.message)

        self.inputtext=QTextEdit(self)
        self.inputtext.move(20,300)


        self.show()
    def message(self):
        self.inputtext.append("hell0")



if __name__=="__main__":




    app=QApplication(sys.argv)
    qq=QQ()
    sys.exit(app.exec_())

