# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Plugins\VcsPlugins\vcsPySvn\SvnCommitDialog.ui'
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

class Ui_SvnCommitDialog(object):
    def setupUi(self, SvnCommitDialog):
        SvnCommitDialog.setObjectName(_fromUtf8("SvnCommitDialog"))
        SvnCommitDialog.resize(450, 384)
        self.verticalLayout_3 = QtGui.QVBoxLayout(SvnCommitDialog)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.logGroup = QtGui.QGroupBox(SvnCommitDialog)
        self.logGroup.setObjectName(_fromUtf8("logGroup"))
        self.verticalLayout = QtGui.QVBoxLayout(self.logGroup)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.logEdit = QtGui.QTextEdit(self.logGroup)
        self.logEdit.setTabChangesFocus(True)
        self.logEdit.setAcceptRichText(False)
        self.logEdit.setObjectName(_fromUtf8("logEdit"))
        self.verticalLayout.addWidget(self.logEdit)
        self.label = QtGui.QLabel(self.logGroup)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.recentComboBox = QtGui.QComboBox(self.logGroup)
        self.recentComboBox.setObjectName(_fromUtf8("recentComboBox"))
        self.verticalLayout.addWidget(self.recentComboBox)
        self.verticalLayout_3.addWidget(self.logGroup)
        self.changeListsGroup = QtGui.QGroupBox(SvnCommitDialog)
        self.changeListsGroup.setObjectName(_fromUtf8("changeListsGroup"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.changeListsGroup)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.changeLists = QtGui.QListWidget(self.changeListsGroup)
        self.changeLists.setObjectName(_fromUtf8("changeLists"))
        self.verticalLayout_2.addWidget(self.changeLists)
        self.keepChangeListsCheckBox = QtGui.QCheckBox(self.changeListsGroup)
        self.keepChangeListsCheckBox.setObjectName(_fromUtf8("keepChangeListsCheckBox"))
        self.verticalLayout_2.addWidget(self.keepChangeListsCheckBox)
        self.verticalLayout_3.addWidget(self.changeListsGroup)
        self.buttonBox = QtGui.QDialogButtonBox(SvnCommitDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Close|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_3.addWidget(self.buttonBox)

        self.retranslateUi(SvnCommitDialog)
        QtCore.QMetaObject.connectSlotsByName(SvnCommitDialog)
        SvnCommitDialog.setTabOrder(self.logEdit, self.recentComboBox)
        SvnCommitDialog.setTabOrder(self.recentComboBox, self.changeLists)
        SvnCommitDialog.setTabOrder(self.changeLists, self.keepChangeListsCheckBox)
        SvnCommitDialog.setTabOrder(self.keepChangeListsCheckBox, self.buttonBox)

    def retranslateUi(self, SvnCommitDialog):
        SvnCommitDialog.setWindowTitle(_translate("SvnCommitDialog", "Subversion", None))
        self.logGroup.setTitle(_translate("SvnCommitDialog", "Commit Message", None))
        self.logEdit.setToolTip(_translate("SvnCommitDialog", "Enter the log message.", None))
        self.logEdit.setWhatsThis(_translate("SvnCommitDialog", "<b>Log Message</b>\n"
"<p>Enter the log message for the commit action.</p>", None))
        self.label.setText(_translate("SvnCommitDialog", "Recent commit messages", None))
        self.recentComboBox.setToolTip(_translate("SvnCommitDialog", "Select a recent commit message to use", None))
        self.changeListsGroup.setTitle(_translate("SvnCommitDialog", "Changelists", None))
        self.changeLists.setToolTip(_translate("SvnCommitDialog", "Select the change lists to limit the commit", None))
        self.keepChangeListsCheckBox.setToolTip(_translate("SvnCommitDialog", "Select to keep the changelists", None))
        self.keepChangeListsCheckBox.setText(_translate("SvnCommitDialog", "Keep changelists", None))

