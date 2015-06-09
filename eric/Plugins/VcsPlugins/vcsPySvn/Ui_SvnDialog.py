# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Plugins\VcsPlugins\vcsPySvn\SvnDialog.ui'
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

class Ui_SvnDialog(object):
    def setupUi(self, SvnDialog):
        SvnDialog.setObjectName(_fromUtf8("SvnDialog"))
        SvnDialog.resize(593, 499)
        SvnDialog.setSizeGripEnabled(True)
        self.vboxlayout = QtGui.QVBoxLayout(SvnDialog)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.outputGroup = QtGui.QGroupBox(SvnDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.outputGroup.sizePolicy().hasHeightForWidth())
        self.outputGroup.setSizePolicy(sizePolicy)
        self.outputGroup.setObjectName(_fromUtf8("outputGroup"))
        self.vboxlayout1 = QtGui.QVBoxLayout(self.outputGroup)
        self.vboxlayout1.setObjectName(_fromUtf8("vboxlayout1"))
        self.resultbox = QtGui.QTextEdit(self.outputGroup)
        self.resultbox.setReadOnly(True)
        self.resultbox.setAcceptRichText(False)
        self.resultbox.setObjectName(_fromUtf8("resultbox"))
        self.vboxlayout1.addWidget(self.resultbox)
        self.vboxlayout.addWidget(self.outputGroup)
        self.errorGroup = QtGui.QGroupBox(SvnDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.errorGroup.sizePolicy().hasHeightForWidth())
        self.errorGroup.setSizePolicy(sizePolicy)
        self.errorGroup.setObjectName(_fromUtf8("errorGroup"))
        self.vboxlayout2 = QtGui.QVBoxLayout(self.errorGroup)
        self.vboxlayout2.setObjectName(_fromUtf8("vboxlayout2"))
        self.errors = QtGui.QTextEdit(self.errorGroup)
        self.errors.setReadOnly(True)
        self.errors.setAcceptRichText(False)
        self.errors.setObjectName(_fromUtf8("errors"))
        self.vboxlayout2.addWidget(self.errors)
        self.vboxlayout.addWidget(self.errorGroup)
        self.buttonBox = QtGui.QDialogButtonBox(SvnDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(SvnDialog)
        QtCore.QMetaObject.connectSlotsByName(SvnDialog)
        SvnDialog.setTabOrder(self.resultbox, self.errors)
        SvnDialog.setTabOrder(self.errors, self.buttonBox)

    def retranslateUi(self, SvnDialog):
        SvnDialog.setWindowTitle(_translate("SvnDialog", "Subversion", None))
        self.outputGroup.setTitle(_translate("SvnDialog", "Output", None))
        self.errorGroup.setTitle(_translate("SvnDialog", "Errors", None))

