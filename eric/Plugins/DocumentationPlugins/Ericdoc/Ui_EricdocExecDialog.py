# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Plugins\DocumentationPlugins\Ericdoc\EricdocExecDialog.ui'
#
# Created: Fri Apr 18 09:56:41 2014
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

class Ui_EricdocExecDialog(object):
    def setupUi(self, EricdocExecDialog):
        EricdocExecDialog.setObjectName(_fromUtf8("EricdocExecDialog"))
        EricdocExecDialog.resize(753, 602)
        EricdocExecDialog.setSizeGripEnabled(True)
        self.verticalLayout_3 = QtGui.QVBoxLayout(EricdocExecDialog)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.messagesGroup = QtGui.QGroupBox(EricdocExecDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.messagesGroup.sizePolicy().hasHeightForWidth())
        self.messagesGroup.setSizePolicy(sizePolicy)
        self.messagesGroup.setObjectName(_fromUtf8("messagesGroup"))
        self.verticalLayout = QtGui.QVBoxLayout(self.messagesGroup)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.contents = QtGui.QTextBrowser(self.messagesGroup)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.contents.sizePolicy().hasHeightForWidth())
        self.contents.setSizePolicy(sizePolicy)
        self.contents.setObjectName(_fromUtf8("contents"))
        self.verticalLayout.addWidget(self.contents)
        self.verticalLayout_3.addWidget(self.messagesGroup)
        self.errorGroup = QtGui.QGroupBox(EricdocExecDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.errorGroup.sizePolicy().hasHeightForWidth())
        self.errorGroup.setSizePolicy(sizePolicy)
        self.errorGroup.setObjectName(_fromUtf8("errorGroup"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.errorGroup)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.errors = QtGui.QTextBrowser(self.errorGroup)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.errors.sizePolicy().hasHeightForWidth())
        self.errors.setSizePolicy(sizePolicy)
        self.errors.setObjectName(_fromUtf8("errors"))
        self.verticalLayout_2.addWidget(self.errors)
        self.verticalLayout_3.addWidget(self.errorGroup)
        self.buttonBox = QtGui.QDialogButtonBox(EricdocExecDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_3.addWidget(self.buttonBox)

        self.retranslateUi(EricdocExecDialog)
        QtCore.QMetaObject.connectSlotsByName(EricdocExecDialog)
        EricdocExecDialog.setTabOrder(self.contents, self.errors)
        EricdocExecDialog.setTabOrder(self.errors, self.buttonBox)

    def retranslateUi(self, EricdocExecDialog):
        EricdocExecDialog.setWindowTitle(_translate("EricdocExecDialog", "Ericdoc", None))
        self.messagesGroup.setTitle(_translate("EricdocExecDialog", "Messages", None))
        self.contents.setWhatsThis(_translate("EricdocExecDialog", "<b>Ericdoc Execution</b>\n"
"<p>This shows the output of the Ericdoc generator command.</p>", None))
        self.errorGroup.setTitle(_translate("EricdocExecDialog", "Errors", None))
        self.errors.setWhatsThis(_translate("EricdocExecDialog", "<b>Ericdoc Execution</b>\n"
"<p>This shows the errors of the Ericdoc generator command.</p>", None))

