# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Preferences\ConfigurationPages\TrayStarterPage.ui'
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

class Ui_TrayStarterPage(object):
    def setupUi(self, TrayStarterPage):
        TrayStarterPage.setObjectName(_fromUtf8("TrayStarterPage"))
        TrayStarterPage.resize(482, 473)
        self.verticalLayout_2 = QtGui.QVBoxLayout(TrayStarterPage)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.headerLabel = QtGui.QLabel(TrayStarterPage)
        self.headerLabel.setObjectName(_fromUtf8("headerLabel"))
        self.verticalLayout_2.addWidget(self.headerLabel)
        self.line1 = QtGui.QFrame(TrayStarterPage)
        self.line1.setFrameShape(QtGui.QFrame.HLine)
        self.line1.setFrameShadow(QtGui.QFrame.Sunken)
        self.line1.setFrameShape(QtGui.QFrame.HLine)
        self.line1.setFrameShadow(QtGui.QFrame.Sunken)
        self.line1.setObjectName(_fromUtf8("line1"))
        self.verticalLayout_2.addWidget(self.line1)
        self.groupBox = QtGui.QGroupBox(TrayStarterPage)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.standardButton = QtGui.QRadioButton(self.groupBox)
        self.standardButton.setObjectName(_fromUtf8("standardButton"))
        self.verticalLayout.addWidget(self.standardButton)
        self.highContrastButton = QtGui.QRadioButton(self.groupBox)
        self.highContrastButton.setObjectName(_fromUtf8("highContrastButton"))
        self.verticalLayout.addWidget(self.highContrastButton)
        self.blackWhiteButton = QtGui.QRadioButton(self.groupBox)
        self.blackWhiteButton.setObjectName(_fromUtf8("blackWhiteButton"))
        self.verticalLayout.addWidget(self.blackWhiteButton)
        self.blackWhiteInverseButton = QtGui.QRadioButton(self.groupBox)
        self.blackWhiteInverseButton.setObjectName(_fromUtf8("blackWhiteInverseButton"))
        self.verticalLayout.addWidget(self.blackWhiteInverseButton)
        self.verticalLayout_2.addWidget(self.groupBox)
        spacerItem = QtGui.QSpacerItem(464, 41, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)

        self.retranslateUi(TrayStarterPage)
        QtCore.QMetaObject.connectSlotsByName(TrayStarterPage)

    def retranslateUi(self, TrayStarterPage):
        self.headerLabel.setText(_translate("TrayStarterPage", "<b>Configure Tray Starter</b>", None))
        self.groupBox.setTitle(_translate("TrayStarterPage", "Icon", None))
        self.standardButton.setToolTip(_translate("TrayStarterPage", "Select to use the standard icon", None))
        self.standardButton.setText(_translate("TrayStarterPage", "Standard Icon", None))
        self.highContrastButton.setToolTip(_translate("TrayStarterPage", "Select to use the high contrast icon", None))
        self.highContrastButton.setText(_translate("TrayStarterPage", "High Contrast Icon", None))
        self.blackWhiteButton.setToolTip(_translate("TrayStarterPage", "Select to use a black and white icon", None))
        self.blackWhiteButton.setText(_translate("TrayStarterPage", "Black and White Icon", None))
        self.blackWhiteInverseButton.setToolTip(_translate("TrayStarterPage", "Select to use an inverse black and white icon", None))
        self.blackWhiteInverseButton.setText(_translate("TrayStarterPage", "Inverse Black and White Icon", None))

