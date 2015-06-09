# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\PluginManager\PluginUninstallDialog.ui'
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

class Ui_PluginUninstallDialog(object):
    def setupUi(self, PluginUninstallDialog):
        PluginUninstallDialog.setObjectName(_fromUtf8("PluginUninstallDialog"))
        PluginUninstallDialog.resize(400, 300)
        self.vboxlayout = QtGui.QVBoxLayout(PluginUninstallDialog)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.label_3 = QtGui.QLabel(PluginUninstallDialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.vboxlayout.addWidget(self.label_3)
        self.pluginDirectoryCombo = QtGui.QComboBox(PluginUninstallDialog)
        self.pluginDirectoryCombo.setObjectName(_fromUtf8("pluginDirectoryCombo"))
        self.vboxlayout.addWidget(self.pluginDirectoryCombo)
        self.label_2 = QtGui.QLabel(PluginUninstallDialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.vboxlayout.addWidget(self.label_2)
        self.pluginNameCombo = QtGui.QComboBox(PluginUninstallDialog)
        self.pluginNameCombo.setObjectName(_fromUtf8("pluginNameCombo"))
        self.vboxlayout.addWidget(self.pluginNameCombo)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vboxlayout.addItem(spacerItem)
        self.buttonBox = QtGui.QDialogButtonBox(PluginUninstallDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(PluginUninstallDialog)
        QtCore.QMetaObject.connectSlotsByName(PluginUninstallDialog)
        PluginUninstallDialog.setTabOrder(self.pluginDirectoryCombo, self.pluginNameCombo)
        PluginUninstallDialog.setTabOrder(self.pluginNameCombo, self.buttonBox)

    def retranslateUi(self, PluginUninstallDialog):
        PluginUninstallDialog.setWindowTitle(_translate("PluginUninstallDialog", "Plugin Uninstallation", None))
        self.label_3.setText(_translate("PluginUninstallDialog", "Plugin directory:", None))
        self.pluginDirectoryCombo.setToolTip(_translate("PluginUninstallDialog", "Select the plugin area containing the plugin to uninstall", None))
        self.label_2.setText(_translate("PluginUninstallDialog", "Plugin:", None))
        self.pluginNameCombo.setToolTip(_translate("PluginUninstallDialog", "Select the plugin to uninstall", None))

