# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Debugger\EditBreakpointDialog.ui'
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

class Ui_EditBreakpointDialog(object):
    def setupUi(self, EditBreakpointDialog):
        EditBreakpointDialog.setObjectName(_fromUtf8("EditBreakpointDialog"))
        EditBreakpointDialog.resize(428, 216)
        EditBreakpointDialog.setSizeGripEnabled(True)
        self.gridlayout = QtGui.QGridLayout(EditBreakpointDialog)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.buttonBox = QtGui.QDialogButtonBox(EditBreakpointDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridlayout.addWidget(self.buttonBox, 6, 0, 1, 4)
        self.enabledCheckBox = QtGui.QCheckBox(EditBreakpointDialog)
        self.enabledCheckBox.setChecked(True)
        self.enabledCheckBox.setObjectName(_fromUtf8("enabledCheckBox"))
        self.gridlayout.addWidget(self.enabledCheckBox, 5, 0, 1, 4)
        self.temporaryCheckBox = QtGui.QCheckBox(EditBreakpointDialog)
        self.temporaryCheckBox.setObjectName(_fromUtf8("temporaryCheckBox"))
        self.gridlayout.addWidget(self.temporaryCheckBox, 4, 0, 1, 4)
        self.filenameCombo = QtGui.QComboBox(EditBreakpointDialog)
        self.filenameCombo.setEditable(True)
        self.filenameCombo.setAutoCompletion(True)
        self.filenameCombo.setObjectName(_fromUtf8("filenameCombo"))
        self.gridlayout.addWidget(self.filenameCombo, 0, 1, 1, 3)
        self.conditionCombo = QtGui.QComboBox(EditBreakpointDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.conditionCombo.sizePolicy().hasHeightForWidth())
        self.conditionCombo.setSizePolicy(sizePolicy)
        self.conditionCombo.setEditable(True)
        self.conditionCombo.setAutoCompletion(True)
        self.conditionCombo.setObjectName(_fromUtf8("conditionCombo"))
        self.gridlayout.addWidget(self.conditionCombo, 2, 1, 1, 3)
        self.ignoreSpinBox = QtGui.QSpinBox(EditBreakpointDialog)
        self.ignoreSpinBox.setMaximum(9999)
        self.ignoreSpinBox.setObjectName(_fromUtf8("ignoreSpinBox"))
        self.gridlayout.addWidget(self.ignoreSpinBox, 3, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(250, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridlayout.addItem(spacerItem, 3, 2, 1, 2)
        self.linenoSpinBox = QtGui.QSpinBox(EditBreakpointDialog)
        self.linenoSpinBox.setMinimum(1)
        self.linenoSpinBox.setMaximum(99999)
        self.linenoSpinBox.setObjectName(_fromUtf8("linenoSpinBox"))
        self.gridlayout.addWidget(self.linenoSpinBox, 1, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(200, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridlayout.addItem(spacerItem1, 1, 2, 1, 1)
        self.fileButton = QtGui.QPushButton(EditBreakpointDialog)
        self.fileButton.setObjectName(_fromUtf8("fileButton"))
        self.gridlayout.addWidget(self.fileButton, 1, 3, 1, 1)
        self.textLabel2_2 = QtGui.QLabel(EditBreakpointDialog)
        self.textLabel2_2.setObjectName(_fromUtf8("textLabel2_2"))
        self.gridlayout.addWidget(self.textLabel2_2, 1, 0, 1, 1)
        self.textLabel1_2 = QtGui.QLabel(EditBreakpointDialog)
        self.textLabel1_2.setObjectName(_fromUtf8("textLabel1_2"))
        self.gridlayout.addWidget(self.textLabel1_2, 0, 0, 1, 1)
        self.textLabel1 = QtGui.QLabel(EditBreakpointDialog)
        self.textLabel1.setObjectName(_fromUtf8("textLabel1"))
        self.gridlayout.addWidget(self.textLabel1, 2, 0, 1, 1)
        self.textLabel2 = QtGui.QLabel(EditBreakpointDialog)
        self.textLabel2.setObjectName(_fromUtf8("textLabel2"))
        self.gridlayout.addWidget(self.textLabel2, 3, 0, 1, 1)

        self.retranslateUi(EditBreakpointDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), EditBreakpointDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), EditBreakpointDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(EditBreakpointDialog)
        EditBreakpointDialog.setTabOrder(self.filenameCombo, self.linenoSpinBox)
        EditBreakpointDialog.setTabOrder(self.linenoSpinBox, self.fileButton)
        EditBreakpointDialog.setTabOrder(self.fileButton, self.conditionCombo)
        EditBreakpointDialog.setTabOrder(self.conditionCombo, self.ignoreSpinBox)
        EditBreakpointDialog.setTabOrder(self.ignoreSpinBox, self.temporaryCheckBox)
        EditBreakpointDialog.setTabOrder(self.temporaryCheckBox, self.enabledCheckBox)

    def retranslateUi(self, EditBreakpointDialog):
        EditBreakpointDialog.setWindowTitle(_translate("EditBreakpointDialog", "Edit Breakpoint", None))
        self.enabledCheckBox.setToolTip(_translate("EditBreakpointDialog", "Select, whether the breakpoint is enabled", None))
        self.enabledCheckBox.setText(_translate("EditBreakpointDialog", "Enabled", None))
        self.temporaryCheckBox.setToolTip(_translate("EditBreakpointDialog", "Select whether this is a temporary breakpoint", None))
        self.temporaryCheckBox.setText(_translate("EditBreakpointDialog", "Temporary Breakpoint", None))
        self.filenameCombo.setToolTip(_translate("EditBreakpointDialog", "Enter the filename of the breakpoint", None))
        self.conditionCombo.setToolTip(_translate("EditBreakpointDialog", "Enter or select a condition for the breakpoint", None))
        self.ignoreSpinBox.setToolTip(_translate("EditBreakpointDialog", "Enter an ignore count for the breakpoint", None))
        self.linenoSpinBox.setToolTip(_translate("EditBreakpointDialog", "Enter the linenumber of the breakpoint", None))
        self.fileButton.setToolTip(_translate("EditBreakpointDialog", "Press to open a file selection dialog", None))
        self.fileButton.setText(_translate("EditBreakpointDialog", "...", None))
        self.textLabel2_2.setText(_translate("EditBreakpointDialog", "Linenumber:", None))
        self.textLabel1_2.setText(_translate("EditBreakpointDialog", "Filename:", None))
        self.textLabel1.setText(_translate("EditBreakpointDialog", "Condition:", None))
        self.textLabel2.setText(_translate("EditBreakpointDialog", "Ignore Count:", None))

