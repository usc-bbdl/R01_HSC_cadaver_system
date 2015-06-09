# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\QScintilla\ShellHistoryDialog.ui'
#
# Created: Fri Apr 18 09:56:43 2014
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

class Ui_ShellHistoryDialog(object):
    def setupUi(self, ShellHistoryDialog):
        ShellHistoryDialog.setObjectName(_fromUtf8("ShellHistoryDialog"))
        ShellHistoryDialog.resize(540, 506)
        ShellHistoryDialog.setSizeGripEnabled(True)
        self.gridLayout = QtGui.QGridLayout(ShellHistoryDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.historyList = QtGui.QListWidget(ShellHistoryDialog)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Monospace"))
        self.historyList.setFont(font)
        self.historyList.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.historyList.setAlternatingRowColors(True)
        self.historyList.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.historyList.setWordWrap(True)
        self.historyList.setObjectName(_fromUtf8("historyList"))
        self.gridLayout.addWidget(self.historyList, 0, 0, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.deleteButton = QtGui.QPushButton(ShellHistoryDialog)
        self.deleteButton.setEnabled(False)
        self.deleteButton.setObjectName(_fromUtf8("deleteButton"))
        self.verticalLayout.addWidget(self.deleteButton)
        self.copyButton = QtGui.QPushButton(ShellHistoryDialog)
        self.copyButton.setEnabled(False)
        self.copyButton.setObjectName(_fromUtf8("copyButton"))
        self.verticalLayout.addWidget(self.copyButton)
        self.executeButton = QtGui.QPushButton(ShellHistoryDialog)
        self.executeButton.setEnabled(False)
        self.executeButton.setObjectName(_fromUtf8("executeButton"))
        self.verticalLayout.addWidget(self.executeButton)
        self.reloadButton = QtGui.QPushButton(ShellHistoryDialog)
        self.reloadButton.setObjectName(_fromUtf8("reloadButton"))
        self.verticalLayout.addWidget(self.reloadButton)
        spacerItem = QtGui.QSpacerItem(72, 208, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(ShellHistoryDialog)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 2)

        self.retranslateUi(ShellHistoryDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ShellHistoryDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ShellHistoryDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ShellHistoryDialog)
        ShellHistoryDialog.setTabOrder(self.historyList, self.deleteButton)
        ShellHistoryDialog.setTabOrder(self.deleteButton, self.copyButton)
        ShellHistoryDialog.setTabOrder(self.copyButton, self.executeButton)
        ShellHistoryDialog.setTabOrder(self.executeButton, self.reloadButton)
        ShellHistoryDialog.setTabOrder(self.reloadButton, self.buttonBox)

    def retranslateUi(self, ShellHistoryDialog):
        ShellHistoryDialog.setWindowTitle(_translate("ShellHistoryDialog", "Shell History", None))
        self.deleteButton.setToolTip(_translate("ShellHistoryDialog", "Delete the selected entries", None))
        self.deleteButton.setText(_translate("ShellHistoryDialog", "&Delete", None))
        self.copyButton.setToolTip(_translate("ShellHistoryDialog", "Copy the selected entries to the current editor", None))
        self.copyButton.setText(_translate("ShellHistoryDialog", "C&opy", None))
        self.executeButton.setToolTip(_translate("ShellHistoryDialog", "Execute the selected entries", None))
        self.executeButton.setText(_translate("ShellHistoryDialog", "&Execute", None))
        self.reloadButton.setToolTip(_translate("ShellHistoryDialog", "Reload the history", None))
        self.reloadButton.setText(_translate("ShellHistoryDialog", "&Reload", None))

