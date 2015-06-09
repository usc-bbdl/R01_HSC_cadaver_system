# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\SqlBrowser\SqlConnectionDialog.ui'
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

class Ui_SqlConnectionDialog(object):
    def setupUi(self, SqlConnectionDialog):
        SqlConnectionDialog.setObjectName(_fromUtf8("SqlConnectionDialog"))
        SqlConnectionDialog.resize(400, 259)
        self.verticalLayout = QtGui.QVBoxLayout(SqlConnectionDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.textLabel2 = QtGui.QLabel(SqlConnectionDialog)
        self.textLabel2.setObjectName(_fromUtf8("textLabel2"))
        self.gridLayout.addWidget(self.textLabel2, 0, 0, 1, 1)
        self.driverCombo = QtGui.QComboBox(SqlConnectionDialog)
        self.driverCombo.setObjectName(_fromUtf8("driverCombo"))
        self.gridLayout.addWidget(self.driverCombo, 0, 1, 1, 2)
        self.textLabel3 = QtGui.QLabel(SqlConnectionDialog)
        self.textLabel3.setObjectName(_fromUtf8("textLabel3"))
        self.gridLayout.addWidget(self.textLabel3, 1, 0, 1, 1)
        self.databaseEdit = QtGui.QLineEdit(SqlConnectionDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.databaseEdit.sizePolicy().hasHeightForWidth())
        self.databaseEdit.setSizePolicy(sizePolicy)
        self.databaseEdit.setObjectName(_fromUtf8("databaseEdit"))
        self.gridLayout.addWidget(self.databaseEdit, 1, 1, 1, 2)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 1)
        self.databaseFileButton = QtGui.QPushButton(SqlConnectionDialog)
        self.databaseFileButton.setObjectName(_fromUtf8("databaseFileButton"))
        self.gridLayout.addWidget(self.databaseFileButton, 2, 2, 1, 1)
        self.textLabel4 = QtGui.QLabel(SqlConnectionDialog)
        self.textLabel4.setObjectName(_fromUtf8("textLabel4"))
        self.gridLayout.addWidget(self.textLabel4, 3, 0, 1, 1)
        self.usernameEdit = QtGui.QLineEdit(SqlConnectionDialog)
        self.usernameEdit.setObjectName(_fromUtf8("usernameEdit"))
        self.gridLayout.addWidget(self.usernameEdit, 3, 1, 1, 2)
        self.textLabel4_2 = QtGui.QLabel(SqlConnectionDialog)
        self.textLabel4_2.setObjectName(_fromUtf8("textLabel4_2"))
        self.gridLayout.addWidget(self.textLabel4_2, 4, 0, 1, 1)
        self.passwordEdit = QtGui.QLineEdit(SqlConnectionDialog)
        self.passwordEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.passwordEdit.setObjectName(_fromUtf8("passwordEdit"))
        self.gridLayout.addWidget(self.passwordEdit, 4, 1, 1, 2)
        self.textLabel5 = QtGui.QLabel(SqlConnectionDialog)
        self.textLabel5.setObjectName(_fromUtf8("textLabel5"))
        self.gridLayout.addWidget(self.textLabel5, 5, 0, 1, 1)
        self.hostnameEdit = QtGui.QLineEdit(SqlConnectionDialog)
        self.hostnameEdit.setObjectName(_fromUtf8("hostnameEdit"))
        self.gridLayout.addWidget(self.hostnameEdit, 5, 1, 1, 2)
        self.textLabel5_2 = QtGui.QLabel(SqlConnectionDialog)
        self.textLabel5_2.setObjectName(_fromUtf8("textLabel5_2"))
        self.gridLayout.addWidget(self.textLabel5_2, 6, 0, 1, 1)
        self.portSpinBox = QtGui.QSpinBox(SqlConnectionDialog)
        self.portSpinBox.setMinimum(-1)
        self.portSpinBox.setMaximum(65535)
        self.portSpinBox.setProperty("value", -1)
        self.portSpinBox.setObjectName(_fromUtf8("portSpinBox"))
        self.gridLayout.addWidget(self.portSpinBox, 6, 1, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout)
        self.buttonBox = QtGui.QDialogButtonBox(SqlConnectionDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        self.textLabel2.setBuddy(self.driverCombo)
        self.textLabel3.setBuddy(self.databaseEdit)
        self.textLabel4.setBuddy(self.usernameEdit)
        self.textLabel4_2.setBuddy(self.passwordEdit)
        self.textLabel5.setBuddy(self.hostnameEdit)
        self.textLabel5_2.setBuddy(self.portSpinBox)

        self.retranslateUi(SqlConnectionDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), SqlConnectionDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), SqlConnectionDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SqlConnectionDialog)
        SqlConnectionDialog.setTabOrder(self.driverCombo, self.databaseEdit)
        SqlConnectionDialog.setTabOrder(self.databaseEdit, self.databaseFileButton)
        SqlConnectionDialog.setTabOrder(self.databaseFileButton, self.usernameEdit)
        SqlConnectionDialog.setTabOrder(self.usernameEdit, self.passwordEdit)
        SqlConnectionDialog.setTabOrder(self.passwordEdit, self.hostnameEdit)
        SqlConnectionDialog.setTabOrder(self.hostnameEdit, self.portSpinBox)
        SqlConnectionDialog.setTabOrder(self.portSpinBox, self.buttonBox)

    def retranslateUi(self, SqlConnectionDialog):
        SqlConnectionDialog.setWindowTitle(_translate("SqlConnectionDialog", "Connect...", None))
        self.textLabel2.setText(_translate("SqlConnectionDialog", "D&river:", None))
        self.driverCombo.setToolTip(_translate("SqlConnectionDialog", "Select the database driver", None))
        self.textLabel3.setText(_translate("SqlConnectionDialog", "&Database Name:", None))
        self.databaseEdit.setToolTip(_translate("SqlConnectionDialog", "Enter the database name", None))
        self.databaseFileButton.setToolTip(_translate("SqlConnectionDialog", "Press to select a database file", None))
        self.databaseFileButton.setText(_translate("SqlConnectionDialog", "...", None))
        self.textLabel4.setText(_translate("SqlConnectionDialog", "&Username:", None))
        self.usernameEdit.setToolTip(_translate("SqlConnectionDialog", "Enter the user name", None))
        self.textLabel4_2.setText(_translate("SqlConnectionDialog", "&Password:", None))
        self.textLabel5.setText(_translate("SqlConnectionDialog", "&Hostname:", None))
        self.hostnameEdit.setToolTip(_translate("SqlConnectionDialog", "Enter the hostname", None))
        self.textLabel5_2.setText(_translate("SqlConnectionDialog", "P&ort:", None))
        self.portSpinBox.setToolTip(_translate("SqlConnectionDialog", "Enter the port number", None))
        self.portSpinBox.setSpecialValueText(_translate("SqlConnectionDialog", "Default", None))

