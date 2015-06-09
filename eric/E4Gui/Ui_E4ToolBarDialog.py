# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\E4Gui\E4ToolBarDialog.ui'
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

class Ui_E4ToolBarDialog(object):
    def setupUi(self, E4ToolBarDialog):
        E4ToolBarDialog.setObjectName(_fromUtf8("E4ToolBarDialog"))
        E4ToolBarDialog.resize(600, 500)
        E4ToolBarDialog.setSizeGripEnabled(True)
        self.vboxlayout = QtGui.QVBoxLayout(E4ToolBarDialog)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        self.label = QtGui.QLabel(E4ToolBarDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.hboxlayout.addWidget(self.label)
        self.toolbarComboBox = QtGui.QComboBox(E4ToolBarDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolbarComboBox.sizePolicy().hasHeightForWidth())
        self.toolbarComboBox.setSizePolicy(sizePolicy)
        self.toolbarComboBox.setObjectName(_fromUtf8("toolbarComboBox"))
        self.hboxlayout.addWidget(self.toolbarComboBox)
        self.newButton = QtGui.QPushButton(E4ToolBarDialog)
        self.newButton.setObjectName(_fromUtf8("newButton"))
        self.hboxlayout.addWidget(self.newButton)
        self.removeButton = QtGui.QPushButton(E4ToolBarDialog)
        self.removeButton.setObjectName(_fromUtf8("removeButton"))
        self.hboxlayout.addWidget(self.removeButton)
        self.renameButton = QtGui.QPushButton(E4ToolBarDialog)
        self.renameButton.setObjectName(_fromUtf8("renameButton"))
        self.hboxlayout.addWidget(self.renameButton)
        self.vboxlayout.addLayout(self.hboxlayout)
        self.line = QtGui.QFrame(E4ToolBarDialog)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.vboxlayout.addWidget(self.line)
        self.gridlayout = QtGui.QGridLayout()
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.label_2 = QtGui.QLabel(E4ToolBarDialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridlayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_3 = QtGui.QLabel(E4ToolBarDialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridlayout.addWidget(self.label_3, 0, 2, 1, 1)
        self.actionsTree = QtGui.QTreeWidget(E4ToolBarDialog)
        self.actionsTree.setAlternatingRowColors(True)
        self.actionsTree.setRootIsDecorated(False)
        self.actionsTree.setObjectName(_fromUtf8("actionsTree"))
        self.gridlayout.addWidget(self.actionsTree, 1, 0, 3, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridlayout.addItem(spacerItem, 1, 1, 1, 1)
        self.toolbarActionsList = QtGui.QListWidget(E4ToolBarDialog)
        self.toolbarActionsList.setObjectName(_fromUtf8("toolbarActionsList"))
        self.gridlayout.addWidget(self.toolbarActionsList, 1, 2, 3, 1)
        self.gridlayout1 = QtGui.QGridLayout()
        self.gridlayout1.setSpacing(0)
        self.gridlayout1.setObjectName(_fromUtf8("gridlayout1"))
        self.upButton = QtGui.QToolButton(E4ToolBarDialog)
        self.upButton.setText(_fromUtf8(""))
        self.upButton.setObjectName(_fromUtf8("upButton"))
        self.gridlayout1.addWidget(self.upButton, 0, 1, 1, 1)
        self.leftButton = QtGui.QToolButton(E4ToolBarDialog)
        self.leftButton.setText(_fromUtf8(""))
        self.leftButton.setObjectName(_fromUtf8("leftButton"))
        self.gridlayout1.addWidget(self.leftButton, 1, 0, 1, 1)
        self.rightButton = QtGui.QToolButton(E4ToolBarDialog)
        self.rightButton.setText(_fromUtf8(""))
        self.rightButton.setObjectName(_fromUtf8("rightButton"))
        self.gridlayout1.addWidget(self.rightButton, 1, 2, 1, 1)
        self.downButton = QtGui.QToolButton(E4ToolBarDialog)
        self.downButton.setText(_fromUtf8(""))
        self.downButton.setObjectName(_fromUtf8("downButton"))
        self.gridlayout1.addWidget(self.downButton, 2, 1, 1, 1)
        self.gridlayout.addLayout(self.gridlayout1, 2, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridlayout.addItem(spacerItem1, 3, 1, 1, 1)
        self.vboxlayout.addLayout(self.gridlayout)
        self.buttonBox = QtGui.QDialogButtonBox(E4ToolBarDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Apply|QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok|QtGui.QDialogButtonBox.Reset|QtGui.QDialogButtonBox.RestoreDefaults)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.vboxlayout.addWidget(self.buttonBox)
        self.label.setBuddy(self.toolbarComboBox)

        self.retranslateUi(E4ToolBarDialog)
        QtCore.QMetaObject.connectSlotsByName(E4ToolBarDialog)
        E4ToolBarDialog.setTabOrder(self.toolbarComboBox, self.newButton)
        E4ToolBarDialog.setTabOrder(self.newButton, self.removeButton)
        E4ToolBarDialog.setTabOrder(self.removeButton, self.renameButton)
        E4ToolBarDialog.setTabOrder(self.renameButton, self.actionsTree)
        E4ToolBarDialog.setTabOrder(self.actionsTree, self.toolbarActionsList)
        E4ToolBarDialog.setTabOrder(self.toolbarActionsList, self.upButton)
        E4ToolBarDialog.setTabOrder(self.upButton, self.downButton)
        E4ToolBarDialog.setTabOrder(self.downButton, self.rightButton)
        E4ToolBarDialog.setTabOrder(self.rightButton, self.leftButton)
        E4ToolBarDialog.setTabOrder(self.leftButton, self.buttonBox)

    def retranslateUi(self, E4ToolBarDialog):
        E4ToolBarDialog.setWindowTitle(_translate("E4ToolBarDialog", "Configure Toolbars", None))
        self.label.setText(_translate("E4ToolBarDialog", "&Toolbar:", None))
        self.toolbarComboBox.setToolTip(_translate("E4ToolBarDialog", "Select the toolbar to configure", None))
        self.newButton.setToolTip(_translate("E4ToolBarDialog", "Press to create a new toolbar", None))
        self.newButton.setText(_translate("E4ToolBarDialog", "&New", None))
        self.removeButton.setToolTip(_translate("E4ToolBarDialog", "Press to remove the selected toolbar", None))
        self.removeButton.setText(_translate("E4ToolBarDialog", "&Remove", None))
        self.renameButton.setToolTip(_translate("E4ToolBarDialog", "Press to rename the selected toolbar", None))
        self.renameButton.setText(_translate("E4ToolBarDialog", "R&ename", None))
        self.label_2.setText(_translate("E4ToolBarDialog", "Actions:", None))
        self.label_3.setText(_translate("E4ToolBarDialog", "Current Toolbar Actions:", None))
        self.actionsTree.setToolTip(_translate("E4ToolBarDialog", "Select the action to add to the current toolbar", None))
        self.toolbarActionsList.setToolTip(_translate("E4ToolBarDialog", "Select the action to work on", None))
        self.toolbarActionsList.setWhatsThis(_translate("E4ToolBarDialog", "<b>Current Toolbar Actions</b><p>This list shows the actions of the selected toolbar. Select an action and use the up or down button to change the order of actions or the left button to delete it. To add an action to the toolbar, select it in the list of available actions and press the right button.</p>", None))
        self.upButton.setToolTip(_translate("E4ToolBarDialog", "Press to move the selected action up.", None))
        self.leftButton.setToolTip(_translate("E4ToolBarDialog", "Press to delete the selected action from the toolbar", None))
        self.rightButton.setToolTip(_translate("E4ToolBarDialog", "Press to add the selected action to the toolbar", None))
        self.downButton.setToolTip(_translate("E4ToolBarDialog", "Press to move the selected action down.", None))

