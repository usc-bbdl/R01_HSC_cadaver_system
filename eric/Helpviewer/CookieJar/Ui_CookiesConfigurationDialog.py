# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Helpviewer\CookieJar\CookiesConfigurationDialog.ui'
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

class Ui_CookiesConfigurationDialog(object):
    def setupUi(self, CookiesConfigurationDialog):
        CookiesConfigurationDialog.setObjectName(_fromUtf8("CookiesConfigurationDialog"))
        CookiesConfigurationDialog.resize(500, 200)
        CookiesConfigurationDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtGui.QVBoxLayout(CookiesConfigurationDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.headerLabel = QtGui.QLabel(CookiesConfigurationDialog)
        self.headerLabel.setObjectName(_fromUtf8("headerLabel"))
        self.verticalLayout.addWidget(self.headerLabel)
        self.line17 = QtGui.QFrame(CookiesConfigurationDialog)
        self.line17.setFrameShape(QtGui.QFrame.HLine)
        self.line17.setFrameShadow(QtGui.QFrame.Sunken)
        self.line17.setFrameShape(QtGui.QFrame.HLine)
        self.line17.setFrameShadow(QtGui.QFrame.Sunken)
        self.line17.setObjectName(_fromUtf8("line17"))
        self.verticalLayout.addWidget(self.line17)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_2 = QtGui.QLabel(CookiesConfigurationDialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.acceptCombo = QtGui.QComboBox(CookiesConfigurationDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.acceptCombo.sizePolicy().hasHeightForWidth())
        self.acceptCombo.setSizePolicy(sizePolicy)
        self.acceptCombo.setObjectName(_fromUtf8("acceptCombo"))
        self.acceptCombo.addItem(_fromUtf8(""))
        self.acceptCombo.addItem(_fromUtf8(""))
        self.acceptCombo.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.acceptCombo, 0, 1, 1, 1)
        self.exceptionsButton = QtGui.QPushButton(CookiesConfigurationDialog)
        self.exceptionsButton.setObjectName(_fromUtf8("exceptionsButton"))
        self.gridLayout.addWidget(self.exceptionsButton, 0, 2, 1, 1)
        self.label = QtGui.QLabel(CookiesConfigurationDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.keepUntilCombo = QtGui.QComboBox(CookiesConfigurationDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.keepUntilCombo.sizePolicy().hasHeightForWidth())
        self.keepUntilCombo.setSizePolicy(sizePolicy)
        self.keepUntilCombo.setObjectName(_fromUtf8("keepUntilCombo"))
        self.keepUntilCombo.addItem(_fromUtf8(""))
        self.keepUntilCombo.addItem(_fromUtf8(""))
        self.keepUntilCombo.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.keepUntilCombo, 1, 1, 1, 1)
        self.cookiesButton = QtGui.QPushButton(CookiesConfigurationDialog)
        self.cookiesButton.setObjectName(_fromUtf8("cookiesButton"))
        self.gridLayout.addWidget(self.cookiesButton, 1, 2, 1, 1)
        self.filterTrackingCookiesCheckbox = QtGui.QCheckBox(CookiesConfigurationDialog)
        self.filterTrackingCookiesCheckbox.setObjectName(_fromUtf8("filterTrackingCookiesCheckbox"))
        self.gridLayout.addWidget(self.filterTrackingCookiesCheckbox, 2, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem = QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.buttonBox = QtGui.QDialogButtonBox(CookiesConfigurationDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        self.label_2.setBuddy(self.acceptCombo)
        self.label.setBuddy(self.keepUntilCombo)

        self.retranslateUi(CookiesConfigurationDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), CookiesConfigurationDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), CookiesConfigurationDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(CookiesConfigurationDialog)
        CookiesConfigurationDialog.setTabOrder(self.acceptCombo, self.exceptionsButton)
        CookiesConfigurationDialog.setTabOrder(self.exceptionsButton, self.keepUntilCombo)
        CookiesConfigurationDialog.setTabOrder(self.keepUntilCombo, self.cookiesButton)
        CookiesConfigurationDialog.setTabOrder(self.cookiesButton, self.filterTrackingCookiesCheckbox)
        CookiesConfigurationDialog.setTabOrder(self.filterTrackingCookiesCheckbox, self.buttonBox)

    def retranslateUi(self, CookiesConfigurationDialog):
        CookiesConfigurationDialog.setWindowTitle(_translate("CookiesConfigurationDialog", "Configure cookies", None))
        self.headerLabel.setText(_translate("CookiesConfigurationDialog", "<b>Configure cookies</b>", None))
        self.label_2.setText(_translate("CookiesConfigurationDialog", "&Accept Cookies:", None))
        self.acceptCombo.setToolTip(_translate("CookiesConfigurationDialog", "Select the accept policy", None))
        self.acceptCombo.setItemText(0, _translate("CookiesConfigurationDialog", "Always", None))
        self.acceptCombo.setItemText(1, _translate("CookiesConfigurationDialog", "Never", None))
        self.acceptCombo.setItemText(2, _translate("CookiesConfigurationDialog", "Only from sites you navigate to", None))
        self.exceptionsButton.setToolTip(_translate("CookiesConfigurationDialog", "Show a dialog to configure exceptions", None))
        self.exceptionsButton.setText(_translate("CookiesConfigurationDialog", "&Exceptions...", None))
        self.label.setText(_translate("CookiesConfigurationDialog", "&Keep until:", None))
        self.keepUntilCombo.setToolTip(_translate("CookiesConfigurationDialog", "Select the keep policy", None))
        self.keepUntilCombo.setItemText(0, _translate("CookiesConfigurationDialog", "They expire", None))
        self.keepUntilCombo.setItemText(1, _translate("CookiesConfigurationDialog", "I exit the application", None))
        self.keepUntilCombo.setItemText(2, _translate("CookiesConfigurationDialog", "At most 90 days", None))
        self.cookiesButton.setToolTip(_translate("CookiesConfigurationDialog", "Show a dialog listing all cookies", None))
        self.cookiesButton.setText(_translate("CookiesConfigurationDialog", "&Show Cookies...", None))
        self.filterTrackingCookiesCheckbox.setToolTip(_translate("CookiesConfigurationDialog", "Select to filter tracking cookies", None))
        self.filterTrackingCookiesCheckbox.setText(_translate("CookiesConfigurationDialog", "&Filter Tracking Cookies", None))

