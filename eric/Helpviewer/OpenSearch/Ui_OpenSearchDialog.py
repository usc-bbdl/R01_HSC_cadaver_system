# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Helpviewer\OpenSearch\OpenSearchDialog.ui'
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

class Ui_OpenSearchDialog(object):
    def setupUi(self, OpenSearchDialog):
        OpenSearchDialog.setObjectName(_fromUtf8("OpenSearchDialog"))
        OpenSearchDialog.resize(650, 350)
        OpenSearchDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtGui.QVBoxLayout(OpenSearchDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.enginesTable = E4TableView(OpenSearchDialog)
        self.enginesTable.setAlternatingRowColors(True)
        self.enginesTable.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.enginesTable.setShowGrid(False)
        self.enginesTable.setObjectName(_fromUtf8("enginesTable"))
        self.gridLayout.addWidget(self.enginesTable, 0, 0, 5, 1)
        self.addButton = QtGui.QPushButton(OpenSearchDialog)
        self.addButton.setAutoDefault(False)
        self.addButton.setObjectName(_fromUtf8("addButton"))
        self.gridLayout.addWidget(self.addButton, 0, 1, 1, 1)
        self.deleteButton = QtGui.QPushButton(OpenSearchDialog)
        self.deleteButton.setAutoDefault(False)
        self.deleteButton.setObjectName(_fromUtf8("deleteButton"))
        self.gridLayout.addWidget(self.deleteButton, 1, 1, 1, 1)
        self.editButton = QtGui.QPushButton(OpenSearchDialog)
        self.editButton.setAutoDefault(False)
        self.editButton.setObjectName(_fromUtf8("editButton"))
        self.gridLayout.addWidget(self.editButton, 2, 1, 1, 1)
        self.restoreButton = QtGui.QPushButton(OpenSearchDialog)
        self.restoreButton.setAutoDefault(False)
        self.restoreButton.setObjectName(_fromUtf8("restoreButton"))
        self.gridLayout.addWidget(self.restoreButton, 3, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 38, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 4, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.buttonBox = QtGui.QDialogButtonBox(OpenSearchDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(OpenSearchDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), OpenSearchDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), OpenSearchDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(OpenSearchDialog)
        OpenSearchDialog.setTabOrder(self.enginesTable, self.addButton)
        OpenSearchDialog.setTabOrder(self.addButton, self.deleteButton)
        OpenSearchDialog.setTabOrder(self.deleteButton, self.editButton)
        OpenSearchDialog.setTabOrder(self.editButton, self.restoreButton)
        OpenSearchDialog.setTabOrder(self.restoreButton, self.buttonBox)

    def retranslateUi(self, OpenSearchDialog):
        OpenSearchDialog.setWindowTitle(_translate("OpenSearchDialog", "Open Search Engines Configuration", None))
        self.addButton.setToolTip(_translate("OpenSearchDialog", "Press to add a new search engine from file", None))
        self.addButton.setText(_translate("OpenSearchDialog", "&Add...", None))
        self.deleteButton.setToolTip(_translate("OpenSearchDialog", "Press to delete the selected engines", None))
        self.deleteButton.setText(_translate("OpenSearchDialog", "&Delete", None))
        self.editButton.setToolTip(_translate("OpenSearchDialog", "Press to edit the data of the current engine", None))
        self.editButton.setText(_translate("OpenSearchDialog", "Edit...", None))
        self.restoreButton.setToolTip(_translate("OpenSearchDialog", "Press to restore the default engines", None))
        self.restoreButton.setText(_translate("OpenSearchDialog", "&Restore Defaults", None))

from E4Gui.E4TableView import E4TableView
