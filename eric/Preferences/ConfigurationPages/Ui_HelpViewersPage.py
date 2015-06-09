# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Preferences\ConfigurationPages\HelpViewersPage.ui'
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

class Ui_HelpViewersPage(object):
    def setupUi(self, HelpViewersPage):
        HelpViewersPage.setObjectName(_fromUtf8("HelpViewersPage"))
        HelpViewersPage.resize(613, 634)
        self.verticalLayout_3 = QtGui.QVBoxLayout(HelpViewersPage)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.headerLabel = QtGui.QLabel(HelpViewersPage)
        self.headerLabel.setObjectName(_fromUtf8("headerLabel"))
        self.verticalLayout_3.addWidget(self.headerLabel)
        self.line17 = QtGui.QFrame(HelpViewersPage)
        self.line17.setFrameShape(QtGui.QFrame.HLine)
        self.line17.setFrameShadow(QtGui.QFrame.Sunken)
        self.line17.setFrameShape(QtGui.QFrame.HLine)
        self.line17.setFrameShadow(QtGui.QFrame.Sunken)
        self.line17.setObjectName(_fromUtf8("line17"))
        self.verticalLayout_3.addWidget(self.line17)
        self.groupBox = QtGui.QGroupBox(HelpViewersPage)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridlayout = QtGui.QGridLayout(self.groupBox)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        self.customViewerEdit = QtGui.QLineEdit(self.groupBox)
        self.customViewerEdit.setEnabled(False)
        self.customViewerEdit.setObjectName(_fromUtf8("customViewerEdit"))
        self.hboxlayout.addWidget(self.customViewerEdit)
        self.customViewerSelectionButton = QtGui.QPushButton(self.groupBox)
        self.customViewerSelectionButton.setEnabled(False)
        self.customViewerSelectionButton.setObjectName(_fromUtf8("customViewerSelectionButton"))
        self.hboxlayout.addWidget(self.customViewerSelectionButton)
        self.gridlayout.addLayout(self.hboxlayout, 1, 0, 1, 4)
        self.customViewerButton = QtGui.QRadioButton(self.groupBox)
        self.customViewerButton.setObjectName(_fromUtf8("customViewerButton"))
        self.gridlayout.addWidget(self.customViewerButton, 0, 3, 1, 1)
        self.qtAssistantButton = QtGui.QRadioButton(self.groupBox)
        self.qtAssistantButton.setObjectName(_fromUtf8("qtAssistantButton"))
        self.gridlayout.addWidget(self.qtAssistantButton, 0, 1, 1, 1)
        self.helpBrowserButton = QtGui.QRadioButton(self.groupBox)
        self.helpBrowserButton.setChecked(True)
        self.helpBrowserButton.setObjectName(_fromUtf8("helpBrowserButton"))
        self.gridlayout.addWidget(self.helpBrowserButton, 0, 0, 1, 1)
        self.webBrowserButton = QtGui.QRadioButton(self.groupBox)
        self.webBrowserButton.setObjectName(_fromUtf8("webBrowserButton"))
        self.gridlayout.addWidget(self.webBrowserButton, 0, 2, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBox)
        spacerItem = QtGui.QSpacerItem(479, 121, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)

        self.retranslateUi(HelpViewersPage)
        QtCore.QObject.connect(self.customViewerButton, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.customViewerEdit.setEnabled)
        QtCore.QObject.connect(self.customViewerButton, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.customViewerSelectionButton.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(HelpViewersPage)
        HelpViewersPage.setTabOrder(self.helpBrowserButton, self.qtAssistantButton)
        HelpViewersPage.setTabOrder(self.qtAssistantButton, self.webBrowserButton)
        HelpViewersPage.setTabOrder(self.webBrowserButton, self.customViewerButton)
        HelpViewersPage.setTabOrder(self.customViewerButton, self.customViewerEdit)
        HelpViewersPage.setTabOrder(self.customViewerEdit, self.customViewerSelectionButton)

    def retranslateUi(self, HelpViewersPage):
        self.headerLabel.setText(_translate("HelpViewersPage", "<b>Configure help viewers</b>", None))
        self.groupBox.setTitle(_translate("HelpViewersPage", "Help Viewer", None))
        self.customViewerEdit.setToolTip(_translate("HelpViewersPage", "Enter the custom viewer to be used", None))
        self.customViewerSelectionButton.setToolTip(_translate("HelpViewersPage", "Press to select the custom viewer via a file selection dialog", None))
        self.customViewerSelectionButton.setText(_translate("HelpViewersPage", "...", None))
        self.customViewerButton.setToolTip(_translate("HelpViewersPage", "Select to use a custom viewer", None))
        self.customViewerButton.setText(_translate("HelpViewersPage", "Custom", None))
        self.qtAssistantButton.setToolTip(_translate("HelpViewersPage", "Select to use Qt Assistant", None))
        self.qtAssistantButton.setText(_translate("HelpViewersPage", "Qt Assistant", None))
        self.helpBrowserButton.setToolTip(_translate("HelpViewersPage", "Select to use the Eric Web Browser", None))
        self.helpBrowserButton.setText(_translate("HelpViewersPage", "Eric Web Browser", None))
        self.webBrowserButton.setToolTip(_translate("HelpViewersPage", "Select to use the configured web browser", None))
        self.webBrowserButton.setText(_translate("HelpViewersPage", "Web Browser", None))

