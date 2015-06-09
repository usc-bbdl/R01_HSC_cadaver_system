# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Preferences\ShortcutDialog.ui'
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

class Ui_ShortcutDialog(object):
    def setupUi(self, ShortcutDialog):
        ShortcutDialog.setObjectName(_fromUtf8("ShortcutDialog"))
        ShortcutDialog.resize(539, 142)
        self.vboxlayout = QtGui.QVBoxLayout(ShortcutDialog)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.shortcutsGroup = QtGui.QGroupBox(ShortcutDialog)
        self.shortcutsGroup.setTitle(_fromUtf8(""))
        self.shortcutsGroup.setObjectName(_fromUtf8("shortcutsGroup"))
        self.gridLayout = QtGui.QGridLayout(self.shortcutsGroup)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.primaryButton = QtGui.QRadioButton(self.shortcutsGroup)
        self.primaryButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.primaryButton.setChecked(True)
        self.primaryButton.setObjectName(_fromUtf8("primaryButton"))
        self.gridLayout.addWidget(self.primaryButton, 0, 0, 1, 1)
        self.primaryClearButton = QtGui.QPushButton(self.shortcutsGroup)
        self.primaryClearButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.primaryClearButton.setObjectName(_fromUtf8("primaryClearButton"))
        self.gridLayout.addWidget(self.primaryClearButton, 0, 1, 1, 1)
        self.keyEdit = QtGui.QLineEdit(self.shortcutsGroup)
        self.keyEdit.setReadOnly(True)
        self.keyEdit.setObjectName(_fromUtf8("keyEdit"))
        self.gridLayout.addWidget(self.keyEdit, 0, 2, 1, 1)
        self.alternateButton = QtGui.QRadioButton(self.shortcutsGroup)
        self.alternateButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.alternateButton.setObjectName(_fromUtf8("alternateButton"))
        self.gridLayout.addWidget(self.alternateButton, 1, 0, 1, 1)
        self.alternateClearButton = QtGui.QPushButton(self.shortcutsGroup)
        self.alternateClearButton.setEnabled(False)
        self.alternateClearButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.alternateClearButton.setObjectName(_fromUtf8("alternateClearButton"))
        self.gridLayout.addWidget(self.alternateClearButton, 1, 1, 1, 1)
        self.alternateKeyEdit = QtGui.QLineEdit(self.shortcutsGroup)
        self.alternateKeyEdit.setReadOnly(True)
        self.alternateKeyEdit.setObjectName(_fromUtf8("alternateKeyEdit"))
        self.gridLayout.addWidget(self.alternateKeyEdit, 1, 2, 1, 1)
        self.vboxlayout.addWidget(self.shortcutsGroup)
        self.buttonBox = QtGui.QDialogButtonBox(ShortcutDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(ShortcutDialog)
        QtCore.QObject.connect(self.primaryButton, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.primaryClearButton.setEnabled)
        QtCore.QObject.connect(self.alternateButton, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.alternateClearButton.setEnabled)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ShortcutDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ShortcutDialog)

    def retranslateUi(self, ShortcutDialog):
        ShortcutDialog.setWindowTitle(_translate("ShortcutDialog", "Edit Shortcut", None))
        ShortcutDialog.setWhatsThis(_translate("ShortcutDialog", "Press your shortcut keys and select OK", None))
        self.primaryButton.setToolTip(_translate("ShortcutDialog", "Select to change the primary keyboard shortcut", None))
        self.primaryButton.setText(_translate("ShortcutDialog", "Primary Shortcut:", None))
        self.primaryClearButton.setToolTip(_translate("ShortcutDialog", "Press to clear the key sequence buffer.", None))
        self.primaryClearButton.setText(_translate("ShortcutDialog", "Clear", None))
        self.alternateButton.setToolTip(_translate("ShortcutDialog", "Select to change the alternative keyboard shortcut", None))
        self.alternateButton.setText(_translate("ShortcutDialog", "Alternative Shortcut:", None))
        self.alternateClearButton.setToolTip(_translate("ShortcutDialog", "Press to clear the key sequence buffer.", None))
        self.alternateClearButton.setText(_translate("ShortcutDialog", "Clear", None))

