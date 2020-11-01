# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ipCalc.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(634, 763)
        self.actionfile = QAction(MainWindow)
        self.actionfile.setObjectName(u"actionfile")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.subnetting = QTabWidget(self.centralwidget)
        self.subnetting.setObjectName(u"subnetting")
        self.widget = QWidget()
        self.widget.setObjectName(u"widget")
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.ip_segment_label = QLabel(self.widget)
        self.ip_segment_label.setObjectName(u"ip_segment_label")

        self.horizontalLayout_3.addWidget(self.ip_segment_label)

        self.ip_segment_value = QLineEdit(self.widget)
        self.ip_segment_value.setObjectName(u"ip_segment_value")
        self.ip_segment_value.setMinimumSize(QSize(274, 0))
        self.ip_segment_value.setMaximumSize(QSize(274, 16777215))
        self.ip_segment_value.setMaxLength(32767)

        self.horizontalLayout_3.addWidget(self.ip_segment_value)

        self.line_2 = QFrame(self.widget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.line_2)

        self.split_netmask_label = QLabel(self.widget)
        self.split_netmask_label.setObjectName(u"split_netmask_label")

        self.horizontalLayout_3.addWidget(self.split_netmask_label)

        self.split_netmask_value = QSpinBox(self.widget)
        self.split_netmask_value.setObjectName(u"split_netmask_value")
        self.split_netmask_value.setMaximum(32)
        self.split_netmask_value.setValue(30)

        self.horizontalLayout_3.addWidget(self.split_netmask_value)

        self.line_3 = QFrame(self.widget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.line_3)

        self.split_subnet_button = QPushButton(self.widget)
        self.split_subnet_button.setObjectName(u"split_subnet_button")

        self.horizontalLayout_3.addWidget(self.split_subnet_button)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.subnet_Slider = QSlider(self.widget)
        self.subnet_Slider.setObjectName(u"subnet_Slider")
        self.subnet_Slider.setMouseTracking(False)
        self.subnet_Slider.setTabletTracking(False)
        self.subnet_Slider.setMaximum(32)
        self.subnet_Slider.setPageStep(15)
        self.subnet_Slider.setValue(30)
        self.subnet_Slider.setOrientation(Qt.Horizontal)

        self.verticalLayout.addWidget(self.subnet_Slider)

        self.line = QFrame(self.widget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.subnet_result = QTextEdit(self.widget)
        self.subnet_result.setObjectName(u"subnet_result")

        self.verticalLayout.addWidget(self.subnet_result)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.subnetting.addTab(self.widget, "")
        self.aggregation = QWidget()
        self.aggregation.setObjectName(u"aggregation")
        self.subnetting.addTab(self.aggregation, "")

        self.verticalLayout_2.addWidget(self.subnetting)


        self.gridLayout.addLayout(self.verticalLayout_2, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 634, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.subnet_Slider.valueChanged.connect(self.split_netmask_value.setValue)
        self.split_netmask_value.valueChanged.connect(self.subnet_Slider.setValue)

        self.subnetting.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionfile.setText(QCoreApplication.translate("MainWindow", u"file", None))
        self.ip_segment_label.setText(QCoreApplication.translate("MainWindow", u"IP\u6bb5\uff1a", None))
        self.ip_segment_value.setPlaceholderText(QCoreApplication.translate("MainWindow", u"192.168.0.0/24", None))
        self.split_netmask_label.setText(QCoreApplication.translate("MainWindow", u"\u62c6\u5206\u63a9\u7801\uff1a", None))
        self.split_subnet_button.setText(QCoreApplication.translate("MainWindow", u"\u62c6\u5206", None))
        self.subnet_result.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u663e\u793a20\u4e2a\u5b50\u7f51", None))
        self.subnetting.setTabText(self.subnetting.indexOf(self.widget), QCoreApplication.translate("MainWindow", u"\u5b50\u7f51\u5212\u5206", None))
        self.subnetting.setTabText(self.subnetting.indexOf(self.aggregation), QCoreApplication.translate("MainWindow", u"\u8def\u7531\u6c47\u805a", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

