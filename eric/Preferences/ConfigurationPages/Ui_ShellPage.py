# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Preferences\ConfigurationPages\ShellPage.ui'
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

class Ui_ShellPage(object):
    def setupUi(self, ShellPage):
        ShellPage.setObjectName(_fromUtf8("ShellPage"))
        ShellPage.resize(587, 538)
        self.verticalLayout = QtGui.QVBoxLayout(ShellPage)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.headerLabel = QtGui.QLabel(ShellPage)
        self.headerLabel.setObjectName(_fromUtf8("headerLabel"))
        self.verticalLayout.addWidget(self.headerLabel)
        self.line14 = QtGui.QFrame(ShellPage)
        self.line14.setFrameShape(QtGui.QFrame.HLine)
        self.line14.setFrameShadow(QtGui.QFrame.Sunken)
        self.line14.setFrameShape(QtGui.QFrame.HLine)
        self.line14.setFrameShadow(QtGui.QFrame.Sunken)
        self.line14.setObjectName(_fromUtf8("line14"))
        self.verticalLayout.addWidget(self.line14)
        self.gridlayout = QtGui.QGridLayout()
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.shellLinenoCheckBox = QtGui.QCheckBox(ShellPage)
        self.shellLinenoCheckBox.setObjectName(_fromUtf8("shellLinenoCheckBox"))
        self.gridlayout.addWidget(self.shellLinenoCheckBox, 0, 0, 1, 1)
        self.shellCTEnabledCheckBox = QtGui.QCheckBox(ShellPage)
        self.shellCTEnabledCheckBox.setObjectName(_fromUtf8("shellCTEnabledCheckBox"))
        self.gridlayout.addWidget(self.shellCTEnabledCheckBox, 1, 1, 1, 1)
        self.shellWordWrapCheckBox = QtGui.QCheckBox(ShellPage)
        self.shellWordWrapCheckBox.setObjectName(_fromUtf8("shellWordWrapCheckBox"))
        self.gridlayout.addWidget(self.shellWordWrapCheckBox, 0, 1, 1, 1)
        self.shellACEnabledCheckBox = QtGui.QCheckBox(ShellPage)
        self.shellACEnabledCheckBox.setObjectName(_fromUtf8("shellACEnabledCheckBox"))
        self.gridlayout.addWidget(self.shellACEnabledCheckBox, 1, 0, 1, 1)
        self.shellSyntaxHighlightingCheckBox = QtGui.QCheckBox(ShellPage)
        self.shellSyntaxHighlightingCheckBox.setObjectName(_fromUtf8("shellSyntaxHighlightingCheckBox"))
        self.gridlayout.addWidget(self.shellSyntaxHighlightingCheckBox, 2, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridlayout)
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        self.textLabel1_20 = QtGui.QLabel(ShellPage)
        self.textLabel1_20.setObjectName(_fromUtf8("textLabel1_20"))
        self.hboxlayout.addWidget(self.textLabel1_20)
        self.shellHistorySpinBox = QtGui.QSpinBox(ShellPage)
        self.shellHistorySpinBox.setMinimum(10)
        self.shellHistorySpinBox.setMaximum(1000)
        self.shellHistorySpinBox.setSingleStep(10)
        self.shellHistorySpinBox.setProperty("value", 100)
        self.shellHistorySpinBox.setObjectName(_fromUtf8("shellHistorySpinBox"))
        self.hboxlayout.addWidget(self.shellHistorySpinBox)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.hboxlayout)
        self.stdOutErrCheckBox = QtGui.QCheckBox(ShellPage)
        self.stdOutErrCheckBox.setObjectName(_fromUtf8("stdOutErrCheckBox"))
        self.verticalLayout.addWidget(self.stdOutErrCheckBox)
        self.groupBox_5 = QtGui.QGroupBox(ShellPage)
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_5)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.monospacedFontButton = QtGui.QPushButton(self.groupBox_5)
        self.monospacedFontButton.setObjectName(_fromUtf8("monospacedFontButton"))
        self.gridLayout_2.addWidget(self.monospacedFontButton, 0, 0, 1, 1)
        self.monospacedFontSample = QtGui.QLineEdit(self.groupBox_5)
        self.monospacedFontSample.setFocusPolicy(QtCore.Qt.NoFocus)
        self.monospacedFontSample.setAlignment(QtCore.Qt.AlignHCenter)
        self.monospacedFontSample.setReadOnly(True)
        self.monospacedFontSample.setObjectName(_fromUtf8("monospacedFontSample"))
        self.gridLayout_2.addWidget(self.monospacedFontSample, 0, 1, 1, 1)
        self.monospacedCheckBox = QtGui.QCheckBox(self.groupBox_5)
        self.monospacedCheckBox.setObjectName(_fromUtf8("monospacedCheckBox"))
        self.gridLayout_2.addWidget(self.monospacedCheckBox, 0, 2, 1, 1)
        self.linenumbersFontButton = QtGui.QPushButton(self.groupBox_5)
        self.linenumbersFontButton.setObjectName(_fromUtf8("linenumbersFontButton"))
        self.gridLayout_2.addWidget(self.linenumbersFontButton, 1, 0, 1, 1)
        self.marginsFontSample = QtGui.QLineEdit(self.groupBox_5)
        self.marginsFontSample.setMinimumSize(QtCore.QSize(200, 0))
        self.marginsFontSample.setFocusPolicy(QtCore.Qt.NoFocus)
        self.marginsFontSample.setAlignment(QtCore.Qt.AlignHCenter)
        self.marginsFontSample.setReadOnly(True)
        self.marginsFontSample.setObjectName(_fromUtf8("marginsFontSample"))
        self.gridLayout_2.addWidget(self.marginsFontSample, 1, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_5)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)

        self.retranslateUi(ShellPage)
        QtCore.QMetaObject.connectSlotsByName(ShellPage)
        ShellPage.setTabOrder(self.shellLinenoCheckBox, self.shellACEnabledCheckBox)
        ShellPage.setTabOrder(self.shellACEnabledCheckBox, self.shellSyntaxHighlightingCheckBox)
        ShellPage.setTabOrder(self.shellSyntaxHighlightingCheckBox, self.shellWordWrapCheckBox)
        ShellPage.setTabOrder(self.shellWordWrapCheckBox, self.shellCTEnabledCheckBox)
        ShellPage.setTabOrder(self.shellCTEnabledCheckBox, self.shellHistorySpinBox)

    def retranslateUi(self, ShellPage):
        self.headerLabel.setText(_translate("ShellPage", "<b>Configure Shell</b>", None))
        self.shellLinenoCheckBox.setToolTip(_translate("ShellPage", "Select whether line numbers margin should be shown.", None))
        self.shellLinenoCheckBox.setText(_translate("ShellPage", "Show Line Numbers Margin", None))
        self.shellCTEnabledCheckBox.setToolTip(_translate("ShellPage", "Select this to enable calltips", None))
        self.shellCTEnabledCheckBox.setText(_translate("ShellPage", "Calltips Enabled", None))
        self.shellWordWrapCheckBox.setToolTip(_translate("ShellPage", "Select to enable wrapping at word boundaries", None))
        self.shellWordWrapCheckBox.setText(_translate("ShellPage", "Word Wrap Enabled", None))
        self.shellACEnabledCheckBox.setToolTip(_translate("ShellPage", "Select this to enable autocompletion", None))
        self.shellACEnabledCheckBox.setText(_translate("ShellPage", "Autocompletion Enabled", None))
        self.shellSyntaxHighlightingCheckBox.setToolTip(_translate("ShellPage", "Select to enable syntax highlighting", None))
        self.shellSyntaxHighlightingCheckBox.setText(_translate("ShellPage", "Syntax Highlighting Enabled", None))
        self.textLabel1_20.setText(_translate("ShellPage", "max. History Entries:", None))
        self.shellHistorySpinBox.setToolTip(_translate("ShellPage", "Enter the number of history entries allowed", None))
        self.stdOutErrCheckBox.setToolTip(_translate("ShellPage", "Select to show debuggee stdout and stderr", None))
        self.stdOutErrCheckBox.setText(_translate("ShellPage", "Show stdout and stderr of debuggee", None))
        self.groupBox_5.setTitle(_translate("ShellPage", "Font", None))
        self.monospacedFontButton.setToolTip(_translate("ShellPage", "Press to select the font to be used as the monospaced font", None))
        self.monospacedFontButton.setText(_translate("ShellPage", "Monospaced Font", None))
        self.monospacedFontSample.setText(_translate("ShellPage", "Monospaced Text", None))
        self.monospacedCheckBox.setToolTip(_translate("ShellPage", "Select, whether the monospaced font should be used as default", None))
        self.monospacedCheckBox.setText(_translate("ShellPage", "Use monospaced as default", None))
        self.linenumbersFontButton.setToolTip(_translate("ShellPage", "Press to select the font for the line numbers", None))
        self.linenumbersFontButton.setText(_translate("ShellPage", "Line Numbers Font", None))
        self.marginsFontSample.setText(_translate("ShellPage", "2345", None))

