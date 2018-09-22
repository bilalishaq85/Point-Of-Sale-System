# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\bilal\workspace\DesignSheets\ui_popup.ui'
#
# Created: Sun Oct  8 15:55:50 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_sDialog(object):
    def setupUi(self, sDialog):
        sDialog.setObjectName("sDialog")
        sDialog.resize(332, 175)

        self.verticalLayoutWidget = QtGui.QWidget(sDialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(90, 40, 160, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        self.rbt_vout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.rbt_vout.setContentsMargins(0, 0, 0, 0)
        self.rbt_vout.setObjectName("rbt_vout")

        self.layoutWidget = QtGui.QWidget(sDialog)
        self.layoutWidget.setGeometry(QtCore.QRect(160, 140, 162, 27))
        self.layoutWidget.setObjectName("layoutWidget")

        self.bt_hout = QtGui.QHBoxLayout(self.layoutWidget)
        self.bt_hout.setContentsMargins(0, 0, 0, 0)
        self.bt_hout.setObjectName("bt_hout")

        self.retranslateUi(sDialog)
        QtCore.QMetaObject.connectSlotsByName(sDialog)

    def retranslateUi(self, sDialog):
        sDialog.setWindowTitle(QtGui.QApplication.translate("sDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))


