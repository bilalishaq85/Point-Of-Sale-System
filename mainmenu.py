from PySide import QtGui
from PySide import QtCore
from templates.ui_menuwin import Ui_menuWin
from DAL.dataAccess import *
from popup import popUp
from prdCart import TableModel
import sys
from prdCart import SpinBoxDelegate


# class mainMenu(QtGui.QWidget, Ui_menuWin):
class mainMenu(QtGui.QMainWindow, Ui_menuWin):
    def __init__(self, parent=None):
        super(mainMenu, self).__init__(parent)
        # self.setupUi(parent)
        self.setupUi(self)
        # ********************************** Initializing Constants ****************************************************
        self.lstBtn = 0
        self.const = readConst("app_conf", "constants")
        self.selectedPrd = ()
        self.order = []
        # **************************************************************************************************************
        self.btnGrp = QtGui.QButtonGroup()
        self.disMMenu()
        self.show()

    def disMMenu(self):
        result = dataAccess.mainMenu()
        if result:
            for row in result:
                self.mmenu_bt = QtGui.QPushButton(row[1])
                self.mmenu_bt.setObjectName(row[0])

                # *********************************** Buttons Layout ***************************************************
                self.mmenu_bt.setMinimumSize(QtCore.QSize(int(self.const['bt_minw']), int(self.const['bt_minh'])))
                self.mmenu_bt.setMaximumSize(QtCore.QSize(int(self.const['bt_maxw']), int(self.const['bt_maxh'])))
                font = QtGui.QFont()
                font.setFamily(self.const['bt_txt_font'])
                font.setPointSize(int(self.const['bt_txt_size']))
                self.mmenu_bt.setFont(font)
                self.mmenu_vout.setAlignment(QtCore.Qt.AlignTop)
                self.mmenu_vout.setSpacing(int(self.const['bt_space']))
                self.mmenu_bt.setCheckable(True)
                # ******************************************************************************************************
                self.btnGrp.addButton(self.mmenu_bt)
                self.mmenu_bt.clicked.connect(lambda mpid=row[0]: self.disSMenu(mpid))
                # self.mmenu_bt.clicked.connect(self.mmenu_bt_clk)
                self.mmenu_vout.addWidget(self.mmenu_bt)

                # *********************************** Auto Checked First Button  ***************************************
                if row[0] == 'A001':
                    self.mmenu_bt.setChecked(True)
                    self.mmenu_bt.connectNotify(self.disSMenu(row[0]))
                    # ******************************************************************************************************
        else:
            Logger.logr.error("Main Menu not found")
            reply = QtGui.QMessageBox.critical(self, 'Message',
                                               readConst('usr_msgs', 'constants')['crit_msg'], QtGui.QMessageBox.Ok)
            if reply == QtGui.QMessageBox.Ok:
                sys.exit(0)
                # def mmenu_bt_clk(self):
                #   button = self.sender()
                #  if isinstance(button, QtGui.QPushButton):
                #     print("You pressed %s!" % button.text())

                # def whichbtn(self, b):
                # print("clicked button is " + b)

    def disSMenu(self, mpid):
        if self.lstBtn != mpid:
            clearLayout(self.smenu_gout)
            result = dataAccess.subMenu(mpid)
            if result:
                x = 0
                y = 0
                for row in result:
                    # ********************* Display Price/Disable button if no price ***********************************
                    if row[3] == 1 and all(row):
                        self.smenu_bt = QtGui.QPushButton(row[1] + "{price}".format(price="\n$" + str(row[2])))
                    elif row[2] is None and row[3] == 1:
                        self.smenu_bt = QtGui.QPushButton(row[1])
                        self.smenu_bt.setEnabled(False)
                        Logger.logr.error("price for product named, " + row[1] + " is missing at lvl-2 in prod. hier.")
                        self.statusbar.setStyleSheet("color:red")
                        self.statusbar.showMessage(readConst('usr_msgs', 'constants')['crit_msg'],
                                                   int(readConst('usr_msgs', 'constants')['distime_msg']))
                    else:
                        self.smenu_bt = QtGui.QPushButton(row[1])
                    # **************************************************************************************************
                    self.smenu_bt.setObjectName(row[0])
                    # *********************************** Buttons Layout ***********************************************
                    self.smenu_bt.setMinimumSize(QtCore.QSize(int(self.const['bt_minw']), int(self.const['bt_minh'])))
                    # self.smenu_bt.setMaximumSize(QtCore.QSize(118, 50))
                    font = QtGui.QFont()
                    font.setFamily(self.const['bt_txt_font'])
                    font.setPointSize(int(self.const['bt_txt_size']))
                    self.smenu_bt.setFont(font)
                    self.smenu_gout.setAlignment(QtCore.Qt.AlignTop)
                    self.smenu_gout.setSpacing(int(self.const['bt_space']))
                    # **************************************************************************************************
                    # *********************************** Click Function ***********************************************
                    self.smenu_bt.clicked.connect(
                        lambda mpid=row[4], mpdes=row[5], spid=row[0], spdes=row[1], lst_lvl=row[3], lvl_or_prc=row[2]:
                        self.disDialog(mpid, mpdes, spid, spdes, lst_lvl, lvl_or_prc))
                    # **************************************************************************************************
                    self.smenu_gout.addWidget(self.smenu_bt, x, y, 1, 1)
                    y += 1
                    if y > (int(self.const['smen_colno'])):
                        y = 0
                        x += 1
            else:
                reply = QtGui.QMessageBox.critical(self, 'Message',
                                                   readConst('usr_msgs', 'constants')['crit_msg'], QtGui.QMessageBox.Ok)
                if reply == QtGui.QMessageBox.Ok:
                    sys.exit(0)
        self.lstBtn = mpid

    def disDialog(self, mpid, mpdes, spid, spdes, lst_lvl, lvl_or_prc):
        self.selectedPrd += (mpid,)
        self.selectedPrd += (mpdes,)
        self.selectedPrd += (spid,)
        self.selectedPrd += (spdes,)
        if lst_lvl == 0:
            result = dataAccess.s1Dialog(spid)
            if result:
                # ****************************** Display Dialog ********************************************************
                s1 = popUp(result)
                if s1.exec_():
                    s1_rbtId = s1.rbtId
                    self.selectedPrd += (s1_rbtId,)
                    self.selectedPrd += (s1.rbtSize,)
                    self.selectedPrd += (str(s1.rbtPrc),)
                    # **************************************************************************************************
                    # ****************************** Display SubDialog *************************************************
                    if result[0][3] == 0:
                        result = dataAccess.s1Dialog(s1_rbtId)
                        s1 = popUp(result)
                        if s1.exec_():
                            s2_rbtid = s1.rbtId
                            # ******************************************************************************************
                            self.selectedPrd += (s2_rbtid,)
                            self.selectedPrd += (s1.rbtSize,)
                            self.selectedPrd += (str(s1.rbtPrc),)
                        else:
                            self.selectedPrd = ()
                else:
                    self.selectedPrd = ()
        else:
            self.selectedPrd += (str(lvl_or_prc),)
        # *************************** Building Orderlist/full Product Details ******************************************
        if len(self.selectedPrd) is not 0:
            self.order.append(buildPrdDtl(self.selectedPrd))
            print(self.order)
            # **********************************************************************************************************
            # ************** Initializing TableClass/Connecting Emitted Signal Upon ValueChanged ***********************
            self.tblModl = TableModel(self, self.order)
            delegate = SpinBoxDelegate(self.prdCart, self.order)
            self.prdCart.setModel(self.tblModl)
            self.prdCart.setItemDelegateForColumn(0, delegate)
            self.prdCart.setItemDelegateForColumn(3, delegate)
            for row in range(0, self.tblModl.rowCount()):
                self.prdCart.openPersistentEditor(self.tblModl.index(row, 3))
            self.tblModl.orderUpdSig.connect(self.updateOrder)
            delegate.orderDelSig.connect(self.updateOrder)
            # **********************************************************************************************************
            # *********************** Setting up Cart Display **********************************************************
            vh = self.prdCart.verticalHeader()
            vh.setVisible(False)
            hh = self.prdCart.horizontalHeader()
            hh.setVisible(True)
            self.prdCart.setColumnWidth(0, 17)
            self.prdCart.setColumnWidth(1, 107)
            self.prdCart.setColumnWidth(2, 174)
            self.prdCart.setColumnWidth(3, 66)
            self.prdCart.setColumnWidth(4, 40)
            self.selectedPrd = ()  # ***** Empty tuple after displayed in cart *****

    def updateOrder(self, index, value, signal):
        self.tblModl.layoutAboutToBeChanged.emit()
        if signal == "D":
            del (self.order[index])
            self.tblModl.layoutChanged.emit()
        if signal == "U":
            ordList = list(self.order[index])
            self.order[index] = (ordList[0], ordList[1], ordList[2], value, value * 10.99)
        print(self.order)
        self.tblModl.layoutChanged.emit()





        # self.prdCart.setIndexWidget()
        # self.prdCart.setItemDelegateForColumn(2,ComboDelegate(self))

        # header = self.prdCart.horizontalHeader()
        # header.setResizeMode(0, QtGui.QHeaderView.setFixedWidth(10))
        # header.setResizeMode(1, QtGui.QHeaderView.Stretch)
        # header.setResizeMode(2, QtGui.QHeaderView.ResizeToContents)


def main():
    app = QtGui.QApplication(sys.argv)
    mainWin = mainMenu()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
