# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Sat Feb  7 15:22:23 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(790, 531)
        self.verticalLayoutWidget = QtGui.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 161, 174))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setEnabled(True)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.spinBox = QtGui.QSpinBox(self.verticalLayoutWidget)
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(20)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout.addWidget(self.spinBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.neighbourhood = QtGui.QComboBox(self.verticalLayoutWidget)
        self.neighbourhood.setStatusTip("")
        self.neighbourhood.setObjectName("neighbourhood")
        self.verticalLayout.addWidget(self.neighbourhood)
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.comboBox_2 = QtGui.QComboBox(self.verticalLayoutWidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.verticalLayout.addWidget(self.comboBox_2)
        self.verticalLayoutWidget_2 = QtGui.QWidget(Form)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 440, 161, 81))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.horizontalSlidera = QtGui.QSlider(self.verticalLayoutWidget_2)
        self.horizontalSlidera.setMinimum(50)
        self.horizontalSlidera.setMaximum(1000)
        self.horizontalSlidera.setProperty("value", 525)
        self.horizontalSlidera.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlidera.setObjectName("horizontalSlidera")
        self.verticalLayout_2.addWidget(self.horizontalSlidera)
        self.progressBar = QtGui.QProgressBar(self.verticalLayoutWidget_2)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_2.addWidget(self.progressBar)
        self.graphicsView = QtGui.QGraphicsView(Form)
        self.graphicsView.setGeometry(QtCore.QRect(180, 10, 601, 511))
        self.graphicsView.setObjectName("graphicsView")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Form", "START", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "Grains number", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Neighbourhood", None, QtGui.QApplication.UnicodeUTF8))
        self.neighbourhood.setToolTip(QtGui.QApplication.translate("Form", "neighbourhood", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Inclusion type", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_2.setToolTip(QtGui.QApplication.translate("Form", "inclusion", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Form", "Animation speed", None, QtGui.QApplication.UnicodeUTF8))
        self.horizontalSlidera.setToolTip(QtGui.QApplication.translate("Form", "animation speed (ms)", None, QtGui.QApplication.UnicodeUTF8))
        self.progressBar.setToolTip(QtGui.QApplication.translate("Form", "progress", None, QtGui.QApplication.UnicodeUTF8))

