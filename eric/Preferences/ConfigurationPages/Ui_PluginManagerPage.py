# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Preferences\ConfigurationPages\PluginManagerPage.ui'
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

class Ui_PluginManagerPage(object):
    def setupUi(self, PluginManagerPage):
        PluginManagerPage.setObjectName(_fromUtf8("PluginManagerPage"))
        PluginManagerPage.resize(507, 299)
        self.gridlayout = QtGui.QGridLayout(PluginManagerPage)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.headerLabel = QtGui.QLabel(PluginManagerPage)
        self.headerLabel.setObjectName(_fromUtf8("headerLabel"))
        self.gridlayout.addWidget(self.headerLabel, 0, 0, 1, 3)
        self.line9_2 = QtGui.QFrame(PluginManagerPage)
        self.line9_2.setFrameShape(QtGui.QFrame.HLine)
        self.line9_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line9_2.setFrameShape(QtGui.QFrame.HLine)
        self.line9_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line9_2.setObjectName(_fromUtf8("line9_2"))
        self.gridlayout.addWidget(self.line9_2, 1, 0, 1, 3)
        self.label = QtGui.QLabel(PluginManagerPage)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridlayout.addWidget(self.label, 2, 0, 1, 1)
        self.downloadDirEdit = QtGui.QLineEdit(PluginManagerPage)
        self.downloadDirEdit.setObjectName(_fromUtf8("downloadDirEdit"))
        self.gridlayout.addWidget(self.downloadDirEdit, 2, 1, 1, 1)
        self.downloadDirButton = QtGui.QPushButton(PluginManagerPage)
        self.downloadDirButton.setObjectName(_fromUtf8("downloadDirButton"))
        self.gridlayout.addWidget(self.downloadDirButton, 2, 2, 1, 1)
        self.TextLabel1_2_2_2_3 = QtGui.QLabel(PluginManagerPage)
        self.TextLabel1_2_2_2_3.setObjectName(_fromUtf8("TextLabel1_2_2_2_3"))
        self.gridlayout.addWidget(self.TextLabel1_2_2_2_3, 3, 0, 1, 3)
        self.activateExternalPluginsCheckBox = QtGui.QCheckBox(PluginManagerPage)
        self.activateExternalPluginsCheckBox.setObjectName(_fromUtf8("activateExternalPluginsCheckBox"))
        self.gridlayout.addWidget(self.activateExternalPluginsCheckBox, 4, 0, 1, 3)
        spacerItem = QtGui.QSpacerItem(435, 121, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridlayout.addItem(spacerItem, 5, 0, 1, 3)

        self.retranslateUi(PluginManagerPage)
        QtCore.QMetaObject.connectSlotsByName(PluginManagerPage)
        PluginManagerPage.setTabOrder(self.downloadDirEdit, self.downloadDirButton)
        PluginManagerPage.setTabOrder(self.downloadDirButton, self.activateExternalPluginsCheckBox)

    def retranslateUi(self, PluginManagerPage):
        self.headerLabel.setText(_translate("PluginManagerPage", "<b>Configure plugin manager</b>", None))
        self.label.setText(_translate("PluginManagerPage", "Plugins download directory:", None))
        self.downloadDirEdit.setToolTip(_translate("PluginManagerPage", "Enter the plugins download directory", None))
        self.downloadDirButton.setToolTip(_translate("PluginManagerPage", "Select the plugins download directory via a directory selection dialog", None))
        self.downloadDirButton.setText(_translate("PluginManagerPage", "...", None))
        self.TextLabel1_2_2_2_3.setText(_translate("PluginManagerPage", "<font color=\"#FF0000\"><b>Note:</b> The following setting is activated at the next startup of the application.</font>", None))
        self.activateExternalPluginsCheckBox.setToolTip(_translate("PluginManagerPage", "Select to enable third party plugins to be loaded", None))
        self.activateExternalPluginsCheckBox.setText(_translate("PluginManagerPage", "Load third party plugins", None))

