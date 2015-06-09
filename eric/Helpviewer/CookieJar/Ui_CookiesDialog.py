# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Helpviewer\CookieJar\CookiesDialog.ui'
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

class Ui_CookiesDialog(object):
    def setupUi(self, CookiesDialog):
        CookiesDialog.setObjectName(_fromUtf8("CookiesDialog"))
        CookiesDialog.resize(500, 350)
        CookiesDialog.setSizeGripEnabled(True)
        self.gridLayout = QtGui.QGridLayout(CookiesDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.searchEdit = QtGui.QLineEdit(CookiesDialog)
        self.searchEdit.setObjectName(_fromUtf8("searchEdit"))
        self.horizontalLayout.addWidget(self.searchEdit)
        self.clearButton = QtGui.QToolButton(CookiesDialog)
        self.clearButton.setText(_fromUtf8(""))
        self.clearButton.setObjectName(_fromUtf8("clearButton"))
        self.horizontalLayout.addWidget(self.clearButton)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 4)
        self.cookiesTable = E4TableView(CookiesDialog)
        self.cookiesTable.setAlternatingRowColors(True)
        self.cookiesTable.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.cookiesTable.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.cookiesTable.setShowGrid(False)
        self.cookiesTable.setSortingEnabled(True)
        self.cookiesTable.setObjectName(_fromUtf8("cookiesTable"))
        self.gridLayout.addWidget(self.cookiesTable, 1, 0, 1, 4)
        self.removeButton = QtGui.QPushButton(CookiesDialog)
        self.removeButton.setAutoDefault(False)
        self.removeButton.setObjectName(_fromUtf8("removeButton"))
        self.gridLayout.addWidget(self.removeButton, 2, 0, 1, 1)
        self.removeAllButton = QtGui.QPushButton(CookiesDialog)
        self.removeAllButton.setAutoDefault(False)
        self.removeAllButton.setObjectName(_fromUtf8("removeAllButton"))
        self.gridLayout.addWidget(self.removeAllButton, 2, 1, 1, 1)
        self.addButton = QtGui.QPushButton(CookiesDialog)
        self.addButton.setAutoDefault(False)
        self.addButton.setObjectName(_fromUtf8("addButton"))
        self.gridLayout.addWidget(self.addButton, 2, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(208, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 3, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(CookiesDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 3, 0, 1, 4)

        self.retranslateUi(CookiesDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), CookiesDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), CookiesDialog.reject)
        QtCore.QObject.connect(self.clearButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.searchEdit.clear)
        QtCore.QMetaObject.connectSlotsByName(CookiesDialog)
        CookiesDialog.setTabOrder(self.searchEdit, self.clearButton)
        CookiesDialog.setTabOrder(self.clearButton, self.cookiesTable)
        CookiesDialog.setTabOrder(self.cookiesTable, self.removeButton)
        CookiesDialog.setTabOrder(self.removeButton, self.removeAllButton)
        CookiesDialog.setTabOrder(self.removeAllButton, self.addButton)
        CookiesDialog.setTabOrder(self.addButton, self.buttonBox)

    def retranslateUi(self, CookiesDialog):
        CookiesDialog.setWindowTitle(_translate("CookiesDialog", "Cookies", None))
        self.searchEdit.setToolTip(_translate("CookiesDialog", "Enter search term for cookies", None))
        self.clearButton.setToolTip(_translate("CookiesDialog", "Press to clear the search edit", None))
        self.removeButton.setToolTip(_translate("CookiesDialog", "Press to remove the selected entries", None))
        self.removeButton.setText(_translate("CookiesDialog", "&Remove", None))
        self.removeAllButton.setToolTip(_translate("CookiesDialog", "Press to remove all entries", None))
        self.removeAllButton.setText(_translate("CookiesDialog", "Remove &All", None))
        self.addButton.setToolTip(_translate("CookiesDialog", "Press to open the cookies exceptions dialog to add a new rule", None))
        self.addButton.setText(_translate("CookiesDialog", "Add R&ule...", None))

from E4Gui.E4TableView import E4TableView
