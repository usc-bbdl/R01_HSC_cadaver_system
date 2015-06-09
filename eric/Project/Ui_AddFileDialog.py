# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Project\AddFileDialog.ui'
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

class Ui_AddFileDialog(object):
    def setupUi(self, AddFileDialog):
        AddFileDialog.setObjectName(_fromUtf8("AddFileDialog"))
        AddFileDialog.resize(391, 141)
        AddFileDialog.setSizeGripEnabled(True)
        self.vboxlayout = QtGui.QVBoxLayout(AddFileDialog)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.gridlayout = QtGui.QGridLayout()
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.sourceFileButton = QtGui.QPushButton(AddFileDialog)
        self.sourceFileButton.setObjectName(_fromUtf8("sourceFileButton"))
        self.gridlayout.addWidget(self.sourceFileButton, 0, 2, 1, 1)
        self.targetDirLabel = QtGui.QLabel(AddFileDialog)
        self.targetDirLabel.setObjectName(_fromUtf8("targetDirLabel"))
        self.gridlayout.addWidget(self.targetDirLabel, 1, 0, 1, 1)
        self.targetDirEdit = QtGui.QLineEdit(AddFileDialog)
        self.targetDirEdit.setObjectName(_fromUtf8("targetDirEdit"))
        self.gridlayout.addWidget(self.targetDirEdit, 1, 1, 1, 1)
        self.targetDirButton = QtGui.QPushButton(AddFileDialog)
        self.targetDirButton.setObjectName(_fromUtf8("targetDirButton"))
        self.gridlayout.addWidget(self.targetDirButton, 1, 2, 1, 1)
        self.sourceFileLabel = QtGui.QLabel(AddFileDialog)
        self.sourceFileLabel.setObjectName(_fromUtf8("sourceFileLabel"))
        self.gridlayout.addWidget(self.sourceFileLabel, 0, 0, 1, 1)
        self.sourceFileEdit = QtGui.QLineEdit(AddFileDialog)
        self.sourceFileEdit.setObjectName(_fromUtf8("sourceFileEdit"))
        self.gridlayout.addWidget(self.sourceFileEdit, 0, 1, 1, 1)
        self.vboxlayout.addLayout(self.gridlayout)
        self.sourcecodeCheckBox = QtGui.QCheckBox(AddFileDialog)
        self.sourcecodeCheckBox.setObjectName(_fromUtf8("sourcecodeCheckBox"))
        self.vboxlayout.addWidget(self.sourcecodeCheckBox)
        self.buttonBox = QtGui.QDialogButtonBox(AddFileDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.vboxlayout.addWidget(self.buttonBox)
        self.targetDirLabel.setBuddy(self.targetDirEdit)
        self.sourceFileLabel.setBuddy(self.sourceFileEdit)

        self.retranslateUi(AddFileDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), AddFileDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), AddFileDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(AddFileDialog)
        AddFileDialog.setTabOrder(self.sourceFileEdit, self.sourceFileButton)
        AddFileDialog.setTabOrder(self.sourceFileButton, self.targetDirEdit)
        AddFileDialog.setTabOrder(self.targetDirEdit, self.targetDirButton)
        AddFileDialog.setTabOrder(self.targetDirButton, self.sourcecodeCheckBox)

    def retranslateUi(self, AddFileDialog):
        AddFileDialog.setWindowTitle(_translate("AddFileDialog", "Add Files", None))
        AddFileDialog.setWhatsThis(_translate("AddFileDialog", "<b>Add Files Dialog</b>\n"
"<p>This dialog is used to add files to the current project.</p>", None))
        self.sourceFileButton.setWhatsThis(_translate("AddFileDialog", "<b>Source Files</b>\n"
"<p>Select the source files via a files selection dialog.</p>", None))
        self.sourceFileButton.setText(_translate("AddFileDialog", "...", None))
        self.targetDirLabel.setText(_translate("AddFileDialog", "&Target Directory:", None))
        self.targetDirEdit.setToolTip(_translate("AddFileDialog", "Enter the target directory for the file", None))
        self.targetDirEdit.setWhatsThis(_translate("AddFileDialog", "<b>Target Directory</b>\n"
"<p>Enter the target directory. You may select it\n"
" with a dialog by pressing the button to the right.</p>", None))
        self.targetDirButton.setWhatsThis(_translate("AddFileDialog", "<b>Target Directory</b>\n"
"<p>Select the target directory via a directory selection dialog.</p>", None))
        self.targetDirButton.setText(_translate("AddFileDialog", "...", None))
        self.sourceFileLabel.setText(_translate("AddFileDialog", "&Source Files:", None))
        self.sourceFileEdit.setToolTip(_translate("AddFileDialog", "Enter the name of files to add separated by the path separator", None))
        self.sourceFileEdit.setWhatsThis(_translate("AddFileDialog", "<b>Source Files</b>\n"
"<p>Enter the name of files to add to the current project separated\n"
"by the path separator. You may select them with a dialog by pressing \n"
"the button to the right.</p>", None))
        self.sourcecodeCheckBox.setToolTip(_translate("AddFileDialog", "Select, if the files should be added as sourcecode (overriding automatic detection)", None))
        self.sourcecodeCheckBox.setText(_translate("AddFileDialog", "Is source&code files", None))
        self.sourcecodeCheckBox.setShortcut(_translate("AddFileDialog", "Alt+C", None))

