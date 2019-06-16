#coding=utf-8

import sys
from PyQt5.QtWidgets import (QApplication,QWidget,QListWidget,QListWidgetItem,QFormLayout, QTextBrowser)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize


class qqview(QListWidget):

    def __init__(self):
        super().__init__()
        self.init()


    def init(self):
        self.setGeometry(100, 50, 800, 550)
        self.setWindowTitle('QQ聊天室')
        self.setWindowIcon(QIcon('image/QQicon.ico'))

        item = QListWidgetItem()
        item.setIcon(QIcon('D:\py\PyQt5学习\image\icon.jpg'))
        item.setText("frist")
        self.setIconSize(QSize(25,25))


        self.addItem(item)
        self.addItem("Item 2")
        self.addItem("Item 3")
        self.addItem("Item 4")

        self.setStyleSheet("QListWidget{border:1px solid black; color:black; }"
                           "QListWidget::Item{padding-top:20px; padding-bottom:4px; }"
                           "QListWidget::Item:hover{background:skyblue; }"
                           "QListWidget::item:selected:!active{border-width:0px; background:lightgreen; }"
                           )




        self.show()





if __name__ == "__main__":
    app = QApplication(sys.argv)
    qq = qqview()
    sys.exit(app.exec_())