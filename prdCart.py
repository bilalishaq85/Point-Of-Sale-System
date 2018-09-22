from PySide.QtCore import *
from PySide import QtGui, QtCore


class TableModel(QAbstractTableModel):
    orderUpdSig = QtCore.Signal(int, int, str)

    def __init__(self, parent, mylist, *args):
        QAbstractTableModel.__init__(self, parent, *args)
        self.mylist = mylist

    def rowCount(self, parent=QtCore.QModelIndex()):
        return len(self.mylist)

    def columnCount(self, parent=QtCore.QModelIndex()):
        if self.mylist:
            return len(self.mylist[0])
        else:
            return 0

    def data(self, index, role):
        if not index.isValid():
            return None
        if role != Qt.DisplayRole:
            return None
        return self.mylist[index.row()][index.column()]

    def setData(self, index, value, role=QtCore.Qt.DisplayRole):
        # ************************* Emit Signal only on QSpinBox value change ******************************************
        if value != 1:
            self.orderUpdSig.emit(index.row(), value, "U")
        else:
            return None


class SpinBoxDelegate(QtGui.QItemDelegate):
    orderDelSig = QtCore.Signal(int, int, str)

    def __init__(self, parent=None):
        super(SpinBoxDelegate, self).__init__(parent)

    def paint(self, painter, option, index):
        if index.column() == 0:
            path = 'C:\\Users\\bilal\\workspace\\PycharmProjects\\Pointofsale\\b_drop.png'
            image = QtGui.QImage(str(path))
            pixmap = QtGui.QPixmap.fromImage(image)
            painter.drawPixmap(option.rect.x(), option.rect.y() + 8, pixmap)

    def createEditor(self, parent, option, index):
        editor = QtGui.QSpinBox(parent)
        editor.lineEdit().setStyleSheet('selection-background-color:white; selection-color:black;')
        editor.lineEdit().setReadOnly(True)
        editor.setStyleSheet("QSpinBox { border: 0px inset grey; } \n"
                             "QSpinBox::up-button { subcontrol-position: left; width: 25px; height: 17px;}\n"
                             "QSpinBox::down-button { subcontrol-position: right; width: 25px; height: 17px;}")
        editor.setAlignment(QtCore.Qt.AlignCenter)
        editor.setButtonSymbols(QtGui.QAbstractSpinBox.PlusMinus)
        editor.setMinimum(1)
        editor.valueChanged.connect(self.editorValChg)
        return editor

    # def setEditorData(self, editor, index):
    #     value = index.model().data(index, QtCore.Qt.EditRole)
    #     print(value)
    #     editor.setValue(value)

    def setModelData(self, editor, model, index):
        editor.interpretText()
        value = editor.value()
        model.setData(index, value, QtCore.Qt.EditRole)

    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)

    def editorValChg(self):
        self.commitData.emit(self.sender())

    def editorEvent(self, event, model, option, index):
        if event.type() == QtCore.QEvent.MouseButtonRelease:
            self.orderDelSig.emit(index.row(), 0, "D")
        return True
        # return True
        # if event.type() == QtCore.QEvent.MouseButtonDblClick:
        #     print('Double-Clicked on Item', index.row())
        # return True


