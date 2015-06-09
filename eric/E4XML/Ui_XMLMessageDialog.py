# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\E4XML\XMLMessageDialog.ui'
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

class Ui_XMLMessageDialog(object):
    def setupUi(self, XMLMessageDialog):
        XMLMessageDialog.setObjectName(_fromUtf8("XMLMessageDialog"))
        XMLMessageDialog.resize(567, 253)
        XMLMessageDialog.setSizeGripEnabled(True)
        self.vboxlayout = QtGui.QVBoxLayout(XMLMessageDialog)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.messages = QtGui.QTextEdit(XMLMessageDialog)
        self.messages.setReadOnly(True)
        self.messages.setObjectName(_fromUtf8("messages"))
        self.vboxlayout.addWidget(self.messages)
        self.buttonBox = QtGui.QDialogButtonBox(XMLMessageDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(XMLMessageDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), XMLMessageDialog.accept)
        QtCore.QMetaObject.connectSlotsByName(XMLMessageDialog)

    def retranslateUi(self, XMLMessageDialog):
        XMLMessageDialog.setWindowTitle(_translate("XMLMessageDialog", "XML Parse Messages", None))

