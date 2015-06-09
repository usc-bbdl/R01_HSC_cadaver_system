# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Plugins\VcsPlugins\vcsSubversion\SvnPropSetDialog.ui'
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

class Ui_SvnPropSetDialog(object):
    def setupUi(self, SvnPropSetDialog):
        SvnPropSetDialog.setObjectName(_fromUtf8("SvnPropSetDialog"))
        SvnPropSetDialog.resize(494, 385)
        SvnPropSetDialog.setSizeGripEnabled(True)
        self.vboxlayout = QtGui.QVBoxLayout(SvnPropSetDialog)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        self.textLabel1 = QtGui.QLabel(SvnPropSetDialog)
        self.textLabel1.setObjectName(_fromUtf8("textLabel1"))
        self.hboxlayout.addWidget(self.textLabel1)
        self.propNameEdit = QtGui.QLineEdit(SvnPropSetDialog)
        self.propNameEdit.setObjectName(_fromUtf8("propNameEdit"))
        self.hboxlayout.addWidget(self.propNameEdit)
        self.vboxlayout.addLayout(self.hboxlayout)
        self.groupBox = QtGui.QGroupBox(SvnPropSetDialog)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridlayout = QtGui.QGridLayout(self.groupBox)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.fileRadioButton = QtGui.QRadioButton(self.groupBox)
        self.fileRadioButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.fileRadioButton.setObjectName(_fromUtf8("fileRadioButton"))
        self.gridlayout.addWidget(self.fileRadioButton, 2, 0, 1, 2)
        self.textRadioButton = QtGui.QRadioButton(self.groupBox)
        self.textRadioButton.setChecked(True)
        self.textRadioButton.setObjectName(_fromUtf8("textRadioButton"))
        self.gridlayout.addWidget(self.textRadioButton, 0, 0, 1, 2)
        self.propTextEdit = QtGui.QTextEdit(self.groupBox)
        self.propTextEdit.setTabChangesFocus(True)
        self.propTextEdit.setAcceptRichText(False)
        self.propTextEdit.setObjectName(_fromUtf8("propTextEdit"))
        self.gridlayout.addWidget(self.propTextEdit, 1, 0, 1, 2)
        self.fileButton = QtGui.QPushButton(self.groupBox)
        self.fileButton.setEnabled(False)
        self.fileButton.setObjectName(_fromUtf8("fileButton"))
        self.gridlayout.addWidget(self.fileButton, 3, 1, 1, 1)
        self.propFileEdit = QtGui.QLineEdit(self.groupBox)
        self.propFileEdit.setEnabled(False)
        self.propFileEdit.setObjectName(_fromUtf8("propFileEdit"))
        self.gridlayout.addWidget(self.propFileEdit, 3, 0, 1, 1)
        self.vboxlayout.addWidget(self.groupBox)
        self.buttonBox = QtGui.QDialogButtonBox(SvnPropSetDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(SvnPropSetDialog)
        QtCore.QObject.connect(self.textRadioButton, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.propTextEdit.setEnabled)
        QtCore.QObject.connect(self.fileRadioButton, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.propFileEdit.setEnabled)
        QtCore.QObject.connect(self.fileRadioButton, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.fileButton.setEnabled)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), SvnPropSetDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), SvnPropSetDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SvnPropSetDialog)
        SvnPropSetDialog.setTabOrder(self.propNameEdit, self.textRadioButton)
        SvnPropSetDialog.setTabOrder(self.textRadioButton, self.propTextEdit)
        SvnPropSetDialog.setTabOrder(self.propTextEdit, self.propFileEdit)
        SvnPropSetDialog.setTabOrder(self.propFileEdit, self.fileButton)

    def retranslateUi(self, SvnPropSetDialog):
        SvnPropSetDialog.setWindowTitle(_translate("SvnPropSetDialog", "Set Subversion Property", None))
        self.textLabel1.setText(_translate("SvnPropSetDialog", "Property Name:", None))
        self.propNameEdit.setToolTip(_translate("SvnPropSetDialog", "Enter the name of the property to be set", None))
        self.groupBox.setTitle(_translate("SvnPropSetDialog", "Select property source", None))
        self.fileRadioButton.setText(_translate("SvnPropSetDialog", "File", None))
        self.textRadioButton.setText(_translate("SvnPropSetDialog", "Text", None))
        self.propTextEdit.setToolTip(_translate("SvnPropSetDialog", "Enter text of the property", None))
        self.fileButton.setToolTip(_translate("SvnPropSetDialog", "Press to select the file via a file selection dialog", None))
        self.fileButton.setText(_translate("SvnPropSetDialog", "...", None))
        self.propFileEdit.setToolTip(_translate("SvnPropSetDialog", "Enter the name of a file for the property", None))

