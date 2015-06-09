# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Preferences\ToolGroupConfigurationDialog.ui'
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

class Ui_ToolGroupConfigurationDialog(object):
    def setupUi(self, ToolGroupConfigurationDialog):
        ToolGroupConfigurationDialog.setObjectName(_fromUtf8("ToolGroupConfigurationDialog"))
        ToolGroupConfigurationDialog.resize(475, 391)
        ToolGroupConfigurationDialog.setSizeGripEnabled(True)
        self.vboxlayout = QtGui.QVBoxLayout(ToolGroupConfigurationDialog)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.gridlayout = QtGui.QGridLayout()
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.deleteButton = QtGui.QPushButton(ToolGroupConfigurationDialog)
        self.deleteButton.setEnabled(False)
        self.deleteButton.setObjectName(_fromUtf8("deleteButton"))
        self.gridlayout.addWidget(self.deleteButton, 3, 2, 1, 1)
        self.addButton = QtGui.QPushButton(ToolGroupConfigurationDialog)
        self.addButton.setObjectName(_fromUtf8("addButton"))
        self.gridlayout.addWidget(self.addButton, 1, 2, 1, 1)
        self.TextLabel2 = QtGui.QLabel(ToolGroupConfigurationDialog)
        self.TextLabel2.setObjectName(_fromUtf8("TextLabel2"))
        self.gridlayout.addWidget(self.TextLabel2, 7, 0, 1, 1)
        self.changeButton = QtGui.QPushButton(ToolGroupConfigurationDialog)
        self.changeButton.setEnabled(False)
        self.changeButton.setObjectName(_fromUtf8("changeButton"))
        self.gridlayout.addWidget(self.changeButton, 2, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(87, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridlayout.addItem(spacerItem, 6, 2, 1, 1)
        self.newButton = QtGui.QPushButton(ToolGroupConfigurationDialog)
        self.newButton.setObjectName(_fromUtf8("newButton"))
        self.gridlayout.addWidget(self.newButton, 0, 2, 1, 1)
        self.upButton = QtGui.QPushButton(ToolGroupConfigurationDialog)
        self.upButton.setEnabled(False)
        self.upButton.setObjectName(_fromUtf8("upButton"))
        self.gridlayout.addWidget(self.upButton, 4, 2, 1, 1)
        self.downButton = QtGui.QPushButton(ToolGroupConfigurationDialog)
        self.downButton.setEnabled(False)
        self.downButton.setObjectName(_fromUtf8("downButton"))
        self.gridlayout.addWidget(self.downButton, 5, 2, 1, 1)
        self.groupsList = QtGui.QListWidget(ToolGroupConfigurationDialog)
        self.groupsList.setObjectName(_fromUtf8("groupsList"))
        self.gridlayout.addWidget(self.groupsList, 0, 0, 7, 2)
        self.nameEdit = QtGui.QLineEdit(ToolGroupConfigurationDialog)
        self.nameEdit.setObjectName(_fromUtf8("nameEdit"))
        self.gridlayout.addWidget(self.nameEdit, 7, 1, 1, 1)
        self.vboxlayout.addLayout(self.gridlayout)
        self.buttonBox = QtGui.QDialogButtonBox(ToolGroupConfigurationDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.vboxlayout.addWidget(self.buttonBox)
        self.TextLabel2.setBuddy(self.nameEdit)

        self.retranslateUi(ToolGroupConfigurationDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ToolGroupConfigurationDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ToolGroupConfigurationDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ToolGroupConfigurationDialog)
        ToolGroupConfigurationDialog.setTabOrder(self.groupsList, self.nameEdit)
        ToolGroupConfigurationDialog.setTabOrder(self.nameEdit, self.newButton)
        ToolGroupConfigurationDialog.setTabOrder(self.newButton, self.addButton)
        ToolGroupConfigurationDialog.setTabOrder(self.addButton, self.changeButton)
        ToolGroupConfigurationDialog.setTabOrder(self.changeButton, self.deleteButton)
        ToolGroupConfigurationDialog.setTabOrder(self.deleteButton, self.upButton)
        ToolGroupConfigurationDialog.setTabOrder(self.upButton, self.downButton)

    def retranslateUi(self, ToolGroupConfigurationDialog):
        ToolGroupConfigurationDialog.setWindowTitle(_translate("ToolGroupConfigurationDialog", "Configure Tool Groups", None))
        self.deleteButton.setToolTip(_translate("ToolGroupConfigurationDialog", "Delete the selected entry", None))
        self.deleteButton.setWhatsThis(_translate("ToolGroupConfigurationDialog", "<b>Delete</b>\n"
"<p>Delete the selected entry.</p>", None))
        self.deleteButton.setText(_translate("ToolGroupConfigurationDialog", "&Delete", None))
        self.deleteButton.setShortcut(_translate("ToolGroupConfigurationDialog", "Alt+D", None))
        self.addButton.setToolTip(_translate("ToolGroupConfigurationDialog", "Add a new tools entry", None))
        self.addButton.setWhatsThis(_translate("ToolGroupConfigurationDialog", "<b>Add</b>\n"
"<p>Add a new tool groups entry with the name entered below.</p>", None))
        self.addButton.setText(_translate("ToolGroupConfigurationDialog", "&Add", None))
        self.addButton.setShortcut(_translate("ToolGroupConfigurationDialog", "Alt+A", None))
        self.TextLabel2.setText(_translate("ToolGroupConfigurationDialog", "&Group name:", None))
        self.changeButton.setToolTip(_translate("ToolGroupConfigurationDialog", "Change the values of the selected entry", None))
        self.changeButton.setWhatsThis(_translate("ToolGroupConfigurationDialog", "<b>Change</b>\n"
"<p>Change the values of the selected entry.</p>", None))
        self.changeButton.setText(_translate("ToolGroupConfigurationDialog", "C&hange", None))
        self.changeButton.setShortcut(_translate("ToolGroupConfigurationDialog", "Alt+H", None))
        self.newButton.setToolTip(_translate("ToolGroupConfigurationDialog", "Clear all entry fields", None))
        self.newButton.setWhatsThis(_translate("ToolGroupConfigurationDialog", "<b>New</b>\n"
"<p>Clear all entry fields for entering a new tool groups entry.</p>", None))
        self.newButton.setText(_translate("ToolGroupConfigurationDialog", "&New", None))
        self.newButton.setShortcut(_translate("ToolGroupConfigurationDialog", "Alt+N", None))
        self.upButton.setToolTip(_translate("ToolGroupConfigurationDialog", "Move up", None))
        self.upButton.setWhatsThis(_translate("ToolGroupConfigurationDialog", "<b>Move Up</b>\n"
"<p>Move the selected entry up.</p>", None))
        self.upButton.setText(_translate("ToolGroupConfigurationDialog", "&Up", None))
        self.upButton.setShortcut(_translate("ToolGroupConfigurationDialog", "Alt+U", None))
        self.downButton.setToolTip(_translate("ToolGroupConfigurationDialog", "Move down", None))
        self.downButton.setWhatsThis(_translate("ToolGroupConfigurationDialog", "<b>Move Down</b>\n"
"<p>Move the selected entry down.</p>", None))
        self.downButton.setText(_translate("ToolGroupConfigurationDialog", "Do&wn", None))
        self.downButton.setShortcut(_translate("ToolGroupConfigurationDialog", "Alt+W", None))
        self.nameEdit.setToolTip(_translate("ToolGroupConfigurationDialog", "Enter the menu text", None))
        self.nameEdit.setWhatsThis(_translate("ToolGroupConfigurationDialog", "<b>Menu text</b>\n"
"<p>Enter the menu text. Precede the accelerator key with an & character.</p>", None))

