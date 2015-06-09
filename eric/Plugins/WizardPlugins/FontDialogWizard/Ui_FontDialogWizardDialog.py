# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Plugins\WizardPlugins\FontDialogWizard\FontDialogWizardDialog.ui'
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

class Ui_FontDialogWizardDialog(object):
    def setupUi(self, FontDialogWizardDialog):
        FontDialogWizardDialog.setObjectName(_fromUtf8("FontDialogWizardDialog"))
        FontDialogWizardDialog.resize(377, 118)
        FontDialogWizardDialog.setSizeGripEnabled(True)
        self.vboxlayout = QtGui.QVBoxLayout(FontDialogWizardDialog)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        spacerItem = QtGui.QSpacerItem(30, 0, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)
        self.fontButton = QtGui.QPushButton(FontDialogWizardDialog)
        self.fontButton.setObjectName(_fromUtf8("fontButton"))
        self.hboxlayout.addWidget(self.fontButton)
        spacerItem1 = QtGui.QSpacerItem(30, 0, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem1)
        self.vboxlayout.addLayout(self.hboxlayout)
        self.TextLabel1 = QtGui.QLabel(FontDialogWizardDialog)
        self.TextLabel1.setObjectName(_fromUtf8("TextLabel1"))
        self.vboxlayout.addWidget(self.TextLabel1)
        self.eVariable = QtGui.QLineEdit(FontDialogWizardDialog)
        self.eVariable.setObjectName(_fromUtf8("eVariable"))
        self.vboxlayout.addWidget(self.eVariable)
        self.buttonBox = QtGui.QDialogButtonBox(FontDialogWizardDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(FontDialogWizardDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), FontDialogWizardDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), FontDialogWizardDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(FontDialogWizardDialog)
        FontDialogWizardDialog.setTabOrder(self.fontButton, self.eVariable)

    def retranslateUi(self, FontDialogWizardDialog):
        FontDialogWizardDialog.setWindowTitle(_translate("FontDialogWizardDialog", "QFontDialog Wizard", None))
        self.fontButton.setToolTip(_translate("FontDialogWizardDialog", "Press to select a font via a dialog", None))
        self.fontButton.setText(_translate("FontDialogWizardDialog", "Select Font ...", None))
        self.TextLabel1.setText(_translate("FontDialogWizardDialog", "Variable", None))
        self.eVariable.setToolTip(_translate("FontDialogWizardDialog", "Enter a variable name", None))

