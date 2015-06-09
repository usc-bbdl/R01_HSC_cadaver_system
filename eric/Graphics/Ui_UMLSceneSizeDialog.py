# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Graphics\UMLSceneSizeDialog.ui'
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

class Ui_UMLSceneSizeDialog(object):
    def setupUi(self, UMLSceneSizeDialog):
        UMLSceneSizeDialog.setObjectName(_fromUtf8("UMLSceneSizeDialog"))
        UMLSceneSizeDialog.resize(314, 103)
        UMLSceneSizeDialog.setSizeGripEnabled(True)
        self.gridlayout = QtGui.QGridLayout(UMLSceneSizeDialog)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.buttonBox = QtGui.QDialogButtonBox(UMLSceneSizeDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridlayout.addWidget(self.buttonBox, 2, 0, 1, 2)
        self.textLabel2 = QtGui.QLabel(UMLSceneSizeDialog)
        self.textLabel2.setObjectName(_fromUtf8("textLabel2"))
        self.gridlayout.addWidget(self.textLabel2, 1, 0, 1, 1)
        self.textLabel1 = QtGui.QLabel(UMLSceneSizeDialog)
        self.textLabel1.setObjectName(_fromUtf8("textLabel1"))
        self.gridlayout.addWidget(self.textLabel1, 0, 0, 1, 1)
        self.heightSpinBox = QtGui.QSpinBox(UMLSceneSizeDialog)
        self.heightSpinBox.setMinimum(100)
        self.heightSpinBox.setMaximum(100000)
        self.heightSpinBox.setObjectName(_fromUtf8("heightSpinBox"))
        self.gridlayout.addWidget(self.heightSpinBox, 1, 1, 1, 1)
        self.widthSpinBox = QtGui.QSpinBox(UMLSceneSizeDialog)
        self.widthSpinBox.setMinimum(100)
        self.widthSpinBox.setMaximum(100000)
        self.widthSpinBox.setObjectName(_fromUtf8("widthSpinBox"))
        self.gridlayout.addWidget(self.widthSpinBox, 0, 1, 1, 1)

        self.retranslateUi(UMLSceneSizeDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), UMLSceneSizeDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), UMLSceneSizeDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(UMLSceneSizeDialog)

    def retranslateUi(self, UMLSceneSizeDialog):
        UMLSceneSizeDialog.setWindowTitle(_translate("UMLSceneSizeDialog", "Set Size", None))
        self.textLabel2.setText(_translate("UMLSceneSizeDialog", "Height (in pixels):", None))
        self.textLabel1.setText(_translate("UMLSceneSizeDialog", "Width (in pixels):", None))
        self.heightSpinBox.setToolTip(_translate("UMLSceneSizeDialog", "Select the height of the diagram", None))
        self.widthSpinBox.setToolTip(_translate("UMLSceneSizeDialog", "Select the width of the diagram", None))

