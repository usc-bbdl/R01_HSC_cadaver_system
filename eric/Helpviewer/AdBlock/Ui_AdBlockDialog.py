# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Helpviewer\AdBlock\AdBlockDialog.ui'
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

class Ui_AdBlockDialog(object):
    def setupUi(self, AdBlockDialog):
        AdBlockDialog.setObjectName(_fromUtf8("AdBlockDialog"))
        AdBlockDialog.resize(650, 600)
        AdBlockDialog.setSizeGripEnabled(True)
        self.verticalLayout_2 = QtGui.QVBoxLayout(AdBlockDialog)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.adBlockGroup = QtGui.QGroupBox(AdBlockDialog)
        self.adBlockGroup.setCheckable(True)
        self.adBlockGroup.setObjectName(_fromUtf8("adBlockGroup"))
        self.verticalLayout = QtGui.QVBoxLayout(self.adBlockGroup)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.searchEdit = QtGui.QLineEdit(self.adBlockGroup)
        self.searchEdit.setObjectName(_fromUtf8("searchEdit"))
        self.horizontalLayout.addWidget(self.searchEdit)
        self.clearButton = QtGui.QToolButton(self.adBlockGroup)
        self.clearButton.setText(_fromUtf8(""))
        self.clearButton.setObjectName(_fromUtf8("clearButton"))
        self.horizontalLayout.addWidget(self.clearButton)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.subscriptionsTree = E4TreeView(self.adBlockGroup)
        self.subscriptionsTree.setDragDropMode(QtGui.QAbstractItemView.InternalMove)
        self.subscriptionsTree.setAlternatingRowColors(True)
        self.subscriptionsTree.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.subscriptionsTree.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.subscriptionsTree.setUniformRowHeights(True)
        self.subscriptionsTree.setObjectName(_fromUtf8("subscriptionsTree"))
        self.verticalLayout.addWidget(self.subscriptionsTree)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.actionButton = QtGui.QToolButton(self.adBlockGroup)
        self.actionButton.setObjectName(_fromUtf8("actionButton"))
        self.horizontalLayout_3.addWidget(self.actionButton)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addWidget(self.adBlockGroup)
        self.buttonBox = QtGui.QDialogButtonBox(AdBlockDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(AdBlockDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), AdBlockDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), AdBlockDialog.reject)
        QtCore.QObject.connect(self.clearButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.searchEdit.clear)
        QtCore.QMetaObject.connectSlotsByName(AdBlockDialog)
        AdBlockDialog.setTabOrder(self.adBlockGroup, self.searchEdit)
        AdBlockDialog.setTabOrder(self.searchEdit, self.clearButton)
        AdBlockDialog.setTabOrder(self.clearButton, self.subscriptionsTree)
        AdBlockDialog.setTabOrder(self.subscriptionsTree, self.actionButton)
        AdBlockDialog.setTabOrder(self.actionButton, self.buttonBox)

    def retranslateUi(self, AdBlockDialog):
        AdBlockDialog.setWindowTitle(_translate("AdBlockDialog", "AdBlock Configuration", None))
        self.adBlockGroup.setTitle(_translate("AdBlockDialog", "Enable AdBlock", None))
        self.searchEdit.setToolTip(_translate("AdBlockDialog", "Enter search term for subscriptions and rules", None))
        self.clearButton.setToolTip(_translate("AdBlockDialog", "Press to clear the search edit", None))
        self.actionButton.setText(_translate("AdBlockDialog", "Actions", None))

from E4Gui.E4TreeView import E4TreeView
