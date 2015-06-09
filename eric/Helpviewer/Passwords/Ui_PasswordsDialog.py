# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Helpviewer\Passwords\PasswordsDialog.ui'
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

class Ui_PasswordsDialog(object):
    def setupUi(self, PasswordsDialog):
        PasswordsDialog.setObjectName(_fromUtf8("PasswordsDialog"))
        PasswordsDialog.resize(500, 350)
        PasswordsDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtGui.QVBoxLayout(PasswordsDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.searchEdit = QtGui.QLineEdit(PasswordsDialog)
        self.searchEdit.setObjectName(_fromUtf8("searchEdit"))
        self.horizontalLayout.addWidget(self.searchEdit)
        self.clearButton = QtGui.QToolButton(PasswordsDialog)
        self.clearButton.setText(_fromUtf8(""))
        self.clearButton.setObjectName(_fromUtf8("clearButton"))
        self.horizontalLayout.addWidget(self.clearButton)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.passwordsTable = E4TableView(PasswordsDialog)
        self.passwordsTable.setAlternatingRowColors(True)
        self.passwordsTable.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.passwordsTable.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.passwordsTable.setShowGrid(False)
        self.passwordsTable.setSortingEnabled(True)
        self.passwordsTable.setObjectName(_fromUtf8("passwordsTable"))
        self.verticalLayout.addWidget(self.passwordsTable)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.removeButton = QtGui.QPushButton(PasswordsDialog)
        self.removeButton.setAutoDefault(False)
        self.removeButton.setObjectName(_fromUtf8("removeButton"))
        self.horizontalLayout_3.addWidget(self.removeButton)
        self.removeAllButton = QtGui.QPushButton(PasswordsDialog)
        self.removeAllButton.setAutoDefault(False)
        self.removeAllButton.setObjectName(_fromUtf8("removeAllButton"))
        self.horizontalLayout_3.addWidget(self.removeAllButton)
        spacerItem1 = QtGui.QSpacerItem(208, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.passwordsButton = QtGui.QPushButton(PasswordsDialog)
        self.passwordsButton.setText(_fromUtf8(""))
        self.passwordsButton.setObjectName(_fromUtf8("passwordsButton"))
        self.horizontalLayout_3.addWidget(self.passwordsButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.buttonBox = QtGui.QDialogButtonBox(PasswordsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(PasswordsDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), PasswordsDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), PasswordsDialog.reject)
        QtCore.QObject.connect(self.clearButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.searchEdit.clear)
        QtCore.QMetaObject.connectSlotsByName(PasswordsDialog)
        PasswordsDialog.setTabOrder(self.searchEdit, self.clearButton)
        PasswordsDialog.setTabOrder(self.clearButton, self.passwordsTable)
        PasswordsDialog.setTabOrder(self.passwordsTable, self.removeButton)
        PasswordsDialog.setTabOrder(self.removeButton, self.removeAllButton)
        PasswordsDialog.setTabOrder(self.removeAllButton, self.passwordsButton)
        PasswordsDialog.setTabOrder(self.passwordsButton, self.buttonBox)

    def retranslateUi(self, PasswordsDialog):
        PasswordsDialog.setWindowTitle(_translate("PasswordsDialog", "Saved Passwords", None))
        self.searchEdit.setToolTip(_translate("PasswordsDialog", "Enter search term", None))
        self.clearButton.setToolTip(_translate("PasswordsDialog", "Press to clear the search edit", None))
        self.removeButton.setToolTip(_translate("PasswordsDialog", "Press to remove the selected entries", None))
        self.removeButton.setText(_translate("PasswordsDialog", "&Remove", None))
        self.removeAllButton.setToolTip(_translate("PasswordsDialog", "Press to remove all entries", None))
        self.removeAllButton.setText(_translate("PasswordsDialog", "Remove &All", None))
        self.passwordsButton.setToolTip(_translate("PasswordsDialog", "Press to toggle the display of passwords", None))

from E4Gui.E4TableView import E4TableView
