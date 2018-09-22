from PySide import QtGui, QtCore
from templates.ui_popup import Ui_sDialog
from DAL.dataAccess import *


class popUp(QtGui.QDialog, Ui_sDialog):
    def __init__(self, result, parent=None):
        super(popUp, self).__init__(parent)
        # ********************************** Initializing Constants ****************************************************
        self.rbtId = 0
        self.rbtSize = 0
        self.rbtPrc = 0

        self.result = result
        self.const = readConst("app_conf", "constants")

        # ********************* Removing/Disabling help & close button from dialog *************************************
        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowContextHelpButtonHint)
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.CustomizeWindowHint)
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowCloseButtonHint)

        # *************************** Blocking Main window while dialog is open  ***************************************
        self.setWindowModality(QtCore.Qt.ApplicationModal)

        # ********************************* Initializing Classes *******************************************************
        self.setupUi(self)
        self.rbtGrp = QtGui.QButtonGroup()
        self.font = QtGui.QFont()
        # **************************************************************************************************************
        self.disOpts()
        self.show()

    def disOpts(self):
        # *********************************** Label Layout *************************************************************
        self.label = QtGui.QLabel(self)
        self.label.setGeometry(QtCore.QRect(5, 15, 201, 16))
        self.label.setObjectName("label")
        self.label.setText("Please select size:")
        self.font.setFamily(self.const['hd_font'])
        self.font.setPointSize(int(self.const['hd_txt_size']))
        self.label.setFont(self.font)
        # **************************************************************************************************************
        # print(self.result)
        for row in self.result:
            #print(row)
            # ********************* Display Radio button with Price ****************************************************
            self.radioButton = QtGui.QRadioButton(
                row[1] + "{price}".format(price=" - $" + str(row[2]) if len(row) > 2 and row[3] == 1 else ''))
            self.radioButton.setObjectName(row[0])
            # *********************************** Radio Button Layout **************************************************
            self.font.setFamily(self.const['lbl_txt_font'])
            self.font.setPointSize(int(self.const['lbl_text_size']))
            self.radioButton.setFont(self.font)
            self.rbt_vout.setSpacing(int(self.const['rbt_space']))
            # **********************************************************************************************************
            self.rbtGrp.addButton(self.radioButton)
            self.rbt_vout.addWidget(self.radioButton)
            self.radioButton.clicked.connect(
                lambda rbtId=row[0], rbtSize=row[1],
                       rbtPrc=row[2] if len(row) > 2 and row[3] == 1 else '': self.getSelection(rbtId, rbtSize, rbtPrc))

        # *********************************** Ok/Cancel Layout *********************************************************
        self.buttonBox = QtGui.QDialogButtonBox(QtGui.QDialogButtonBox.Ok | QtGui.QDialogButtonBox.Cancel)
        self.bt_hout.addWidget(self.buttonBox)
        self.buttonBox.accepted.connect(self.hanBtClk)
        self.buttonBox.rejected.connect(self.reject)

    def getSelection(self, rbt_id, rbtSize, rbt_prc):
        self.rbtId = rbt_id
        self.rbtSize = rbtSize
        self.rbtPrc = rbt_prc

    def hanBtClk(self):
        if self.rbtId == 0:
            self.label.setStyleSheet("color:red")
        else:
            self.accept()
