# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Plugins\VcsPlugins\vcsPySvn\SvnLoginDialog.ui'
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

class Ui_SvnLoginDialog(object):
    def setupUi(self, SvnLoginDialog):
        SvnLoginDialog.setObjectName(_fromUtf8("SvnLoginDialog"))
        SvnLoginDialog.resize(400, 145)
        SvnLoginDialog.setSizeGripEnabled(True)
        self.vboxlayout = QtGui.QVBoxLayout(SvnLoginDialog)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.gridlayout = QtGui.QGridLayout()
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.saveCheckBox = QtGui.QCheckBox(SvnLoginDialog)
        self.saveCheckBox.setObjectName(_fromUtf8("saveCheckBox"))
        self.gridlayout.addWidget(self.saveCheckBox, 3, 0, 1, 2)
        self.passwordEdit = QtGui.QLineEdit(SvnLoginDialog)
        self.passwordEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.passwordEdit.setObjectName(_fromUtf8("passwordEdit"))
        self.gridlayout.addWidget(self.passwordEdit, 2, 1, 1, 1)
        self.label_2 = QtGui.QLabel(SvnLoginDialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridlayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.label = QtGui.QLabel(SvnLoginDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridlayout.addWidget(self.label, 1, 0, 1, 1)
        self.realmLabel = QtGui.QLabel(SvnLoginDialog)
        self.realmLabel.setText(_fromUtf8(""))
        self.realmLabel.setObjectName(_fromUtf8("realmLabel"))
        self.gridlayout.addWidget(self.realmLabel, 0, 0, 1, 2)
        self.usernameEdit = QtGui.QLineEdit(SvnLoginDialog)
        self.usernameEdit.setObjectName(_fromUtf8("usernameEdit"))
        self.gridlayout.addWidget(self.usernameEdit, 1, 1, 1, 1)
        self.vboxlayout.addLayout(self.gridlayout)
        self.buttonBox = QtGui.QDialogButtonBox(SvnLoginDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(SvnLoginDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), SvnLoginDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), SvnLoginDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SvnLoginDialog)
        SvnLoginDialog.setTabOrder(self.usernameEdit, self.passwordEdit)
        SvnLoginDialog.setTabOrder(self.passwordEdit, self.saveCheckBox)

    def retranslateUi(self, SvnLoginDialog):
        SvnLoginDialog.setWindowTitle(_translate("SvnLoginDialog", "Subversion Login", None))
        self.saveCheckBox.setToolTip(_translate("SvnLoginDialog", "Select, if the login data should be saved.", None))
        self.saveCheckBox.setText(_translate("SvnLoginDialog", "Save login data", None))
        self.passwordEdit.setToolTip(_translate("SvnLoginDialog", "Enter password", None))
        self.label_2.setText(_translate("SvnLoginDialog", "Password:", None))
        self.label.setText(_translate("SvnLoginDialog", "Username:", None))
        self.usernameEdit.setToolTip(_translate("SvnLoginDialog", "Enter username", None))

