# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Helpviewer\HelpClearPrivateDataDialog.ui'
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

class Ui_HelpClearPrivateDataDialog(object):
    def setupUi(self, HelpClearPrivateDataDialog):
        HelpClearPrivateDataDialog.setObjectName(_fromUtf8("HelpClearPrivateDataDialog"))
        HelpClearPrivateDataDialog.resize(305, 191)
        HelpClearPrivateDataDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtGui.QVBoxLayout(HelpClearPrivateDataDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.historyCheckBox = QtGui.QCheckBox(HelpClearPrivateDataDialog)
        self.historyCheckBox.setChecked(True)
        self.historyCheckBox.setObjectName(_fromUtf8("historyCheckBox"))
        self.verticalLayout.addWidget(self.historyCheckBox)
        self.searchCheckBox = QtGui.QCheckBox(HelpClearPrivateDataDialog)
        self.searchCheckBox.setChecked(True)
        self.searchCheckBox.setObjectName(_fromUtf8("searchCheckBox"))
        self.verticalLayout.addWidget(self.searchCheckBox)
        self.cookiesCheckBox = QtGui.QCheckBox(HelpClearPrivateDataDialog)
        self.cookiesCheckBox.setChecked(True)
        self.cookiesCheckBox.setObjectName(_fromUtf8("cookiesCheckBox"))
        self.verticalLayout.addWidget(self.cookiesCheckBox)
        self.cacheCheckBox = QtGui.QCheckBox(HelpClearPrivateDataDialog)
        self.cacheCheckBox.setChecked(True)
        self.cacheCheckBox.setObjectName(_fromUtf8("cacheCheckBox"))
        self.verticalLayout.addWidget(self.cacheCheckBox)
        self.iconsCheckBox = QtGui.QCheckBox(HelpClearPrivateDataDialog)
        self.iconsCheckBox.setChecked(True)
        self.iconsCheckBox.setObjectName(_fromUtf8("iconsCheckBox"))
        self.verticalLayout.addWidget(self.iconsCheckBox)
        self.passwordsCheckBox = QtGui.QCheckBox(HelpClearPrivateDataDialog)
        self.passwordsCheckBox.setChecked(False)
        self.passwordsCheckBox.setObjectName(_fromUtf8("passwordsCheckBox"))
        self.verticalLayout.addWidget(self.passwordsCheckBox)
        self.buttonBox = QtGui.QDialogButtonBox(HelpClearPrivateDataDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(HelpClearPrivateDataDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), HelpClearPrivateDataDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), HelpClearPrivateDataDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(HelpClearPrivateDataDialog)
        HelpClearPrivateDataDialog.setTabOrder(self.historyCheckBox, self.searchCheckBox)
        HelpClearPrivateDataDialog.setTabOrder(self.searchCheckBox, self.cookiesCheckBox)
        HelpClearPrivateDataDialog.setTabOrder(self.cookiesCheckBox, self.cacheCheckBox)
        HelpClearPrivateDataDialog.setTabOrder(self.cacheCheckBox, self.iconsCheckBox)
        HelpClearPrivateDataDialog.setTabOrder(self.iconsCheckBox, self.passwordsCheckBox)
        HelpClearPrivateDataDialog.setTabOrder(self.passwordsCheckBox, self.buttonBox)

    def retranslateUi(self, HelpClearPrivateDataDialog):
        HelpClearPrivateDataDialog.setWindowTitle(_translate("HelpClearPrivateDataDialog", "Clear Private Data", None))
        self.historyCheckBox.setToolTip(_translate("HelpClearPrivateDataDialog", "Select to clear the browsing history", None))
        self.historyCheckBox.setText(_translate("HelpClearPrivateDataDialog", "&Browsing History", None))
        self.searchCheckBox.setToolTip(_translate("HelpClearPrivateDataDialog", "Select to clear the search history", None))
        self.searchCheckBox.setText(_translate("HelpClearPrivateDataDialog", "&Search History", None))
        self.cookiesCheckBox.setToolTip(_translate("HelpClearPrivateDataDialog", "Select to clear the cookies", None))
        self.cookiesCheckBox.setText(_translate("HelpClearPrivateDataDialog", "&Cookies", None))
        self.cacheCheckBox.setToolTip(_translate("HelpClearPrivateDataDialog", "Select to clear the disk cache", None))
        self.cacheCheckBox.setText(_translate("HelpClearPrivateDataDialog", "Cached &Web Pages", None))
        self.iconsCheckBox.setToolTip(_translate("HelpClearPrivateDataDialog", "Select to clear the website icons", None))
        self.iconsCheckBox.setText(_translate("HelpClearPrivateDataDialog", "Website &Icons", None))
        self.passwordsCheckBox.setToolTip(_translate("HelpClearPrivateDataDialog", "Select to clear the saved passwords", None))
        self.passwordsCheckBox.setText(_translate("HelpClearPrivateDataDialog", "Saved &Passwords", None))

