# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\bilal\workspace\DesignSheets\ui_menuwin.ui'
#
# Created: Thu Sep 28 14:03:25 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui


class Ui_menuWin(object):
    def setupUi(self, menuWin):
        menuWin.setObjectName("menuWin")
        # menuWin.resize(1024, 768)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(menuWin.sizePolicy().hasHeightForWidth())
        menuWin.setSizePolicy(sizePolicy)
        menuWin.setMinimumSize(QtCore.QSize(1024, 768))
        menuWin.setSizeIncrement(QtCore.QSize(100, 100))
        self.centralwidget = QtGui.QWidget(menuWin)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.MainMenu = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MainMenu.sizePolicy().hasHeightForWidth())
        self.MainMenu.setSizePolicy(sizePolicy)
        self.MainMenu.setMinimumSize(QtCore.QSize(140, 730))
        self.MainMenu.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.MainMenu.setFrameShape(QtGui.QFrame.StyledPanel)
        self.MainMenu.setFrameShadow(QtGui.QFrame.Raised)
        self.MainMenu.setObjectName("MainMenu")
        self.mmenu_vout = QtGui.QVBoxLayout(self.MainMenu)
        self.mmenu_vout.setObjectName("mmenu_vout")
        self.horizontalLayout.addWidget(self.MainMenu)
        self.SubMenu = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SubMenu.sizePolicy().hasHeightForWidth())
        self.SubMenu.setSizePolicy(sizePolicy)
        self.SubMenu.setMinimumSize(QtCore.QSize(460, 730))
        self.SubMenu.setFrameShape(QtGui.QFrame.StyledPanel)
        self.SubMenu.setFrameShadow(QtGui.QFrame.Raised)
        self.SubMenu.setObjectName("SubMenu")
        self.smenu_gout = QtGui.QGridLayout(self.SubMenu)
        self.smenu_gout.setObjectName("smenu_gout")
        self.horizontalLayout.addWidget(self.SubMenu)
        self.CheckOut = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CheckOut.sizePolicy().hasHeightForWidth())
        self.CheckOut.setSizePolicy(sizePolicy)
        self.CheckOut.setMaximumSize(QtCore.QSize(470, 730))
        self.CheckOut.setFrameShape(QtGui.QFrame.StyledPanel)
        self.CheckOut.setFrameShadow(QtGui.QFrame.Raised)
        self.CheckOut.setObjectName("CheckOut")
        self.gridLayout = QtGui.QGridLayout(self.CheckOut)
        self.gridLayout.setContentsMargins(1, 1, 1, 1)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.Tax_Val_Lbl = QtGui.QLabel(self.CheckOut)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(13)
        self.Tax_Val_Lbl.setFont(font)
        self.Tax_Val_Lbl.setStyleSheet("")
        self.Tax_Val_Lbl.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.Tax_Val_Lbl.setObjectName("Tax_Val_Lbl")
        self.gridLayout.addWidget(self.Tax_Val_Lbl, 3, 2, 1, 1)
        self.line = QtGui.QFrame(self.CheckOut)
        self.line.setMinimumSize(QtCore.QSize(0, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 6, 0, 1, 3)
        self.TaxLbl = QtGui.QLabel(self.CheckOut)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setItalic(False)
        self.TaxLbl.setFont(font)
        self.TaxLbl.setStyleSheet("font: 14pt \"Calibri\";")
        self.TaxLbl.setObjectName("TaxLbl")
        self.gridLayout.addWidget(self.TaxLbl, 3, 0, 1, 1)
        self.AdjtBtn = QtGui.QPushButton(self.CheckOut)
        self.AdjtBtn.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.AdjtBtn.setFont(font)
        self.AdjtBtn.setObjectName("AdjtBtn")
        self.gridLayout.addWidget(self.AdjtBtn, 7, 2, 1, 1)
        self.PayBtn = QtGui.QPushButton(self.CheckOut)
        self.PayBtn.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.PayBtn.setFont(font)
        self.PayBtn.setAutoDefault(False)
        self.PayBtn.setDefault(False)
        self.PayBtn.setFlat(False)
        self.PayBtn.setObjectName("PayBtn")
        self.gridLayout.addWidget(self.PayBtn, 5, 0, 1, 3)
        self.Dis_Val_Lbl = QtGui.QLabel(self.CheckOut)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(13)
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.Dis_Val_Lbl.setFont(font)
        self.Dis_Val_Lbl.setStyleSheet("")
        self.Dis_Val_Lbl.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.Dis_Val_Lbl.setObjectName("Dis_Val_Lbl")
        self.gridLayout.addWidget(self.Dis_Val_Lbl, 2, 2, 1, 1)
        self.Tot_Val_Lbl = QtGui.QLabel(self.CheckOut)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(13)
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.Tot_Val_Lbl.setFont(font)
        self.Tot_Val_Lbl.setStyleSheet("")
        self.Tot_Val_Lbl.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.Tot_Val_Lbl.setObjectName("Tot_Val_Lbl")
        self.gridLayout.addWidget(self.Tot_Val_Lbl, 1, 2, 1, 1)
        self.GTot_Val_Lbl = QtGui.QLabel(self.CheckOut)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(13)
        self.GTot_Val_Lbl.setFont(font)
        self.GTot_Val_Lbl.setStyleSheet("")
        self.GTot_Val_Lbl.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.GTot_Val_Lbl.setObjectName("GTot_Val_Lbl")
        self.gridLayout.addWidget(self.GTot_Val_Lbl, 4, 2, 1, 1)
        self.CorrBtn = QtGui.QPushButton(self.CheckOut)
        self.CorrBtn.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.CorrBtn.setFont(font)
        self.CorrBtn.setObjectName("CorrBtn")
        self.gridLayout.addWidget(self.CorrBtn, 7, 1, 1, 1)
        self.DisLbl = QtGui.QLabel(self.CheckOut)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setWeight(75)
        font.setItalic(False)
        font.setStrikeOut(False)
        font.setBold(True)
        self.DisLbl.setFont(font)
        self.DisLbl.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.DisLbl.setAutoFillBackground(False)
        self.DisLbl.setStyleSheet("")
        self.DisLbl.setFrameShape(QtGui.QFrame.NoFrame)
        self.DisLbl.setFrameShadow(QtGui.QFrame.Raised)
        self.DisLbl.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.DisLbl.setObjectName("DisLbl")
        self.gridLayout.addWidget(self.DisLbl, 2, 0, 1, 1)
        self.CancBtn = QtGui.QPushButton(self.CheckOut)
        self.CancBtn.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.CancBtn.setFont(font)
        self.CancBtn.setObjectName("CancBtn")
        self.gridLayout.addWidget(self.CancBtn, 7, 0, 1, 1)
        self.GTotlbl = QtGui.QLabel(self.CheckOut)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setItalic(False)
        self.GTotlbl.setFont(font)
        self.GTotlbl.setStyleSheet("font: 14pt \"Calibri\";")
        self.GTotlbl.setObjectName("GTotlbl")
        self.gridLayout.addWidget(self.GTotlbl, 4, 0, 1, 1)
        self.TotLbl = QtGui.QLabel(self.CheckOut)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setWeight(75)
        font.setItalic(False)
        font.setStrikeOut(False)
        font.setBold(True)
        self.TotLbl.setFont(font)
        self.TotLbl.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.TotLbl.setAutoFillBackground(False)
        self.TotLbl.setStyleSheet("")
        self.TotLbl.setFrameShape(QtGui.QFrame.NoFrame)
        self.TotLbl.setFrameShadow(QtGui.QFrame.Raised)
        self.TotLbl.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.TotLbl.setObjectName("TotLbl")
        self.gridLayout.addWidget(self.TotLbl, 1, 0, 1, 1)

        self.prdCart = QtGui.QTableView(self.CheckOut)
        # self.prdCart.setItemDelegateForColumn(2, SpinBoxDelegate(self.prdCart))
        self.prdCart.setObjectName("prdCart")
        self.gridLayout.addWidget(self.prdCart, 0, 0, 1, 3)
        self.horizontalLayout.addWidget(self.CheckOut)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        menuWin.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(menuWin)
        self.statusbar.setObjectName("statusbar")
        menuWin.setStatusBar(self.statusbar)

        self.retranslateUi(menuWin)
        QtCore.QMetaObject.connectSlotsByName(menuWin)

    def retranslateUi(self, menuWin):
        menuWin.setWindowTitle(
            QtGui.QApplication.translate("menuWin", "LeGrandPit POS", None, QtGui.QApplication.UnicodeUTF8))
        self.Tax_Val_Lbl.setText(QtGui.QApplication.translate("menuWin", "$0.00", None, QtGui.QApplication.UnicodeUTF8))
        self.TaxLbl.setText(QtGui.QApplication.translate("menuWin", "Tax", None, QtGui.QApplication.UnicodeUTF8))
        self.AdjtBtn.setText(
            QtGui.QApplication.translate("menuWin", "Print Receipt", None, QtGui.QApplication.UnicodeUTF8))
        self.PayBtn.setText(QtGui.QApplication.translate("menuWin", "PAY", None, QtGui.QApplication.UnicodeUTF8))
        self.Dis_Val_Lbl.setText(QtGui.QApplication.translate("menuWin", "$0.00", None, QtGui.QApplication.UnicodeUTF8))
        self.Tot_Val_Lbl.setText(QtGui.QApplication.translate("menuWin", "$0.00", None, QtGui.QApplication.UnicodeUTF8))
        self.GTot_Val_Lbl.setText(
            QtGui.QApplication.translate("menuWin", "$0.00", None, QtGui.QApplication.UnicodeUTF8))
        self.CorrBtn.setText(
            QtGui.QApplication.translate("menuWin", "Correction", None, QtGui.QApplication.UnicodeUTF8))
        self.DisLbl.setText(QtGui.QApplication.translate("menuWin", "Discount", None, QtGui.QApplication.UnicodeUTF8))
        self.CancBtn.setText(QtGui.QApplication.translate("menuWin", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.GTotlbl.setText(
            QtGui.QApplication.translate("menuWin", "Grand Total", None, QtGui.QApplication.UnicodeUTF8))
        self.TotLbl.setText(QtGui.QApplication.translate("menuWin", "Total", None, QtGui.QApplication.UnicodeUTF8))
