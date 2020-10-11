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
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.base_tab = QWidget()
        self.base_tab.setObjectName(u"base_tab")
        self.verticalLayout_3 = QVBoxLayout(self.base_tab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.ip_segment_label = QLabel(self.base_tab)
        self.ip_segment_label.setObjectName(u"ip_segment_label")

        self.horizontalLayout_3.addWidget(self.ip_segment_label)

        self.ip_segment_value = QLineEdit(self.base_tab)
        self.ip_segment_value.setObjectName(u"ip_segment_value")

        self.horizontalLayout_3.addWidget(self.ip_segment_value)

        self.subnet_calc = QPushButton(self.base_tab)
        self.subnet_calc.setObjectName(u"subnet_calc")

        self.horizontalLayout_3.addWidget(self.subnet_calc)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.ip_prefix_label = QLabel(self.base_tab)
        self.ip_prefix_label.setObjectName(u"ip_prefix_label")

        self.horizontalLayout_6.addWidget(self.ip_prefix_label)

        self.ip_prefix_value = QSpinBox(self.base_tab)
        self.ip_prefix_value.setObjectName(u"ip_prefix_value")
        self.ip_prefix_value.setMaximum(32)
        self.ip_prefix_value.setValue(16)

        self.horizontalLayout_6.addWidget(self.ip_prefix_value)

        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 2)

        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.host_range_label = QLabel(self.base_tab)
        self.host_range_label.setObjectName(u"host_range_label")

        self.verticalLayout.addWidget(self.host_range_label)

        self.subnet_Slider = QSlider(self.base_tab)
        self.subnet_Slider.setObjectName(u"subnet_Slider")
        self.subnet_Slider.setMouseTracking(False)
        self.subnet_Slider.setTabletTracking(False)
        self.subnet_Slider.setMaximum(32)
        self.subnet_Slider.setPageStep(15)
        self.subnet_Slider.setValue(15)
        self.subnet_Slider.setOrientation(Qt.Horizontal)

        self.verticalLayout.addWidget(self.subnet_Slider)

        self.line = QFrame(self.base_tab)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.subnet_result = QTextEdit(self.base_tab)
        self.subnet_result.setObjectName(u"subnet_result")

        self.verticalLayout.addWidget(self.subnet_result)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.tabWidget.addTab(self.base_tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.tabWidget.addTab(self.tab_5, "")

        self.verticalLayout_2.addWidget(self.tabWidget)


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
        self.subnet_Slider.valueChanged.connect(self.ip_prefix_value.setValue)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionfile.setText(QCoreApplication.translate("MainWindow", u"file", None))
        self.ip_segment_label.setText(QCoreApplication.translate("MainWindow", u"IP\u6bb5\uff1a", None))
        self.subnet_calc.setText(QCoreApplication.translate("MainWindow", u"\u5b50\u7f51\u8ba1\u7b97", None))
        self.ip_prefix_label.setText(QCoreApplication.translate("MainWindow", u"\u524d\u7f00\uff1a", None))
        self.host_range_label.setText(QCoreApplication.translate("MainWindow", u"\u4e3b\u673a\u8303\u56f4\uff1a", None))
        self.subnet_result.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u663e\u793a20\u4e2a\u5b50\u7f51", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.base_tab), QCoreApplication.translate("MainWindow", u"\u57fa\u7840\u8ba1\u7b97", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u8def\u7531\u6c47\u805a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"Prefix_list", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

