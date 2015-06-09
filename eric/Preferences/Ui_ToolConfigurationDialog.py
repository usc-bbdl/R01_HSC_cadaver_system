# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Preferences\ToolConfigurationDialog.ui'
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

class Ui_ToolConfigurationDialog(object):
    def setupUi(self, ToolConfigurationDialog):
        ToolConfigurationDialog.setObjectName(_fromUtf8("ToolConfigurationDialog"))
        ToolConfigurationDialog.resize(591, 487)
        ToolConfigurationDialog.setSizeGripEnabled(True)
        self.vboxlayout = QtGui.QVBoxLayout(ToolConfigurationDialog)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.gridlayout = QtGui.QGridLayout()
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.separatorButton = QtGui.QPushButton(ToolConfigurationDialog)
        self.separatorButton.setObjectName(_fromUtf8("separatorButton"))
        self.gridlayout.addWidget(self.separatorButton, 7, 3, 1, 1)
        self.addButton = QtGui.QPushButton(ToolConfigurationDialog)
        self.addButton.setObjectName(_fromUtf8("addButton"))
        self.gridlayout.addWidget(self.addButton, 1, 3, 1, 1)
        self.toolsList = QtGui.QListWidget(ToolConfigurationDialog)
        self.toolsList.setObjectName(_fromUtf8("toolsList"))
        self.gridlayout.addWidget(self.toolsList, 0, 0, 9, 3)
        self.redirectCombo = QtGui.QComboBox(ToolConfigurationDialog)
        self.redirectCombo.setObjectName(_fromUtf8("redirectCombo"))
        self.gridlayout.addWidget(self.redirectCombo, 13, 1, 1, 2)
        self.argumentsEdit = QtGui.QLineEdit(ToolConfigurationDialog)
        self.argumentsEdit.setObjectName(_fromUtf8("argumentsEdit"))
        self.gridlayout.addWidget(self.argumentsEdit, 12, 1, 1, 1)
        self.upButton = QtGui.QPushButton(ToolConfigurationDialog)
        self.upButton.setEnabled(False)
        self.upButton.setObjectName(_fromUtf8("upButton"))
        self.gridlayout.addWidget(self.upButton, 4, 3, 1, 1)
        self.deleteButton = QtGui.QPushButton(ToolConfigurationDialog)
        self.deleteButton.setEnabled(False)
        self.deleteButton.setObjectName(_fromUtf8("deleteButton"))
        self.gridlayout.addWidget(self.deleteButton, 3, 3, 1, 1)
        self.newButton = QtGui.QPushButton(ToolConfigurationDialog)
        self.newButton.setObjectName(_fromUtf8("newButton"))
        self.gridlayout.addWidget(self.newButton, 0, 3, 1, 1)
        self.iconButton = QtGui.QPushButton(ToolConfigurationDialog)
        self.iconButton.setObjectName(_fromUtf8("iconButton"))
        self.gridlayout.addWidget(self.iconButton, 10, 2, 1, 1)
        self.executableEdit = QtGui.QLineEdit(ToolConfigurationDialog)
        self.executableEdit.setObjectName(_fromUtf8("executableEdit"))
        self.gridlayout.addWidget(self.executableEdit, 11, 1, 1, 1)
        self.downButton = QtGui.QPushButton(ToolConfigurationDialog)
        self.downButton.setEnabled(False)
        self.downButton.setObjectName(_fromUtf8("downButton"))
        self.gridlayout.addWidget(self.downButton, 5, 3, 1, 1)
        spacerItem = QtGui.QSpacerItem(105, 22, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridlayout.addItem(spacerItem, 8, 3, 1, 1)
        self.menuEdit = QtGui.QLineEdit(ToolConfigurationDialog)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        self.gridlayout.addWidget(self.menuEdit, 9, 1, 1, 1)
        self.changeButton = QtGui.QPushButton(ToolConfigurationDialog)
        self.changeButton.setEnabled(False)
        self.changeButton.setObjectName(_fromUtf8("changeButton"))
        self.gridlayout.addWidget(self.changeButton, 2, 3, 1, 1)
        self.label = QtGui.QLabel(ToolConfigurationDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridlayout.addWidget(self.label, 10, 0, 1, 1)
        self.TextLabel3 = QtGui.QLabel(ToolConfigurationDialog)
        self.TextLabel3.setObjectName(_fromUtf8("TextLabel3"))
        self.gridlayout.addWidget(self.TextLabel3, 12, 0, 1, 1)
        self.TextLabel2 = QtGui.QLabel(ToolConfigurationDialog)
        self.TextLabel2.setObjectName(_fromUtf8("TextLabel2"))
        self.gridlayout.addWidget(self.TextLabel2, 9, 0, 1, 1)
        self.line = QtGui.QFrame(ToolConfigurationDialog)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridlayout.addWidget(self.line, 6, 3, 1, 1)
        self.executableButton = QtGui.QPushButton(ToolConfigurationDialog)
        self.executableButton.setObjectName(_fromUtf8("executableButton"))
        self.gridlayout.addWidget(self.executableButton, 11, 2, 1, 1)
        self.iconEdit = QtGui.QLineEdit(ToolConfigurationDialog)
        self.iconEdit.setObjectName(_fromUtf8("iconEdit"))
        self.gridlayout.addWidget(self.iconEdit, 10, 1, 1, 1)
        self.label_2 = QtGui.QLabel(ToolConfigurationDialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridlayout.addWidget(self.label_2, 13, 0, 1, 1)
        self.TextLabel1 = QtGui.QLabel(ToolConfigurationDialog)
        self.TextLabel1.setObjectName(_fromUtf8("TextLabel1"))
        self.gridlayout.addWidget(self.TextLabel1, 11, 0, 1, 1)
        self.vboxlayout.addLayout(self.gridlayout)
        self.buttonBox = QtGui.QDialogButtonBox(ToolConfigurationDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.vboxlayout.addWidget(self.buttonBox)
        self.label.setBuddy(self.iconEdit)
        self.TextLabel3.setBuddy(self.argumentsEdit)
        self.TextLabel2.setBuddy(self.menuEdit)
        self.label_2.setBuddy(self.redirectCombo)
        self.TextLabel1.setBuddy(self.executableEdit)

        self.retranslateUi(ToolConfigurationDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ToolConfigurationDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ToolConfigurationDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ToolConfigurationDialog)
        ToolConfigurationDialog.setTabOrder(self.toolsList, self.menuEdit)
        ToolConfigurationDialog.setTabOrder(self.menuEdit, self.iconEdit)
        ToolConfigurationDialog.setTabOrder(self.iconEdit, self.iconButton)
        ToolConfigurationDialog.setTabOrder(self.iconButton, self.executableEdit)
        ToolConfigurationDialog.setTabOrder(self.executableEdit, self.executableButton)
        ToolConfigurationDialog.setTabOrder(self.executableButton, self.argumentsEdit)
        ToolConfigurationDialog.setTabOrder(self.argumentsEdit, self.redirectCombo)
        ToolConfigurationDialog.setTabOrder(self.redirectCombo, self.newButton)
        ToolConfigurationDialog.setTabOrder(self.newButton, self.addButton)
        ToolConfigurationDialog.setTabOrder(self.addButton, self.changeButton)
        ToolConfigurationDialog.setTabOrder(self.changeButton, self.deleteButton)
        ToolConfigurationDialog.setTabOrder(self.deleteButton, self.upButton)
        ToolConfigurationDialog.setTabOrder(self.upButton, self.downButton)
        ToolConfigurationDialog.setTabOrder(self.downButton, self.separatorButton)

    def retranslateUi(self, ToolConfigurationDialog):
        ToolConfigurationDialog.setWindowTitle(_translate("ToolConfigurationDialog", "Configure Tools Menu", None))
        self.separatorButton.setToolTip(_translate("ToolConfigurationDialog", "Add a separator", None))
        self.separatorButton.setWhatsThis(_translate("ToolConfigurationDialog", "<b>Add separator</b><p>Add a separator for the menu.</p>", None))
        self.separatorButton.setText(_translate("ToolConfigurationDialog", "Add &Separator", None))
        self.addButton.setToolTip(_translate("ToolConfigurationDialog", "Add a new tools entry", None))
        self.addButton.setWhatsThis(_translate("ToolConfigurationDialog", "<b>Add</b>\n"
"<p>Add a new tools entry with the values entered below.</p>", None))
        self.addButton.setText(_translate("ToolConfigurationDialog", "&Add", None))
        self.addButton.setShortcut(_translate("ToolConfigurationDialog", "Alt+A", None))
        self.redirectCombo.setToolTip(_translate("ToolConfigurationDialog", "Select the output redirection mode", None))
        self.redirectCombo.setWhatsThis(_translate("ToolConfigurationDialog", "<b>Redirect output<b><p>Select the output redirection mode. The standard error channel is either not redirected or shown in the log viewer.</p>", None))
        self.argumentsEdit.setToolTip(_translate("ToolConfigurationDialog", "Enter the arguments for the executable", None))
        self.argumentsEdit.setWhatsThis(_translate("ToolConfigurationDialog", "<b>Arguments</b>\n"
"<p>Enter the arguments for the executable.</p>", None))
        self.upButton.setToolTip(_translate("ToolConfigurationDialog", "Move up", None))
        self.upButton.setWhatsThis(_translate("ToolConfigurationDialog", "<b>Move Up</b>\n"
"<p>Move the selected entry up.</p>", None))
        self.upButton.setText(_translate("ToolConfigurationDialog", "&Up", None))
        self.upButton.setShortcut(_translate("ToolConfigurationDialog", "Alt+U", None))
        self.deleteButton.setToolTip(_translate("ToolConfigurationDialog", "Delete the selected entry", None))
        self.deleteButton.setWhatsThis(_translate("ToolConfigurationDialog", "<b>Delete</b>\n"
"<p>Delete the selected entry.</p>", None))
        self.deleteButton.setText(_translate("ToolConfigurationDialog", "&Delete", None))
        self.deleteButton.setShortcut(_translate("ToolConfigurationDialog", "Alt+D", None))
        self.newButton.setToolTip(_translate("ToolConfigurationDialog", "Clear all entry fields", None))
        self.newButton.setWhatsThis(_translate("ToolConfigurationDialog", "<b>New</b>\n"
"<p>Clear all entry fields for entering a new tools entry.</p>", None))
        self.newButton.setText(_translate("ToolConfigurationDialog", "&New", None))
        self.newButton.setShortcut(_translate("ToolConfigurationDialog", "Alt+N", None))
        self.iconButton.setToolTip(_translate("ToolConfigurationDialog", "Select the icon via a file selection dialog", None))
        self.iconButton.setWhatsThis(_translate("ToolConfigurationDialog", "<b>Icon</b>\n"
"<p>Select the icon via a file selection dialog.</p>", None))
        self.iconButton.setText(_translate("ToolConfigurationDialog", "...", None))
        self.executableEdit.setToolTip(_translate("ToolConfigurationDialog", "Enter the filename of the executable", None))
        self.executableEdit.setWhatsThis(_translate("ToolConfigurationDialog", "<b>Executable</b>\n"
"<p>Enter the filename of the executable.</p>", None))
        self.downButton.setToolTip(_translate("ToolConfigurationDialog", "Move down", None))
        self.downButton.setWhatsThis(_translate("ToolConfigurationDialog", "<b>Move Down</b>\n"
"<p>Move the selected entry down.</p>", None))
        self.downButton.setText(_translate("ToolConfigurationDialog", "Do&wn", None))
        self.downButton.setShortcut(_translate("ToolConfigurationDialog", "Alt+W", None))
        self.menuEdit.setToolTip(_translate("ToolConfigurationDialog", "Enter the menu text", None))
        self.menuEdit.setWhatsThis(_translate("ToolConfigurationDialog", "<b>Menu text</b>\n"
"<p>Enter the menu text. Precede the accelerator key with an & character.</p>", None))
        self.changeButton.setToolTip(_translate("ToolConfigurationDialog", "Change the values of the selected entry", None))
        self.changeButton.setWhatsThis(_translate("ToolConfigurationDialog", "<b>Change</b>\n"
"<p>Change the values of the selected entry.</p>", None))
        self.changeButton.setText(_translate("ToolConfigurationDialog", "C&hange", None))
        self.changeButton.setShortcut(_translate("ToolConfigurationDialog", "Alt+H", None))
        self.label.setText(_translate("ToolConfigurationDialog", "&Icon file:", None))
        self.TextLabel3.setText(_translate("ToolConfigurationDialog", "Ar&guments:", None))
        self.TextLabel2.setText(_translate("ToolConfigurationDialog", "&Menu text:", None))
        self.executableButton.setToolTip(_translate("ToolConfigurationDialog", "Select the executable via a file selection dialog", None))
        self.executableButton.setWhatsThis(_translate("ToolConfigurationDialog", "<b>Executable</b>\n"
"<p>Select the executable via a file selection dialog.</p>", None))
        self.executableButton.setText(_translate("ToolConfigurationDialog", "...", None))
        self.iconEdit.setToolTip(_translate("ToolConfigurationDialog", "Enter the filename of the icon", None))
        self.iconEdit.setWhatsThis(_translate("ToolConfigurationDialog", "<b>Icon</b>\n"
"<p>Enter the filename of the icon.</p>", None))
        self.label_2.setText(_translate("ToolConfigurationDialog", "&Redirect output", None))
        self.TextLabel1.setText(_translate("ToolConfigurationDialog", "&Executable file:", None))

