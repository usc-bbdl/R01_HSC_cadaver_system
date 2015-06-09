# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\UI\DiffDialog.ui'
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

class Ui_DiffDialog(object):
    def setupUi(self, DiffDialog):
        DiffDialog.setObjectName(_fromUtf8("DiffDialog"))
        DiffDialog.resize(750, 600)
        self.vboxlayout = QtGui.QVBoxLayout(DiffDialog)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        self.textLabel1 = QtGui.QLabel(DiffDialog)
        self.textLabel1.setObjectName(_fromUtf8("textLabel1"))
        self.hboxlayout.addWidget(self.textLabel1)
        self.file1Edit = QtGui.QLineEdit(DiffDialog)
        self.file1Edit.setObjectName(_fromUtf8("file1Edit"))
        self.hboxlayout.addWidget(self.file1Edit)
        self.file1Button = QtGui.QPushButton(DiffDialog)
        self.file1Button.setObjectName(_fromUtf8("file1Button"))
        self.hboxlayout.addWidget(self.file1Button)
        self.vboxlayout.addLayout(self.hboxlayout)
        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setObjectName(_fromUtf8("hboxlayout1"))
        self.textLabel2 = QtGui.QLabel(DiffDialog)
        self.textLabel2.setObjectName(_fromUtf8("textLabel2"))
        self.hboxlayout1.addWidget(self.textLabel2)
        self.file2Edit = QtGui.QLineEdit(DiffDialog)
        self.file2Edit.setObjectName(_fromUtf8("file2Edit"))
        self.hboxlayout1.addWidget(self.file2Edit)
        self.file2Button = QtGui.QPushButton(DiffDialog)
        self.file2Button.setObjectName(_fromUtf8("file2Button"))
        self.hboxlayout1.addWidget(self.file2Button)
        self.vboxlayout.addLayout(self.hboxlayout1)
        self.diffFormatGroup = QtGui.QGroupBox(DiffDialog)
        self.diffFormatGroup.setTitle(_fromUtf8(""))
        self.diffFormatGroup.setObjectName(_fromUtf8("diffFormatGroup"))
        self.hboxlayout2 = QtGui.QHBoxLayout(self.diffFormatGroup)
        self.hboxlayout2.setObjectName(_fromUtf8("hboxlayout2"))
        self.unifiedRadioButton = QtGui.QRadioButton(self.diffFormatGroup)
        self.unifiedRadioButton.setChecked(True)
        self.unifiedRadioButton.setObjectName(_fromUtf8("unifiedRadioButton"))
        self.hboxlayout2.addWidget(self.unifiedRadioButton)
        self.contextRadioButton = QtGui.QRadioButton(self.diffFormatGroup)
        self.contextRadioButton.setObjectName(_fromUtf8("contextRadioButton"))
        self.hboxlayout2.addWidget(self.contextRadioButton)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout2.addItem(spacerItem)
        self.vboxlayout.addWidget(self.diffFormatGroup)
        self.contents = QtGui.QTextEdit(DiffDialog)
        self.contents.setLineWrapMode(QtGui.QTextEdit.NoWrap)
        self.contents.setReadOnly(True)
        self.contents.setTabStopWidth(8)
        self.contents.setAcceptRichText(False)
        self.contents.setObjectName(_fromUtf8("contents"))
        self.vboxlayout.addWidget(self.contents)
        self.buttonBox = QtGui.QDialogButtonBox(DiffDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.vboxlayout.addWidget(self.buttonBox)
        self.textLabel1.setBuddy(self.file1Edit)
        self.textLabel2.setBuddy(self.file1Edit)

        self.retranslateUi(DiffDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), DiffDialog.close)
        QtCore.QMetaObject.connectSlotsByName(DiffDialog)
        DiffDialog.setTabOrder(self.file1Edit, self.file1Button)
        DiffDialog.setTabOrder(self.file1Button, self.file2Edit)
        DiffDialog.setTabOrder(self.file2Edit, self.file2Button)
        DiffDialog.setTabOrder(self.file2Button, self.unifiedRadioButton)
        DiffDialog.setTabOrder(self.unifiedRadioButton, self.contextRadioButton)
        DiffDialog.setTabOrder(self.contextRadioButton, self.contents)
        DiffDialog.setTabOrder(self.contents, self.buttonBox)

    def retranslateUi(self, DiffDialog):
        DiffDialog.setWindowTitle(_translate("DiffDialog", "File Differences", None))
        self.textLabel1.setText(_translate("DiffDialog", "File &1:", None))
        self.file1Edit.setToolTip(_translate("DiffDialog", "Enter the name of the first file", None))
        self.file1Button.setToolTip(_translate("DiffDialog", "Press to select the file via a file selection dialog", None))
        self.file1Button.setText(_translate("DiffDialog", "...", None))
        self.textLabel2.setText(_translate("DiffDialog", "File &2:", None))
        self.file2Edit.setToolTip(_translate("DiffDialog", "Enter the name of the second file", None))
        self.file2Button.setToolTip(_translate("DiffDialog", "Press to select the file via a file selection dialog", None))
        self.file2Button.setText(_translate("DiffDialog", "...", None))
        self.unifiedRadioButton.setToolTip(_translate("DiffDialog", "Select to generate a unified diff", None))
        self.unifiedRadioButton.setText(_translate("DiffDialog", "&Unified Diff", None))
        self.unifiedRadioButton.setShortcut(_translate("DiffDialog", "Alt+U", None))
        self.contextRadioButton.setToolTip(_translate("DiffDialog", "Select to generate a context diff", None))
        self.contextRadioButton.setText(_translate("DiffDialog", "Co&ntext Diff", None))
        self.contextRadioButton.setShortcut(_translate("DiffDialog", "Alt+N", None))

