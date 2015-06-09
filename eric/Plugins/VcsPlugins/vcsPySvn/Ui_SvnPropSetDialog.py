# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Plugins\VcsPlugins\vcsPySvn\SvnPropSetDialog.ui'
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
        self.gridlayout = QtGui.QGridLayout()
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.propTextEdit = QtGui.QTextEdit(SvnPropSetDialog)
        self.propTextEdit.setTabChangesFocus(True)
        self.propTextEdit.setAcceptRichText(False)
        self.propTextEdit.setObjectName(_fromUtf8("propTextEdit"))
        self.gridlayout.addWidget(self.propTextEdit, 1, 1, 1, 1)
        self.textLabel1 = QtGui.QLabel(SvnPropSetDialog)
        self.textLabel1.setObjectName(_fromUtf8("textLabel1"))
        self.gridlayout.addWidget(self.textLabel1, 0, 0, 1, 1)
        self.propNameEdit = QtGui.QLineEdit(SvnPropSetDialog)
        self.propNameEdit.setObjectName(_fromUtf8("propNameEdit"))
        self.gridlayout.addWidget(self.propNameEdit, 0, 1, 1, 1)
        self.recurseCheckBox = QtGui.QCheckBox(SvnPropSetDialog)
        self.recurseCheckBox.setObjectName(_fromUtf8("recurseCheckBox"))
        self.gridlayout.addWidget(self.recurseCheckBox, 2, 0, 1, 2)
        self.label = QtGui.QLabel(SvnPropSetDialog)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridlayout.addWidget(self.label, 1, 0, 1, 1)
        self.vboxlayout.addLayout(self.gridlayout)
        self.buttonBox = QtGui.QDialogButtonBox(SvnPropSetDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.vboxlayout.addWidget(self.buttonBox)
        self.textLabel1.setBuddy(self.propNameEdit)
        self.label.setBuddy(self.propTextEdit)

        self.retranslateUi(SvnPropSetDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), SvnPropSetDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), SvnPropSetDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SvnPropSetDialog)
        SvnPropSetDialog.setTabOrder(self.propNameEdit, self.propTextEdit)
        SvnPropSetDialog.setTabOrder(self.propTextEdit, self.recurseCheckBox)

    def retranslateUi(self, SvnPropSetDialog):
        SvnPropSetDialog.setWindowTitle(_translate("SvnPropSetDialog", "Set Subversion Property", None))
        self.propTextEdit.setToolTip(_translate("SvnPropSetDialog", "Enter text of the property", None))
        self.textLabel1.setText(_translate("SvnPropSetDialog", "Property &Name:", None))
        self.propNameEdit.setToolTip(_translate("SvnPropSetDialog", "Enter the name of the property to be set", None))
        self.recurseCheckBox.setToolTip(_translate("SvnPropSetDialog", "Select to apply the property recursively", None))
        self.recurseCheckBox.setText(_translate("SvnPropSetDialog", "Apply &recursively", None))
        self.label.setText(_translate("SvnPropSetDialog", "Property &Value:", None))

