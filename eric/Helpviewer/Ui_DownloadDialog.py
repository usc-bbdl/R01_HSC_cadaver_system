# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Helpviewer\DownloadDialog.ui'
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

class Ui_DownloadDialog(object):
    def setupUi(self, DownloadDialog):
        DownloadDialog.setObjectName(_fromUtf8("DownloadDialog"))
        DownloadDialog.resize(400, 148)
        self.verticalLayout_2 = QtGui.QVBoxLayout(DownloadDialog)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.fileIcon = QtGui.QLabel(DownloadDialog)
        self.fileIcon.setObjectName(_fromUtf8("fileIcon"))
        self.horizontalLayout.addWidget(self.fileIcon)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.filenameLabel = QtGui.QLabel(DownloadDialog)
        self.filenameLabel.setObjectName(_fromUtf8("filenameLabel"))
        self.verticalLayout.addWidget(self.filenameLabel)
        self.progressBar = QtGui.QProgressBar(DownloadDialog)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.verticalLayout.addWidget(self.progressBar)
        self.infoLabel = QtGui.QLabel(DownloadDialog)
        self.infoLabel.setObjectName(_fromUtf8("infoLabel"))
        self.verticalLayout.addWidget(self.infoLabel)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.keepOpenCheckBox = QtGui.QCheckBox(DownloadDialog)
        self.keepOpenCheckBox.setObjectName(_fromUtf8("keepOpenCheckBox"))
        self.verticalLayout_2.addWidget(self.keepOpenCheckBox)
        self.buttonBox = QtGui.QDialogButtonBox(DownloadDialog)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close|QtGui.QDialogButtonBox.Open)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(DownloadDialog)
        QtCore.QMetaObject.connectSlotsByName(DownloadDialog)

    def retranslateUi(self, DownloadDialog):
        DownloadDialog.setWindowTitle(_translate("DownloadDialog", "Eric4 Download", None))
        self.fileIcon.setText(_translate("DownloadDialog", "Icon", None))
        self.filenameLabel.setText(_translate("DownloadDialog", "Filename", None))
        self.infoLabel.setText(_translate("DownloadDialog", "Info", None))
        self.keepOpenCheckBox.setToolTip(_translate("DownloadDialog", "Select to keep the dialog open when finished", None))
        self.keepOpenCheckBox.setText(_translate("DownloadDialog", "Keep open when finished", None))

