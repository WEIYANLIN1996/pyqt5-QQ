# -*- coding: utf-8 -*-

import sys
from QQlogin import Ui_Form
from PyQt5.QtWidgets import (QApplication,QWidget,QListWidget,QListWidgetItem,QFormLayout, QTextBrowser)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = QWidget()
    w.setWindowTitle('Simple')
    ui = Ui_Form()
    ui.setupUi(w)
    w.show()
    sys.exit(app.exec_())