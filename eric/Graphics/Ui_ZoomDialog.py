# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Graphics\ZoomDialog.ui'
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

class Ui_ZoomDialog(object):
    def setupUi(self, ZoomDialog):
        ZoomDialog.setObjectName(_fromUtf8("ZoomDialog"))
        ZoomDialog.resize(271, 77)
        ZoomDialog.setSizeGripEnabled(True)
        self.vboxlayout = QtGui.QVBoxLayout(ZoomDialog)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        self.label = QtGui.QLabel(ZoomDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.hboxlayout.addWidget(self.label)
        self.zoomSpinBox = QtGui.QDoubleSpinBox(ZoomDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zoomSpinBox.sizePolicy().hasHeightForWidth())
        self.zoomSpinBox.setSizePolicy(sizePolicy)
        self.zoomSpinBox.setAlignment(QtCore.Qt.AlignRight)
        self.zoomSpinBox.setMinimum(0.01)
        self.zoomSpinBox.setMaximum(1000.0)
        self.zoomSpinBox.setProperty("value", 1.0)
        self.zoomSpinBox.setObjectName(_fromUtf8("zoomSpinBox"))
        self.hboxlayout.addWidget(self.zoomSpinBox)
        self.vboxlayout.addLayout(self.hboxlayout)
        self.buttonBox = QtGui.QDialogButtonBox(ZoomDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.vboxlayout.addWidget(self.buttonBox)
        self.label.setBuddy(self.zoomSpinBox)

        self.retranslateUi(ZoomDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ZoomDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ZoomDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ZoomDialog)

    def retranslateUi(self, ZoomDialog):
        ZoomDialog.setWindowTitle(_translate("ZoomDialog", "Zoom", None))
        self.label.setText(_translate("ZoomDialog", "Zoom &Factor:", None))
        self.zoomSpinBox.setToolTip(_translate("ZoomDialog", "Enter zoom factor", None))

