# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\UI\EmailDialog.ui'
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

class Ui_EmailDialog(object):
    def setupUi(self, EmailDialog):
        EmailDialog.setObjectName(_fromUtf8("EmailDialog"))
        EmailDialog.resize(600, 547)
        EmailDialog.setSizeGripEnabled(True)
        self.verticalLayout_2 = QtGui.QVBoxLayout(EmailDialog)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.mainSplitter = QtGui.QSplitter(EmailDialog)
        self.mainSplitter.setOrientation(QtCore.Qt.Vertical)
        self.mainSplitter.setObjectName(_fromUtf8("mainSplitter"))
        self.messageGroup = QtGui.QGroupBox(self.mainSplitter)
        self.messageGroup.setObjectName(_fromUtf8("messageGroup"))
        self.verticalLayout = QtGui.QVBoxLayout(self.messageGroup)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        self.textLabel1 = QtGui.QLabel(self.messageGroup)
        self.textLabel1.setObjectName(_fromUtf8("textLabel1"))
        self.hboxlayout.addWidget(self.textLabel1)
        self.subject = QtGui.QLineEdit(self.messageGroup)
        self.subject.setObjectName(_fromUtf8("subject"))
        self.hboxlayout.addWidget(self.subject)
        self.verticalLayout.addLayout(self.hboxlayout)
        self.msgLabel = QtGui.QLabel(self.messageGroup)
        self.msgLabel.setObjectName(_fromUtf8("msgLabel"))
        self.verticalLayout.addWidget(self.msgLabel)
        self.message = QtGui.QTextEdit(self.messageGroup)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.message.sizePolicy().hasHeightForWidth())
        self.message.setSizePolicy(sizePolicy)
        self.message.setLineWrapMode(QtGui.QTextEdit.FixedColumnWidth)
        self.message.setLineWrapColumnOrWidth(70)
        self.message.setTabStopWidth(8)
        self.message.setAcceptRichText(False)
        self.message.setObjectName(_fromUtf8("message"))
        self.verticalLayout.addWidget(self.message)
        self.attachmentsGroup = QtGui.QGroupBox(self.mainSplitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.attachmentsGroup.sizePolicy().hasHeightForWidth())
        self.attachmentsGroup.setSizePolicy(sizePolicy)
        self.attachmentsGroup.setObjectName(_fromUtf8("attachmentsGroup"))
        self.gridLayout = QtGui.QGridLayout(self.attachmentsGroup)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.attachments = QtGui.QTreeWidget(self.attachmentsGroup)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.attachments.sizePolicy().hasHeightForWidth())
        self.attachments.setSizePolicy(sizePolicy)
        self.attachments.setAlternatingRowColors(True)
        self.attachments.setRootIsDecorated(False)
        self.attachments.setObjectName(_fromUtf8("attachments"))
        self.gridLayout.addWidget(self.attachments, 0, 0, 1, 1)
        self.vboxlayout = QtGui.QVBoxLayout()
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.addButton = QtGui.QPushButton(self.attachmentsGroup)
        self.addButton.setObjectName(_fromUtf8("addButton"))
        self.vboxlayout.addWidget(self.addButton)
        self.deleteButton = QtGui.QPushButton(self.attachmentsGroup)
        self.deleteButton.setObjectName(_fromUtf8("deleteButton"))
        self.vboxlayout.addWidget(self.deleteButton)
        spacerItem = QtGui.QSpacerItem(20, 16, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vboxlayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.vboxlayout, 0, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.mainSplitter)
        self.buttonBox = QtGui.QDialogButtonBox(EmailDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_2.addWidget(self.buttonBox)
        self.textLabel1.setBuddy(self.subject)
        self.msgLabel.setBuddy(self.message)

        self.retranslateUi(EmailDialog)
        QtCore.QMetaObject.connectSlotsByName(EmailDialog)
        EmailDialog.setTabOrder(self.subject, self.message)
        EmailDialog.setTabOrder(self.message, self.addButton)
        EmailDialog.setTabOrder(self.addButton, self.attachments)
        EmailDialog.setTabOrder(self.attachments, self.deleteButton)

    def retranslateUi(self, EmailDialog):
        EmailDialog.setWindowTitle(_translate("EmailDialog", "Send bug report", None))
        self.messageGroup.setTitle(_translate("EmailDialog", "Message", None))
        self.textLabel1.setText(_translate("EmailDialog", "&Subject:", None))
        self.subject.setToolTip(_translate("EmailDialog", "Enter the subject", None))
        self.attachmentsGroup.setTitle(_translate("EmailDialog", "Attachments", None))
        self.attachments.headerItem().setText(0, _translate("EmailDialog", "Name", None))
        self.attachments.headerItem().setText(1, _translate("EmailDialog", "Type", None))
        self.addButton.setToolTip(_translate("EmailDialog", "Press to add an attachment", None))
        self.addButton.setText(_translate("EmailDialog", "&Add...", None))
        self.addButton.setShortcut(_translate("EmailDialog", "Alt+A", None))
        self.deleteButton.setToolTip(_translate("EmailDialog", "Delete the selected entry from the list of attachments", None))
        self.deleteButton.setText(_translate("EmailDialog", "&Delete", None))
        self.deleteButton.setShortcut(_translate("EmailDialog", "Alt+D", None))

