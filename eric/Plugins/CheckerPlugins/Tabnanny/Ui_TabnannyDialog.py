# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Plugins\CheckerPlugins\Tabnanny\TabnannyDialog.ui'
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

class Ui_TabnannyDialog(object):
    def setupUi(self, TabnannyDialog):
        TabnannyDialog.setObjectName(_fromUtf8("TabnannyDialog"))
        TabnannyDialog.resize(572, 339)
        TabnannyDialog.setSizeGripEnabled(True)
        self.vboxlayout = QtGui.QVBoxLayout(TabnannyDialog)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.resultList = QtGui.QTreeWidget(TabnannyDialog)
        self.resultList.setAlternatingRowColors(True)
        self.resultList.setRootIsDecorated(False)
        self.resultList.setItemsExpandable(False)
        self.resultList.setObjectName(_fromUtf8("resultList"))
        self.vboxlayout.addWidget(self.resultList)
        self.checkProgress = QtGui.QProgressBar(TabnannyDialog)
        self.checkProgress.setProperty("value", 0)
        self.checkProgress.setOrientation(QtCore.Qt.Horizontal)
        self.checkProgress.setObjectName(_fromUtf8("checkProgress"))
        self.vboxlayout.addWidget(self.checkProgress)
        self.buttonBox = QtGui.QDialogButtonBox(TabnannyDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(TabnannyDialog)
        QtCore.QMetaObject.connectSlotsByName(TabnannyDialog)

    def retranslateUi(self, TabnannyDialog):
        TabnannyDialog.setWindowTitle(_translate("TabnannyDialog", "Tabnanny Result", None))
        TabnannyDialog.setWhatsThis(_translate("TabnannyDialog", "<b>Tabnanny Results</b>\n"
"<p>This dialog shows the results of the tabnanny command. Double clicking an\n"
"entry will open an editor window and position the cursor at the respective line.</p>", None))
        self.resultList.setWhatsThis(_translate("TabnannyDialog", "<b>Result List</b>\n"
"<p>This list shows the results of the tabnanny command. Double clicking\n"
"an entry will open this entry in an editor window and position the cursor at\n"
"the respective line.</p>", None))
        self.resultList.setSortingEnabled(True)
        self.resultList.headerItem().setText(0, _translate("TabnannyDialog", "Filename", None))
        self.resultList.headerItem().setText(1, _translate("TabnannyDialog", "#", None))
        self.resultList.headerItem().setText(2, _translate("TabnannyDialog", "Source", None))
        self.checkProgress.setToolTip(_translate("TabnannyDialog", "Shows the progress of the tabnanny action", None))

