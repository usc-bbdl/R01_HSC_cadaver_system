# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\PyUnit\UnittestStacktraceDialog.ui'
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

class Ui_UnittestStacktraceDialog(object):
    def setupUi(self, UnittestStacktraceDialog):
        UnittestStacktraceDialog.setObjectName(_fromUtf8("UnittestStacktraceDialog"))
        UnittestStacktraceDialog.resize(600, 250)
        self.vboxlayout = QtGui.QVBoxLayout(UnittestStacktraceDialog)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.testLabel = QtGui.QLabel(UnittestStacktraceDialog)
        self.testLabel.setObjectName(_fromUtf8("testLabel"))
        self.vboxlayout.addWidget(self.testLabel)
        self.traceback = QtGui.QTextEdit(UnittestStacktraceDialog)
        self.traceback.setReadOnly(True)
        self.traceback.setAcceptRichText(False)
        self.traceback.setObjectName(_fromUtf8("traceback"))
        self.vboxlayout.addWidget(self.traceback)
        self.buttonBox = QtGui.QDialogButtonBox(UnittestStacktraceDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(UnittestStacktraceDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), UnittestStacktraceDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), UnittestStacktraceDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(UnittestStacktraceDialog)

    def retranslateUi(self, UnittestStacktraceDialog):
        pass

