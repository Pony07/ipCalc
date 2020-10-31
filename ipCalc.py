#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from ui.ipCalc import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        # 初始化父类 init
        super(MainWindow, self).__init__()
        self.setupUi(self)
        # 连接槽函数
        self.subnet_calc.clicked.connect(self.test)

    def test(self):
        self.subnet_result.insertPlainText('192.168.1.0/24\n')
        # 解决 macos 文本框不刷新问题
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
