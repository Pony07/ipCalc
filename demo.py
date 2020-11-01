#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from IPy import IP, IPSet
from netaddr import IPNetwork
from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox
from ipCalc.ui.ipCalc import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        # 初始化父类 init
        super(MainWindow, self).__init__()
        self.setupUi(self)
        # 连接按钮槽函数
        self.split_subnet_button.clicked.connect(self.subnet_split)

    def is_ip(self, address):
        """
        判断 ip 是否合规
        :param address:
        :return:
        """
        try:
            IP(address)
            return True
        except Exception as e:
            return False

    def calc(self, ip_segment, split_netmask):
        """
        功能：子网拆分
        :param ip_segment: 传入 ip 段
        :param split_netmask: 传入拆分掩码
        :return:
        """
        # 子网划分
        subnets = list(IPNetwork(ip_segment).subnet(split_netmask))
        subnet_result = ""
        # 遍历子网
        for subnet in subnets:
            subnet_result += str(subnet) + "\n"
        return subnet_result

    def subnet_split(self):
        # 获取 ip 网段信息
        ip_segment = self.ip_segment_value.text()
        # 获取分割掩码
        split_netmask = int(self.split_netmask_value.value())
        if self.is_ip(ip_segment):
            # 传入 ip 段和分割掩码，返回结果
            result = self.calc(ip_segment, split_netmask)
            # 文本框清空内容
            self.subnet_result.setPlainText('')
            # 文本框插入内容
            self.subnet_result.insertPlainText(result)
            # 解决 macos 文本框不刷新问题
            self.repaint()
        else:
            self.msg()

    def msg(self):
        """
        弹窗
        :return:
        """
        QMessageBox().warning(self, 'title', 'IP段：配置不合规')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
