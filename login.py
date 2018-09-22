from PySide import QtGui
from DAL.dataAccess import *
from Lib.Functions import *
from templates.ui_loginwin import Ui_loginWin
from mainmenu import mainMenu


class login(QtGui.QMainWindow, Ui_loginWin):
    def __init__(self, parent=None):
        Logger.logr.info("***** Initializing POS System *****")
        super(login, self).__init__(parent)
        self.startLogWin()

    def startLogWin(self):
        self.setupUi(self)
        self.show()

        # ****************************** Checking DB Conn **************************************************************
        if not dataAccess.chkDbCon():
            reply = QtGui.QMessageBox.critical(self, 'Error',
                                               readConst('usr_msgs', 'constants')['crit_msg'], QtGui.QMessageBox.Ok)
            if reply == QtGui.QMessageBox.Ok:
                sys.exit(0)

        self.login_btn.clicked.connect(self.chkLogin)

    def chkLogin(self):
        result = dataAccess.varifyLogin(self.uname.text(), self.pwd.text())
        if result:
            uname, pwd = result[0]
            if (uname == self.uname.text()) and (pwd == self.pwd.text()):
                Logger.logr.info("User has successfully logged into the application")
                mainMenu(self)
            else:
                Logger.logr.error("Login Failed: User does not exist in the database")
                self.statusbar.setStyleSheet("color:red")
                self.statusbar.showMessage(readConst('usr_msgs', 'constants')['logfail_msg2'],
                                           int(readConst('usr_msgs', 'constants')['distime_msg']))
        else:
            Logger.logr.error("Please enter username and password:")
            self.statusbar.setStyleSheet("color:red")
            self.statusbar.showMessage(readConst('usr_msgs', 'constants')['logfail_msg1'],
                                       int(readConst('usr_msgs', 'constants')['distime_msg']))

    def closeEvent(self, event):
        reply = QtGui.QMessageBox.question(self, 'Message',
                                           readConst('usr_msgs', 'constants')['quit_msg'], QtGui.QMessageBox.Yes,
                                           QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            Logger.logr.info("User has manually close the application")
            sys.exit(0)
            event.accept()

        else:
            event.ignore()


def main():
    app = QtGui.QApplication(sys.argv)
    mainWin = login()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
