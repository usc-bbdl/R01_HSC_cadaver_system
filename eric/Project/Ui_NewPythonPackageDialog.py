# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Project\NewPythonPackageDialog.ui'
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

class Ui_NewPythonPackageDialog(object):
    def setupUi(self, NewPythonPackageDialog):
        NewPythonPackageDialog.setObjectName(_fromUtf8("NewPythonPackageDialog"))
        NewPythonPackageDialog.resize(400, 95)
        self.vboxlayout = QtGui.QVBoxLayout(NewPythonPackageDialog)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.label_2 = QtGui.QLabel(NewPythonPackageDialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.vboxlayout.addWidget(self.label_2)
        self.packageEdit = QtGui.QLineEdit(NewPythonPackageDialog)
        self.packageEdit.setObjectName(_fromUtf8("packageEdit"))
        self.vboxlayout.addWidget(self.packageEdit)
        self.buttonBox = QtGui.QDialogButtonBox(NewPythonPackageDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(NewPythonPackageDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), NewPythonPackageDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), NewPythonPackageDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(NewPythonPackageDialog)

    def retranslateUi(self, NewPythonPackageDialog):
        NewPythonPackageDialog.setWindowTitle(_translate("NewPythonPackageDialog", "Add new Python package", None))
        self.label_2.setText(_translate("NewPythonPackageDialog", "Enter the dotted name of the new package", None))
        self.packageEdit.setToolTip(_translate("NewPythonPackageDialog", "Enter the dotted package name", None))

