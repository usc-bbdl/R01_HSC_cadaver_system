# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Preferences\ViewProfileToolboxesDialog.ui'
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

class Ui_ViewProfileToolboxesDialog(object):
    def setupUi(self, ViewProfileToolboxesDialog):
        ViewProfileToolboxesDialog.setObjectName(_fromUtf8("ViewProfileToolboxesDialog"))
        ViewProfileToolboxesDialog.resize(608, 179)
        ViewProfileToolboxesDialog.setSizeGripEnabled(True)
        self.gridLayout = QtGui.QGridLayout(ViewProfileToolboxesDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.textLabel1 = QtGui.QLabel(ViewProfileToolboxesDialog)
        self.textLabel1.setAlignment(QtCore.Qt.AlignVCenter)
        self.textLabel1.setObjectName(_fromUtf8("textLabel1"))
        self.gridLayout.addWidget(self.textLabel1, 0, 0, 1, 2)
        self.editGroup = QtGui.QGroupBox(ViewProfileToolboxesDialog)
        self.editGroup.setObjectName(_fromUtf8("editGroup"))
        self.verticalLayout = QtGui.QVBoxLayout(self.editGroup)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.epvtCheckBox = QtGui.QCheckBox(self.editGroup)
        self.epvtCheckBox.setChecked(True)
        self.epvtCheckBox.setObjectName(_fromUtf8("epvtCheckBox"))
        self.verticalLayout.addWidget(self.epvtCheckBox)
        self.ephtCheckBox = QtGui.QCheckBox(self.editGroup)
        self.ephtCheckBox.setChecked(True)
        self.ephtCheckBox.setObjectName(_fromUtf8("ephtCheckBox"))
        self.verticalLayout.addWidget(self.ephtCheckBox)
        self.epdbCheckBox = QtGui.QCheckBox(self.editGroup)
        self.epdbCheckBox.setObjectName(_fromUtf8("epdbCheckBox"))
        self.verticalLayout.addWidget(self.epdbCheckBox)
        self.gridLayout.addWidget(self.editGroup, 1, 0, 1, 1)
        self.debugGroup = QtGui.QGroupBox(ViewProfileToolboxesDialog)
        self.debugGroup.setObjectName(_fromUtf8("debugGroup"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.debugGroup)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.dpvtCheckBox = QtGui.QCheckBox(self.debugGroup)
        self.dpvtCheckBox.setObjectName(_fromUtf8("dpvtCheckBox"))
        self.verticalLayout_2.addWidget(self.dpvtCheckBox)
        self.dphtCheckBox = QtGui.QCheckBox(self.debugGroup)
        self.dphtCheckBox.setChecked(True)
        self.dphtCheckBox.setObjectName(_fromUtf8("dphtCheckBox"))
        self.verticalLayout_2.addWidget(self.dphtCheckBox)
        self.dpdbCheckBox = QtGui.QCheckBox(self.debugGroup)
        self.dpdbCheckBox.setChecked(True)
        self.dpdbCheckBox.setObjectName(_fromUtf8("dpdbCheckBox"))
        self.verticalLayout_2.addWidget(self.dpdbCheckBox)
        self.gridLayout.addWidget(self.debugGroup, 1, 1, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(ViewProfileToolboxesDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 2)

        self.retranslateUi(ViewProfileToolboxesDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ViewProfileToolboxesDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ViewProfileToolboxesDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ViewProfileToolboxesDialog)
        ViewProfileToolboxesDialog.setTabOrder(self.epvtCheckBox, self.ephtCheckBox)
        ViewProfileToolboxesDialog.setTabOrder(self.ephtCheckBox, self.epdbCheckBox)
        ViewProfileToolboxesDialog.setTabOrder(self.epdbCheckBox, self.dpvtCheckBox)
        ViewProfileToolboxesDialog.setTabOrder(self.dpvtCheckBox, self.dphtCheckBox)
        ViewProfileToolboxesDialog.setTabOrder(self.dphtCheckBox, self.dpdbCheckBox)
        ViewProfileToolboxesDialog.setTabOrder(self.dpdbCheckBox, self.buttonBox)

    def retranslateUi(self, ViewProfileToolboxesDialog):
        ViewProfileToolboxesDialog.setWindowTitle(_translate("ViewProfileToolboxesDialog", "Configure View Profiles", None))
        self.textLabel1.setText(_translate("ViewProfileToolboxesDialog", "Select the windows, that should be visible, when the different profiles are active.", None))
        self.editGroup.setTitle(_translate("ViewProfileToolboxesDialog", "&Edit Profile", None))
        self.epvtCheckBox.setText(_translate("ViewProfileToolboxesDialog", "Vertical Toolbox", None))
        self.ephtCheckBox.setText(_translate("ViewProfileToolboxesDialog", "Horizontal Toolbox", None))
        self.epdbCheckBox.setText(_translate("ViewProfileToolboxesDialog", "Debug-Viewer", None))
        self.debugGroup.setTitle(_translate("ViewProfileToolboxesDialog", "&Debug Profile", None))
        self.dpvtCheckBox.setText(_translate("ViewProfileToolboxesDialog", "Vertical Toolbox", None))
        self.dphtCheckBox.setText(_translate("ViewProfileToolboxesDialog", "Horizontal Toolbox", None))
        self.dpdbCheckBox.setText(_translate("ViewProfileToolboxesDialog", "Debug-Viewer", None))

