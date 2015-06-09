# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Plugins\VcsPlugins\vcsPySvn\SvnLogDialog.ui'
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

class Ui_SvnLogDialog(object):
    def setupUi(self, SvnLogDialog):
        SvnLogDialog.setObjectName(_fromUtf8("SvnLogDialog"))
        SvnLogDialog.resize(751, 649)
        self.vboxlayout = QtGui.QVBoxLayout(SvnLogDialog)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.contentsGroup = QtGui.QGroupBox(SvnLogDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(self.contentsGroup.sizePolicy().hasHeightForWidth())
        self.contentsGroup.setSizePolicy(sizePolicy)
        self.contentsGroup.setObjectName(_fromUtf8("contentsGroup"))
        self.vboxlayout1 = QtGui.QVBoxLayout(self.contentsGroup)
        self.vboxlayout1.setObjectName(_fromUtf8("vboxlayout1"))
        self.contents = QtGui.QTextBrowser(self.contentsGroup)
        self.contents.setObjectName(_fromUtf8("contents"))
        self.vboxlayout1.addWidget(self.contents)
        self.vboxlayout.addWidget(self.contentsGroup)
        self.errorGroup = QtGui.QGroupBox(SvnLogDialog)
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
        self.buttonBox = QtGui.QDialogButtonBox(SvnLogDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(SvnLogDialog)
        QtCore.QMetaObject.connectSlotsByName(SvnLogDialog)
        SvnLogDialog.setTabOrder(self.contents, self.errors)
        SvnLogDialog.setTabOrder(self.errors, self.buttonBox)

    def retranslateUi(self, SvnLogDialog):
        SvnLogDialog.setWindowTitle(_translate("SvnLogDialog", "Subversion Log", None))
        self.contentsGroup.setTitle(_translate("SvnLogDialog", "Log", None))
        self.contents.setWhatsThis(_translate("SvnLogDialog", "<b>Subversion Log</b><p>This shows the output of the svn log command. By clicking on the links you may show the difference between versions.</p>", None))
        self.errorGroup.setTitle(_translate("SvnLogDialog", "Errors", None))
        self.errors.setWhatsThis(_translate("SvnLogDialog", "<b>Subversion log errors</b><p>This shows possible error messages of the svn log command.</p>", None))

