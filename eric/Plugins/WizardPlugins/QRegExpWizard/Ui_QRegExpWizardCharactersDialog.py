# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Plugins\WizardPlugins\QRegExpWizard\QRegExpWizardCharactersDialog.ui'
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

class Ui_QRegExpWizardCharactersDialog(object):
    def setupUi(self, QRegExpWizardCharactersDialog):
        QRegExpWizardCharactersDialog.setObjectName(_fromUtf8("QRegExpWizardCharactersDialog"))
        QRegExpWizardCharactersDialog.resize(800, 500)
        QRegExpWizardCharactersDialog.setSizeGripEnabled(True)
        self.vboxlayout = QtGui.QVBoxLayout(QRegExpWizardCharactersDialog)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.negativeCheckBox = QtGui.QCheckBox(QRegExpWizardCharactersDialog)
        self.negativeCheckBox.setObjectName(_fromUtf8("negativeCheckBox"))
        self.vboxlayout.addWidget(self.negativeCheckBox)
        self.groupBox = QtGui.QGroupBox(QRegExpWizardCharactersDialog)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridlayout = QtGui.QGridLayout(self.groupBox)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.nonWhitespaceCheckBox = QtGui.QCheckBox(self.groupBox)
        self.nonWhitespaceCheckBox.setObjectName(_fromUtf8("nonWhitespaceCheckBox"))
        self.gridlayout.addWidget(self.nonWhitespaceCheckBox, 1, 2, 1, 1)
        self.nonDigitsCheckBox = QtGui.QCheckBox(self.groupBox)
        self.nonDigitsCheckBox.setObjectName(_fromUtf8("nonDigitsCheckBox"))
        self.gridlayout.addWidget(self.nonDigitsCheckBox, 1, 1, 1, 1)
        self.whitespaceCheckBox = QtGui.QCheckBox(self.groupBox)
        self.whitespaceCheckBox.setObjectName(_fromUtf8("whitespaceCheckBox"))
        self.gridlayout.addWidget(self.whitespaceCheckBox, 0, 2, 1, 1)
        self.digitsCheckBox = QtGui.QCheckBox(self.groupBox)
        self.digitsCheckBox.setObjectName(_fromUtf8("digitsCheckBox"))
        self.gridlayout.addWidget(self.digitsCheckBox, 0, 1, 1, 1)
        self.nonWordCharCheckBox = QtGui.QCheckBox(self.groupBox)
        self.nonWordCharCheckBox.setObjectName(_fromUtf8("nonWordCharCheckBox"))
        self.gridlayout.addWidget(self.nonWordCharCheckBox, 1, 0, 1, 1)
        self.wordCharCheckBox = QtGui.QCheckBox(self.groupBox)
        self.wordCharCheckBox.setObjectName(_fromUtf8("wordCharCheckBox"))
        self.gridlayout.addWidget(self.wordCharCheckBox, 0, 0, 1, 1)
        self.vboxlayout.addWidget(self.groupBox)
        self.singlesBox = QtGui.QGroupBox(QRegExpWizardCharactersDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.singlesBox.sizePolicy().hasHeightForWidth())
        self.singlesBox.setSizePolicy(sizePolicy)
        self.singlesBox.setObjectName(_fromUtf8("singlesBox"))
        self.vboxlayout.addWidget(self.singlesBox)
        self.rangesBox = QtGui.QGroupBox(QRegExpWizardCharactersDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rangesBox.sizePolicy().hasHeightForWidth())
        self.rangesBox.setSizePolicy(sizePolicy)
        self.rangesBox.setObjectName(_fromUtf8("rangesBox"))
        self.vboxlayout.addWidget(self.rangesBox)
        self.buttonBox = QtGui.QDialogButtonBox(QRegExpWizardCharactersDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(QRegExpWizardCharactersDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), QRegExpWizardCharactersDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), QRegExpWizardCharactersDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(QRegExpWizardCharactersDialog)
        QRegExpWizardCharactersDialog.setTabOrder(self.negativeCheckBox, self.wordCharCheckBox)
        QRegExpWizardCharactersDialog.setTabOrder(self.wordCharCheckBox, self.nonWordCharCheckBox)
        QRegExpWizardCharactersDialog.setTabOrder(self.nonWordCharCheckBox, self.digitsCheckBox)
        QRegExpWizardCharactersDialog.setTabOrder(self.digitsCheckBox, self.nonDigitsCheckBox)
        QRegExpWizardCharactersDialog.setTabOrder(self.nonDigitsCheckBox, self.whitespaceCheckBox)
        QRegExpWizardCharactersDialog.setTabOrder(self.whitespaceCheckBox, self.nonWhitespaceCheckBox)

    def retranslateUi(self, QRegExpWizardCharactersDialog):
        QRegExpWizardCharactersDialog.setWindowTitle(_translate("QRegExpWizardCharactersDialog", "Editor for character sets", None))
        self.negativeCheckBox.setText(_translate("QRegExpWizardCharactersDialog", "The defined characters should not match", None))
        self.groupBox.setTitle(_translate("QRegExpWizardCharactersDialog", "Predefined character ranges", None))
        self.nonWhitespaceCheckBox.setText(_translate("QRegExpWizardCharactersDialog", "Non-whitespace characters", None))
        self.nonDigitsCheckBox.setText(_translate("QRegExpWizardCharactersDialog", "Non-digits", None))
        self.whitespaceCheckBox.setText(_translate("QRegExpWizardCharactersDialog", "Whitespace characters", None))
        self.digitsCheckBox.setText(_translate("QRegExpWizardCharactersDialog", "Digits", None))
        self.nonWordCharCheckBox.setText(_translate("QRegExpWizardCharactersDialog", "Non-word characters", None))
        self.wordCharCheckBox.setText(_translate("QRegExpWizardCharactersDialog", "Word character", None))
        self.singlesBox.setTitle(_translate("QRegExpWizardCharactersDialog", "Single character", None))
        self.rangesBox.setTitle(_translate("QRegExpWizardCharactersDialog", "Character ranges", None))

