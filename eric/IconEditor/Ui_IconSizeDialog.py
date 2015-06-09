# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\IconEditor\IconSizeDialog.ui'
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

class Ui_IconSizeDialog(object):
    def setupUi(self, IconSizeDialog):
        IconSizeDialog.setObjectName(_fromUtf8("IconSizeDialog"))
        IconSizeDialog.resize(232, 78)
        IconSizeDialog.setSizeGripEnabled(True)
        self.gridLayout = QtGui.QGridLayout(IconSizeDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(IconSizeDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.widthSpin = QtGui.QSpinBox(IconSizeDialog)
        self.widthSpin.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.widthSpin.setMinimum(1)
        self.widthSpin.setMaximum(256)
        self.widthSpin.setProperty("value", 32)
        self.widthSpin.setObjectName(_fromUtf8("widthSpin"))
        self.gridLayout.addWidget(self.widthSpin, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(IconSizeDialog)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.heightSpin = QtGui.QSpinBox(IconSizeDialog)
        self.heightSpin.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.heightSpin.setMinimum(1)
        self.heightSpin.setMaximum(256)
        self.heightSpin.setProperty("value", 32)
        self.heightSpin.setObjectName(_fromUtf8("heightSpin"))
        self.gridLayout.addWidget(self.heightSpin, 0, 3, 1, 1)
        spacerItem = QtGui.QSpacerItem(42, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 4, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(IconSizeDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 5)

        self.retranslateUi(IconSizeDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), IconSizeDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), IconSizeDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(IconSizeDialog)
        IconSizeDialog.setTabOrder(self.widthSpin, self.heightSpin)
        IconSizeDialog.setTabOrder(self.heightSpin, self.buttonBox)

    def retranslateUi(self, IconSizeDialog):
        IconSizeDialog.setWindowTitle(_translate("IconSizeDialog", "Icon Size", None))
        self.label.setText(_translate("IconSizeDialog", "Size:", None))
        self.widthSpin.setToolTip(_translate("IconSizeDialog", "Enter the width of the icon", None))
        self.label_2.setText(_translate("IconSizeDialog", "X", None))
        self.heightSpin.setToolTip(_translate("IconSizeDialog", "Enter the height of the icon", None))

