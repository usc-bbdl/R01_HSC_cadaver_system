# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Templates\TemplateSingleVariableDialog.ui'
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

class Ui_TemplateSingleVariableDialog(object):
    def setupUi(self, TemplateSingleVariableDialog):
        TemplateSingleVariableDialog.setObjectName(_fromUtf8("TemplateSingleVariableDialog"))
        TemplateSingleVariableDialog.resize(403, 218)
        TemplateSingleVariableDialog.setSizeGripEnabled(True)
        self.gridlayout = QtGui.QGridLayout(TemplateSingleVariableDialog)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.variableEdit = QtGui.QTextEdit(TemplateSingleVariableDialog)
        self.variableEdit.setLineWrapMode(QtGui.QTextEdit.NoWrap)
        self.variableEdit.setAcceptRichText(False)
        self.variableEdit.setObjectName(_fromUtf8("variableEdit"))
        self.gridlayout.addWidget(self.variableEdit, 0, 1, 1, 1)
        self.variableLabel = QtGui.QLabel(TemplateSingleVariableDialog)
        self.variableLabel.setAlignment(QtCore.Qt.AlignTop)
        self.variableLabel.setObjectName(_fromUtf8("variableLabel"))
        self.gridlayout.addWidget(self.variableLabel, 0, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(TemplateSingleVariableDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridlayout.addWidget(self.buttonBox, 1, 0, 1, 2)

        self.retranslateUi(TemplateSingleVariableDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), TemplateSingleVariableDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), TemplateSingleVariableDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(TemplateSingleVariableDialog)

    def retranslateUi(self, TemplateSingleVariableDialog):
        TemplateSingleVariableDialog.setWindowTitle(_translate("TemplateSingleVariableDialog", "Enter Template Variable", None))
        self.variableEdit.setToolTip(_translate("TemplateSingleVariableDialog", "Enter the value for the variable.", None))
        self.variableLabel.setText(_translate("TemplateSingleVariableDialog", "Variable:", None))

