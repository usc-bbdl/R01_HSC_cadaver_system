# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Plugins\VcsPlugins\vcsSubversion\SvnRepoBrowserDialog.ui'
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

class Ui_SvnRepoBrowserDialog(object):
    def setupUi(self, SvnRepoBrowserDialog):
        SvnRepoBrowserDialog.setObjectName(_fromUtf8("SvnRepoBrowserDialog"))
        SvnRepoBrowserDialog.resize(650, 667)
        self.gridlayout = QtGui.QGridLayout(SvnRepoBrowserDialog)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.label = QtGui.QLabel(SvnRepoBrowserDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridlayout.addWidget(self.label, 0, 0, 1, 1)
        self.urlCombo = QtGui.QComboBox(SvnRepoBrowserDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.urlCombo.sizePolicy().hasHeightForWidth())
        self.urlCombo.setSizePolicy(sizePolicy)
        self.urlCombo.setEditable(True)
        self.urlCombo.setInsertPolicy(QtGui.QComboBox.InsertAtTop)
        self.urlCombo.setObjectName(_fromUtf8("urlCombo"))
        self.gridlayout.addWidget(self.urlCombo, 0, 1, 1, 1)
        self.repoTree = QtGui.QTreeWidget(SvnRepoBrowserDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(self.repoTree.sizePolicy().hasHeightForWidth())
        self.repoTree.setSizePolicy(sizePolicy)
        self.repoTree.setAlternatingRowColors(True)
        self.repoTree.setAllColumnsShowFocus(True)
        self.repoTree.setColumnCount(5)
        self.repoTree.setObjectName(_fromUtf8("repoTree"))
        self.gridlayout.addWidget(self.repoTree, 1, 0, 1, 2)
        self.errorGroup = QtGui.QGroupBox(SvnRepoBrowserDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.errorGroup.sizePolicy().hasHeightForWidth())
        self.errorGroup.setSizePolicy(sizePolicy)
        self.errorGroup.setObjectName(_fromUtf8("errorGroup"))
        self.vboxlayout = QtGui.QVBoxLayout(self.errorGroup)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.errors = QtGui.QTextEdit(self.errorGroup)
        self.errors.setReadOnly(True)
        self.errors.setAcceptRichText(False)
        self.errors.setObjectName(_fromUtf8("errors"))
        self.vboxlayout.addWidget(self.errors)
        self.gridlayout.addWidget(self.errorGroup, 2, 0, 1, 2)
        self.inputGroup = QtGui.QGroupBox(SvnRepoBrowserDialog)
        self.inputGroup.setObjectName(_fromUtf8("inputGroup"))
        self.gridlayout1 = QtGui.QGridLayout(self.inputGroup)
        self.gridlayout1.setObjectName(_fromUtf8("gridlayout1"))
        spacerItem = QtGui.QSpacerItem(327, 29, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridlayout1.addItem(spacerItem, 1, 1, 1, 1)
        self.sendButton = QtGui.QPushButton(self.inputGroup)
        self.sendButton.setObjectName(_fromUtf8("sendButton"))
        self.gridlayout1.addWidget(self.sendButton, 1, 2, 1, 1)
        self.input = QtGui.QLineEdit(self.inputGroup)
        self.input.setObjectName(_fromUtf8("input"))
        self.gridlayout1.addWidget(self.input, 0, 0, 1, 3)
        self.passwordCheckBox = QtGui.QCheckBox(self.inputGroup)
        self.passwordCheckBox.setObjectName(_fromUtf8("passwordCheckBox"))
        self.gridlayout1.addWidget(self.passwordCheckBox, 1, 0, 1, 1)
        self.gridlayout.addWidget(self.inputGroup, 3, 0, 1, 2)
        self.buttonBox = QtGui.QDialogButtonBox(SvnRepoBrowserDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Close|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridlayout.addWidget(self.buttonBox, 4, 0, 1, 2)

        self.retranslateUi(SvnRepoBrowserDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), SvnRepoBrowserDialog.reject)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), SvnRepoBrowserDialog.accept)
        QtCore.QMetaObject.connectSlotsByName(SvnRepoBrowserDialog)
        SvnRepoBrowserDialog.setTabOrder(self.urlCombo, self.repoTree)
        SvnRepoBrowserDialog.setTabOrder(self.repoTree, self.errors)
        SvnRepoBrowserDialog.setTabOrder(self.errors, self.input)
        SvnRepoBrowserDialog.setTabOrder(self.input, self.passwordCheckBox)
        SvnRepoBrowserDialog.setTabOrder(self.passwordCheckBox, self.sendButton)
        SvnRepoBrowserDialog.setTabOrder(self.sendButton, self.buttonBox)

    def retranslateUi(self, SvnRepoBrowserDialog):
        SvnRepoBrowserDialog.setWindowTitle(_translate("SvnRepoBrowserDialog", "Subversion Repository Browser", None))
        self.label.setText(_translate("SvnRepoBrowserDialog", "URL:", None))
        self.urlCombo.setToolTip(_translate("SvnRepoBrowserDialog", "Enter the URL of the repository", None))
        self.repoTree.setSortingEnabled(True)
        self.repoTree.headerItem().setText(0, _translate("SvnRepoBrowserDialog", "File", None))
        self.repoTree.headerItem().setText(1, _translate("SvnRepoBrowserDialog", "Revision", None))
        self.repoTree.headerItem().setText(2, _translate("SvnRepoBrowserDialog", "Author", None))
        self.repoTree.headerItem().setText(3, _translate("SvnRepoBrowserDialog", "Size", None))
        self.repoTree.headerItem().setText(4, _translate("SvnRepoBrowserDialog", "Date", None))
        self.errorGroup.setTitle(_translate("SvnRepoBrowserDialog", "Errors", None))
        self.errors.setWhatsThis(_translate("SvnRepoBrowserDialog", "<b>Subversion errors</b><p>This shows possible error messages of the svn list and svn info commands.</p>", None))
        self.inputGroup.setTitle(_translate("SvnRepoBrowserDialog", "Input", None))
        self.sendButton.setToolTip(_translate("SvnRepoBrowserDialog", "Press to send the input to the subversion process", None))
        self.sendButton.setText(_translate("SvnRepoBrowserDialog", "&Send", None))
        self.sendButton.setShortcut(_translate("SvnRepoBrowserDialog", "Alt+S", None))
        self.input.setToolTip(_translate("SvnRepoBrowserDialog", "Enter data to be sent to the subversion process", None))
        self.passwordCheckBox.setToolTip(_translate("SvnRepoBrowserDialog", "Select to switch the input field to password mode", None))
        self.passwordCheckBox.setText(_translate("SvnRepoBrowserDialog", "&Password Mode", None))
        self.passwordCheckBox.setShortcut(_translate("SvnRepoBrowserDialog", "Alt+P", None))

