# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Helpviewer\CookieJar\CookiesExceptionsDialog.ui'
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

class Ui_CookiesExceptionsDialog(object):
    def setupUi(self, CookiesExceptionsDialog):
        CookiesExceptionsDialog.setObjectName(_fromUtf8("CookiesExceptionsDialog"))
        CookiesExceptionsDialog.resize(500, 450)
        CookiesExceptionsDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtGui.QVBoxLayout(CookiesExceptionsDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.newExceptionGroupBox = QtGui.QGroupBox(CookiesExceptionsDialog)
        self.newExceptionGroupBox.setObjectName(_fromUtf8("newExceptionGroupBox"))
        self.gridlayout = QtGui.QGridLayout(self.newExceptionGroupBox)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self._2 = QtGui.QHBoxLayout()
        self._2.setObjectName(_fromUtf8("_2"))
        self.label = QtGui.QLabel(self.newExceptionGroupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self._2.addWidget(self.label)
        self.domainEdit = QtGui.QLineEdit(self.newExceptionGroupBox)
        self.domainEdit.setObjectName(_fromUtf8("domainEdit"))
        self._2.addWidget(self.domainEdit)
        self.gridlayout.addLayout(self._2, 0, 0, 1, 1)
        self._3 = QtGui.QHBoxLayout()
        self._3.setObjectName(_fromUtf8("_3"))
        spacerItem = QtGui.QSpacerItem(81, 25, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self._3.addItem(spacerItem)
        self.blockButton = QtGui.QPushButton(self.newExceptionGroupBox)
        self.blockButton.setEnabled(False)
        self.blockButton.setAutoDefault(False)
        self.blockButton.setObjectName(_fromUtf8("blockButton"))
        self._3.addWidget(self.blockButton)
        self.allowForSessionButton = QtGui.QPushButton(self.newExceptionGroupBox)
        self.allowForSessionButton.setEnabled(False)
        self.allowForSessionButton.setAutoDefault(False)
        self.allowForSessionButton.setObjectName(_fromUtf8("allowForSessionButton"))
        self._3.addWidget(self.allowForSessionButton)
        self.allowButton = QtGui.QPushButton(self.newExceptionGroupBox)
        self.allowButton.setEnabled(False)
        self.allowButton.setAutoDefault(False)
        self.allowButton.setObjectName(_fromUtf8("allowButton"))
        self._3.addWidget(self.allowButton)
        self.gridlayout.addLayout(self._3, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.newExceptionGroupBox)
        self.exceptionsGroup = QtGui.QGroupBox(CookiesExceptionsDialog)
        self.exceptionsGroup.setObjectName(_fromUtf8("exceptionsGroup"))
        self.gridLayout = QtGui.QGridLayout(self.exceptionsGroup)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.searchEdit = QtGui.QLineEdit(self.exceptionsGroup)
        self.searchEdit.setObjectName(_fromUtf8("searchEdit"))
        self.horizontalLayout.addWidget(self.searchEdit)
        self.clearButton = QtGui.QToolButton(self.exceptionsGroup)
        self.clearButton.setText(_fromUtf8(""))
        self.clearButton.setObjectName(_fromUtf8("clearButton"))
        self.horizontalLayout.addWidget(self.clearButton)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 3)
        self.exceptionsTable = E4TableView(self.exceptionsGroup)
        self.exceptionsTable.setAlternatingRowColors(True)
        self.exceptionsTable.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.exceptionsTable.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.exceptionsTable.setShowGrid(False)
        self.exceptionsTable.setSortingEnabled(True)
        self.exceptionsTable.setObjectName(_fromUtf8("exceptionsTable"))
        self.exceptionsTable.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.exceptionsTable, 1, 0, 1, 3)
        self.removeButton = QtGui.QPushButton(self.exceptionsGroup)
        self.removeButton.setAutoDefault(False)
        self.removeButton.setObjectName(_fromUtf8("removeButton"))
        self.gridLayout.addWidget(self.removeButton, 2, 0, 1, 1)
        self.removeAllButton = QtGui.QPushButton(self.exceptionsGroup)
        self.removeAllButton.setAutoDefault(False)
        self.removeAllButton.setObjectName(_fromUtf8("removeAllButton"))
        self.gridLayout.addWidget(self.removeAllButton, 2, 1, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(286, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 2, 2, 1, 1)
        self.verticalLayout.addWidget(self.exceptionsGroup)
        self.buttonBox = QtGui.QDialogButtonBox(CookiesExceptionsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        self.label.setBuddy(self.domainEdit)

        self.retranslateUi(CookiesExceptionsDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), CookiesExceptionsDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), CookiesExceptionsDialog.reject)
        QtCore.QObject.connect(self.clearButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.searchEdit.clear)
        QtCore.QMetaObject.connectSlotsByName(CookiesExceptionsDialog)
        CookiesExceptionsDialog.setTabOrder(self.domainEdit, self.blockButton)
        CookiesExceptionsDialog.setTabOrder(self.blockButton, self.allowForSessionButton)
        CookiesExceptionsDialog.setTabOrder(self.allowForSessionButton, self.allowButton)
        CookiesExceptionsDialog.setTabOrder(self.allowButton, self.searchEdit)
        CookiesExceptionsDialog.setTabOrder(self.searchEdit, self.clearButton)
        CookiesExceptionsDialog.setTabOrder(self.clearButton, self.exceptionsTable)
        CookiesExceptionsDialog.setTabOrder(self.exceptionsTable, self.removeButton)
        CookiesExceptionsDialog.setTabOrder(self.removeButton, self.removeAllButton)
        CookiesExceptionsDialog.setTabOrder(self.removeAllButton, self.buttonBox)

    def retranslateUi(self, CookiesExceptionsDialog):
        CookiesExceptionsDialog.setWindowTitle(_translate("CookiesExceptionsDialog", "Cookie Exceptions", None))
        self.newExceptionGroupBox.setTitle(_translate("CookiesExceptionsDialog", "New Exception", None))
        self.label.setText(_translate("CookiesExceptionsDialog", "&Domain:", None))
        self.domainEdit.setToolTip(_translate("CookiesExceptionsDialog", "Enter the domain name", None))
        self.blockButton.setToolTip(_translate("CookiesExceptionsDialog", "Press to always reject cookies for the domain", None))
        self.blockButton.setText(_translate("CookiesExceptionsDialog", "&Block", None))
        self.allowForSessionButton.setToolTip(_translate("CookiesExceptionsDialog", "Press to accept cookies for the domain for the current session", None))
        self.allowForSessionButton.setText(_translate("CookiesExceptionsDialog", "Allow For &Session", None))
        self.allowButton.setToolTip(_translate("CookiesExceptionsDialog", "Press to always accept cookies for the domain", None))
        self.allowButton.setText(_translate("CookiesExceptionsDialog", "Allo&w", None))
        self.exceptionsGroup.setTitle(_translate("CookiesExceptionsDialog", "Exceptions", None))
        self.searchEdit.setToolTip(_translate("CookiesExceptionsDialog", "Enter search term for exceptions", None))
        self.clearButton.setToolTip(_translate("CookiesExceptionsDialog", "Press to clear the search edit", None))
        self.removeButton.setToolTip(_translate("CookiesExceptionsDialog", "Press to remove the selected entries", None))
        self.removeButton.setText(_translate("CookiesExceptionsDialog", "&Remove", None))
        self.removeAllButton.setToolTip(_translate("CookiesExceptionsDialog", "Press to remove all entries", None))
        self.removeAllButton.setText(_translate("CookiesExceptionsDialog", "Remove &All", None))

from E4Gui.E4TableView import E4TableView
