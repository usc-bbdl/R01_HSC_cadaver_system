# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Preferences\ConfigurationPages\EditorAPIsPage.ui'
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

class Ui_EditorAPIsPage(object):
    def setupUi(self, EditorAPIsPage):
        EditorAPIsPage.setObjectName(_fromUtf8("EditorAPIsPage"))
        EditorAPIsPage.resize(462, 422)
        self.vboxlayout = QtGui.QVBoxLayout(EditorAPIsPage)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.headerLabel = QtGui.QLabel(EditorAPIsPage)
        self.headerLabel.setObjectName(_fromUtf8("headerLabel"))
        self.vboxlayout.addWidget(self.headerLabel)
        self.line5 = QtGui.QFrame(EditorAPIsPage)
        self.line5.setFrameShape(QtGui.QFrame.HLine)
        self.line5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line5.setFrameShape(QtGui.QFrame.HLine)
        self.line5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line5.setObjectName(_fromUtf8("line5"))
        self.vboxlayout.addWidget(self.line5)
        self.apiAutoPrepareCheckBox = QtGui.QCheckBox(EditorAPIsPage)
        self.apiAutoPrepareCheckBox.setObjectName(_fromUtf8("apiAutoPrepareCheckBox"))
        self.vboxlayout.addWidget(self.apiAutoPrepareCheckBox)
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        self.TextLabel1_3_3 = QtGui.QLabel(EditorAPIsPage)
        self.TextLabel1_3_3.setToolTip(_fromUtf8(""))
        self.TextLabel1_3_3.setObjectName(_fromUtf8("TextLabel1_3_3"))
        self.hboxlayout.addWidget(self.TextLabel1_3_3)
        self.apiLanguageComboBox = QtGui.QComboBox(EditorAPIsPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.apiLanguageComboBox.sizePolicy().hasHeightForWidth())
        self.apiLanguageComboBox.setSizePolicy(sizePolicy)
        self.apiLanguageComboBox.setObjectName(_fromUtf8("apiLanguageComboBox"))
        self.hboxlayout.addWidget(self.apiLanguageComboBox)
        self.vboxlayout.addLayout(self.hboxlayout)
        self.apiGroup = QtGui.QGroupBox(EditorAPIsPage)
        self.apiGroup.setEnabled(False)
        self.apiGroup.setObjectName(_fromUtf8("apiGroup"))
        self.gridlayout = QtGui.QGridLayout(self.apiGroup)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.apiList = QtGui.QListWidget(self.apiGroup)
        self.apiList.setAlternatingRowColors(True)
        self.apiList.setObjectName(_fromUtf8("apiList"))
        self.gridlayout.addWidget(self.apiList, 0, 0, 1, 4)
        self.deleteApiFileButton = QtGui.QPushButton(self.apiGroup)
        self.deleteApiFileButton.setObjectName(_fromUtf8("deleteApiFileButton"))
        self.gridlayout.addWidget(self.deleteApiFileButton, 1, 0, 1, 1)
        self.addApiFileButton = QtGui.QPushButton(self.apiGroup)
        self.addApiFileButton.setObjectName(_fromUtf8("addApiFileButton"))
        self.gridlayout.addWidget(self.addApiFileButton, 1, 1, 1, 1)
        self.apiFileEdit = QtGui.QLineEdit(self.apiGroup)
        self.apiFileEdit.setObjectName(_fromUtf8("apiFileEdit"))
        self.gridlayout.addWidget(self.apiFileEdit, 1, 2, 1, 1)
        self.apiFileButton = QtGui.QPushButton(self.apiGroup)
        self.apiFileButton.setObjectName(_fromUtf8("apiFileButton"))
        self.gridlayout.addWidget(self.apiFileButton, 1, 3, 1, 1)
        self.addInstalledApiFileButton = QtGui.QPushButton(self.apiGroup)
        self.addInstalledApiFileButton.setObjectName(_fromUtf8("addInstalledApiFileButton"))
        self.gridlayout.addWidget(self.addInstalledApiFileButton, 2, 1, 1, 3)
        self.addPluginApiFileButton = QtGui.QPushButton(self.apiGroup)
        self.addPluginApiFileButton.setObjectName(_fromUtf8("addPluginApiFileButton"))
        self.gridlayout.addWidget(self.addPluginApiFileButton, 3, 1, 1, 3)
        self.line = QtGui.QFrame(self.apiGroup)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridlayout.addWidget(self.line, 4, 0, 1, 4)
        self.prepareApiButton = QtGui.QPushButton(self.apiGroup)
        self.prepareApiButton.setObjectName(_fromUtf8("prepareApiButton"))
        self.gridlayout.addWidget(self.prepareApiButton, 5, 0, 1, 2)
        self.prepareApiProgressBar = QtGui.QProgressBar(self.apiGroup)
        self.prepareApiProgressBar.setProperty("value", 0)
        self.prepareApiProgressBar.setTextVisible(False)
        self.prepareApiProgressBar.setOrientation(QtCore.Qt.Horizontal)
        self.prepareApiProgressBar.setObjectName(_fromUtf8("prepareApiProgressBar"))
        self.gridlayout.addWidget(self.prepareApiProgressBar, 5, 2, 1, 2)
        self.vboxlayout.addWidget(self.apiGroup)

        self.retranslateUi(EditorAPIsPage)
        QtCore.QMetaObject.connectSlotsByName(EditorAPIsPage)
        EditorAPIsPage.setTabOrder(self.apiAutoPrepareCheckBox, self.apiLanguageComboBox)
        EditorAPIsPage.setTabOrder(self.apiLanguageComboBox, self.apiList)
        EditorAPIsPage.setTabOrder(self.apiList, self.deleteApiFileButton)
        EditorAPIsPage.setTabOrder(self.deleteApiFileButton, self.apiFileEdit)
        EditorAPIsPage.setTabOrder(self.apiFileEdit, self.apiFileButton)
        EditorAPIsPage.setTabOrder(self.apiFileButton, self.addApiFileButton)
        EditorAPIsPage.setTabOrder(self.addApiFileButton, self.addInstalledApiFileButton)
        EditorAPIsPage.setTabOrder(self.addInstalledApiFileButton, self.addPluginApiFileButton)
        EditorAPIsPage.setTabOrder(self.addPluginApiFileButton, self.prepareApiButton)

    def retranslateUi(self, EditorAPIsPage):
        self.headerLabel.setText(_translate("EditorAPIsPage", "<b>Configure API files</b>", None))
        self.apiAutoPrepareCheckBox.setToolTip(_translate("EditorAPIsPage", "Select to compile the APIs automatically upon loading", None))
        self.apiAutoPrepareCheckBox.setText(_translate("EditorAPIsPage", "Compile APIs automatically", None))
        self.TextLabel1_3_3.setText(_translate("EditorAPIsPage", "Language:", None))
        self.apiLanguageComboBox.setToolTip(_translate("EditorAPIsPage", "Select the language to be configured.", None))
        self.apiGroup.setTitle(_translate("EditorAPIsPage", "APIs", None))
        self.apiList.setToolTip(_translate("EditorAPIsPage", "List of API files", None))
        self.deleteApiFileButton.setToolTip(_translate("EditorAPIsPage", "Press to delete the selected file from the list", None))
        self.deleteApiFileButton.setText(_translate("EditorAPIsPage", "Delete", None))
        self.addApiFileButton.setToolTip(_translate("EditorAPIsPage", "Press to add the entered file to the list", None))
        self.addApiFileButton.setText(_translate("EditorAPIsPage", "Add", None))
        self.apiFileEdit.setToolTip(_translate("EditorAPIsPage", "Enter a file to be added", None))
        self.apiFileButton.setToolTip(_translate("EditorAPIsPage", "Press to select an API file via a selection dialog", None))
        self.apiFileButton.setText(_translate("EditorAPIsPage", "...", None))
        self.addInstalledApiFileButton.setToolTip(_translate("EditorAPIsPage", "Press to select an API file from the list of installed API files", None))
        self.addInstalledApiFileButton.setText(_translate("EditorAPIsPage", "Add from installed APIs", None))
        self.addPluginApiFileButton.setToolTip(_translate("EditorAPIsPage", "Press to select an API file from the list of API files installed by plugins", None))
        self.addPluginApiFileButton.setText(_translate("EditorAPIsPage", "Add from Plugin APIs", None))
        self.prepareApiButton.setToolTip(_translate("EditorAPIsPage", "Press to compile the selected APIs definition", None))
        self.prepareApiButton.setText(_translate("EditorAPIsPage", "Compile APIs", None))

