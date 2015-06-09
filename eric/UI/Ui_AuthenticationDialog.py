# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\UI\AuthenticationDialog.ui'
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

class Ui_AuthenticationDialog(object):
    def setupUi(self, AuthenticationDialog):
        AuthenticationDialog.setObjectName(_fromUtf8("AuthenticationDialog"))
        AuthenticationDialog.resize(400, 154)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AuthenticationDialog.sizePolicy().hasHeightForWidth())
        AuthenticationDialog.setSizePolicy(sizePolicy)
        AuthenticationDialog.setSizeGripEnabled(True)
        self.gridLayout = QtGui.QGridLayout(AuthenticationDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.iconLabel = QtGui.QLabel(AuthenticationDialog)
        self.iconLabel.setObjectName(_fromUtf8("iconLabel"))
        self.horizontalLayout.addWidget(self.iconLabel)
        self.infoLabel = QtGui.QLabel(AuthenticationDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.infoLabel.sizePolicy().hasHeightForWidth())
        self.infoLabel.setSizePolicy(sizePolicy)
        self.infoLabel.setWordWrap(True)
        self.infoLabel.setObjectName(_fromUtf8("infoLabel"))
        self.horizontalLayout.addWidget(self.infoLabel)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 2)
        self.label = QtGui.QLabel(AuthenticationDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.usernameEdit = QtGui.QLineEdit(AuthenticationDialog)
        self.usernameEdit.setObjectName(_fromUtf8("usernameEdit"))
        self.gridLayout.addWidget(self.usernameEdit, 1, 1, 1, 1)
        self.label_2 = QtGui.QLabel(AuthenticationDialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.passwordEdit = QtGui.QLineEdit(AuthenticationDialog)
        self.passwordEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.passwordEdit.setObjectName(_fromUtf8("passwordEdit"))
        self.gridLayout.addWidget(self.passwordEdit, 2, 1, 1, 1)
        self.saveCheckBox = QtGui.QCheckBox(AuthenticationDialog)
        self.saveCheckBox.setObjectName(_fromUtf8("saveCheckBox"))
        self.gridLayout.addWidget(self.saveCheckBox, 3, 0, 1, 2)
        self.buttonBox = QtGui.QDialogButtonBox(AuthenticationDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 4, 0, 1, 2)

        self.retranslateUi(AuthenticationDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), AuthenticationDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), AuthenticationDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(AuthenticationDialog)
        AuthenticationDialog.setTabOrder(self.usernameEdit, self.passwordEdit)
        AuthenticationDialog.setTabOrder(self.passwordEdit, self.saveCheckBox)
        AuthenticationDialog.setTabOrder(self.saveCheckBox, self.buttonBox)

    def retranslateUi(self, AuthenticationDialog):
        AuthenticationDialog.setWindowTitle(_translate("AuthenticationDialog", "Authentication Required", None))
        self.iconLabel.setText(_translate("AuthenticationDialog", "Icon", None))
        self.infoLabel.setText(_translate("AuthenticationDialog", "Info", None))
        self.label.setText(_translate("AuthenticationDialog", "Username:", None))
        self.usernameEdit.setToolTip(_translate("AuthenticationDialog", "Enter username", None))
        self.label_2.setText(_translate("AuthenticationDialog", "Password:", None))
        self.passwordEdit.setToolTip(_translate("AuthenticationDialog", "Enter password", None))
        self.saveCheckBox.setToolTip(_translate("AuthenticationDialog", "Select to save the login data", None))
        self.saveCheckBox.setText(_translate("AuthenticationDialog", "Save login data", None))

