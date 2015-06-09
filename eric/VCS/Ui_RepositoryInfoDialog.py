# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\VCS\RepositoryInfoDialog.ui'
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

class Ui_VcsRepositoryInfoDialog(object):
    def setupUi(self, VcsRepositoryInfoDialog):
        VcsRepositoryInfoDialog.setObjectName(_fromUtf8("VcsRepositoryInfoDialog"))
        VcsRepositoryInfoDialog.resize(590, 437)
        VcsRepositoryInfoDialog.setSizeGripEnabled(True)
        self.vboxlayout = QtGui.QVBoxLayout(VcsRepositoryInfoDialog)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.infoBrowser = QtGui.QTextEdit(VcsRepositoryInfoDialog)
        self.infoBrowser.setReadOnly(True)
        self.infoBrowser.setObjectName(_fromUtf8("infoBrowser"))
        self.vboxlayout.addWidget(self.infoBrowser)
        self.buttonBox = QtGui.QDialogButtonBox(VcsRepositoryInfoDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(VcsRepositoryInfoDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), VcsRepositoryInfoDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), VcsRepositoryInfoDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(VcsRepositoryInfoDialog)

    def retranslateUi(self, VcsRepositoryInfoDialog):
        VcsRepositoryInfoDialog.setWindowTitle(_translate("VcsRepositoryInfoDialog", "Repository Information", None))

