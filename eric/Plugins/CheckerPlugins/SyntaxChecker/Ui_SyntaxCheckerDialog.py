# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Plugins\CheckerPlugins\SyntaxChecker\SyntaxCheckerDialog.ui'
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

class Ui_SyntaxCheckerDialog(object):
    def setupUi(self, SyntaxCheckerDialog):
        SyntaxCheckerDialog.setObjectName(_fromUtf8("SyntaxCheckerDialog"))
        SyntaxCheckerDialog.resize(572, 424)
        SyntaxCheckerDialog.setSizeGripEnabled(True)
        self.vboxlayout = QtGui.QVBoxLayout(SyntaxCheckerDialog)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.resultList = QtGui.QTreeWidget(SyntaxCheckerDialog)
        self.resultList.setAlternatingRowColors(True)
        self.resultList.setRootIsDecorated(False)
        self.resultList.setItemsExpandable(False)
        self.resultList.setObjectName(_fromUtf8("resultList"))
        self.vboxlayout.addWidget(self.resultList)
        self.checkProgress = QtGui.QProgressBar(SyntaxCheckerDialog)
        self.checkProgress.setProperty("value", 0)
        self.checkProgress.setOrientation(QtCore.Qt.Horizontal)
        self.checkProgress.setObjectName(_fromUtf8("checkProgress"))
        self.vboxlayout.addWidget(self.checkProgress)
        self.buttonBox = QtGui.QDialogButtonBox(SyntaxCheckerDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(SyntaxCheckerDialog)
        QtCore.QMetaObject.connectSlotsByName(SyntaxCheckerDialog)

    def retranslateUi(self, SyntaxCheckerDialog):
        SyntaxCheckerDialog.setWindowTitle(_translate("SyntaxCheckerDialog", "Syntax Check Result", None))
        SyntaxCheckerDialog.setWhatsThis(_translate("SyntaxCheckerDialog", "<b>Syntax Check Results</b>\n"
"<p>This dialog shows the results of the syntax check. Double clicking an\n"
"entry will open an editor window and position the cursor at the respective line.</p>", None))
        self.resultList.setWhatsThis(_translate("SyntaxCheckerDialog", "<b>Result List</b>\n"
"<p>This list shows the results of the syntax check. Double clicking\n"
"an entry will open this entry in an editor window and position the cursor at\n"
"the respective line.</p>", None))
        self.resultList.setSortingEnabled(True)
        self.resultList.headerItem().setText(0, _translate("SyntaxCheckerDialog", "Filename", None))
        self.resultList.headerItem().setText(1, _translate("SyntaxCheckerDialog", "#", None))
        self.resultList.headerItem().setText(2, _translate("SyntaxCheckerDialog", "Syntax Error", None))
        self.resultList.headerItem().setText(3, _translate("SyntaxCheckerDialog", "Source", None))
        self.checkProgress.setToolTip(_translate("SyntaxCheckerDialog", "Shows the progress of the syntax check action", None))

