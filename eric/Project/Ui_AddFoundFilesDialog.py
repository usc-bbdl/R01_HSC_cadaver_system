# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Project\AddFoundFilesDialog.ui'
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

class Ui_AddFoundFilesDialog(object):
    def setupUi(self, AddFoundFilesDialog):
        AddFoundFilesDialog.setObjectName(_fromUtf8("AddFoundFilesDialog"))
        AddFoundFilesDialog.resize(600, 480)
        AddFoundFilesDialog.setSizeGripEnabled(True)
        self.vboxlayout = QtGui.QVBoxLayout(AddFoundFilesDialog)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.fileList = QtGui.QListWidget(AddFoundFilesDialog)
        self.fileList.setAlternatingRowColors(True)
        self.fileList.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.fileList.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.fileList.setObjectName(_fromUtf8("fileList"))
        self.vboxlayout.addWidget(self.fileList)
        self.buttonBox = QtGui.QDialogButtonBox(AddFoundFilesDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(AddFoundFilesDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), AddFoundFilesDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(AddFoundFilesDialog)

    def retranslateUi(self, AddFoundFilesDialog):
        AddFoundFilesDialog.setWindowTitle(_translate("AddFoundFilesDialog", "Add found files to project", None))
        AddFoundFilesDialog.setToolTip(_translate("AddFoundFilesDialog", "Adds the found files to the current project.", None))
        self.fileList.setToolTip(_translate("AddFoundFilesDialog", "List of found files.", None))

