# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Helpviewer\History\HistoryDialog.ui'
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

class Ui_HistoryDialog(object):
    def setupUi(self, HistoryDialog):
        HistoryDialog.setObjectName(_fromUtf8("HistoryDialog"))
        HistoryDialog.resize(750, 450)
        HistoryDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtGui.QVBoxLayout(HistoryDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.searchEdit = QtGui.QLineEdit(HistoryDialog)
        self.searchEdit.setObjectName(_fromUtf8("searchEdit"))
        self.horizontalLayout.addWidget(self.searchEdit)
        self.clearButton = QtGui.QToolButton(HistoryDialog)
        self.clearButton.setText(_fromUtf8(""))
        self.clearButton.setObjectName(_fromUtf8("clearButton"))
        self.horizontalLayout.addWidget(self.clearButton)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.historyTree = E4TreeView(HistoryDialog)
        self.historyTree.setAlternatingRowColors(True)
        self.historyTree.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.historyTree.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.historyTree.setUniformRowHeights(True)
        self.historyTree.setObjectName(_fromUtf8("historyTree"))
        self.verticalLayout.addWidget(self.historyTree)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.removeButton = QtGui.QPushButton(HistoryDialog)
        self.removeButton.setAutoDefault(False)
        self.removeButton.setObjectName(_fromUtf8("removeButton"))
        self.horizontalLayout_3.addWidget(self.removeButton)
        self.removeAllButton = QtGui.QPushButton(HistoryDialog)
        self.removeAllButton.setAutoDefault(False)
        self.removeAllButton.setObjectName(_fromUtf8("removeAllButton"))
        self.horizontalLayout_3.addWidget(self.removeAllButton)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.buttonBox = QtGui.QDialogButtonBox(HistoryDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(HistoryDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), HistoryDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), HistoryDialog.reject)
        QtCore.QObject.connect(self.clearButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.searchEdit.clear)
        QtCore.QMetaObject.connectSlotsByName(HistoryDialog)
        HistoryDialog.setTabOrder(self.searchEdit, self.clearButton)
        HistoryDialog.setTabOrder(self.clearButton, self.historyTree)
        HistoryDialog.setTabOrder(self.historyTree, self.removeButton)
        HistoryDialog.setTabOrder(self.removeButton, self.removeAllButton)
        HistoryDialog.setTabOrder(self.removeAllButton, self.buttonBox)

    def retranslateUi(self, HistoryDialog):
        HistoryDialog.setWindowTitle(_translate("HistoryDialog", "Manage History", None))
        self.searchEdit.setToolTip(_translate("HistoryDialog", "Enter search term for history entries", None))
        self.clearButton.setToolTip(_translate("HistoryDialog", "Press to clear the search edit", None))
        self.removeButton.setToolTip(_translate("HistoryDialog", "Press to remove the selected entries", None))
        self.removeButton.setText(_translate("HistoryDialog", "&Remove", None))
        self.removeAllButton.setToolTip(_translate("HistoryDialog", "Press to remove all entries", None))
        self.removeAllButton.setText(_translate("HistoryDialog", "Remove &All", None))

from E4Gui.E4TreeView import E4TreeView
