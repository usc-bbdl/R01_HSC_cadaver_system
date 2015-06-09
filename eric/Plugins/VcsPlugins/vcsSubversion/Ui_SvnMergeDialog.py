# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Plugins\VcsPlugins\vcsSubversion\SvnMergeDialog.ui'
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

class Ui_SvnMergeDialog(object):
    def setupUi(self, SvnMergeDialog):
        SvnMergeDialog.setObjectName(_fromUtf8("SvnMergeDialog"))
        SvnMergeDialog.resize(456, 152)
        SvnMergeDialog.setSizeGripEnabled(True)
        self.gridlayout = QtGui.QGridLayout(SvnMergeDialog)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.forceCheckBox = QtGui.QCheckBox(SvnMergeDialog)
        self.forceCheckBox.setObjectName(_fromUtf8("forceCheckBox"))
        self.gridlayout.addWidget(self.forceCheckBox, 3, 0, 1, 2)
        self.buttonBox = QtGui.QDialogButtonBox(SvnMergeDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridlayout.addWidget(self.buttonBox, 4, 0, 1, 2)
        self.textLabel1 = QtGui.QLabel(SvnMergeDialog)
        self.textLabel1.setObjectName(_fromUtf8("textLabel1"))
        self.gridlayout.addWidget(self.textLabel1, 2, 0, 1, 1)
        self.targetCombo = QtGui.QComboBox(SvnMergeDialog)
        self.targetCombo.setEditable(True)
        self.targetCombo.setInsertPolicy(QtGui.QComboBox.InsertAtTop)
        self.targetCombo.setAutoCompletion(True)
        self.targetCombo.setDuplicatesEnabled(False)
        self.targetCombo.setObjectName(_fromUtf8("targetCombo"))
        self.gridlayout.addWidget(self.targetCombo, 2, 1, 1, 1)
        self.TextLabel1 = QtGui.QLabel(SvnMergeDialog)
        self.TextLabel1.setObjectName(_fromUtf8("TextLabel1"))
        self.gridlayout.addWidget(self.TextLabel1, 0, 0, 1, 1)
        self.tag2Combo = QtGui.QComboBox(SvnMergeDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tag2Combo.sizePolicy().hasHeightForWidth())
        self.tag2Combo.setSizePolicy(sizePolicy)
        self.tag2Combo.setEditable(True)
        self.tag2Combo.setAutoCompletion(True)
        self.tag2Combo.setDuplicatesEnabled(False)
        self.tag2Combo.setObjectName(_fromUtf8("tag2Combo"))
        self.gridlayout.addWidget(self.tag2Combo, 1, 1, 1, 1)
        self.tag1Combo = QtGui.QComboBox(SvnMergeDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tag1Combo.sizePolicy().hasHeightForWidth())
        self.tag1Combo.setSizePolicy(sizePolicy)
        self.tag1Combo.setEditable(True)
        self.tag1Combo.setAutoCompletion(True)
        self.tag1Combo.setDuplicatesEnabled(False)
        self.tag1Combo.setObjectName(_fromUtf8("tag1Combo"))
        self.gridlayout.addWidget(self.tag1Combo, 0, 1, 1, 1)
        self.TextLabel1_2 = QtGui.QLabel(SvnMergeDialog)
        self.TextLabel1_2.setObjectName(_fromUtf8("TextLabel1_2"))
        self.gridlayout.addWidget(self.TextLabel1_2, 1, 0, 1, 1)

        self.retranslateUi(SvnMergeDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), SvnMergeDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), SvnMergeDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SvnMergeDialog)
        SvnMergeDialog.setTabOrder(self.tag1Combo, self.tag2Combo)
        SvnMergeDialog.setTabOrder(self.tag2Combo, self.targetCombo)
        SvnMergeDialog.setTabOrder(self.targetCombo, self.forceCheckBox)
        SvnMergeDialog.setTabOrder(self.forceCheckBox, self.buttonBox)

    def retranslateUi(self, SvnMergeDialog):
        SvnMergeDialog.setWindowTitle(_translate("SvnMergeDialog", "Subversion Merge", None))
        self.forceCheckBox.setToolTip(_translate("SvnMergeDialog", "Select to force the merge operation", None))
        self.forceCheckBox.setText(_translate("SvnMergeDialog", "Enforce merge", None))
        self.textLabel1.setText(_translate("SvnMergeDialog", "Target:", None))
        self.targetCombo.setToolTip(_translate("SvnMergeDialog", "Enter the target", None))
        self.targetCombo.setWhatsThis(_translate("SvnMergeDialog", "<b>Target</b>\n"
"<p>Enter the target for the merge operation into this field. Leave it empty to\n"
"get the target URL from the working copy.</p>\n"
"<p><b>Note:</b> This entry is only needed, if you enter revision numbers above.</p>", None))
        self.TextLabel1.setText(_translate("SvnMergeDialog", "1. URL/Revision:", None))
        self.tag2Combo.setToolTip(_translate("SvnMergeDialog", "Enter an URL or a revision number", None))
        self.tag2Combo.setWhatsThis(_translate("SvnMergeDialog", "<b>URL/Revision</b>\n"
"<p>Enter an URL or a revision number to be merged into\n"
"the working copy.</p>", None))
        self.tag1Combo.setToolTip(_translate("SvnMergeDialog", "Enter an URL or a revision number", None))
        self.tag1Combo.setWhatsThis(_translate("SvnMergeDialog", "<b>URL/Revision</b>\n"
"<p>Enter an URL or a revision number to be merged into\n"
"the working copy.</p>", None))
        self.TextLabel1_2.setText(_translate("SvnMergeDialog", "2. URL/Revision:", None))

