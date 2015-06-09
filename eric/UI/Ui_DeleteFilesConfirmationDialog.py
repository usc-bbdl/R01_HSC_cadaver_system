# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\UI\DeleteFilesConfirmationDialog.ui'
#
# Created: Fri Apr 18 09:56:43 2014
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

class Ui_DeleteFilesConfirmationDialog(object):
    def setupUi(self, DeleteFilesConfirmationDialog):
        DeleteFilesConfirmationDialog.setObjectName(_fromUtf8("DeleteFilesConfirmationDialog"))
        DeleteFilesConfirmationDialog.resize(458, 288)
        DeleteFilesConfirmationDialog.setWindowTitle(_fromUtf8(""))
        DeleteFilesConfirmationDialog.setSizeGripEnabled(True)
        self.vboxlayout = QtGui.QVBoxLayout(DeleteFilesConfirmationDialog)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.message = QtGui.QLabel(DeleteFilesConfirmationDialog)
        self.message.setAlignment(QtCore.Qt.AlignVCenter)
        self.message.setObjectName(_fromUtf8("message"))
        self.vboxlayout.addWidget(self.message)
        self.filesList = QtGui.QListWidget(DeleteFilesConfirmationDialog)
        self.filesList.setFocusPolicy(QtCore.Qt.NoFocus)
        self.filesList.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.filesList.setObjectName(_fromUtf8("filesList"))
        self.vboxlayout.addWidget(self.filesList)
        self.buttonBox = QtGui.QDialogButtonBox(DeleteFilesConfirmationDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.No|QtGui.QDialogButtonBox.Yes)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(DeleteFilesConfirmationDialog)
        QtCore.QMetaObject.connectSlotsByName(DeleteFilesConfirmationDialog)

    def retranslateUi(self, DeleteFilesConfirmationDialog):
        self.message.setText(_translate("DeleteFilesConfirmationDialog", "Dummy", None))

