# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Plugins\VcsPlugins\vcsSubversion\SvnUrlSelectionDialog.ui'
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

class Ui_SvnUrlSelectionDialog(object):
    def setupUi(self, SvnUrlSelectionDialog):
        SvnUrlSelectionDialog.setObjectName(_fromUtf8("SvnUrlSelectionDialog"))
        SvnUrlSelectionDialog.resize(542, 195)
        SvnUrlSelectionDialog.setSizeGripEnabled(True)
        self.vboxlayout = QtGui.QVBoxLayout(SvnUrlSelectionDialog)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.urlGroup1 = QtGui.QGroupBox(SvnUrlSelectionDialog)
        self.urlGroup1.setObjectName(_fromUtf8("urlGroup1"))
        self.hboxlayout = QtGui.QHBoxLayout(self.urlGroup1)
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        self.repoRootLabel1 = QtGui.QLabel(self.urlGroup1)
        self.repoRootLabel1.setObjectName(_fromUtf8("repoRootLabel1"))
        self.hboxlayout.addWidget(self.repoRootLabel1)
        self.typeCombo1 = QtGui.QComboBox(self.urlGroup1)
        self.typeCombo1.setObjectName(_fromUtf8("typeCombo1"))
        self.hboxlayout.addWidget(self.typeCombo1)
        self.labelCombo1 = QtGui.QComboBox(self.urlGroup1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelCombo1.sizePolicy().hasHeightForWidth())
        self.labelCombo1.setSizePolicy(sizePolicy)
        self.labelCombo1.setEditable(True)
        self.labelCombo1.setObjectName(_fromUtf8("labelCombo1"))
        self.hboxlayout.addWidget(self.labelCombo1)
        self.vboxlayout.addWidget(self.urlGroup1)
        self.urlGroup2 = QtGui.QGroupBox(SvnUrlSelectionDialog)
        self.urlGroup2.setObjectName(_fromUtf8("urlGroup2"))
        self.hboxlayout1 = QtGui.QHBoxLayout(self.urlGroup2)
        self.hboxlayout1.setObjectName(_fromUtf8("hboxlayout1"))
        self.repoRootLabel2 = QtGui.QLabel(self.urlGroup2)
        self.repoRootLabel2.setObjectName(_fromUtf8("repoRootLabel2"))
        self.hboxlayout1.addWidget(self.repoRootLabel2)
        self.typeCombo2 = QtGui.QComboBox(self.urlGroup2)
        self.typeCombo2.setObjectName(_fromUtf8("typeCombo2"))
        self.hboxlayout1.addWidget(self.typeCombo2)
        self.labelCombo2 = QtGui.QComboBox(self.urlGroup2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelCombo2.sizePolicy().hasHeightForWidth())
        self.labelCombo2.setSizePolicy(sizePolicy)
        self.labelCombo2.setEditable(True)
        self.labelCombo2.setObjectName(_fromUtf8("labelCombo2"))
        self.hboxlayout1.addWidget(self.labelCombo2)
        self.vboxlayout.addWidget(self.urlGroup2)
        self.summaryCheckBox = QtGui.QCheckBox(SvnUrlSelectionDialog)
        self.summaryCheckBox.setObjectName(_fromUtf8("summaryCheckBox"))
        self.vboxlayout.addWidget(self.summaryCheckBox)
        self.buttonBox = QtGui.QDialogButtonBox(SvnUrlSelectionDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(SvnUrlSelectionDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), SvnUrlSelectionDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), SvnUrlSelectionDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SvnUrlSelectionDialog)
        SvnUrlSelectionDialog.setTabOrder(self.typeCombo1, self.labelCombo1)
        SvnUrlSelectionDialog.setTabOrder(self.labelCombo1, self.typeCombo2)
        SvnUrlSelectionDialog.setTabOrder(self.typeCombo2, self.labelCombo2)
        SvnUrlSelectionDialog.setTabOrder(self.labelCombo2, self.summaryCheckBox)
        SvnUrlSelectionDialog.setTabOrder(self.summaryCheckBox, self.buttonBox)

    def retranslateUi(self, SvnUrlSelectionDialog):
        SvnUrlSelectionDialog.setWindowTitle(_translate("SvnUrlSelectionDialog", "Subversion Diff", None))
        self.urlGroup1.setTitle(_translate("SvnUrlSelectionDialog", "Repository URL 1", None))
        self.typeCombo1.setToolTip(_translate("SvnUrlSelectionDialog", "Select the URL type", None))
        self.labelCombo1.setToolTip(_translate("SvnUrlSelectionDialog", "Enter the label name or path", None))
        self.urlGroup2.setTitle(_translate("SvnUrlSelectionDialog", "Repository URL 2", None))
        self.typeCombo2.setToolTip(_translate("SvnUrlSelectionDialog", "Select the URL type", None))
        self.labelCombo2.setToolTip(_translate("SvnUrlSelectionDialog", "Enter the label name or path", None))
        self.summaryCheckBox.setToolTip(_translate("SvnUrlSelectionDialog", "Select to just show a summary of differences", None))
        self.summaryCheckBox.setText(_translate("SvnUrlSelectionDialog", "Summary only", None))

