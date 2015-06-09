# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\QScintilla\GotoDialog.ui'
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

class Ui_GotoDialog(object):
    def setupUi(self, GotoDialog):
        GotoDialog.setObjectName(_fromUtf8("GotoDialog"))
        GotoDialog.resize(206, 77)
        self._3 = QtGui.QVBoxLayout(GotoDialog)
        self._3.setObjectName(_fromUtf8("_3"))
        self._2 = QtGui.QHBoxLayout()
        self._2.setObjectName(_fromUtf8("_2"))
        self.linenumberLabel = QtGui.QLabel(GotoDialog)
        self.linenumberLabel.setObjectName(_fromUtf8("linenumberLabel"))
        self._2.addWidget(self.linenumberLabel)
        self.linenumberSpinBox = QtGui.QSpinBox(GotoDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.linenumberSpinBox.sizePolicy().hasHeightForWidth())
        self.linenumberSpinBox.setSizePolicy(sizePolicy)
        self.linenumberSpinBox.setAlignment(QtCore.Qt.AlignRight)
        self.linenumberSpinBox.setMinimum(1)
        self.linenumberSpinBox.setMaximum(99999)
        self.linenumberSpinBox.setObjectName(_fromUtf8("linenumberSpinBox"))
        self._2.addWidget(self.linenumberSpinBox)
        self._3.addLayout(self._2)
        self.buttonBox = QtGui.QDialogButtonBox(GotoDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self._3.addWidget(self.buttonBox)
        self.linenumberLabel.setBuddy(self.linenumberSpinBox)

        self.retranslateUi(GotoDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), GotoDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), GotoDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(GotoDialog)

    def retranslateUi(self, GotoDialog):
        GotoDialog.setWindowTitle(_translate("GotoDialog", "Goto", None))
        self.linenumberLabel.setText(_translate("GotoDialog", "&Line Number:", None))
        self.linenumberSpinBox.setToolTip(_translate("GotoDialog", "Enter linenumber to go to", None))
        self.linenumberSpinBox.setWhatsThis(_translate("GotoDialog", "<b>Linenumber</b>\n"
"<p>Enter the linenumber to go to in this entry field.</p>", None))

