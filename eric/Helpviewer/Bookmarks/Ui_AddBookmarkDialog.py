# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Helpviewer\Bookmarks\AddBookmarkDialog.ui'
#
# Created: Fri Apr 18 09:56:41 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_AddBookmarkDialog(object):
    def setupUi(self, AddBookmarkDialog):
        AddBookmarkDialog.setObjectName(_fromUtf8("AddBookmarkDialog"))
        AddBookmarkDialog.resize(400, 174)
        AddBookmarkDialog.setMinimumSize(QtCore.QSize(400, 0))
        AddBookmarkDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtGui.QVBoxLayout(AddBookmarkDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(AddBookmarkDialog)
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.nameEdit = E4LineEdit(AddBookmarkDialog)
        self.nameEdit.setObjectName(_fromUtf8("nameEdit"))
        self.verticalLayout.addWidget(self.nameEdit)
        self.addressEdit = E4LineEdit(AddBookmarkDialog)
        self.addressEdit.setObjectName(_fromUtf8("addressEdit"))
        self.verticalLayout.addWidget(self.addressEdit)
        self.locationCombo = QtGui.QComboBox(AddBookmarkDialog)
        self.locationCombo.setObjectName(_fromUtf8("locationCombo"))
        self.verticalLayout.addWidget(self.locationCombo)
        spacerItem = QtGui.QSpacerItem(20, 9, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.buttonBox = QtGui.QDialogButtonBox(AddBookmarkDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(AddBookmarkDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), AddBookmarkDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), AddBookmarkDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(AddBookmarkDialog)
        AddBookmarkDialog.setTabOrder(self.nameEdit, self.addressEdit)
        AddBookmarkDialog.setTabOrder(self.addressEdit, self.locationCombo)
        AddBookmarkDialog.setTabOrder(self.locationCombo, self.buttonBox)

    def retranslateUi(self, AddBookmarkDialog):
        AddBookmarkDialog.setWindowTitle(_translate("AddBookmarkDialog", "Add Bookmark", None))
        self.label.setText(_translate("AddBookmarkDialog", "Type a name for the bookmark, and choose where to keep it.", None))
        self.nameEdit.setToolTip(_translate("AddBookmarkDialog", "Enter the name", None))
        self.addressEdit.setToolTip(_translate("AddBookmarkDialog", "Enter the address", None))

from E4Gui.E4LineEdit import E4LineEdit
