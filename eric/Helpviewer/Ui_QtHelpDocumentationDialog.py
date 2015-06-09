# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Helpviewer\QtHelpDocumentationDialog.ui'
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

class Ui_QtHelpDocumentationDialog(object):
    def setupUi(self, QtHelpDocumentationDialog):
        QtHelpDocumentationDialog.setObjectName(_fromUtf8("QtHelpDocumentationDialog"))
        QtHelpDocumentationDialog.resize(425, 391)
        QtHelpDocumentationDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtGui.QVBoxLayout(QtHelpDocumentationDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(QtHelpDocumentationDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.documentsList = QtGui.QListWidget(QtHelpDocumentationDialog)
        self.documentsList.setToolTip(_fromUtf8(""))
        self.documentsList.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.documentsList.setObjectName(_fromUtf8("documentsList"))
        self.gridLayout.addWidget(self.documentsList, 0, 0, 3, 1)
        self.addButton = QtGui.QPushButton(QtHelpDocumentationDialog)
        self.addButton.setObjectName(_fromUtf8("addButton"))
        self.gridLayout.addWidget(self.addButton, 0, 1, 1, 1)
        self.removeButton = QtGui.QPushButton(QtHelpDocumentationDialog)
        self.removeButton.setObjectName(_fromUtf8("removeButton"))
        self.gridLayout.addWidget(self.removeButton, 1, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 98, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.buttonBox = QtGui.QDialogButtonBox(QtHelpDocumentationDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(QtHelpDocumentationDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), QtHelpDocumentationDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), QtHelpDocumentationDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(QtHelpDocumentationDialog)
        QtHelpDocumentationDialog.setTabOrder(self.documentsList, self.addButton)
        QtHelpDocumentationDialog.setTabOrder(self.addButton, self.removeButton)
        QtHelpDocumentationDialog.setTabOrder(self.removeButton, self.buttonBox)

    def retranslateUi(self, QtHelpDocumentationDialog):
        QtHelpDocumentationDialog.setWindowTitle(_translate("QtHelpDocumentationDialog", "Manage QtHelp Documentation Database", None))
        self.label.setText(_translate("QtHelpDocumentationDialog", "Registered Documents", None))
        self.addButton.setToolTip(_translate("QtHelpDocumentationDialog", "Press to select QtHelp documents to add to the database", None))
        self.addButton.setText(_translate("QtHelpDocumentationDialog", "Add...", None))
        self.removeButton.setToolTip(_translate("QtHelpDocumentationDialog", "Press to remove the selected documents from the database", None))
        self.removeButton.setText(_translate("QtHelpDocumentationDialog", "Remove", None))

