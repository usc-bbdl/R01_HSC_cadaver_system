# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Plugins\WizardPlugins\InputDialogWizard\InputDialogWizardDialog.ui'
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

class Ui_InputDialogWizardDialog(object):
    def setupUi(self, InputDialogWizardDialog):
        InputDialogWizardDialog.setObjectName(_fromUtf8("InputDialogWizardDialog"))
        InputDialogWizardDialog.resize(501, 658)
        InputDialogWizardDialog.setSizeGripEnabled(True)
        self.vboxlayout = QtGui.QVBoxLayout(InputDialogWizardDialog)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.groupBox = QtGui.QGroupBox(InputDialogWizardDialog)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.hboxlayout = QtGui.QHBoxLayout(self.groupBox)
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        self.rText = QtGui.QRadioButton(self.groupBox)
        self.rText.setChecked(True)
        self.rText.setObjectName(_fromUtf8("rText"))
        self.hboxlayout.addWidget(self.rText)
        self.rInteger = QtGui.QRadioButton(self.groupBox)
        self.rInteger.setObjectName(_fromUtf8("rInteger"))
        self.hboxlayout.addWidget(self.rInteger)
        self.rDouble = QtGui.QRadioButton(self.groupBox)
        self.rDouble.setObjectName(_fromUtf8("rDouble"))
        self.hboxlayout.addWidget(self.rDouble)
        self.rItem = QtGui.QRadioButton(self.groupBox)
        self.rItem.setObjectName(_fromUtf8("rItem"))
        self.hboxlayout.addWidget(self.rItem)
        self.vboxlayout.addWidget(self.groupBox)
        self.TextLabel1 = QtGui.QLabel(InputDialogWizardDialog)
        self.TextLabel1.setObjectName(_fromUtf8("TextLabel1"))
        self.vboxlayout.addWidget(self.TextLabel1)
        self.eCaption = QtGui.QLineEdit(InputDialogWizardDialog)
        self.eCaption.setObjectName(_fromUtf8("eCaption"))
        self.vboxlayout.addWidget(self.eCaption)
        self.TextLabel2 = QtGui.QLabel(InputDialogWizardDialog)
        self.TextLabel2.setObjectName(_fromUtf8("TextLabel2"))
        self.vboxlayout.addWidget(self.TextLabel2)
        self.eLabel = QtGui.QLineEdit(InputDialogWizardDialog)
        self.eLabel.setObjectName(_fromUtf8("eLabel"))
        self.vboxlayout.addWidget(self.eLabel)
        self.groupBox_2 = QtGui.QGroupBox(InputDialogWizardDialog)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.vboxlayout1 = QtGui.QVBoxLayout(self.groupBox_2)
        self.vboxlayout1.setObjectName(_fromUtf8("vboxlayout1"))
        self.groupBox_3 = QtGui.QGroupBox(self.groupBox_2)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.hboxlayout1 = QtGui.QHBoxLayout(self.groupBox_3)
        self.hboxlayout1.setObjectName(_fromUtf8("hboxlayout1"))
        self.rEchoNormal = QtGui.QRadioButton(self.groupBox_3)
        self.rEchoNormal.setChecked(True)
        self.rEchoNormal.setObjectName(_fromUtf8("rEchoNormal"))
        self.hboxlayout1.addWidget(self.rEchoNormal)
        self.rEchoNoEcho = QtGui.QRadioButton(self.groupBox_3)
        self.rEchoNoEcho.setObjectName(_fromUtf8("rEchoNoEcho"))
        self.hboxlayout1.addWidget(self.rEchoNoEcho)
        self.rEchoPassword = QtGui.QRadioButton(self.groupBox_3)
        self.rEchoPassword.setObjectName(_fromUtf8("rEchoPassword"))
        self.hboxlayout1.addWidget(self.rEchoPassword)
        self.vboxlayout1.addWidget(self.groupBox_3)
        self.TextLabel3 = QtGui.QLabel(self.groupBox_2)
        self.TextLabel3.setObjectName(_fromUtf8("TextLabel3"))
        self.vboxlayout1.addWidget(self.TextLabel3)
        self.eTextDefault = QtGui.QLineEdit(self.groupBox_2)
        self.eTextDefault.setObjectName(_fromUtf8("eTextDefault"))
        self.vboxlayout1.addWidget(self.eTextDefault)
        self.vboxlayout.addWidget(self.groupBox_2)
        self.groupBox_4 = QtGui.QGroupBox(InputDialogWizardDialog)
        self.groupBox_4.setEnabled(False)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.gridlayout = QtGui.QGridLayout(self.groupBox_4)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.sIntStep = QtGui.QSpinBox(self.groupBox_4)
        self.sIntStep.setMinimum(-2147483647)
        self.sIntStep.setMaximum(2147483647)
        self.sIntStep.setProperty("value", 1)
        self.sIntStep.setObjectName(_fromUtf8("sIntStep"))
        self.gridlayout.addWidget(self.sIntStep, 1, 3, 1, 1)
        self.sIntTo = QtGui.QSpinBox(self.groupBox_4)
        self.sIntTo.setMinimum(-2147483647)
        self.sIntTo.setMaximum(2147483647)
        self.sIntTo.setProperty("value", 2147483647)
        self.sIntTo.setObjectName(_fromUtf8("sIntTo"))
        self.gridlayout.addWidget(self.sIntTo, 1, 2, 1, 1)
        self.sIntFrom = QtGui.QSpinBox(self.groupBox_4)
        self.sIntFrom.setMinimum(-2147483647)
        self.sIntFrom.setMaximum(2147483647)
        self.sIntFrom.setProperty("value", -2147483647)
        self.sIntFrom.setObjectName(_fromUtf8("sIntFrom"))
        self.gridlayout.addWidget(self.sIntFrom, 1, 1, 1, 1)
        self.sIntDefault = QtGui.QSpinBox(self.groupBox_4)
        self.sIntDefault.setMinimum(-2147483647)
        self.sIntDefault.setMaximum(2147483647)
        self.sIntDefault.setObjectName(_fromUtf8("sIntDefault"))
        self.gridlayout.addWidget(self.sIntDefault, 1, 0, 1, 1)
        self.TextLabel4_4 = QtGui.QLabel(self.groupBox_4)
        self.TextLabel4_4.setObjectName(_fromUtf8("TextLabel4_4"))
        self.gridlayout.addWidget(self.TextLabel4_4, 0, 3, 1, 1)
        self.TextLabel4_3 = QtGui.QLabel(self.groupBox_4)
        self.TextLabel4_3.setObjectName(_fromUtf8("TextLabel4_3"))
        self.gridlayout.addWidget(self.TextLabel4_3, 0, 2, 1, 1)
        self.TextLabel4_2 = QtGui.QLabel(self.groupBox_4)
        self.TextLabel4_2.setObjectName(_fromUtf8("TextLabel4_2"))
        self.gridlayout.addWidget(self.TextLabel4_2, 0, 1, 1, 1)
        self.TextLabel4 = QtGui.QLabel(self.groupBox_4)
        self.TextLabel4.setObjectName(_fromUtf8("TextLabel4"))
        self.gridlayout.addWidget(self.TextLabel4, 0, 0, 1, 1)
        self.vboxlayout.addWidget(self.groupBox_4)
        self.groupBox_5 = QtGui.QGroupBox(InputDialogWizardDialog)
        self.groupBox_5.setEnabled(False)
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.gridlayout1 = QtGui.QGridLayout(self.groupBox_5)
        self.gridlayout1.setObjectName(_fromUtf8("gridlayout1"))
        self.sDoubleDecimals = QtGui.QSpinBox(self.groupBox_5)
        self.sDoubleDecimals.setMinimum(-2147483647)
        self.sDoubleDecimals.setMaximum(2147483647)
        self.sDoubleDecimals.setProperty("value", 1)
        self.sDoubleDecimals.setObjectName(_fromUtf8("sDoubleDecimals"))
        self.gridlayout1.addWidget(self.sDoubleDecimals, 1, 3, 1, 1)
        self.eDoubleTo = QtGui.QLineEdit(self.groupBox_5)
        self.eDoubleTo.setObjectName(_fromUtf8("eDoubleTo"))
        self.gridlayout1.addWidget(self.eDoubleTo, 1, 2, 1, 1)
        self.eDoubleFrom = QtGui.QLineEdit(self.groupBox_5)
        self.eDoubleFrom.setObjectName(_fromUtf8("eDoubleFrom"))
        self.gridlayout1.addWidget(self.eDoubleFrom, 1, 1, 1, 1)
        self.eDoubleDefault = QtGui.QLineEdit(self.groupBox_5)
        self.eDoubleDefault.setObjectName(_fromUtf8("eDoubleDefault"))
        self.gridlayout1.addWidget(self.eDoubleDefault, 1, 0, 1, 1)
        self.TextLabel5 = QtGui.QLabel(self.groupBox_5)
        self.TextLabel5.setObjectName(_fromUtf8("TextLabel5"))
        self.gridlayout1.addWidget(self.TextLabel5, 0, 0, 1, 1)
        self.TextLabel6 = QtGui.QLabel(self.groupBox_5)
        self.TextLabel6.setObjectName(_fromUtf8("TextLabel6"))
        self.gridlayout1.addWidget(self.TextLabel6, 0, 1, 1, 1)
        self.TextLabel7 = QtGui.QLabel(self.groupBox_5)
        self.TextLabel7.setObjectName(_fromUtf8("TextLabel7"))
        self.gridlayout1.addWidget(self.TextLabel7, 0, 2, 1, 1)
        self.TextLabel8 = QtGui.QLabel(self.groupBox_5)
        self.TextLabel8.setObjectName(_fromUtf8("TextLabel8"))
        self.gridlayout1.addWidget(self.TextLabel8, 0, 3, 1, 1)
        self.vboxlayout.addWidget(self.groupBox_5)
        self.groupBox_6 = QtGui.QGroupBox(InputDialogWizardDialog)
        self.groupBox_6.setEnabled(False)
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.gridlayout2 = QtGui.QGridLayout(self.groupBox_6)
        self.gridlayout2.setObjectName(_fromUtf8("gridlayout2"))
        self.cEditable = QtGui.QCheckBox(self.groupBox_6)
        self.cEditable.setChecked(True)
        self.cEditable.setObjectName(_fromUtf8("cEditable"))
        self.gridlayout2.addWidget(self.cEditable, 1, 2, 1, 1)
        self.sCurrentItem = QtGui.QSpinBox(self.groupBox_6)
        self.sCurrentItem.setObjectName(_fromUtf8("sCurrentItem"))
        self.gridlayout2.addWidget(self.sCurrentItem, 1, 1, 1, 1)
        self.eVariable = QtGui.QLineEdit(self.groupBox_6)
        self.eVariable.setObjectName(_fromUtf8("eVariable"))
        self.gridlayout2.addWidget(self.eVariable, 1, 0, 1, 1)
        self.TextLabel10 = QtGui.QLabel(self.groupBox_6)
        self.TextLabel10.setObjectName(_fromUtf8("TextLabel10"))
        self.gridlayout2.addWidget(self.TextLabel10, 0, 1, 1, 1)
        self.TextLabel9 = QtGui.QLabel(self.groupBox_6)
        self.TextLabel9.setObjectName(_fromUtf8("TextLabel9"))
        self.gridlayout2.addWidget(self.TextLabel9, 0, 0, 1, 1)
        self.vboxlayout.addWidget(self.groupBox_6)
        self.buttonBox = QtGui.QDialogButtonBox(InputDialogWizardDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(InputDialogWizardDialog)
        QtCore.QObject.connect(self.rText, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.groupBox_2.setEnabled)
        QtCore.QObject.connect(self.rInteger, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.groupBox_4.setEnabled)
        QtCore.QObject.connect(self.rDouble, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.groupBox_5.setEnabled)
        QtCore.QObject.connect(self.rItem, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.groupBox_6.setEnabled)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), InputDialogWizardDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), InputDialogWizardDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(InputDialogWizardDialog)
        InputDialogWizardDialog.setTabOrder(self.rText, self.rInteger)
        InputDialogWizardDialog.setTabOrder(self.rInteger, self.rDouble)
        InputDialogWizardDialog.setTabOrder(self.rDouble, self.rItem)
        InputDialogWizardDialog.setTabOrder(self.rItem, self.eCaption)
        InputDialogWizardDialog.setTabOrder(self.eCaption, self.eLabel)
        InputDialogWizardDialog.setTabOrder(self.eLabel, self.rEchoNormal)
        InputDialogWizardDialog.setTabOrder(self.rEchoNormal, self.rEchoNoEcho)
        InputDialogWizardDialog.setTabOrder(self.rEchoNoEcho, self.rEchoPassword)
        InputDialogWizardDialog.setTabOrder(self.rEchoPassword, self.eTextDefault)
        InputDialogWizardDialog.setTabOrder(self.eTextDefault, self.sIntDefault)
        InputDialogWizardDialog.setTabOrder(self.sIntDefault, self.sIntFrom)
        InputDialogWizardDialog.setTabOrder(self.sIntFrom, self.sIntTo)
        InputDialogWizardDialog.setTabOrder(self.sIntTo, self.sIntStep)
        InputDialogWizardDialog.setTabOrder(self.sIntStep, self.eDoubleDefault)
        InputDialogWizardDialog.setTabOrder(self.eDoubleDefault, self.eDoubleFrom)
        InputDialogWizardDialog.setTabOrder(self.eDoubleFrom, self.eDoubleTo)
        InputDialogWizardDialog.setTabOrder(self.eDoubleTo, self.sDoubleDecimals)
        InputDialogWizardDialog.setTabOrder(self.sDoubleDecimals, self.eVariable)
        InputDialogWizardDialog.setTabOrder(self.eVariable, self.sCurrentItem)
        InputDialogWizardDialog.setTabOrder(self.sCurrentItem, self.cEditable)

    def retranslateUi(self, InputDialogWizardDialog):
        InputDialogWizardDialog.setWindowTitle(_translate("InputDialogWizardDialog", "QInputDialog Wizard", None))
        self.groupBox.setTitle(_translate("InputDialogWizardDialog", "Type", None))
        self.rText.setText(_translate("InputDialogWizardDialog", "Text", None))
        self.rInteger.setText(_translate("InputDialogWizardDialog", "Integer", None))
        self.rDouble.setText(_translate("InputDialogWizardDialog", "Double", None))
        self.rItem.setText(_translate("InputDialogWizardDialog", "Item", None))
        self.TextLabel1.setText(_translate("InputDialogWizardDialog", "Caption", None))
        self.TextLabel2.setText(_translate("InputDialogWizardDialog", "Label", None))
        self.groupBox_2.setTitle(_translate("InputDialogWizardDialog", "Text", None))
        self.groupBox_3.setTitle(_translate("InputDialogWizardDialog", "Echo Mode", None))
        self.rEchoNormal.setText(_translate("InputDialogWizardDialog", "Normal", None))
        self.rEchoNoEcho.setText(_translate("InputDialogWizardDialog", "No Echo", None))
        self.rEchoPassword.setText(_translate("InputDialogWizardDialog", "Password", None))
        self.TextLabel3.setText(_translate("InputDialogWizardDialog", "Default", None))
        self.groupBox_4.setTitle(_translate("InputDialogWizardDialog", "Integer", None))
        self.TextLabel4_4.setText(_translate("InputDialogWizardDialog", "Step", None))
        self.TextLabel4_3.setText(_translate("InputDialogWizardDialog", "To", None))
        self.TextLabel4_2.setText(_translate("InputDialogWizardDialog", "From", None))
        self.TextLabel4.setText(_translate("InputDialogWizardDialog", "Default", None))
        self.groupBox_5.setTitle(_translate("InputDialogWizardDialog", "Double", None))
        self.eDoubleTo.setText(_translate("InputDialogWizardDialog", "2147483647", None))
        self.eDoubleFrom.setText(_translate("InputDialogWizardDialog", "-2147483647", None))
        self.eDoubleDefault.setText(_translate("InputDialogWizardDialog", "0", None))
        self.TextLabel5.setText(_translate("InputDialogWizardDialog", "Default", None))
        self.TextLabel6.setText(_translate("InputDialogWizardDialog", "From", None))
        self.TextLabel7.setText(_translate("InputDialogWizardDialog", "To", None))
        self.TextLabel8.setText(_translate("InputDialogWizardDialog", "Decimals", None))
        self.groupBox_6.setTitle(_translate("InputDialogWizardDialog", "Item", None))
        self.cEditable.setText(_translate("InputDialogWizardDialog", "Editable", None))
        self.TextLabel10.setText(_translate("InputDialogWizardDialog", "Current Item", None))
        self.TextLabel9.setText(_translate("InputDialogWizardDialog", "String List Variable", None))
