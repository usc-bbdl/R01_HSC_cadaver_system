# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Plugins\VcsPlugins\vcsSubversion\SvnSwitchDialog.ui'
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

class Ui_SvnSwitchDialog(object):
    def setupUi(self, SvnSwitchDialog):
        SvnSwitchDialog.setObjectName(_fromUtf8("SvnSwitchDialog"))
        SvnSwitchDialog.resize(391, 146)
        SvnSwitchDialog.setSizeGripEnabled(True)
        self.gridlayout = QtGui.QGridLayout(SvnSwitchDialog)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.buttonBox = QtGui.QDialogButtonBox(SvnSwitchDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridlayout.addWidget(self.buttonBox, 2, 0, 1, 2)
        self.TextLabel1 = QtGui.QLabel(SvnSwitchDialog)
        self.TextLabel1.setObjectName(_fromUtf8("TextLabel1"))
        self.gridlayout.addWidget(self.TextLabel1, 0, 0, 1, 1)
        self.tagCombo = QtGui.QComboBox(SvnSwitchDialog)
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
        self.TagTypeGroup = QtGui.QGroupBox(SvnSwitchDialog)
        self.TagTypeGroup.setObjectName(_fromUtf8("TagTypeGroup"))
        self.vboxlayout = QtGui.QVBoxLayout(self.TagTypeGroup)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.regularButton = QtGui.QRadioButton(self.TagTypeGroup)
        self.regularButton.setChecked(True)
        self.regularButton.setObjectName(_fromUtf8("regularButton"))
        self.vboxlayout.addWidget(self.regularButton)
        self.branchButton = QtGui.QRadioButton(self.TagTypeGroup)
        self.branchButton.setObjectName(_fromUtf8("branchButton"))
        self.vboxlayout.addWidget(self.branchButton)
        self.gridlayout.addWidget(self.TagTypeGroup, 1, 1, 1, 1)

        self.retranslateUi(SvnSwitchDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), SvnSwitchDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), SvnSwitchDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SvnSwitchDialog)
        SvnSwitchDialog.setTabOrder(self.tagCombo, self.regularButton)
        SvnSwitchDialog.setTabOrder(self.regularButton, self.branchButton)

    def retranslateUi(self, SvnSwitchDialog):
        SvnSwitchDialog.setWindowTitle(_translate("SvnSwitchDialog", "Subversion Switch", None))
        self.TextLabel1.setText(_translate("SvnSwitchDialog", "Tag Name:", None))
        self.tagCombo.setToolTip(_translate("SvnSwitchDialog", "Enter the name of the tag", None))
        self.tagCombo.setWhatsThis(_translate("SvnSwitchDialog", "<b>Tag Name</b>\n"
"<p>Enter the name of the tag to be switched to.\n"
"In order to switch to the trunk version leave it empty.</p>", None))
        self.TagTypeGroup.setTitle(_translate("SvnSwitchDialog", "Tag Type", None))
        self.regularButton.setToolTip(_translate("SvnSwitchDialog", "Select for a regular tag", None))
        self.regularButton.setWhatsThis(_translate("SvnSwitchDialog", "<b>Regular Tag</b>\n"
"<p>Select this entry for a regular tag.</p>", None))
        self.regularButton.setText(_translate("SvnSwitchDialog", "Regular Tag", None))
        self.branchButton.setToolTip(_translate("SvnSwitchDialog", "Select for a branch tag", None))
        self.branchButton.setWhatsThis(_translate("SvnSwitchDialog", "<b>Branch Tag</b>\n"
"<p>Select this entry for a branch tag.</p>", None))
        self.branchButton.setText(_translate("SvnSwitchDialog", "Branch Tag", None))

