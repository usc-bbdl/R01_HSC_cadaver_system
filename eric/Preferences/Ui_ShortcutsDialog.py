# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Preferences\ShortcutsDialog.ui'
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

class Ui_ShortcutsDialog(object):
    def setupUi(self, ShortcutsDialog):
        ShortcutsDialog.setObjectName(_fromUtf8("ShortcutsDialog"))
        ShortcutsDialog.resize(800, 480)
        self.verticalLayout = QtGui.QVBoxLayout(ShortcutsDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(ShortcutsDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.searchEdit = QtGui.QLineEdit(ShortcutsDialog)
        self.searchEdit.setObjectName(_fromUtf8("searchEdit"))
        self.horizontalLayout.addWidget(self.searchEdit)
        self.clearSearchButton = QtGui.QToolButton(ShortcutsDialog)
        self.clearSearchButton.setText(_fromUtf8(""))
        self.clearSearchButton.setObjectName(_fromUtf8("clearSearchButton"))
        self.horizontalLayout.addWidget(self.clearSearchButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(ShortcutsDialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.actionButton = QtGui.QRadioButton(ShortcutsDialog)
        self.actionButton.setChecked(True)
        self.actionButton.setObjectName(_fromUtf8("actionButton"))
        self.horizontalLayout_2.addWidget(self.actionButton)
        self.shortcutButton = QtGui.QRadioButton(ShortcutsDialog)
        self.shortcutButton.setObjectName(_fromUtf8("shortcutButton"))
        self.horizontalLayout_2.addWidget(self.shortcutButton)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.shortcutsList = QtGui.QTreeWidget(ShortcutsDialog)
        self.shortcutsList.setAlternatingRowColors(True)
        self.shortcutsList.setObjectName(_fromUtf8("shortcutsList"))
        self.verticalLayout.addWidget(self.shortcutsList)
        self.buttonBox = QtGui.QDialogButtonBox(ShortcutsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        self.label.setBuddy(self.searchEdit)

        self.retranslateUi(ShortcutsDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ShortcutsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ShortcutsDialog)
        ShortcutsDialog.setTabOrder(self.searchEdit, self.clearSearchButton)
        ShortcutsDialog.setTabOrder(self.clearSearchButton, self.actionButton)
        ShortcutsDialog.setTabOrder(self.actionButton, self.shortcutButton)
        ShortcutsDialog.setTabOrder(self.shortcutButton, self.shortcutsList)
        ShortcutsDialog.setTabOrder(self.shortcutsList, self.buttonBox)

    def retranslateUi(self, ShortcutsDialog):
        ShortcutsDialog.setWindowTitle(_translate("ShortcutsDialog", "Keyboard Shortcuts", None))
        self.label.setText(_translate("ShortcutsDialog", "&Filter:", None))
        self.searchEdit.setToolTip(_translate("ShortcutsDialog", "Enter the regular expression that should be contained in the shortcut action", None))
        self.clearSearchButton.setToolTip(_translate("ShortcutsDialog", "Press to clear the search edit", None))
        self.label_2.setText(_translate("ShortcutsDialog", "Filter on", None))
        self.actionButton.setToolTip(_translate("ShortcutsDialog", "Select to filter based on the actions", None))
        self.actionButton.setText(_translate("ShortcutsDialog", "&Action", None))
        self.shortcutButton.setToolTip(_translate("ShortcutsDialog", "Select to filter based on shortcut or alternative shortcut", None))
        self.shortcutButton.setText(_translate("ShortcutsDialog", "&Shortcut or Alternative", None))
        self.shortcutsList.setToolTip(_translate("ShortcutsDialog", "This list shows all keyboard shortcuts.", None))
        self.shortcutsList.setWhatsThis(_translate("ShortcutsDialog", "<b>Keyboard Shortcuts List</b>\n"
"<p>This list shows all keyboard shortcuts defined in the application. Double click an entry in order to change the respective shortcut. Alternatively, the shortcut might be changed by editing the key sequence in the respective column.</p>", None))
        self.shortcutsList.headerItem().setText(0, _translate("ShortcutsDialog", "Action", None))
        self.shortcutsList.headerItem().setText(1, _translate("ShortcutsDialog", "Shortcut", None))
        self.shortcutsList.headerItem().setText(2, _translate("ShortcutsDialog", "Alternativ", None))

