# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Plugins\VcsPlugins\vcsPySvn\SvnBlameDialog.ui'
#
# Created: Fri Apr 18 09:56:41 2014
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

class Ui_SvnBlameDialog(object):
    def setupUi(self, SvnBlameDialog):
        SvnBlameDialog.setObjectName(_fromUtf8("SvnBlameDialog"))
        SvnBlameDialog.resize(690, 750)
        SvnBlameDialog.setSizeGripEnabled(True)
        self.vboxlayout = QtGui.QVBoxLayout(SvnBlameDialog)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.blameList = QtGui.QTreeWidget(SvnBlameDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(6)
        sizePolicy.setHeightForWidth(self.blameList.sizePolicy().hasHeightForWidth())
        self.blameList.setSizePolicy(sizePolicy)
        self.blameList.setAlternatingRowColors(True)
        self.blameList.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.blameList.setRootIsDecorated(False)
        self.blameList.setItemsExpandable(False)
        self.blameList.setObjectName(_fromUtf8("blameList"))
        self.vboxlayout.addWidget(self.blameList)
        self.errorGroup = QtGui.QGroupBox(SvnBlameDialog)
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
        self.buttonBox = QtGui.QDialogButtonBox(SvnBlameDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(SvnBlameDialog)
        QtCore.QMetaObject.connectSlotsByName(SvnBlameDialog)
        SvnBlameDialog.setTabOrder(self.blameList, self.errors)
        SvnBlameDialog.setTabOrder(self.errors, self.buttonBox)

    def retranslateUi(self, SvnBlameDialog):
        SvnBlameDialog.setWindowTitle(_translate("SvnBlameDialog", "Subversion Blame", None))
        self.blameList.headerItem().setText(0, _translate("SvnBlameDialog", "Revision", None))
        self.blameList.headerItem().setText(1, _translate("SvnBlameDialog", "Author", None))
        self.blameList.headerItem().setText(2, _translate("SvnBlameDialog", "Line", None))
        self.errorGroup.setTitle(_translate("SvnBlameDialog", "Errors", None))

