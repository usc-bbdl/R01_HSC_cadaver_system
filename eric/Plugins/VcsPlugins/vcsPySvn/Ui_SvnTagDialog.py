# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Plugins\VcsPlugins\vcsPySvn\SvnTagDialog.ui'
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

class Ui_SvnTagDialog(object):
    def setupUi(self, SvnTagDialog):
        SvnTagDialog.setObjectName(_fromUtf8("SvnTagDialog"))
        SvnTagDialog.resize(391, 197)
        SvnTagDialog.setSizeGripEnabled(True)
        self.gridlayout = QtGui.QGridLayout(SvnTagDialog)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.buttonBox = QtGui.QDialogButtonBox(SvnTagDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridlayout.addWidget(self.buttonBox, 2, 0, 1, 2)
        self.tagCombo = QtGui.QComboBox(SvnTagDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tagCombo.sizePolicy().hasHeightForWidth())
        self.tagCombo.setSizePolicy(sizePolicy)
        self.tagCombo.setEditable(True)
        self.tagCombo.setAutoCompletion(True)
        self.tagCombo.setDuplicatesEnabled(False)
        self.tagCombo.setObjectName(_fromUtf8("tagCombo"))
        self.gridlayout.addWidget(self.tagCombo, 0, 1, 1, 1)
        self.TextLabel1 = QtGui.QLabel(SvnTagDialog)
        self.TextLabel1.setObjectName(_fromUtf8("TextLabel1"))
        self.gridlayout.addWidget(self.TextLabel1, 0, 0, 1, 1)
        self.TagActionGroup = QtGui.QGroupBox(SvnTagDialog)
        self.TagActionGroup.setObjectName(_fromUtf8("TagActionGroup"))
        self.vboxlayout = QtGui.QVBoxLayout(self.TagActionGroup)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.createRegularButton = QtGui.QRadioButton(self.TagActionGroup)
        self.createRegularButton.setChecked(True)
        self.createRegularButton.setObjectName(_fromUtf8("createRegularButton"))
        self.vboxlayout.addWidget(self.createRegularButton)
        self.createBranchButton = QtGui.QRadioButton(self.TagActionGroup)
        self.createBranchButton.setObjectName(_fromUtf8("createBranchButton"))
        self.vboxlayout.addWidget(self.createBranchButton)
        self.deleteRegularButton = QtGui.QRadioButton(self.TagActionGroup)
        self.deleteRegularButton.setObjectName(_fromUtf8("deleteRegularButton"))
        self.vboxlayout.addWidget(self.deleteRegularButton)
        self.deleteBranchButton = QtGui.QRadioButton(self.TagActionGroup)
        self.deleteBranchButton.setObjectName(_fromUtf8("deleteBranchButton"))
        self.vboxlayout.addWidget(self.deleteBranchButton)
        self.gridlayout.addWidget(self.TagActionGroup, 1, 1, 1, 1)

        self.retranslateUi(SvnTagDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), SvnTagDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), SvnTagDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SvnTagDialog)
        SvnTagDialog.setTabOrder(self.tagCombo, self.createRegularButton)
        SvnTagDialog.setTabOrder(self.createRegularButton, self.createBranchButton)
        SvnTagDialog.setTabOrder(self.createBranchButton, self.deleteRegularButton)
        SvnTagDialog.setTabOrder(self.deleteRegularButton, self.deleteBranchButton)

    def retranslateUi(self, SvnTagDialog):
        SvnTagDialog.setWindowTitle(_translate("SvnTagDialog", "Subversion Tag", None))
        self.tagCombo.setToolTip(_translate("SvnTagDialog", "Enter the name of the tag", None))
        self.tagCombo.setWhatsThis(_translate("SvnTagDialog", "<b>Tag Name</b>\n"
"<p>Enter the name of the tag to be created, moved or deleted.</p>", None))
        self.TextLabel1.setText(_translate("SvnTagDialog", "Name:", None))
        self.TagActionGroup.setTitle(_translate("SvnTagDialog", "Tag Action", None))
        self.createRegularButton.setToolTip(_translate("SvnTagDialog", "Select to create a regular tag", None))
        self.createRegularButton.setWhatsThis(_translate("SvnTagDialog", "<b>Create Regular Tag</b>\n"
"<p>Select this entry in order to create a regular tag in the repository.</p>", None))
        self.createRegularButton.setText(_translate("SvnTagDialog", "Create Regular Tag", None))
        self.createBranchButton.setToolTip(_translate("SvnTagDialog", "Select to create a branch tag", None))
        self.createBranchButton.setWhatsThis(_translate("SvnTagDialog", "<b>Create Branch Tag</b>\n"
"<p>Select this entry in order to create a branch in the repository.</p>", None))
        self.createBranchButton.setText(_translate("SvnTagDialog", "Create Branch Tag", None))
        self.deleteRegularButton.setToolTip(_translate("SvnTagDialog", "Select to delete a regular tag", None))
        self.deleteRegularButton.setWhatsThis(_translate("SvnTagDialog", "<b>Delete Regular Tag</b>\n"
"<p>Select this entry in order to delete the selected regular tag.</p>", None))
        self.deleteRegularButton.setText(_translate("SvnTagDialog", "Delete Regular Tag", None))
        self.deleteBranchButton.setToolTip(_translate("SvnTagDialog", "Select to delete a branch tag", None))
        self.deleteBranchButton.setWhatsThis(_translate("SvnTagDialog", "<b>Delete Branch Tag</b>\n"
"<p>Select this entry in order to delete the selected branch tag.</p>", None))
        self.deleteBranchButton.setText(_translate("SvnTagDialog", "Delete Branch Tag", None))

