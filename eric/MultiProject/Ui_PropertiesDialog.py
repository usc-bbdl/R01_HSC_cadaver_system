# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\MultiProject\PropertiesDialog.ui'
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

class Ui_PropertiesDialog(object):
    def setupUi(self, PropertiesDialog):
        PropertiesDialog.setObjectName(_fromUtf8("PropertiesDialog"))
        PropertiesDialog.resize(530, 227)
        PropertiesDialog.setSizeGripEnabled(True)
        self.vboxlayout = QtGui.QVBoxLayout(PropertiesDialog)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.gridlayout = QtGui.QGridLayout()
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.descriptionLabel = QtGui.QLabel(PropertiesDialog)
        self.descriptionLabel.setAlignment(QtCore.Qt.AlignTop)
        self.descriptionLabel.setObjectName(_fromUtf8("descriptionLabel"))
        self.gridlayout.addWidget(self.descriptionLabel, 0, 0, 1, 1)
        self.descriptionEdit = QtGui.QTextEdit(PropertiesDialog)
        self.descriptionEdit.setTabChangesFocus(True)
        self.descriptionEdit.setAcceptRichText(False)
        self.descriptionEdit.setObjectName(_fromUtf8("descriptionEdit"))
        self.gridlayout.addWidget(self.descriptionEdit, 0, 1, 1, 1)
        self.vboxlayout.addLayout(self.gridlayout)
        self.buttonBox = QtGui.QDialogButtonBox(PropertiesDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.vboxlayout.addWidget(self.buttonBox)
        self.descriptionLabel.setBuddy(self.descriptionEdit)

        self.retranslateUi(PropertiesDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), PropertiesDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), PropertiesDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(PropertiesDialog)
        PropertiesDialog.setTabOrder(self.descriptionEdit, self.buttonBox)

    def retranslateUi(self, PropertiesDialog):
        PropertiesDialog.setWindowTitle(_translate("PropertiesDialog", "Multiproject Properties", None))
        self.descriptionLabel.setText(_translate("PropertiesDialog", "&Description:", None))
        self.descriptionEdit.setToolTip(_translate("PropertiesDialog", "Enter description", None))
        self.descriptionEdit.setWhatsThis(_translate("PropertiesDialog", "<b>Description</b>\n"
"<p>Enter a short description for the multiproject.</p>", None))

