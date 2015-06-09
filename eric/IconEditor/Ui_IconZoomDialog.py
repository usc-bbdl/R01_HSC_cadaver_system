# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\IconEditor\IconZoomDialog.ui'
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

class Ui_IconZoomDialog(object):
    def setupUi(self, IconZoomDialog):
        IconZoomDialog.setObjectName(_fromUtf8("IconZoomDialog"))
        IconZoomDialog.resize(206, 78)
        self.vboxlayout = QtGui.QVBoxLayout(IconZoomDialog)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        self.zoomLabel = QtGui.QLabel(IconZoomDialog)
        self.zoomLabel.setObjectName(_fromUtf8("zoomLabel"))
        self.hboxlayout.addWidget(self.zoomLabel)
        self.zoomSpinBox = QtGui.QSpinBox(IconZoomDialog)
        self.zoomSpinBox.setAlignment(QtCore.Qt.AlignRight)
        self.zoomSpinBox.setMinimum(100)
        self.zoomSpinBox.setMaximum(10000)
        self.zoomSpinBox.setSingleStep(100)
        self.zoomSpinBox.setProperty("value", 1200)
        self.zoomSpinBox.setObjectName(_fromUtf8("zoomSpinBox"))
        self.hboxlayout.addWidget(self.zoomSpinBox)
        self.vboxlayout.addLayout(self.hboxlayout)
        self.buttonBox = QtGui.QDialogButtonBox(IconZoomDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.vboxlayout.addWidget(self.buttonBox)
        self.zoomLabel.setBuddy(self.zoomSpinBox)

        self.retranslateUi(IconZoomDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), IconZoomDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), IconZoomDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(IconZoomDialog)
        IconZoomDialog.setTabOrder(self.zoomSpinBox, self.buttonBox)

    def retranslateUi(self, IconZoomDialog):
        IconZoomDialog.setWindowTitle(_translate("IconZoomDialog", "Zoom", None))
        self.zoomLabel.setText(_translate("IconZoomDialog", "Zoom &Factor:", None))
        self.zoomSpinBox.setToolTip(_translate("IconZoomDialog", "Enter zoom factor", None))
        self.zoomSpinBox.setWhatsThis(_translate("IconZoomDialog", "<b>Zoom Factor</b>\n"
"<p>Enter the desired zoom factor here. The zoom factor\n"
"may be between -10 and +20 and is the increment that is \n"
"added to the size of the fonts used in the editor windows.</p>", None))
        self.zoomSpinBox.setSuffix(_translate("IconZoomDialog", "%", None))

