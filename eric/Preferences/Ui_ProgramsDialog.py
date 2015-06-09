# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Preferences\ProgramsDialog.ui'
#
# Created: Fri Apr 18 09:56:42 2014
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

class Ui_ProgramsDialog(object):
    def setupUi(self, ProgramsDialog):
        ProgramsDialog.setObjectName(_fromUtf8("ProgramsDialog"))
        ProgramsDialog.resize(700, 570)
        self.vboxlayout = QtGui.QVBoxLayout(ProgramsDialog)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.programsList = QtGui.QTreeWidget(ProgramsDialog)
        self.programsList.setRootIsDecorated(False)
        self.programsList.setObjectName(_fromUtf8("programsList"))
        self.vboxlayout.addWidget(self.programsList)
        self.buttonBox = QtGui.QDialogButtonBox(ProgramsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(ProgramsDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ProgramsDialog.close)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ProgramsDialog.close)
        QtCore.QMetaObject.connectSlotsByName(ProgramsDialog)

    def retranslateUi(self, ProgramsDialog):
        ProgramsDialog.setWindowTitle(_translate("ProgramsDialog", "External Programs", None))
        self.programsList.setSortingEnabled(True)
        self.programsList.headerItem().setText(0, _translate("ProgramsDialog", "Path", None))
        self.programsList.headerItem().setText(1, _translate("ProgramsDialog", "Version", None))

