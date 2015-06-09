# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Preferences\ConfigurationPages\IconsPreviewDialog.ui'
#
# Created: Fri Apr 18 09:56:43 2014
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

class Ui_IconsPreviewDialog(object):
    def setupUi(self, IconsPreviewDialog):
        IconsPreviewDialog.setObjectName(_fromUtf8("IconsPreviewDialog"))
        IconsPreviewDialog.resize(596, 541)
        IconsPreviewDialog.setSizeGripEnabled(True)
        self.vboxlayout = QtGui.QVBoxLayout(IconsPreviewDialog)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.iconView = QtGui.QListWidget(IconsPreviewDialog)
        self.iconView.setMovement(QtGui.QListView.Free)
        self.iconView.setFlow(QtGui.QListView.LeftToRight)
        self.iconView.setGridSize(QtCore.QSize(100, 50))
        self.iconView.setViewMode(QtGui.QListView.IconMode)
        self.iconView.setObjectName(_fromUtf8("iconView"))
        self.vboxlayout.addWidget(self.iconView)
        self.buttonBox = QtGui.QDialogButtonBox(IconsPreviewDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(IconsPreviewDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), IconsPreviewDialog.accept)
        QtCore.QMetaObject.connectSlotsByName(IconsPreviewDialog)

    def retranslateUi(self, IconsPreviewDialog):
        IconsPreviewDialog.setWindowTitle(_translate("IconsPreviewDialog", "Icons Preview", None))

