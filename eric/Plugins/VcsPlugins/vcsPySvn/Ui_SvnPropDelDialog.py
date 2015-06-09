# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Plugins\VcsPlugins\vcsPySvn\SvnPropDelDialog.ui'
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

class Ui_SvnPropDelDialog(object):
    def setupUi(self, SvnPropDelDialog):
        SvnPropDelDialog.setObjectName(_fromUtf8("SvnPropDelDialog"))
        SvnPropDelDialog.resize(494, 98)
        SvnPropDelDialog.setSizeGripEnabled(True)
        self.vboxlayout = QtGui.QVBoxLayout(SvnPropDelDialog)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.gridlayout = QtGui.QGridLayout()
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.propNameEdit = QtGui.QLineEdit(SvnPropDelDialog)
        self.propNameEdit.setObjectName(_fromUtf8("propNameEdit"))
        self.gridlayout.addWidget(self.propNameEdit, 0, 1, 1, 1)
        self.recurseCheckBox = QtGui.QCheckBox(SvnPropDelDialog)
        self.recurseCheckBox.setObjectName(_fromUtf8("recurseCheckBox"))
        self.gridlayout.addWidget(self.recurseCheckBox, 1, 0, 1, 2)
        self.textLabel1 = QtGui.QLabel(SvnPropDelDialog)
        self.textLabel1.setObjectName(_fromUtf8("textLabel1"))
        self.gridlayout.addWidget(self.textLabel1, 0, 0, 1, 1)
        self.vboxlayout.addLayout(self.gridlayout)
        self.buttonBox = QtGui.QDialogButtonBox(SvnPropDelDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.vboxlayout.addWidget(self.buttonBox)
        self.textLabel1.setBuddy(self.propNameEdit)

        self.retranslateUi(SvnPropDelDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), SvnPropDelDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), SvnPropDelDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SvnPropDelDialog)
        SvnPropDelDialog.setTabOrder(self.propNameEdit, self.recurseCheckBox)

    def retranslateUi(self, SvnPropDelDialog):
        SvnPropDelDialog.setWindowTitle(_translate("SvnPropDelDialog", "Delete Subversion Property", None))
        self.propNameEdit.setToolTip(_translate("SvnPropDelDialog", "Enter the name of the property to be deleted", None))
        self.recurseCheckBox.setToolTip(_translate("SvnPropDelDialog", "Select to apply the property recursively", None))
        self.recurseCheckBox.setText(_translate("SvnPropDelDialog", "Apply &recursively", None))
        self.textLabel1.setText(_translate("SvnPropDelDialog", "Property &Name:", None))

