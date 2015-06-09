# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Plugins\VcsPlugins\vcsPySvn\SvnRepoBrowserDialog.ui'
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
        SvnRepoBrowserDialog.resize(650, 500)
        self.gridlayout = QtGui.QGridLayout(SvnRepoBrowserDialog)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.label = QtGui.QLabel(SvnRepoBrowserDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridlayout.addWidget(self.label, 0, 0, 1, 1)
        self.urlCombo = QtGui.QComboBox(SvnRepoBrowserDialog)
        self.urlCombo.setEditable(True)
        self.urlCombo.setInsertPolicy(QtGui.QComboBox.InsertAtTop)
        self.urlCombo.setObjectName(_fromUtf8("urlCombo"))
        self.gridlayout.addWidget(self.urlCombo, 0, 1, 1, 1)
        self.repoTree = QtGui.QTreeWidget(SvnRepoBrowserDialog)
        self.repoTree.setAlternatingRowColors(True)
        self.repoTree.setAllColumnsShowFocus(True)
        self.repoTree.setColumnCount(5)
        self.repoTree.setObjectName(_fromUtf8("repoTree"))
        self.gridlayout.addWidget(self.repoTree, 1, 0, 1, 2)
        self.buttonBox = QtGui.QDialogButtonBox(SvnRepoBrowserDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Close|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridlayout.addWidget(self.buttonBox, 2, 1, 1, 1)

        self.retranslateUi(SvnRepoBrowserDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), SvnRepoBrowserDialog.reject)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), SvnRepoBrowserDialog.accept)
        QtCore.QMetaObject.connectSlotsByName(SvnRepoBrowserDialog)
        SvnRepoBrowserDialog.setTabOrder(self.urlCombo, self.repoTree)
        SvnRepoBrowserDialog.setTabOrder(self.repoTree, self.buttonBox)

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

