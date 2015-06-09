# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Preferences\ConfigurationPages\EditorAutocompletionPage.ui'
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

class Ui_EditorAutocompletionPage(object):
    def setupUi(self, EditorAutocompletionPage):
        EditorAutocompletionPage.setObjectName(_fromUtf8("EditorAutocompletionPage"))
        EditorAutocompletionPage.resize(506, 294)
        self.verticalLayout = QtGui.QVBoxLayout(EditorAutocompletionPage)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.headerLabel = QtGui.QLabel(EditorAutocompletionPage)
        self.headerLabel.setObjectName(_fromUtf8("headerLabel"))
        self.verticalLayout.addWidget(self.headerLabel)
        self.line6 = QtGui.QFrame(EditorAutocompletionPage)
        self.line6.setFrameShape(QtGui.QFrame.HLine)
        self.line6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line6.setFrameShape(QtGui.QFrame.HLine)
        self.line6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line6.setObjectName(_fromUtf8("line6"))
        self.verticalLayout.addWidget(self.line6)
        self.acEnabledCheckBox = QtGui.QCheckBox(EditorAutocompletionPage)
        self.acEnabledCheckBox.setObjectName(_fromUtf8("acEnabledCheckBox"))
        self.verticalLayout.addWidget(self.acEnabledCheckBox)
        self.groupBox = QtGui.QGroupBox(EditorAutocompletionPage)
        self.groupBox.setEnabled(False)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.acCaseSensitivityCheckBox = QtGui.QCheckBox(self.groupBox)
        self.acCaseSensitivityCheckBox.setObjectName(_fromUtf8("acCaseSensitivityCheckBox"))
        self.gridLayout.addWidget(self.acCaseSensitivityCheckBox, 0, 0, 1, 1)
        self.acReplaceWordCheckBox = QtGui.QCheckBox(self.groupBox)
        self.acReplaceWordCheckBox.setObjectName(_fromUtf8("acReplaceWordCheckBox"))
        self.gridLayout.addWidget(self.acReplaceWordCheckBox, 0, 1, 1, 1)
        self._2 = QtGui.QHBoxLayout()
        self._2.setObjectName(_fromUtf8("_2"))
        self.textLabel1_2 = QtGui.QLabel(self.groupBox)
        self.textLabel1_2.setObjectName(_fromUtf8("textLabel1_2"))
        self._2.addWidget(self.textLabel1_2)
        self.acThresholdSlider = QtGui.QSlider(self.groupBox)
        self.acThresholdSlider.setMaximum(10)
        self.acThresholdSlider.setProperty("value", 2)
        self.acThresholdSlider.setOrientation(QtCore.Qt.Horizontal)
        self.acThresholdSlider.setTickInterval(1)
        self.acThresholdSlider.setObjectName(_fromUtf8("acThresholdSlider"))
        self._2.addWidget(self.acThresholdSlider)
        self.lCDNumber4 = QtGui.QLCDNumber(self.groupBox)
        self.lCDNumber4.setDigitCount(2)
        self.lCDNumber4.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lCDNumber4.setProperty("value", 2.0)
        self.lCDNumber4.setObjectName(_fromUtf8("lCDNumber4"))
        self._2.addWidget(self.lCDNumber4)
        self.gridLayout.addLayout(self._2, 1, 0, 1, 2)
        self.verticalLayout.addWidget(self.groupBox)
        spacerItem = QtGui.QSpacerItem(456, 51, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(EditorAutocompletionPage)
        QtCore.QObject.connect(self.acThresholdSlider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.lCDNumber4.display)
        QtCore.QObject.connect(self.acEnabledCheckBox, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.groupBox.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(EditorAutocompletionPage)

    def retranslateUi(self, EditorAutocompletionPage):
        self.headerLabel.setText(_translate("EditorAutocompletionPage", "<b>Configure Autocompletion</b>", None))
        self.acEnabledCheckBox.setToolTip(_translate("EditorAutocompletionPage", "Select this to enable autocompletion", None))
        self.acEnabledCheckBox.setWhatsThis(_translate("EditorAutocompletionPage", "<b>Autocompletion Enabled</b><p>Select to enable autocompletion. In order to get autocompletion from alternative autocompletion providers (if installed), these have to be enabled on their respective configuration page. Only one alternative provider might be enabled.</p>", None))
        self.acEnabledCheckBox.setText(_translate("EditorAutocompletionPage", "Autocompletion Enabled", None))
        self.groupBox.setTitle(_translate("EditorAutocompletionPage", "General", None))
        self.acCaseSensitivityCheckBox.setToolTip(_translate("EditorAutocompletionPage", "Select this to have case sensitive auto-completion lists", None))
        self.acCaseSensitivityCheckBox.setText(_translate("EditorAutocompletionPage", "Case sensitive", None))
        self.acReplaceWordCheckBox.setToolTip(_translate("EditorAutocompletionPage", "Select this, if the word to the right should be replaced by the selected entry", None))
        self.acReplaceWordCheckBox.setText(_translate("EditorAutocompletionPage", "Replace word", None))
        self.textLabel1_2.setText(_translate("EditorAutocompletionPage", "Threshold:", None))
        self.acThresholdSlider.setToolTip(_translate("EditorAutocompletionPage", "Move to set the threshold for display of an autocompletion list", None))
        self.lCDNumber4.setToolTip(_translate("EditorAutocompletionPage", "Displays the selected autocompletion threshold", None))

