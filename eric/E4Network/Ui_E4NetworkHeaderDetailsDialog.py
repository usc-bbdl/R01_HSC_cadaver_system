# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\E4Network\E4NetworkHeaderDetailsDialog.ui'
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

class Ui_E4NetworkHeaderDetailsDialog(object):
    def setupUi(self, E4NetworkHeaderDetailsDialog):
        E4NetworkHeaderDetailsDialog.setObjectName(_fromUtf8("E4NetworkHeaderDetailsDialog"))
        E4NetworkHeaderDetailsDialog.resize(500, 350)
        E4NetworkHeaderDetailsDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtGui.QVBoxLayout(E4NetworkHeaderDetailsDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(E4NetworkHeaderDetailsDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.nameEdit = QtGui.QLineEdit(E4NetworkHeaderDetailsDialog)
        self.nameEdit.setReadOnly(True)
        self.nameEdit.setObjectName(_fromUtf8("nameEdit"))
        self.verticalLayout.addWidget(self.nameEdit)
        self.label_2 = QtGui.QLabel(E4NetworkHeaderDetailsDialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.valueEdit = QtGui.QPlainTextEdit(E4NetworkHeaderDetailsDialog)
        self.valueEdit.setTabChangesFocus(True)
        self.valueEdit.setReadOnly(True)
        self.valueEdit.setObjectName(_fromUtf8("valueEdit"))
        self.verticalLayout.addWidget(self.valueEdit)
        self.buttonBox = QtGui.QDialogButtonBox(E4NetworkHeaderDetailsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(E4NetworkHeaderDetailsDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), E4NetworkHeaderDetailsDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), E4NetworkHeaderDetailsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(E4NetworkHeaderDetailsDialog)

    def retranslateUi(self, E4NetworkHeaderDetailsDialog):
        E4NetworkHeaderDetailsDialog.setWindowTitle(_translate("E4NetworkHeaderDetailsDialog", "Header Details", None))
        self.label.setText(_translate("E4NetworkHeaderDetailsDialog", "Name:", None))
        self.label_2.setText(_translate("E4NetworkHeaderDetailsDialog", "Value:", None))

