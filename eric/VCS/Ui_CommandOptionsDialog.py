# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\VCS\CommandOptionsDialog.ui'
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

class Ui_vcsCommandOptionsDialog(object):
    def setupUi(self, vcsCommandOptionsDialog):
        vcsCommandOptionsDialog.setObjectName(_fromUtf8("vcsCommandOptionsDialog"))
        vcsCommandOptionsDialog.resize(531, 413)
        vcsCommandOptionsDialog.setSizeGripEnabled(True)
        self.vboxlayout = QtGui.QVBoxLayout(vcsCommandOptionsDialog)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.gridlayout = QtGui.QGridLayout()
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.historyLabel = QtGui.QLabel(vcsCommandOptionsDialog)
        self.historyLabel.setObjectName(_fromUtf8("historyLabel"))
        self.gridlayout.addWidget(self.historyLabel, 8, 0, 1, 1)
        self.addLabel = QtGui.QLabel(vcsCommandOptionsDialog)
        self.addLabel.setObjectName(_fromUtf8("addLabel"))
        self.gridlayout.addWidget(self.addLabel, 4, 0, 1, 1)
        self.removeLabel = QtGui.QLabel(vcsCommandOptionsDialog)
        self.removeLabel.setObjectName(_fromUtf8("removeLabel"))
        self.gridlayout.addWidget(self.removeLabel, 5, 0, 1, 1)
        self.tagLabel = QtGui.QLabel(vcsCommandOptionsDialog)
        self.tagLabel.setObjectName(_fromUtf8("tagLabel"))
        self.gridlayout.addWidget(self.tagLabel, 10, 0, 1, 1)
        self.commitEdit = QtGui.QLineEdit(vcsCommandOptionsDialog)
        self.commitEdit.setObjectName(_fromUtf8("commitEdit"))
        self.gridlayout.addWidget(self.commitEdit, 1, 1, 1, 1)
        self.historyEdit = QtGui.QLineEdit(vcsCommandOptionsDialog)
        self.historyEdit.setObjectName(_fromUtf8("historyEdit"))
        self.gridlayout.addWidget(self.historyEdit, 8, 1, 1, 1)
        self.diffEdit = QtGui.QLineEdit(vcsCommandOptionsDialog)
        self.diffEdit.setObjectName(_fromUtf8("diffEdit"))
        self.gridlayout.addWidget(self.diffEdit, 6, 1, 1, 1)
        self.updateEdit = QtGui.QLineEdit(vcsCommandOptionsDialog)
        self.updateEdit.setObjectName(_fromUtf8("updateEdit"))
        self.gridlayout.addWidget(self.updateEdit, 3, 1, 1, 1)
        self.logEdit = QtGui.QLineEdit(vcsCommandOptionsDialog)
        self.logEdit.setObjectName(_fromUtf8("logEdit"))
        self.gridlayout.addWidget(self.logEdit, 7, 1, 1, 1)
        self.tagEdit = QtGui.QLineEdit(vcsCommandOptionsDialog)
        self.tagEdit.setObjectName(_fromUtf8("tagEdit"))
        self.gridlayout.addWidget(self.tagEdit, 10, 1, 1, 1)
        self.statusEdit = QtGui.QLineEdit(vcsCommandOptionsDialog)
        self.statusEdit.setObjectName(_fromUtf8("statusEdit"))
        self.gridlayout.addWidget(self.statusEdit, 9, 1, 1, 1)
        self.diffLabel = QtGui.QLabel(vcsCommandOptionsDialog)
        self.diffLabel.setObjectName(_fromUtf8("diffLabel"))
        self.gridlayout.addWidget(self.diffLabel, 6, 0, 1, 1)
        self.globalLabel = QtGui.QLabel(vcsCommandOptionsDialog)
        self.globalLabel.setObjectName(_fromUtf8("globalLabel"))
        self.gridlayout.addWidget(self.globalLabel, 0, 0, 1, 1)
        self.exportEdit = QtGui.QLineEdit(vcsCommandOptionsDialog)
        self.exportEdit.setObjectName(_fromUtf8("exportEdit"))
        self.gridlayout.addWidget(self.exportEdit, 11, 1, 1, 1)
        self.addEdit = QtGui.QLineEdit(vcsCommandOptionsDialog)
        self.addEdit.setObjectName(_fromUtf8("addEdit"))
        self.gridlayout.addWidget(self.addEdit, 4, 1, 1, 1)
        self.logLabel = QtGui.QLabel(vcsCommandOptionsDialog)
        self.logLabel.setObjectName(_fromUtf8("logLabel"))
        self.gridlayout.addWidget(self.logLabel, 7, 0, 1, 1)
        self.statusLabel = QtGui.QLabel(vcsCommandOptionsDialog)
        self.statusLabel.setObjectName(_fromUtf8("statusLabel"))
        self.gridlayout.addWidget(self.statusLabel, 9, 0, 1, 1)
        self.removeEdit = QtGui.QLineEdit(vcsCommandOptionsDialog)
        self.removeEdit.setObjectName(_fromUtf8("removeEdit"))
        self.gridlayout.addWidget(self.removeEdit, 5, 1, 1, 1)
        self.checkoutEdit = QtGui.QLineEdit(vcsCommandOptionsDialog)
        self.checkoutEdit.setObjectName(_fromUtf8("checkoutEdit"))
        self.gridlayout.addWidget(self.checkoutEdit, 2, 1, 1, 1)
        self.commitLabel = QtGui.QLabel(vcsCommandOptionsDialog)
        self.commitLabel.setObjectName(_fromUtf8("commitLabel"))
        self.gridlayout.addWidget(self.commitLabel, 1, 0, 1, 1)
        self.exportLabel = QtGui.QLabel(vcsCommandOptionsDialog)
        self.exportLabel.setObjectName(_fromUtf8("exportLabel"))
        self.gridlayout.addWidget(self.exportLabel, 11, 0, 1, 1)
        self.checkoutLabel = QtGui.QLabel(vcsCommandOptionsDialog)
        self.checkoutLabel.setObjectName(_fromUtf8("checkoutLabel"))
        self.gridlayout.addWidget(self.checkoutLabel, 2, 0, 1, 1)
        self.updateLabel = QtGui.QLabel(vcsCommandOptionsDialog)
        self.updateLabel.setObjectName(_fromUtf8("updateLabel"))
        self.gridlayout.addWidget(self.updateLabel, 3, 0, 1, 1)
        self.globalEdit = QtGui.QLineEdit(vcsCommandOptionsDialog)
        self.globalEdit.setObjectName(_fromUtf8("globalEdit"))
        self.gridlayout.addWidget(self.globalEdit, 0, 1, 1, 1)
        self.vboxlayout.addLayout(self.gridlayout)
        self.buttonBox = QtGui.QDialogButtonBox(vcsCommandOptionsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.vboxlayout.addWidget(self.buttonBox)
        self.historyLabel.setBuddy(self.historyEdit)
        self.addLabel.setBuddy(self.addEdit)
        self.removeLabel.setBuddy(self.removeEdit)
        self.tagLabel.setBuddy(self.tagEdit)
        self.diffLabel.setBuddy(self.diffEdit)
        self.globalLabel.setBuddy(self.globalEdit)
        self.logLabel.setBuddy(self.logEdit)
        self.statusLabel.setBuddy(self.statusEdit)
        self.commitLabel.setBuddy(self.commitEdit)
        self.exportLabel.setBuddy(self.exportEdit)
        self.checkoutLabel.setBuddy(self.checkoutEdit)
        self.updateLabel.setBuddy(self.updateEdit)

        self.retranslateUi(vcsCommandOptionsDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), vcsCommandOptionsDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), vcsCommandOptionsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(vcsCommandOptionsDialog)
        vcsCommandOptionsDialog.setTabOrder(self.globalEdit, self.commitEdit)
        vcsCommandOptionsDialog.setTabOrder(self.commitEdit, self.checkoutEdit)
        vcsCommandOptionsDialog.setTabOrder(self.checkoutEdit, self.updateEdit)
        vcsCommandOptionsDialog.setTabOrder(self.updateEdit, self.addEdit)
        vcsCommandOptionsDialog.setTabOrder(self.addEdit, self.removeEdit)
        vcsCommandOptionsDialog.setTabOrder(self.removeEdit, self.diffEdit)
        vcsCommandOptionsDialog.setTabOrder(self.diffEdit, self.logEdit)
        vcsCommandOptionsDialog.setTabOrder(self.logEdit, self.historyEdit)
        vcsCommandOptionsDialog.setTabOrder(self.historyEdit, self.statusEdit)
        vcsCommandOptionsDialog.setTabOrder(self.statusEdit, self.tagEdit)
        vcsCommandOptionsDialog.setTabOrder(self.tagEdit, self.exportEdit)

    def retranslateUi(self, vcsCommandOptionsDialog):
        vcsCommandOptionsDialog.setWindowTitle(_translate("vcsCommandOptionsDialog", "VCS Command Options", None))
        vcsCommandOptionsDialog.setWhatsThis(_translate("vcsCommandOptionsDialog", "<b>VCS Command Options Dialog</b>\n"
"<p>Enter the options for the different VCS commands. The \"Global Options\" entry applies to all VCS commands.</p>", None))
        self.historyLabel.setText(_translate("vcsCommandOptionsDialog", "&History Options:", None))
        self.addLabel.setText(_translate("vcsCommandOptionsDialog", "&Add Options:", None))
        self.removeLabel.setText(_translate("vcsCommandOptionsDialog", "&Remove Options:", None))
        self.tagLabel.setText(_translate("vcsCommandOptionsDialog", "&Tag Options:", None))
        self.commitEdit.setToolTip(_translate("vcsCommandOptionsDialog", "Enter the options for the commit command.", None))
        self.commitEdit.setWhatsThis(_translate("vcsCommandOptionsDialog", "<b>Commit Options</b>\n"
"<p>Enter the options for the commit command.</p>", None))
        self.historyEdit.setToolTip(_translate("vcsCommandOptionsDialog", "Enter the options for the history command.", None))
        self.historyEdit.setWhatsThis(_translate("vcsCommandOptionsDialog", "<b>History Options</b>\n"
"<p>Enter the options for the history command.</p>", None))
        self.diffEdit.setToolTip(_translate("vcsCommandOptionsDialog", "Enter the options for the diff command.", None))
        self.diffEdit.setWhatsThis(_translate("vcsCommandOptionsDialog", "<b>Diff Options</b>\n"
"<p>Enter the options for the diff command.</p>", None))
        self.updateEdit.setToolTip(_translate("vcsCommandOptionsDialog", "Enter the options for the update command.", None))
        self.updateEdit.setWhatsThis(_translate("vcsCommandOptionsDialog", "<b>Update Options</b>\n"
"<p>Enter the options for the update command.</p>", None))
        self.logEdit.setToolTip(_translate("vcsCommandOptionsDialog", "Enter the options for the log command.", None))
        self.logEdit.setWhatsThis(_translate("vcsCommandOptionsDialog", "<b>Log Options</b>\n"
"<p>Enter the options for the log command.</p>", None))
        self.tagEdit.setToolTip(_translate("vcsCommandOptionsDialog", "Enter the options for the tag command.", None))
        self.tagEdit.setWhatsThis(_translate("vcsCommandOptionsDialog", "<b>Tag Options</b>\n"
"<p>Enter the options for the tag command.</p>", None))
        self.statusEdit.setToolTip(_translate("vcsCommandOptionsDialog", "Enter the options for the status command.", None))
        self.statusEdit.setWhatsThis(_translate("vcsCommandOptionsDialog", "<b>Status Options</b>\n"
"<p>Enter the options for the status command.</p>", None))
        self.diffLabel.setText(_translate("vcsCommandOptionsDialog", "&Diff Options:", None))
        self.globalLabel.setText(_translate("vcsCommandOptionsDialog", "&Global Options:", None))
        self.exportEdit.setToolTip(_translate("vcsCommandOptionsDialog", "Enter the options for the export command.", None))
        self.exportEdit.setWhatsThis(_translate("vcsCommandOptionsDialog", "<b>Export Options</b>\n"
"<p>Enter the options for the export command.</p>", None))
        self.addEdit.setToolTip(_translate("vcsCommandOptionsDialog", "Enter the options for the add command.", None))
        self.addEdit.setWhatsThis(_translate("vcsCommandOptionsDialog", "<b>Add Options</b>\n"
"<p>Enter the options for the add command.</p>", None))
        self.logLabel.setText(_translate("vcsCommandOptionsDialog", "&Log Options:", None))
        self.statusLabel.setText(_translate("vcsCommandOptionsDialog", "&StatusOptions:", None))
        self.removeEdit.setToolTip(_translate("vcsCommandOptionsDialog", "Enter the options for the remove command.", None))
        self.removeEdit.setWhatsThis(_translate("vcsCommandOptionsDialog", "<b>Remove Options</b>\n"
"<p>Enter the options for the remove command.</p>", None))
        self.checkoutEdit.setToolTip(_translate("vcsCommandOptionsDialog", "Enter the options for the checkout command.", None))
        self.checkoutEdit.setWhatsThis(_translate("vcsCommandOptionsDialog", "<b>Checkout Options</b>\n"
"<p>Enter the options for the checkout command.</p>", None))
        self.commitLabel.setText(_translate("vcsCommandOptionsDialog", "Co&mmit Options:", None))
        self.exportLabel.setText(_translate("vcsCommandOptionsDialog", "&Export Options:", None))
        self.checkoutLabel.setText(_translate("vcsCommandOptionsDialog", "Check&out Options:", None))
        self.updateLabel.setText(_translate("vcsCommandOptionsDialog", "&Update Options:", None))
        self.globalEdit.setToolTip(_translate("vcsCommandOptionsDialog", "Enter the global options.", None))
        self.globalEdit.setWhatsThis(_translate("vcsCommandOptionsDialog", "<b>Global Options</b>\n"
"<p>Enter the global options.</p>", None))

