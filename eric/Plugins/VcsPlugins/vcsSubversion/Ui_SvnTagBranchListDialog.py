# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Plugins\VcsPlugins\vcsSubversion\SvnTagBranchListDialog.ui'
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

class Ui_SvnTagBranchListDialog(object):
    def setupUi(self, SvnTagBranchListDialog):
        SvnTagBranchListDialog.setObjectName(_fromUtf8("SvnTagBranchListDialog"))
        SvnTagBranchListDialog.resize(634, 494)
        SvnTagBranchListDialog.setSizeGripEnabled(True)
        self.vboxlayout = QtGui.QVBoxLayout(SvnTagBranchListDialog)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.tagList = QtGui.QTreeWidget(SvnTagBranchListDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.tagList.sizePolicy().hasHeightForWidth())
        self.tagList.setSizePolicy(sizePolicy)
        self.tagList.setAlternatingRowColors(True)
        self.tagList.setRootIsDecorated(False)
        self.tagList.setItemsExpandable(False)
        self.tagList.setObjectName(_fromUtf8("tagList"))
        self.vboxlayout.addWidget(self.tagList)
        self.errorGroup = QtGui.QGroupBox(SvnTagBranchListDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.errorGroup.sizePolicy().hasHeightForWidth())
        self.errorGroup.setSizePolicy(sizePolicy)
        self.errorGroup.setObjectName(_fromUtf8("errorGroup"))
        self.vboxlayout1 = QtGui.QVBoxLayout(self.errorGroup)
        self.vboxlayout1.setObjectName(_fromUtf8("vboxlayout1"))
        self.errors = QtGui.QTextEdit(self.errorGroup)
        self.errors.setReadOnly(True)
        self.errors.setAcceptRichText(False)
        self.errors.setObjectName(_fromUtf8("errors"))
        self.vboxlayout1.addWidget(self.errors)
        self.vboxlayout.addWidget(self.errorGroup)
        self.inputGroup = QtGui.QGroupBox(SvnTagBranchListDialog)
        self.inputGroup.setObjectName(_fromUtf8("inputGroup"))
        self.gridlayout = QtGui.QGridLayout(self.inputGroup)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        spacerItem = QtGui.QSpacerItem(327, 29, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridlayout.addItem(spacerItem, 1, 1, 1, 1)
        self.sendButton = QtGui.QPushButton(self.inputGroup)
        self.sendButton.setObjectName(_fromUtf8("sendButton"))
        self.gridlayout.addWidget(self.sendButton, 1, 2, 1, 1)
        self.input = QtGui.QLineEdit(self.inputGroup)
        self.input.setObjectName(_fromUtf8("input"))
        self.gridlayout.addWidget(self.input, 0, 0, 1, 3)
        self.passwordCheckBox = QtGui.QCheckBox(self.inputGroup)
        self.passwordCheckBox.setObjectName(_fromUtf8("passwordCheckBox"))
        self.gridlayout.addWidget(self.passwordCheckBox, 1, 0, 1, 1)
        self.vboxlayout.addWidget(self.inputGroup)
        self.buttonBox = QtGui.QDialogButtonBox(SvnTagBranchListDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(SvnTagBranchListDialog)
        QtCore.QMetaObject.connectSlotsByName(SvnTagBranchListDialog)
        SvnTagBranchListDialog.setTabOrder(self.tagList, self.errors)
        SvnTagBranchListDialog.setTabOrder(self.errors, self.input)
        SvnTagBranchListDialog.setTabOrder(self.input, self.passwordCheckBox)
        SvnTagBranchListDialog.setTabOrder(self.passwordCheckBox, self.sendButton)
        SvnTagBranchListDialog.setTabOrder(self.sendButton, self.buttonBox)

    def retranslateUi(self, SvnTagBranchListDialog):
        SvnTagBranchListDialog.setWindowTitle(_translate("SvnTagBranchListDialog", "Subversion Tag List", None))
        SvnTagBranchListDialog.setWhatsThis(_translate("SvnTagBranchListDialog", "<b>Subversion Tag/Branch List</b>\n"
"<p>This dialog shows a list of the projects tags or branches.</p>", None))
        self.tagList.setWhatsThis(_translate("SvnTagBranchListDialog", "<b>Tag/Branches List</b>\n"
"<p>This shows a list of the projects tags or branches.</p>", None))
        self.tagList.setSortingEnabled(True)
        self.tagList.headerItem().setText(0, _translate("SvnTagBranchListDialog", "Revision", None))
        self.tagList.headerItem().setText(1, _translate("SvnTagBranchListDialog", "Author", None))
        self.tagList.headerItem().setText(2, _translate("SvnTagBranchListDialog", "Date", None))
        self.tagList.headerItem().setText(3, _translate("SvnTagBranchListDialog", "Name", None))
        self.errorGroup.setTitle(_translate("SvnTagBranchListDialog", "Errors", None))
        self.inputGroup.setTitle(_translate("SvnTagBranchListDialog", "Input", None))
        self.sendButton.setToolTip(_translate("SvnTagBranchListDialog", "Press to send the input to the subversion process", None))
        self.sendButton.setText(_translate("SvnTagBranchListDialog", "&Send", None))
        self.sendButton.setShortcut(_translate("SvnTagBranchListDialog", "Alt+S", None))
        self.input.setToolTip(_translate("SvnTagBranchListDialog", "Enter data to be sent to the subversion process", None))
        self.passwordCheckBox.setToolTip(_translate("SvnTagBranchListDialog", "Select to switch the input field to password mode", None))
        self.passwordCheckBox.setText(_translate("SvnTagBranchListDialog", "&Password Mode", None))
        self.passwordCheckBox.setShortcut(_translate("SvnTagBranchListDialog", "Alt+P", None))

