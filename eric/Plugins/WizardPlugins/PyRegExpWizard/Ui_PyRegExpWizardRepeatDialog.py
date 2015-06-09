# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Plugins\WizardPlugins\PyRegExpWizard\PyRegExpWizardRepeatDialog.ui'
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

class Ui_PyRegExpWizardRepeatDialog(object):
    def setupUi(self, PyRegExpWizardRepeatDialog):
        PyRegExpWizardRepeatDialog.setObjectName(_fromUtf8("PyRegExpWizardRepeatDialog"))
        PyRegExpWizardRepeatDialog.resize(331, 223)
        PyRegExpWizardRepeatDialog.setSizeGripEnabled(True)
        self.vboxlayout = QtGui.QVBoxLayout(PyRegExpWizardRepeatDialog)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.groupBox = QtGui.QGroupBox(PyRegExpWizardRepeatDialog)
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setFlat(True)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridlayout = QtGui.QGridLayout(self.groupBox)
        self.gridlayout.setMargin(0)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.textLabel1_6 = QtGui.QLabel(self.groupBox)
        self.textLabel1_6.setObjectName(_fromUtf8("textLabel1_6"))
        self.gridlayout.addWidget(self.textLabel1_6, 2, 2, 1, 1)
        self.textLabel1_7 = QtGui.QLabel(self.groupBox)
        self.textLabel1_7.setObjectName(_fromUtf8("textLabel1_7"))
        self.gridlayout.addWidget(self.textLabel1_7, 3, 2, 1, 1)
        self.textLabel1_5 = QtGui.QLabel(self.groupBox)
        self.textLabel1_5.setObjectName(_fromUtf8("textLabel1_5"))
        self.gridlayout.addWidget(self.textLabel1_5, 1, 2, 1, 1)
        self.lowerSpin = QtGui.QSpinBox(self.groupBox)
        self.lowerSpin.setEnabled(False)
        self.lowerSpin.setAlignment(QtCore.Qt.AlignRight)
        self.lowerSpin.setProperty("value", 1)
        self.lowerSpin.setObjectName(_fromUtf8("lowerSpin"))
        self.gridlayout.addWidget(self.lowerSpin, 4, 1, 1, 1)
        self.upperSpin = QtGui.QSpinBox(self.groupBox)
        self.upperSpin.setEnabled(False)
        self.upperSpin.setAlignment(QtCore.Qt.AlignRight)
        self.upperSpin.setProperty("value", 1)
        self.upperSpin.setObjectName(_fromUtf8("upperSpin"))
        self.gridlayout.addWidget(self.upperSpin, 4, 3, 1, 1)
        self.textLabel6 = QtGui.QLabel(self.groupBox)
        self.textLabel6.setObjectName(_fromUtf8("textLabel6"))
        self.gridlayout.addWidget(self.textLabel6, 4, 2, 1, 1)
        self.betweenButton = QtGui.QRadioButton(self.groupBox)
        self.betweenButton.setObjectName(_fromUtf8("betweenButton"))
        self.gridlayout.addWidget(self.betweenButton, 4, 0, 1, 1)
        self.exactSpin = QtGui.QSpinBox(self.groupBox)
        self.exactSpin.setEnabled(False)
        self.exactSpin.setAlignment(QtCore.Qt.AlignRight)
        self.exactSpin.setProperty("value", 1)
        self.exactSpin.setObjectName(_fromUtf8("exactSpin"))
        self.gridlayout.addWidget(self.exactSpin, 3, 1, 1, 1)
        self.exactButton = QtGui.QRadioButton(self.groupBox)
        self.exactButton.setObjectName(_fromUtf8("exactButton"))
        self.gridlayout.addWidget(self.exactButton, 3, 0, 1, 1)
        self.maxSpin = QtGui.QSpinBox(self.groupBox)
        self.maxSpin.setEnabled(False)
        self.maxSpin.setAlignment(QtCore.Qt.AlignRight)
        self.maxSpin.setProperty("value", 1)
        self.maxSpin.setObjectName(_fromUtf8("maxSpin"))
        self.gridlayout.addWidget(self.maxSpin, 2, 1, 1, 1)
        self.maxButton = QtGui.QRadioButton(self.groupBox)
        self.maxButton.setObjectName(_fromUtf8("maxButton"))
        self.gridlayout.addWidget(self.maxButton, 2, 0, 1, 1)
        self.minButton = QtGui.QRadioButton(self.groupBox)
        self.minButton.setObjectName(_fromUtf8("minButton"))
        self.gridlayout.addWidget(self.minButton, 1, 0, 1, 1)
        self.minSpin = QtGui.QSpinBox(self.groupBox)
        self.minSpin.setEnabled(False)
        self.minSpin.setAlignment(QtCore.Qt.AlignRight)
        self.minSpin.setProperty("value", 1)
        self.minSpin.setObjectName(_fromUtf8("minSpin"))
        self.gridlayout.addWidget(self.minSpin, 1, 1, 1, 1)
        self.unlimitedButton = QtGui.QRadioButton(self.groupBox)
        self.unlimitedButton.setObjectName(_fromUtf8("unlimitedButton"))
        self.gridlayout.addWidget(self.unlimitedButton, 0, 0, 1, 4)
        self.vboxlayout.addWidget(self.groupBox)
        self.minimalCheckBox = QtGui.QCheckBox(PyRegExpWizardRepeatDialog)
        self.minimalCheckBox.setObjectName(_fromUtf8("minimalCheckBox"))
        self.vboxlayout.addWidget(self.minimalCheckBox)
        self.buttonBox = QtGui.QDialogButtonBox(PyRegExpWizardRepeatDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(PyRegExpWizardRepeatDialog)
        QtCore.QObject.connect(self.minButton, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.minSpin.setEnabled)
        QtCore.QObject.connect(self.maxButton, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.maxSpin.setEnabled)
        QtCore.QObject.connect(self.exactButton, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.exactSpin.setEnabled)
        QtCore.QObject.connect(self.betweenButton, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.lowerSpin.setEnabled)
        QtCore.QObject.connect(self.betweenButton, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.upperSpin.setEnabled)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), PyRegExpWizardRepeatDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), PyRegExpWizardRepeatDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(PyRegExpWizardRepeatDialog)
        PyRegExpWizardRepeatDialog.setTabOrder(self.unlimitedButton, self.minButton)
        PyRegExpWizardRepeatDialog.setTabOrder(self.minButton, self.minSpin)
        PyRegExpWizardRepeatDialog.setTabOrder(self.minSpin, self.maxButton)
        PyRegExpWizardRepeatDialog.setTabOrder(self.maxButton, self.maxSpin)
        PyRegExpWizardRepeatDialog.setTabOrder(self.maxSpin, self.exactButton)
        PyRegExpWizardRepeatDialog.setTabOrder(self.exactButton, self.exactSpin)
        PyRegExpWizardRepeatDialog.setTabOrder(self.exactSpin, self.betweenButton)
        PyRegExpWizardRepeatDialog.setTabOrder(self.betweenButton, self.lowerSpin)
        PyRegExpWizardRepeatDialog.setTabOrder(self.lowerSpin, self.upperSpin)
        PyRegExpWizardRepeatDialog.setTabOrder(self.upperSpin, self.minimalCheckBox)

    def retranslateUi(self, PyRegExpWizardRepeatDialog):
        PyRegExpWizardRepeatDialog.setWindowTitle(_translate("PyRegExpWizardRepeatDialog", "Number of repetitions", None))
        self.textLabel1_6.setText(_translate("PyRegExpWizardRepeatDialog", "times", None))
        self.textLabel1_7.setText(_translate("PyRegExpWizardRepeatDialog", "times", None))
        self.textLabel1_5.setText(_translate("PyRegExpWizardRepeatDialog", "times", None))
        self.textLabel6.setText(_translate("PyRegExpWizardRepeatDialog", "and", None))
        self.betweenButton.setText(_translate("PyRegExpWizardRepeatDialog", "Between", None))
        self.exactButton.setText(_translate("PyRegExpWizardRepeatDialog", "Exactly", None))
        self.maxButton.setText(_translate("PyRegExpWizardRepeatDialog", "Maximum", None))
        self.minButton.setText(_translate("PyRegExpWizardRepeatDialog", "Minimum", None))
        self.unlimitedButton.setText(_translate("PyRegExpWizardRepeatDialog", "Unlimited (incl. zero times)", None))
        self.minimalCheckBox.setText(_translate("PyRegExpWizardRepeatDialog", "Minimal match", None))

