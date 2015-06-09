# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\UI\ErrorLogDialog.ui'
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

class Ui_ErrorLogDialog(object):
    def setupUi(self, ErrorLogDialog):
        ErrorLogDialog.setObjectName(_fromUtf8("ErrorLogDialog"))
        ErrorLogDialog.resize(500, 350)
        ErrorLogDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtGui.QVBoxLayout(ErrorLogDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.icon = QtGui.QLabel(ErrorLogDialog)
        self.icon.setObjectName(_fromUtf8("icon"))
        self.horizontalLayout.addWidget(self.icon)
        self.label = QtGui.QLabel(ErrorLogDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.logEdit = QtGui.QPlainTextEdit(ErrorLogDialog)
        self.logEdit.setReadOnly(True)
        self.logEdit.setObjectName(_fromUtf8("logEdit"))
        self.verticalLayout.addWidget(self.logEdit)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.emailButton = QtGui.QPushButton(ErrorLogDialog)
        self.emailButton.setDefault(True)
        self.emailButton.setObjectName(_fromUtf8("emailButton"))
        self.horizontalLayout_2.addWidget(self.emailButton)
        self.deleteButton = QtGui.QPushButton(ErrorLogDialog)
        self.deleteButton.setObjectName(_fromUtf8("deleteButton"))
        self.horizontalLayout_2.addWidget(self.deleteButton)
        self.keepButton = QtGui.QPushButton(ErrorLogDialog)
        self.keepButton.setObjectName(_fromUtf8("keepButton"))
        self.horizontalLayout_2.addWidget(self.keepButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(ErrorLogDialog)
        QtCore.QMetaObject.connectSlotsByName(ErrorLogDialog)
        ErrorLogDialog.setTabOrder(self.logEdit, self.emailButton)
        ErrorLogDialog.setTabOrder(self.emailButton, self.deleteButton)
        ErrorLogDialog.setTabOrder(self.deleteButton, self.keepButton)

    def retranslateUi(self, ErrorLogDialog):
        ErrorLogDialog.setWindowTitle(_translate("ErrorLogDialog", "Error Log Found", None))
        self.label.setText(_translate("ErrorLogDialog", "<b>An error log file was found. What should be done with it?</b>", None))
        self.emailButton.setToolTip(_translate("ErrorLogDialog", "Press to send an email", None))
        self.emailButton.setText(_translate("ErrorLogDialog", "Send Bug Email", None))
        self.deleteButton.setToolTip(_translate("ErrorLogDialog", "Press to ignore the error and delete the log file", None))
        self.deleteButton.setText(_translate("ErrorLogDialog", "Ignore and Delete", None))
        self.keepButton.setToolTip(_translate("ErrorLogDialog", "Press to ignore the error but keep the log file", None))
        self.keepButton.setText(_translate("ErrorLogDialog", "Ignore but Keep", None))

