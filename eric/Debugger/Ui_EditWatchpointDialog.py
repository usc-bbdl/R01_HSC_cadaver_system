# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Debugger\EditWatchpointDialog.ui'
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

class Ui_EditWatchpointDialog(object):
    def setupUi(self, EditWatchpointDialog):
        EditWatchpointDialog.setObjectName(_fromUtf8("EditWatchpointDialog"))
        EditWatchpointDialog.resize(402, 234)
        EditWatchpointDialog.setSizeGripEnabled(True)
        self.gridlayout = QtGui.QGridLayout(EditWatchpointDialog)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.buttonBox = QtGui.QDialogButtonBox(EditWatchpointDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridlayout.addWidget(self.buttonBox, 4, 0, 1, 3)
        spacerItem = QtGui.QSpacerItem(211, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridlayout.addItem(spacerItem, 1, 2, 1, 1)
        self.ignoreSpinBox = QtGui.QSpinBox(EditWatchpointDialog)
        self.ignoreSpinBox.setMaximum(9999)
        self.ignoreSpinBox.setObjectName(_fromUtf8("ignoreSpinBox"))
        self.gridlayout.addWidget(self.ignoreSpinBox, 1, 1, 1, 1)
        self.textLabel2 = QtGui.QLabel(EditWatchpointDialog)
        self.textLabel2.setObjectName(_fromUtf8("textLabel2"))
        self.gridlayout.addWidget(self.textLabel2, 1, 0, 1, 1)
        self.enabledCheckBox = QtGui.QCheckBox(EditWatchpointDialog)
        self.enabledCheckBox.setObjectName(_fromUtf8("enabledCheckBox"))
        self.gridlayout.addWidget(self.enabledCheckBox, 3, 0, 1, 3)
        self.temporaryCheckBox = QtGui.QCheckBox(EditWatchpointDialog)
        self.temporaryCheckBox.setObjectName(_fromUtf8("temporaryCheckBox"))
        self.gridlayout.addWidget(self.temporaryCheckBox, 2, 0, 1, 3)
        self.groupBox = QtGui.QGroupBox(EditWatchpointDialog)
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridlayout1 = QtGui.QGridLayout(self.groupBox)
        self.gridlayout1.setObjectName(_fromUtf8("gridlayout1"))
        self.specialButton = QtGui.QRadioButton(self.groupBox)
        self.specialButton.setObjectName(_fromUtf8("specialButton"))
        self.gridlayout1.addWidget(self.specialButton, 1, 0, 1, 1)
        self.conditionButton = QtGui.QRadioButton(self.groupBox)
        self.conditionButton.setChecked(True)
        self.conditionButton.setObjectName(_fromUtf8("conditionButton"))
        self.gridlayout1.addWidget(self.conditionButton, 0, 0, 1, 1)
        self.specialEdit = QtGui.QLineEdit(self.groupBox)
        self.specialEdit.setEnabled(False)
        self.specialEdit.setObjectName(_fromUtf8("specialEdit"))
        self.gridlayout1.addWidget(self.specialEdit, 1, 1, 1, 1)
        self.specialCombo = QtGui.QComboBox(self.groupBox)
        self.specialCombo.setEnabled(False)
        self.specialCombo.setObjectName(_fromUtf8("specialCombo"))
        self.specialCombo.addItem(_fromUtf8(""))
        self.specialCombo.addItem(_fromUtf8(""))
        self.gridlayout1.addWidget(self.specialCombo, 2, 1, 1, 1)
        self.conditionEdit = QtGui.QLineEdit(self.groupBox)
        self.conditionEdit.setObjectName(_fromUtf8("conditionEdit"))
        self.gridlayout1.addWidget(self.conditionEdit, 0, 1, 1, 1)
        self.gridlayout.addWidget(self.groupBox, 0, 0, 1, 3)

        self.retranslateUi(EditWatchpointDialog)
        QtCore.QObject.connect(self.conditionButton, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.conditionEdit.setEnabled)
        QtCore.QObject.connect(self.specialButton, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.specialCombo.setEnabled)
        QtCore.QObject.connect(self.specialButton, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.specialEdit.setEnabled)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), EditWatchpointDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), EditWatchpointDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(EditWatchpointDialog)
        EditWatchpointDialog.setTabOrder(self.conditionButton, self.conditionEdit)
        EditWatchpointDialog.setTabOrder(self.conditionEdit, self.specialButton)
        EditWatchpointDialog.setTabOrder(self.specialButton, self.specialEdit)
        EditWatchpointDialog.setTabOrder(self.specialEdit, self.specialCombo)
        EditWatchpointDialog.setTabOrder(self.specialCombo, self.ignoreSpinBox)
        EditWatchpointDialog.setTabOrder(self.ignoreSpinBox, self.temporaryCheckBox)
        EditWatchpointDialog.setTabOrder(self.temporaryCheckBox, self.enabledCheckBox)

    def retranslateUi(self, EditWatchpointDialog):
        EditWatchpointDialog.setWindowTitle(_translate("EditWatchpointDialog", "Edit Watch Expression", None))
        self.ignoreSpinBox.setToolTip(_translate("EditWatchpointDialog", "Enter an ignore count for the watch expression", None))
        self.textLabel2.setText(_translate("EditWatchpointDialog", "Ignore Count:", None))
        self.enabledCheckBox.setToolTip(_translate("EditWatchpointDialog", "Select, whether the watch expression is enabled", None))
        self.enabledCheckBox.setText(_translate("EditWatchpointDialog", "Enabled", None))
        self.temporaryCheckBox.setToolTip(_translate("EditWatchpointDialog", "Select whether this is a temporary watch expression", None))
        self.temporaryCheckBox.setText(_translate("EditWatchpointDialog", "Temporary Watch Expression", None))
        self.specialButton.setText(_translate("EditWatchpointDialog", "Variable:", None))
        self.conditionButton.setText(_translate("EditWatchpointDialog", "Expression:", None))
        self.specialEdit.setToolTip(_translate("EditWatchpointDialog", "Enter a variable and select the special condition below", None))
        self.specialCombo.setToolTip(_translate("EditWatchpointDialog", "Select a special condition", None))
        self.specialCombo.setItemText(0, _translate("EditWatchpointDialog", "created", None))
        self.specialCombo.setItemText(1, _translate("EditWatchpointDialog", "changed", None))
        self.conditionEdit.setToolTip(_translate("EditWatchpointDialog", "Enter the expression for the watch expression", None))

