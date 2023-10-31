# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from AnalogGaugeWidget import AnalogGaugeWidget

import background_rc
import logo_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1594, 926)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"#centralwidget{\n"
"border-image :url(:/background/jonathan-borba-3o5oUjrD90w-unsplash.jpg)\n"
"} \n"
"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"QWidget QLabel {\n"
"    background-color: transparent;\n"
"}\n"
"QWidget QLCDNumber {\n"
"    background-color: black;\n"
"}\n"
"")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.guage_frame = QFrame(self.page)
        self.guage_frame.setObjectName(u"guage_frame")
        self.guage_frame.setGeometry(QRect(30, 30, 451, 281))
        self.guage_frame.setFrameShape(QFrame.StyledPanel)
        self.guage_frame.setFrameShadow(QFrame.Sunken)
        self.widget = AnalogGaugeWidget(self.guage_frame)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(50, 40, 331, 151))
        self.label_5 = QLabel(self.guage_frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(160, 10, 91, 31))
        self.label_5.setStyleSheet(u"color:white;\n"
"font-size:16px;\n"
"font:Old Standard TT;\n"
"text-align:center;")
        self.label_18 = QLabel(self.guage_frame)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(30, 200, 141, 31))
        self.label_18.setStyleSheet(u"\n"
"font: 75 15pt \"Ubuntu Condensed\";\n"
"color :rgb(238, 238, 236)")
        self.label_19 = QLabel(self.guage_frame)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(30, 240, 141, 31))
        self.label_19.setStyleSheet(u"\n"
"font: 75 15pt \"Ubuntu Condensed\";\n"
"color :rgb(238, 238, 236)")
        self.timer_7 = QLCDNumber(self.guage_frame)
        self.timer_7.setObjectName(u"timer_7")
        self.timer_7.setGeometry(QRect(240, 200, 81, 31))
        self.timer_7.setStyleSheet(u"color :rgb(255, 255, 255) ;\n"
"")
        self.timer_7.setFrameShape(QFrame.NoFrame)
        self.timer_7.setFrameShadow(QFrame.Sunken)
        self.timer_7.setSmallDecimalPoint(True)
        self.timer_7.setDigitCount(5)
        self.timer_7.setMode(QLCDNumber.Dec)
        self.timer_7.setSegmentStyle(QLCDNumber.Filled)
        self.timer_7.setProperty("value", 0.000000000000000)
        self.timer_7.setProperty("intValue", 0)
        self.timer_8 = QLCDNumber(self.guage_frame)
        self.timer_8.setObjectName(u"timer_8")
        self.timer_8.setGeometry(QRect(240, 240, 81, 31))
        self.timer_8.setStyleSheet(u"color :rgb(255, 255, 255) ;\n"
"")
        self.timer_8.setFrameShape(QFrame.NoFrame)
        self.timer_8.setFrameShadow(QFrame.Sunken)
        self.timer_8.setSmallDecimalPoint(True)
        self.timer_8.setDigitCount(5)
        self.timer_8.setMode(QLCDNumber.Dec)
        self.timer_8.setSegmentStyle(QLCDNumber.Filled)
        self.timer_8.setProperty("value", 0.000000000000000)
        self.timer_8.setProperty("intValue", 0)
        self.motors_frame = QFrame(self.page)
        self.motors_frame.setObjectName(u"motors_frame")
        self.motors_frame.setGeometry(QRect(1060, 10, 461, 291))
        self.motors_frame.setStyleSheet(u" border: 1px solid white;\n"
"")
        self.motors_frame.setFrameShape(QFrame.StyledPanel)
        self.motors_frame.setFrameShadow(QFrame.Raised)
        self.timer_2 = QLCDNumber(self.motors_frame)
        self.timer_2.setObjectName(u"timer_2")
        self.timer_2.setGeometry(QRect(340, 30, 81, 31))
        self.timer_2.setStyleSheet(u"color :rgb(255, 255, 255) ;\n"
"")
        self.timer_2.setFrameShape(QFrame.NoFrame)
        self.timer_2.setFrameShadow(QFrame.Sunken)
        self.timer_2.setSmallDecimalPoint(True)
        self.timer_2.setDigitCount(5)
        self.timer_2.setMode(QLCDNumber.Dec)
        self.timer_2.setSegmentStyle(QLCDNumber.Filled)
        self.timer_2.setProperty("value", 0.000000000000000)
        self.timer_2.setProperty("intValue", 0)
        self.timer_9 = QLCDNumber(self.motors_frame)
        self.timer_9.setObjectName(u"timer_9")
        self.timer_9.setGeometry(QRect(340, 100, 81, 31))
        self.timer_9.setStyleSheet(u"color :rgb(255, 255, 255) ;\n"
"")
        self.timer_9.setFrameShape(QFrame.NoFrame)
        self.timer_9.setFrameShadow(QFrame.Sunken)
        self.timer_9.setSmallDecimalPoint(True)
        self.timer_9.setDigitCount(5)
        self.timer_9.setMode(QLCDNumber.Dec)
        self.timer_9.setSegmentStyle(QLCDNumber.Filled)
        self.timer_9.setProperty("value", 0.000000000000000)
        self.timer_9.setProperty("intValue", 0)
        self.timer_10 = QLCDNumber(self.motors_frame)
        self.timer_10.setObjectName(u"timer_10")
        self.timer_10.setGeometry(QRect(340, 160, 81, 31))
        self.timer_10.setStyleSheet(u"color :rgb(255, 255, 255) ;\n"
"")
        self.timer_10.setFrameShape(QFrame.NoFrame)
        self.timer_10.setFrameShadow(QFrame.Sunken)
        self.timer_10.setSmallDecimalPoint(True)
        self.timer_10.setDigitCount(5)
        self.timer_10.setMode(QLCDNumber.Dec)
        self.timer_10.setSegmentStyle(QLCDNumber.Filled)
        self.timer_10.setProperty("value", 0.000000000000000)
        self.timer_10.setProperty("intValue", 0)
        self.timer_11 = QLCDNumber(self.motors_frame)
        self.timer_11.setObjectName(u"timer_11")
        self.timer_11.setGeometry(QRect(90, 30, 81, 31))
        self.timer_11.setStyleSheet(u"color :rgb(255, 255, 255) ;\n"
"")
        self.timer_11.setFrameShape(QFrame.NoFrame)
        self.timer_11.setFrameShadow(QFrame.Sunken)
        self.timer_11.setSmallDecimalPoint(True)
        self.timer_11.setDigitCount(5)
        self.timer_11.setMode(QLCDNumber.Dec)
        self.timer_11.setSegmentStyle(QLCDNumber.Filled)
        self.timer_11.setProperty("value", 0.000000000000000)
        self.timer_11.setProperty("intValue", 0)
        self.timer_12 = QLCDNumber(self.motors_frame)
        self.timer_12.setObjectName(u"timer_12")
        self.timer_12.setGeometry(QRect(90, 100, 81, 31))
        self.timer_12.setStyleSheet(u"color :rgb(255, 255, 255) ;\n"
"")
        self.timer_12.setFrameShape(QFrame.NoFrame)
        self.timer_12.setFrameShadow(QFrame.Sunken)
        self.timer_12.setSmallDecimalPoint(True)
        self.timer_12.setDigitCount(5)
        self.timer_12.setMode(QLCDNumber.Dec)
        self.timer_12.setSegmentStyle(QLCDNumber.Filled)
        self.timer_12.setProperty("value", 0.000000000000000)
        self.timer_12.setProperty("intValue", 0)
        self.timer_13 = QLCDNumber(self.motors_frame)
        self.timer_13.setObjectName(u"timer_13")
        self.timer_13.setGeometry(QRect(90, 160, 81, 31))
        self.timer_13.setStyleSheet(u"color :rgb(255, 255, 255) ;\n"
"")
        self.timer_13.setFrameShape(QFrame.NoFrame)
        self.timer_13.setFrameShadow(QFrame.Sunken)
        self.timer_13.setSmallDecimalPoint(True)
        self.timer_13.setDigitCount(5)
        self.timer_13.setMode(QLCDNumber.Dec)
        self.timer_13.setSegmentStyle(QLCDNumber.Filled)
        self.timer_13.setProperty("value", 0.000000000000000)
        self.timer_13.setProperty("intValue", 0)
        self.timer_14 = QLCDNumber(self.motors_frame)
        self.timer_14.setObjectName(u"timer_14")
        self.timer_14.setGeometry(QRect(90, 220, 81, 31))
        self.timer_14.setStyleSheet(u"color :rgb(255, 255, 255) ;\n"
"background-color :rgb(7, 7, 7) ;\n"
"\n"
"")
        self.timer_14.setFrameShape(QFrame.NoFrame)
        self.timer_14.setFrameShadow(QFrame.Sunken)
        self.timer_14.setSmallDecimalPoint(True)
        self.timer_14.setDigitCount(5)
        self.timer_14.setMode(QLCDNumber.Dec)
        self.timer_14.setSegmentStyle(QLCDNumber.Filled)
        self.timer_14.setProperty("value", 0.000000000000000)
        self.timer_14.setProperty("intValue", 0)
        self.timer_15 = QLCDNumber(self.motors_frame)
        self.timer_15.setObjectName(u"timer_15")
        self.timer_15.setGeometry(QRect(340, 220, 81, 31))
        self.timer_15.setStyleSheet(u"background-color: rgb(0, 0, 0)\n"
"")
        self.timer_15.setFrameShape(QFrame.NoFrame)
        self.timer_15.setFrameShadow(QFrame.Sunken)
        self.timer_15.setSmallDecimalPoint(True)
        self.timer_15.setDigitCount(5)
        self.timer_15.setMode(QLCDNumber.Dec)
        self.timer_15.setSegmentStyle(QLCDNumber.Filled)
        self.timer_15.setProperty("value", 0.000000000000000)
        self.timer_15.setProperty("intValue", 0)
        self.control_frame = QFrame(self.page)
        self.control_frame.setObjectName(u"control_frame")
        self.control_frame.setGeometry(QRect(10, 530, 441, 291))
        self.control_frame.setStyleSheet(u" border: 1px solid white;\n"
"")
        self.control_frame.setFrameShape(QFrame.StyledPanel)
        self.control_frame.setFrameShadow(QFrame.Raised)
        self.label_23 = QLabel(self.control_frame)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(50, 50, 141, 31))
        self.label_23.setStyleSheet(u"\n"
"font: 75 15pt \"Ubuntu Condensed\";\n"
"color :rgb(238, 238, 236)")
        self.label_25 = QLabel(self.control_frame)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(50, 120, 141, 31))
        self.label_25.setStyleSheet(u"\n"
"font: 75 15pt \"Ubuntu Condensed\";\n"
"color :rgb(238, 238, 236)")
        self.label_27 = QLabel(self.control_frame)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(40, 180, 161, 31))
        self.label_27.setStyleSheet(u"\n"
"font: 75 15pt \"Ubuntu Condensed\";\n"
"color :rgb(238, 238, 236)")
        self.label_29 = QLabel(self.control_frame)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(40, 230, 171, 31))
        self.label_29.setStyleSheet(u"\n"
"font: 75 15pt \"Ubuntu Condensed\";\n"
"color :rgb(238, 238, 236)")
        self.timer_3 = QLCDNumber(self.control_frame)
        self.timer_3.setObjectName(u"timer_3")
        self.timer_3.setGeometry(QRect(280, 230, 81, 31))
        self.timer_3.setStyleSheet(u"color :rgb(255, 255, 255) ;\n"
"")
        self.timer_3.setFrameShape(QFrame.NoFrame)
        self.timer_3.setFrameShadow(QFrame.Sunken)
        self.timer_3.setSmallDecimalPoint(True)
        self.timer_3.setDigitCount(5)
        self.timer_3.setMode(QLCDNumber.Dec)
        self.timer_3.setSegmentStyle(QLCDNumber.Filled)
        self.timer_3.setProperty("value", 0.000000000000000)
        self.timer_3.setProperty("intValue", 0)
        self.timer_4 = QLCDNumber(self.control_frame)
        self.timer_4.setObjectName(u"timer_4")
        self.timer_4.setGeometry(QRect(280, 180, 81, 31))
        self.timer_4.setStyleSheet(u"color :rgb(255, 255, 255) ;\n"
"")
        self.timer_4.setFrameShape(QFrame.NoFrame)
        self.timer_4.setFrameShadow(QFrame.Sunken)
        self.timer_4.setSmallDecimalPoint(True)
        self.timer_4.setDigitCount(5)
        self.timer_4.setMode(QLCDNumber.Dec)
        self.timer_4.setSegmentStyle(QLCDNumber.Filled)
        self.timer_4.setProperty("value", 0.000000000000000)
        self.timer_4.setProperty("intValue", 0)
        self.timer_5 = QLCDNumber(self.control_frame)
        self.timer_5.setObjectName(u"timer_5")
        self.timer_5.setGeometry(QRect(280, 120, 81, 31))
        self.timer_5.setStyleSheet(u"color :rgb(255, 255, 255) ;\n"
"")
        self.timer_5.setFrameShape(QFrame.NoFrame)
        self.timer_5.setFrameShadow(QFrame.Sunken)
        self.timer_5.setSmallDecimalPoint(True)
        self.timer_5.setDigitCount(5)
        self.timer_5.setMode(QLCDNumber.Dec)
        self.timer_5.setSegmentStyle(QLCDNumber.Filled)
        self.timer_5.setProperty("value", 0.000000000000000)
        self.timer_5.setProperty("intValue", 0)
        self.timer_6 = QLCDNumber(self.control_frame)
        self.timer_6.setObjectName(u"timer_6")
        self.timer_6.setGeometry(QRect(280, 60, 81, 31))
        self.timer_6.setStyleSheet(u"color :rgb(255, 255, 255) ;\n"
"")
        self.timer_6.setFrameShape(QFrame.NoFrame)
        self.timer_6.setFrameShadow(QFrame.Sunken)
        self.timer_6.setSmallDecimalPoint(True)
        self.timer_6.setDigitCount(5)
        self.timer_6.setMode(QLCDNumber.Dec)
        self.timer_6.setSegmentStyle(QLCDNumber.Filled)
        self.timer_6.setProperty("value", 0.000000000000000)
        self.timer_6.setProperty("intValue", 0)
        self.mission_frame = QFrame(self.page)
        self.mission_frame.setObjectName(u"mission_frame")
        self.mission_frame.setGeometry(QRect(500, 520, 501, 311))
        self.mission_frame.setStyleSheet(u" border: 1px solid white;\n"
"")
        self.mission_frame.setFrameShape(QFrame.StyledPanel)
        self.mission_frame.setFrameShadow(QFrame.Raised)
        self.label_31 = QLabel(self.mission_frame)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(100, 10, 321, 91))
        self.label_31.setStyleSheet(u"\n"
"font: 40px 15pt \"Ubuntu Condensed\"; \n"
"border: 1px solid transparent;\n"
"\n"
"color :rgb(238, 238, 236)")
        self.checkBox = QCheckBox(self.mission_frame)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(150, 80, 221, 51))
        self.checkBox.setStyleSheet(u"color :rgb(255, 255, 255) ;\n"
"font: 75 15pt \"MS Shell Dlg 2\";\n"
"border: 1px solid transparent;\n"
"")
        self.checkBox_2 = QCheckBox(self.mission_frame)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setGeometry(QRect(150, 180, 221, 51))
        self.checkBox_2.setStyleSheet(u"color :rgb(255, 255, 255) ;\n"
"font: 75 15pt \"MS Shell Dlg 2\";\n"
"border: 1px solid transparent;\n"
"")
        self.checkBox_3 = QCheckBox(self.mission_frame)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setGeometry(QRect(150, 130, 221, 51))
        self.checkBox_3.setStyleSheet(u"color :rgb(255, 255, 255) ;\n"
"font: 75 15pt \"MS Shell Dlg 2\";\n"
"border: 1px solid transparent;\n"
"")
        self.missiontimer_frame = QFrame(self.page)
        self.missiontimer_frame.setObjectName(u"missiontimer_frame")
        self.missiontimer_frame.setGeometry(QRect(1050, 510, 491, 241))
        self.missiontimer_frame.setStyleSheet(u" border: 1px solid white;\n"
"")
        self.missiontimer_frame.setFrameShape(QFrame.StyledPanel)
        self.missiontimer_frame.setFrameShadow(QFrame.Raised)
        self.timer_mession = QLCDNumber(self.missiontimer_frame)
        self.timer_mession.setObjectName(u"timer_mession")
        self.timer_mession.setGeometry(QRect(150, 10, 191, 51))
        self.timer_mession.setStyleSheet(u"color :rgb(255, 255, 255) ;\n"
"font: 75 11pt \"Ubuntu Condensed\";\n"
"background-color:rgb(0, 0, 0) ;")
        self.timer_mession.setFrameShape(QFrame.NoFrame)
        self.timer_mession.setFrameShadow(QFrame.Sunken)
        self.timer_mession.setSmallDecimalPoint(True)
        self.timer_mession.setDigitCount(5)
        self.timer_mession.setMode(QLCDNumber.Dec)
        self.timer_mession.setSegmentStyle(QLCDNumber.Filled)
        self.timer_mession.setProperty("value", 0.000000000000000)
        self.timer_mession.setProperty("intValue", 0)
        self.treeWidget = QTreeWidget(self.missiontimer_frame)
        font = QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setFont(0, font);
        self.treeWidget.setHeaderItem(__qtreewidgetitem)
        QTreeWidgetItem(self.treeWidget)
        QTreeWidgetItem(self.treeWidget)
        QTreeWidgetItem(self.treeWidget)
        QTreeWidgetItem(self.treeWidget)
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.setGeometry(QRect(60, 70, 371, 171))
        self.treeWidget.setStyleSheet(u"background-color :black ;\n"
"color :white")
        self.label_2 = QLabel(self.page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(46, 330, 141, 31))
        self.label_2.setStyleSheet(u"\n"
"font: 75 15pt \"Ubuntu Condensed\";\n"
"color :rgb(238, 238, 236)")
        self.toolButton = QToolButton(self.page)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setGeometry(QRect(280, 330, 51, 24))
        self.toolButton.setStyleSheet(u"background-color :rgb(7, 7, 7) ;\n"
"\n"
"font: 75 15pt \"Ubuntu Condensed\";\n"
"color :rgb(238, 238, 236)")
        self.toolButton_2 = QToolButton(self.page)
        self.toolButton_2.setObjectName(u"toolButton_2")
        self.toolButton_2.setGeometry(QRect(340, 330, 51, 24))
        self.toolButton_2.setStyleSheet(u"background-color :rgb(7, 7, 7) ;\n"
"font: 75 15pt \"Ubuntu Condensed\";\n"
"color :rgb(238, 238, 236)")
        self.label_3 = QLabel(self.page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(50, 390, 141, 31))
        self.label_3.setStyleSheet(u"\n"
"font: 75 15pt \"Ubuntu Condensed\";\n"
"color :rgb(238, 238, 236)")
        self.label_4 = QLabel(self.page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(56, 450, 141, 21))
        self.label_4.setStyleSheet(u"\n"
"font: 75 15pt \"Ubuntu Condensed\";\n"
"color :rgb(238, 238, 236)")
        self.toolButton_3 = QToolButton(self.page)
        self.toolButton_3.setObjectName(u"toolButton_3")
        self.toolButton_3.setGeometry(QRect(280, 390, 51, 24))
        self.toolButton_3.setStyleSheet(u"background-color :rgb(7, 7, 7) ;\n"
"\n"
"font: 75 15pt \"Ubuntu Condensed\";\n"
"color :rgb(238, 238, 236)")
        self.toolButton_4 = QToolButton(self.page)
        self.toolButton_4.setObjectName(u"toolButton_4")
        self.toolButton_4.setGeometry(QRect(340, 390, 51, 24))
        self.toolButton_4.setStyleSheet(u"background-color :rgb(7, 7, 7) ;\n"
"\n"
"font: 75 15pt \"Ubuntu Condensed\";\n"
"color :rgb(238, 238, 236)")
        self.stackedWidget_2 = QStackedWidget(self.page)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setGeometry(QRect(500, 20, 511, 201))
        self.stackedWidget_2.setStyleSheet(u" border: 1px solid white;\n"
"background-color:transparent ;\n"
"QWidget QLabel {\n"
"    border: 1px solid transparent ;\n"
"\n"
"}")
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.timerlcd = QLCDNumber(self.page_5)
        self.timerlcd.setObjectName(u"timerlcd")
        self.timerlcd.setGeometry(QRect(160, 50, 191, 51))
        self.timerlcd.setStyleSheet(u"color :rgb(255, 255, 255) ;\n"
"font: 75 11pt \"Ubuntu Condensed\";\n"
"background-color:rgb(0, 0, 0) ;")
        self.timerlcd.setFrameShape(QFrame.NoFrame)
        self.timerlcd.setFrameShadow(QFrame.Sunken)
        self.timerlcd.setSmallDecimalPoint(True)
        self.timerlcd.setDigitCount(5)
        self.timerlcd.setMode(QLCDNumber.Dec)
        self.timerlcd.setSegmentStyle(QLCDNumber.Filled)
        self.timerlcd.setProperty("value", 0.000000000000000)
        self.timerlcd.setProperty("intValue", 0)
        self.label_20 = QLabel(self.page_5)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(190, 136, 121, 41))
        self.label_20.setStyleSheet(u"background-color :rgb(7, 7, 7) ;\n"
"color:rgb(255, 255, 255) ;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.stackedWidget_2.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.label_6 = QLabel(self.page_6)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 20, 141, 21))
        self.label_6.setStyleSheet(u"\n"
"font: 75 15pt \"Ubuntu Condensed\";\n"
"color :rgb(238, 238, 236)")
        self.label_7 = QLabel(self.page_6)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 70, 141, 21))
        self.label_7.setStyleSheet(u"\n"
"font: 75 15pt \"Ubuntu Condensed\";\n"
"color :rgb(238, 238, 236)")
        self.label_8 = QLabel(self.page_6)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(20, 110, 141, 21))
        self.label_8.setStyleSheet(u"\n"
"font: 75 15pt \"Ubuntu Condensed\";\n"
"color :rgb(238, 238, 236)")
        self.label_9 = QLabel(self.page_6)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 160, 141, 21))
        self.label_9.setStyleSheet(u"\n"
"font: 75 15pt \"Ubuntu Condensed\";\n"
"color :rgb(238, 238, 236)")
        self.label_10 = QLabel(self.page_6)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(20, 210, 141, 21))
        self.label_10.setStyleSheet(u"\n"
"font: 75 15pt \"Ubuntu Condensed\";\n"
"color :rgb(238, 238, 236)")
        self.label_11 = QLabel(self.page_6)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(20, 260, 141, 21))
        self.label_11.setStyleSheet(u"\n"
"font: 75 15pt \"Ubuntu Condensed\";\n"
"color :rgb(238, 238, 236)")
        self.label_12 = QLabel(self.page_6)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(400, 10, 71, 21))
        self.label_12.setStyleSheet(u"\n"
"font: 75 15pt \"Ubuntu Condensed\";\n"
"color :rgb(238, 238, 236)")
        self.label_13 = QLabel(self.page_6)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(400, 70, 71, 21))
        self.label_13.setStyleSheet(u"\n"
"font: 75 15pt \"Ubuntu Condensed\";\n"
"color :rgb(238, 238, 236)")
        self.label_14 = QLabel(self.page_6)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(400, 110, 71, 21))
        self.label_14.setStyleSheet(u"\n"
"font: 75 15pt \"Ubuntu Condensed\";\n"
"color :rgb(238, 238, 236)")
        self.label_15 = QLabel(self.page_6)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(400, 160, 71, 21))
        self.label_15.setStyleSheet(u"\n"
"font: 75 15pt \"Ubuntu Condensed\";\n"
"color :rgb(238, 238, 236)")
        self.label_16 = QLabel(self.page_6)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(400, 210, 71, 21))
        self.label_16.setStyleSheet(u"\n"
"font: 75 15pt \"Ubuntu Condensed\";\n"
"color :rgb(238, 238, 236)")
        self.label_17 = QLabel(self.page_6)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(400, 260, 71, 21))
        self.label_17.setStyleSheet(u"\n"
"font: 75 15pt \"Ubuntu Condensed\";\n"
"color :rgb(238, 238, 236)")
        self.horizontalSlider = QSlider(self.page_6)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setGeometry(QRect(180, 150, 191, 31))
        self.horizontalSlider.setStyleSheet(u"background-color :rgb(35, 35, 35) ;\n"
"")
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.horizontalSlider_2 = QSlider(self.page_6)
        self.horizontalSlider_2.setObjectName(u"horizontalSlider_2")
        self.horizontalSlider_2.setGeometry(QRect(180, 10, 191, 31))
        self.horizontalSlider_2.setStyleSheet(u"background-color:rgb(48, 48, 48) ;\n"
"")
        self.horizontalSlider_2.setOrientation(Qt.Horizontal)
        self.horizontalSlider_3 = QSlider(self.page_6)
        self.horizontalSlider_3.setObjectName(u"horizontalSlider_3")
        self.horizontalSlider_3.setGeometry(QRect(180, 60, 191, 31))
        self.horizontalSlider_3.setStyleSheet(u"background-color :rgb(35, 35, 35) ;\n"
"")
        self.horizontalSlider_3.setOrientation(Qt.Horizontal)
        self.horizontalSlider_4 = QSlider(self.page_6)
        self.horizontalSlider_4.setObjectName(u"horizontalSlider_4")
        self.horizontalSlider_4.setGeometry(QRect(180, 100, 191, 31))
        self.horizontalSlider_4.setStyleSheet(u"background-color :rgb(35, 35, 35) ;\n"
"")
        self.horizontalSlider_4.setOrientation(Qt.Horizontal)
        self.horizontalSlider_5 = QSlider(self.page_6)
        self.horizontalSlider_5.setObjectName(u"horizontalSlider_5")
        self.horizontalSlider_5.setGeometry(QRect(180, 200, 191, 31))
        self.horizontalSlider_5.setStyleSheet(u"background-color :rgb(35, 35, 35) ;\n"
"")
        self.horizontalSlider_5.setOrientation(Qt.Horizontal)
        self.horizontalSlider_6 = QSlider(self.page_6)
        self.horizontalSlider_6.setObjectName(u"horizontalSlider_6")
        self.horizontalSlider_6.setGeometry(QRect(180, 250, 191, 31))
        self.horizontalSlider_6.setStyleSheet(u"background-color :rgb(35, 35, 35) ;\n"
"")
        self.horizontalSlider_6.setOrientation(Qt.Horizontal)
        self.stackedWidget_2.addWidget(self.page_6)
        self.label_22 = QLabel(self.page)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(270, 440, 151, 41))
        self.label_22.setStyleSheet(u"\n"
"font: 75 15pt \"Ubuntu Condensed\";\n"
"color :rgb(238, 238, 236)")
        self.frame = QFrame(self.page)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(660, 350, 271, 131))
        self.frame.setStyleSheet(u"border-image :url(:/logo/logo.png);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.start_timer_button = QPushButton(self.page)
        self.start_timer_button.setObjectName(u"start_timer_button")
        self.start_timer_button.setGeometry(QRect(540, 240, 89, 25))
        self.stop_timer_button = QPushButton(self.page)
        self.stop_timer_button.setObjectName(u"stop_timer_button")
        self.stop_timer_button.setGeometry(QRect(720, 240, 89, 25))
        self.reset_timer_button = QPushButton(self.page)
        self.reset_timer_button.setObjectName(u"reset_timer_button")
        self.reset_timer_button.setGeometry(QRect(880, 240, 89, 25))
        self.stop_mession_button = QPushButton(self.page)
        self.stop_mession_button.setObjectName(u"stop_mession_button")
        self.stop_mession_button.setGeometry(QRect(1230, 780, 89, 25))
        self.reset_mession_button = QPushButton(self.page)
        self.reset_mession_button.setObjectName(u"reset_mession_button")
        self.reset_mession_button.setGeometry(QRect(1390, 780, 89, 25))
        self.start_mession_button = QPushButton(self.page)
        self.start_mession_button.setObjectName(u"start_mession_button")
        self.start_mession_button.setGeometry(QRect(1090, 780, 89, 25))
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1594, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Yaw Angle", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Pitch Angle", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Roll Angle", None))
#if QT_CONFIG(whatsthis)
        self.control_frame.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"System", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"GyroScope", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Accelerometer", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"MagnetoMeter", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Mission Steps", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"step1", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"step3", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"step2", None))
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"time", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"mession", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"name", None));

        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.treeWidget.topLevelItem(0)
        ___qtreewidgetitem1.setText(2, QCoreApplication.translate("MainWindow", u"15", None));
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("MainWindow", u"what you want to do", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"mession1", None));
        ___qtreewidgetitem2 = self.treeWidget.topLevelItem(1)
        ___qtreewidgetitem2.setText(2, QCoreApplication.translate("MainWindow", u"40", None));
        ___qtreewidgetitem2.setText(1, QCoreApplication.translate("MainWindow", u"ay 7aga", None));
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("MainWindow", u"mession 2", None));
        ___qtreewidgetitem3 = self.treeWidget.topLevelItem(2)
        ___qtreewidgetitem3.setText(2, QCoreApplication.translate("MainWindow", u"10", None));
        ___qtreewidgetitem3.setText(1, QCoreApplication.translate("MainWindow", u"ay 7aga", None));
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("MainWindow", u"mession 3", None));
        ___qtreewidgetitem4 = self.treeWidget.topLevelItem(3)
        ___qtreewidgetitem4.setText(2, QCoreApplication.translate("MainWindow", u"20", None));
        ___qtreewidgetitem4.setText(1, QCoreApplication.translate("MainWindow", u"ay 7agaa", None));
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("MainWindow", u"mession 4", None));
        self.treeWidget.setSortingEnabled(__sortingEnabled)

        self.label_2.setText(QCoreApplication.translate("MainWindow", u"CONTROL", None))
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"ON", None))
        self.toolButton_2.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"LED", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"OPERATION MODE", None))
        self.toolButton_3.setText(QCoreApplication.translate("MainWindow", u"ON", None))
        self.toolButton_4.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"   TIMER", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Yaw Kp", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Yaw Ki", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Yaw Kd", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Pitch Kp", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Pitch Ki", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Pitch Kd", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"value", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"value", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"value", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"value", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"value", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"value", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Auto/Manual", None))
        self.start_timer_button.setText(QCoreApplication.translate("MainWindow", u"start", None))
        self.stop_timer_button.setText(QCoreApplication.translate("MainWindow", u"stop", None))
        self.reset_timer_button.setText(QCoreApplication.translate("MainWindow", u"reset", None))
        self.stop_mession_button.setText(QCoreApplication.translate("MainWindow", u"stop", None))
        self.reset_mession_button.setText(QCoreApplication.translate("MainWindow", u"reset", None))
        self.start_mession_button.setText(QCoreApplication.translate("MainWindow", u"start", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

