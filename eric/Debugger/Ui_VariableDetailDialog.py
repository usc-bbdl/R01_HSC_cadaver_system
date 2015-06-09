# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Debugger\VariableDetailDialog.ui'
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

class Ui_VariableDetailDialog(object):
    def setupUi(self, VariableDetailDialog):
        VariableDetailDialog.setObjectName(_fromUtf8("VariableDetailDialog"))
        VariableDetailDialog.resize(800, 350)
        VariableDetailDialog.setSizeGripEnabled(True)
        VariableDetailDialog.setModal(True)
        self.gridlayout = QtGui.QGridLayout(VariableDetailDialog)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.buttonBox = QtGui.QDialogButtonBox(VariableDetailDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridlayout.addWidget(self.buttonBox, 3, 0, 1, 2)
        self.TextLabel1 = QtGui.QLabel(VariableDetailDialog)
        self.TextLabel1.setObjectName(_fromUtf8("TextLabel1"))
        self.gridlayout.addWidget(self.TextLabel1, 0, 0, 1, 1)
        self.eType = QtGui.QLineEdit(VariableDetailDialog)
        self.eType.setReadOnly(True)
        self.eType.setObjectName(_fromUtf8("eType"))
        self.gridlayout.addWidget(self.eType, 1, 1, 1, 1)
        self.eName = QtGui.QLineEdit(VariableDetailDialog)
        self.eName.setReadOnly(True)
        self.eName.setObjectName(_fromUtf8("eName"))
        self.gridlayout.addWidget(self.eName, 0, 1, 1, 1)
        self.TextLabel2 = QtGui.QLabel(VariableDetailDialog)
        self.TextLabel2.setObjectName(_fromUtf8("TextLabel2"))
        self.gridlayout.addWidget(self.TextLabel2, 1, 0, 1, 1)
        self.TextLabel3 = QtGui.QLabel(VariableDetailDialog)
        self.TextLabel3.setAlignment(QtCore.Qt.AlignTop)
        self.TextLabel3.setObjectName(_fromUtf8("TextLabel3"))
        self.gridlayout.addWidget(self.TextLabel3, 2, 0, 1, 1)
        self.eValue = QtGui.QTextEdit(VariableDetailDialog)
        self.eValue.setReadOnly(True)
        self.eValue.setAcceptRichText(False)
        self.eValue.setObjectName(_fromUtf8("eValue"))
        self.gridlayout.addWidget(self.eValue, 2, 1, 1, 1)

        self.retranslateUi(VariableDetailDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), VariableDetailDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), VariableDetailDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(VariableDetailDialog)
        VariableDetailDialog.setTabOrder(self.eName, self.eType)
        VariableDetailDialog.setTabOrder(self.eType, self.eValue)

    def retranslateUi(self, VariableDetailDialog):
        VariableDetailDialog.setWindowTitle(_translate("VariableDetailDialog", "Variable Details", None))
        self.TextLabel1.setText(_translate("VariableDetailDialog", "Name:", None))
        self.TextLabel2.setText(_translate("VariableDetailDialog", "Type:", None))
        self.TextLabel3.setText(_translate("VariableDetailDialog", "Value:", None))

