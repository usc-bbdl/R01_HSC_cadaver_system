# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\QScintilla\ZoomDialog.ui'
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

class Ui_ZoomDialog(object):
    def setupUi(self, ZoomDialog):
        ZoomDialog.setObjectName(_fromUtf8("ZoomDialog"))
        ZoomDialog.resize(206, 77)
        self.vboxlayout = QtGui.QVBoxLayout(ZoomDialog)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        self.zoomLabel = QtGui.QLabel(ZoomDialog)
        self.zoomLabel.setObjectName(_fromUtf8("zoomLabel"))
        self.hboxlayout.addWidget(self.zoomLabel)
        self.zoomSpinBox = QtGui.QSpinBox(ZoomDialog)
        self.zoomSpinBox.setAlignment(QtCore.Qt.AlignRight)
        self.zoomSpinBox.setMinimum(-10)
        self.zoomSpinBox.setMaximum(20)
        self.zoomSpinBox.setProperty("value", 0)
        self.zoomSpinBox.setObjectName(_fromUtf8("zoomSpinBox"))
        self.hboxlayout.addWidget(self.zoomSpinBox)
        self.vboxlayout.addLayout(self.hboxlayout)
        self.buttonBox = QtGui.QDialogButtonBox(ZoomDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.vboxlayout.addWidget(self.buttonBox)
        self.zoomLabel.setBuddy(self.zoomSpinBox)

        self.retranslateUi(ZoomDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ZoomDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ZoomDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ZoomDialog)

    def retranslateUi(self, ZoomDialog):
        ZoomDialog.setWindowTitle(_translate("ZoomDialog", "Zoom", None))
        self.zoomLabel.setText(_translate("ZoomDialog", "Zoom &Factor:", None))
        self.zoomSpinBox.setToolTip(_translate("ZoomDialog", "Enter zoom factor", None))
        self.zoomSpinBox.setWhatsThis(_translate("ZoomDialog", "<b>Zoom Factor</b>\n"
"<p>Enter the desired zoom factor here. The zoom factor\n"
"may be between -10 and +20 and is the increment that is \n"
"added to the size of the fonts used in the editor windows.</p>", None))

