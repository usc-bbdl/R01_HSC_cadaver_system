# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Preferences\ConfigurationPages\EmailPage.ui'
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

class Ui_EmailPage(object):
    def setupUi(self, EmailPage):
        EmailPage.setObjectName(_fromUtf8("EmailPage"))
        EmailPage.resize(422, 512)
        self.verticalLayout = QtGui.QVBoxLayout(EmailPage)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.headerLabel = QtGui.QLabel(EmailPage)
        self.headerLabel.setObjectName(_fromUtf8("headerLabel"))
        self.verticalLayout.addWidget(self.headerLabel)
        self.line16 = QtGui.QFrame(EmailPage)
        self.line16.setFrameShape(QtGui.QFrame.HLine)
        self.line16.setFrameShadow(QtGui.QFrame.Sunken)
        self.line16.setFrameShape(QtGui.QFrame.HLine)
        self.line16.setFrameShadow(QtGui.QFrame.Sunken)
        self.line16.setObjectName(_fromUtf8("line16"))
        self.verticalLayout.addWidget(self.line16)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.textLabel2_2 = QtGui.QLabel(EmailPage)
        self.textLabel2_2.setObjectName(_fromUtf8("textLabel2_2"))
        self.gridLayout_2.addWidget(self.textLabel2_2, 0, 0, 1, 1)
        self.mailServerEdit = QtGui.QLineEdit(EmailPage)
        self.mailServerEdit.setObjectName(_fromUtf8("mailServerEdit"))
        self.gridLayout_2.addWidget(self.mailServerEdit, 0, 1, 1, 2)
        self.label = QtGui.QLabel(EmailPage)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
        self.portSpin = QtGui.QSpinBox(EmailPage)
        self.portSpin.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.portSpin.setMinimum(1)
        self.portSpin.setMaximum(65535)
        self.portSpin.setProperty("value", 25)
        self.portSpin.setObjectName(_fromUtf8("portSpin"))
        self.gridLayout_2.addWidget(self.portSpin, 1, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(118, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 1, 2, 1, 1)
        self.textLabel1_5 = QtGui.QLabel(EmailPage)
        self.textLabel1_5.setObjectName(_fromUtf8("textLabel1_5"))
        self.gridLayout_2.addWidget(self.textLabel1_5, 2, 0, 1, 1)
        self.emailEdit = QtGui.QLineEdit(EmailPage)
        self.emailEdit.setObjectName(_fromUtf8("emailEdit"))
        self.gridLayout_2.addWidget(self.emailEdit, 2, 1, 1, 2)
        self.textLabel1_6 = QtGui.QLabel(EmailPage)
        self.textLabel1_6.setAlignment(QtCore.Qt.AlignTop)
        self.textLabel1_6.setObjectName(_fromUtf8("textLabel1_6"))
        self.gridLayout_2.addWidget(self.textLabel1_6, 3, 0, 1, 1)
        self.signatureEdit = QtGui.QTextEdit(EmailPage)
        self.signatureEdit.setAcceptRichText(False)
        self.signatureEdit.setObjectName(_fromUtf8("signatureEdit"))
        self.gridLayout_2.addWidget(self.signatureEdit, 3, 1, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.useTlsCheckBox = QtGui.QCheckBox(EmailPage)
        self.useTlsCheckBox.setObjectName(_fromUtf8("useTlsCheckBox"))
        self.verticalLayout.addWidget(self.useTlsCheckBox)
        self.mailAuthenticationCheckBox = QtGui.QCheckBox(EmailPage)
        self.mailAuthenticationCheckBox.setObjectName(_fromUtf8("mailAuthenticationCheckBox"))
        self.verticalLayout.addWidget(self.mailAuthenticationCheckBox)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.textLabel1_15 = QtGui.QLabel(EmailPage)
        self.textLabel1_15.setEnabled(False)
        self.textLabel1_15.setObjectName(_fromUtf8("textLabel1_15"))
        self.gridLayout.addWidget(self.textLabel1_15, 0, 0, 1, 1)
        self.mailUserEdit = QtGui.QLineEdit(EmailPage)
        self.mailUserEdit.setEnabled(False)
        self.mailUserEdit.setObjectName(_fromUtf8("mailUserEdit"))
        self.gridLayout.addWidget(self.mailUserEdit, 0, 1, 1, 1)
        self.textLabel2_7 = QtGui.QLabel(EmailPage)
        self.textLabel2_7.setEnabled(False)
        self.textLabel2_7.setObjectName(_fromUtf8("textLabel2_7"))
        self.gridLayout.addWidget(self.textLabel2_7, 1, 0, 1, 1)
        self.mailPasswordEdit = QtGui.QLineEdit(EmailPage)
        self.mailPasswordEdit.setEnabled(False)
        self.mailPasswordEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.mailPasswordEdit.setObjectName(_fromUtf8("mailPasswordEdit"))
        self.gridLayout.addWidget(self.mailPasswordEdit, 1, 1, 1, 1)
        self.testButton = QtGui.QPushButton(EmailPage)
        self.testButton.setObjectName(_fromUtf8("testButton"))
        self.gridLayout.addWidget(self.testButton, 2, 0, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)

        self.retranslateUi(EmailPage)
        QtCore.QObject.connect(self.mailAuthenticationCheckBox, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.textLabel1_15.setEnabled)
        QtCore.QObject.connect(self.mailAuthenticationCheckBox, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.textLabel2_7.setEnabled)
        QtCore.QObject.connect(self.mailAuthenticationCheckBox, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.mailUserEdit.setEnabled)
        QtCore.QObject.connect(self.mailAuthenticationCheckBox, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.mailPasswordEdit.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(EmailPage)
        EmailPage.setTabOrder(self.mailServerEdit, self.portSpin)
        EmailPage.setTabOrder(self.portSpin, self.emailEdit)
        EmailPage.setTabOrder(self.emailEdit, self.signatureEdit)
        EmailPage.setTabOrder(self.signatureEdit, self.useTlsCheckBox)
        EmailPage.setTabOrder(self.useTlsCheckBox, self.mailAuthenticationCheckBox)
        EmailPage.setTabOrder(self.mailAuthenticationCheckBox, self.mailUserEdit)
        EmailPage.setTabOrder(self.mailUserEdit, self.mailPasswordEdit)

    def retranslateUi(self, EmailPage):
        self.headerLabel.setText(_translate("EmailPage", "<b>Configure Email</b>", None))
        self.textLabel2_2.setText(_translate("EmailPage", "Outgoing mail server (SMTP):", None))
        self.mailServerEdit.setToolTip(_translate("EmailPage", "Enter the address of your mail server", None))
        self.label.setText(_translate("EmailPage", "Outgoing mail server port:", None))
        self.portSpin.setToolTip(_translate("EmailPage", "Enter the port of the mail server", None))
        self.textLabel1_5.setText(_translate("EmailPage", "Email address:", None))
        self.emailEdit.setToolTip(_translate("EmailPage", "Enter your email address", None))
        self.textLabel1_6.setText(_translate("EmailPage", "Signature:", None))
        self.signatureEdit.setToolTip(_translate("EmailPage", "Enter your email signature", None))
        self.useTlsCheckBox.setToolTip(_translate("EmailPage", "Select to use TLS", None))
        self.useTlsCheckBox.setText(_translate("EmailPage", "Use TLS", None))
        self.mailAuthenticationCheckBox.setToolTip(_translate("EmailPage", "Select to authenticatate against the mail server", None))
        self.mailAuthenticationCheckBox.setText(_translate("EmailPage", "Mail server needs authentication", None))
        self.textLabel1_15.setText(_translate("EmailPage", "Username:", None))
        self.mailUserEdit.setToolTip(_translate("EmailPage", "Enter your mail server username", None))
        self.textLabel2_7.setText(_translate("EmailPage", "Password:", None))
        self.mailPasswordEdit.setToolTip(_translate("EmailPage", "Enter your password for accessing the mail server", None))
        self.testButton.setToolTip(_translate("EmailPage", "Press to test the login data", None))
        self.testButton.setText(_translate("EmailPage", "Test Login", None))

