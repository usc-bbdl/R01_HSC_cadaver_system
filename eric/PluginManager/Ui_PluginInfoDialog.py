# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\PluginManager\PluginInfoDialog.ui'
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

class Ui_PluginInfoDialog(object):
    def setupUi(self, PluginInfoDialog):
        PluginInfoDialog.setObjectName(_fromUtf8("PluginInfoDialog"))
        PluginInfoDialog.resize(800, 600)
        PluginInfoDialog.setSizeGripEnabled(True)
        self.vboxlayout = QtGui.QVBoxLayout(PluginInfoDialog)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.label = QtGui.QLabel(PluginInfoDialog)
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.vboxlayout.addWidget(self.label)
        self.pluginList = QtGui.QTreeWidget(PluginInfoDialog)
        self.pluginList.setRootIsDecorated(False)
        self.pluginList.setItemsExpandable(False)
        self.pluginList.setAllColumnsShowFocus(True)
        self.pluginList.setObjectName(_fromUtf8("pluginList"))
        self.vboxlayout.addWidget(self.pluginList)
        self.buttonBox = QtGui.QDialogButtonBox(PluginInfoDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(PluginInfoDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), PluginInfoDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), PluginInfoDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(PluginInfoDialog)
        PluginInfoDialog.setTabOrder(self.pluginList, self.buttonBox)

    def retranslateUi(self, PluginInfoDialog):
        PluginInfoDialog.setWindowTitle(_translate("PluginInfoDialog", "Loaded Plugins", None))
        self.label.setText(_translate("PluginInfoDialog", "Double-Click an entry to show detailed info. Plugins with an error are shown in red.", None))
        self.pluginList.setWhatsThis(_translate("PluginInfoDialog", "<b>Plugin List</b><p>This lists all loaded plugins. Double-clicking an entry shows more detailed information in a separate dialog.</p>", None))
        self.pluginList.setSortingEnabled(True)
        self.pluginList.headerItem().setText(0, _translate("PluginInfoDialog", "Module", None))
        self.pluginList.headerItem().setText(1, _translate("PluginInfoDialog", "Name", None))
        self.pluginList.headerItem().setText(2, _translate("PluginInfoDialog", "Version", None))
        self.pluginList.headerItem().setText(3, _translate("PluginInfoDialog", "Autoactivate", None))
        self.pluginList.headerItem().setText(4, _translate("PluginInfoDialog", "Active", None))
        self.pluginList.headerItem().setText(5, _translate("PluginInfoDialog", "Description", None))

