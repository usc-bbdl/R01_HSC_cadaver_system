# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Project\AddDirectoryDialog.ui'
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

class Ui_AddDirectoryDialog(object):
    def setupUi(self, AddDirectoryDialog):
        AddDirectoryDialog.setObjectName(_fromUtf8("AddDirectoryDialog"))
        AddDirectoryDialog.resize(391, 174)
        AddDirectoryDialog.setSizeGripEnabled(True)
        self.vboxlayout = QtGui.QVBoxLayout(AddDirectoryDialog)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.gridlayout = QtGui.QGridLayout()
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.filterComboBox = QtGui.QComboBox(AddDirectoryDialog)
        self.filterComboBox.setObjectName(_fromUtf8("filterComboBox"))
        self.gridlayout.addWidget(self.filterComboBox, 0, 1, 1, 2)
        self.targetDirButton = QtGui.QPushButton(AddDirectoryDialog)
        self.targetDirButton.setObjectName(_fromUtf8("targetDirButton"))
        self.gridlayout.addWidget(self.targetDirButton, 2, 2, 1, 1)
        self.targetDirLabel = QtGui.QLabel(AddDirectoryDialog)
        self.targetDirLabel.setObjectName(_fromUtf8("targetDirLabel"))
        self.gridlayout.addWidget(self.targetDirLabel, 2, 0, 1, 1)
        self.sourceDirEdit = QtGui.QLineEdit(AddDirectoryDialog)
        self.sourceDirEdit.setObjectName(_fromUtf8("sourceDirEdit"))
        self.gridlayout.addWidget(self.sourceDirEdit, 1, 1, 1, 1)
        self.recursiveCheckBox = QtGui.QCheckBox(AddDirectoryDialog)
        self.recursiveCheckBox.setObjectName(_fromUtf8("recursiveCheckBox"))
        self.gridlayout.addWidget(self.recursiveCheckBox, 3, 0, 1, 3)
        self.targetDirEdit = QtGui.QLineEdit(AddDirectoryDialog)
        self.targetDirEdit.setObjectName(_fromUtf8("targetDirEdit"))
        self.gridlayout.addWidget(self.targetDirEdit, 2, 1, 1, 1)
        self.sourceDirButton = QtGui.QPushButton(AddDirectoryDialog)
        self.sourceDirButton.setObjectName(_fromUtf8("sourceDirButton"))
        self.gridlayout.addWidget(self.sourceDirButton, 1, 2, 1, 1)
        self.sourceDirLabel = QtGui.QLabel(AddDirectoryDialog)
        self.sourceDirLabel.setObjectName(_fromUtf8("sourceDirLabel"))
        self.gridlayout.addWidget(self.sourceDirLabel, 1, 0, 1, 1)
        self.textLabel1 = QtGui.QLabel(AddDirectoryDialog)
        self.textLabel1.setObjectName(_fromUtf8("textLabel1"))
        self.gridlayout.addWidget(self.textLabel1, 0, 0, 1, 1)
        self.vboxlayout.addLayout(self.gridlayout)
        self.buttonBox = QtGui.QDialogButtonBox(AddDirectoryDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.vboxlayout.addWidget(self.buttonBox)
        self.targetDirLabel.setBuddy(self.targetDirEdit)
        self.sourceDirLabel.setBuddy(self.sourceDirEdit)
        self.textLabel1.setBuddy(self.filterComboBox)

        self.retranslateUi(AddDirectoryDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), AddDirectoryDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), AddDirectoryDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(AddDirectoryDialog)
        AddDirectoryDialog.setTabOrder(self.filterComboBox, self.sourceDirEdit)
        AddDirectoryDialog.setTabOrder(self.sourceDirEdit, self.sourceDirButton)
        AddDirectoryDialog.setTabOrder(self.sourceDirButton, self.targetDirEdit)
        AddDirectoryDialog.setTabOrder(self.targetDirEdit, self.targetDirButton)
        AddDirectoryDialog.setTabOrder(self.targetDirButton, self.recursiveCheckBox)

    def retranslateUi(self, AddDirectoryDialog):
        AddDirectoryDialog.setWindowTitle(_translate("AddDirectoryDialog", "Add Directory", None))
        AddDirectoryDialog.setToolTip(_translate("AddDirectoryDialog", "Add a directory to the current project", None))
        AddDirectoryDialog.setWhatsThis(_translate("AddDirectoryDialog", "<b>Add Directory Dialog</b>\n"
"<p>This dialog is used to add a directory to the current project.</p>", None))
        self.targetDirButton.setWhatsThis(_translate("AddDirectoryDialog", "<b>Target Directory</b>\n"
"<p>Select the target directory via a directory selection dialog.</p>", None))
        self.targetDirButton.setText(_translate("AddDirectoryDialog", "...", None))
        self.targetDirLabel.setText(_translate("AddDirectoryDialog", "&Target Directory:", None))
        self.sourceDirEdit.setToolTip(_translate("AddDirectoryDialog", "Enter the name of the directory to add", None))
        self.sourceDirEdit.setWhatsThis(_translate("AddDirectoryDialog", "<b>Source Directory</b>\n"
"<p>Enter the name of the directory to add to the current project.\n"
" You may select it with a dialog by pressing the button to\n"
" the right.</p>", None))
        self.recursiveCheckBox.setToolTip(_translate("AddDirectoryDialog", "Select, whether a recursive add should be performed", None))
        self.recursiveCheckBox.setText(_translate("AddDirectoryDialog", "&Recurse into subdirectories", None))
        self.targetDirEdit.setToolTip(_translate("AddDirectoryDialog", "Enter the target directory for the file", None))
        self.targetDirEdit.setWhatsThis(_translate("AddDirectoryDialog", "<b>Target Directory</b>\n"
"<p>Enter the target directory. You may select it\n"
" with a dialog by pressing the button to the right.</p>", None))
        self.sourceDirButton.setWhatsThis(_translate("AddDirectoryDialog", "<b>Source Directory</b>\n"
"<p>Select the source directory via a directory selection dialog.</p>", None))
        self.sourceDirButton.setText(_translate("AddDirectoryDialog", "...", None))
        self.sourceDirLabel.setText(_translate("AddDirectoryDialog", "&Source Directory:", None))
        self.textLabel1.setText(_translate("AddDirectoryDialog", "&File Type:", None))

