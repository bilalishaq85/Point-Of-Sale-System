# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\bilal\workspace\DesignSheets\spinbox.ui'
#
# Created: Thu Oct 26 14:28:10 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        Dialog.setStyleSheet("QSpinBox::up-button { subcontrol-position: left; width: 30px; height: 25px;}\n"
"QSpinBox::down-button { subcontrol-position: right; width: 30px; height: 25px;}")
        self.spinBox = QtGui.QSpinBox(Dialog)
        self.spinBox.setGeometry(QtCore.QRect(90, 92, 71, 20))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox.sizePolicy().hasHeightForWidth())
        self.spinBox.setSizePolicy(sizePolicy)
        self.spinBox.setStyleSheet("QSpinBox { border: 0px inset grey; } \n"
"QSpinBox::up-button { subcontrol-position: left; width: 25px; height: 20px;}\n"
"QSpinBox::down-button { subcontrol-position: right; width: 25px; height: 20px;}")
        self.spinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox.setButtonSymbols(QtGui.QAbstractSpinBox.PlusMinus)
        self.spinBox.setMinimum(1)
        self.spinBox.setObjectName("spinBox")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

