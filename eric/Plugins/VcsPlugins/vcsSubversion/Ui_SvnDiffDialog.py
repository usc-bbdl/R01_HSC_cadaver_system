# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Plugins\VcsPlugins\vcsSubversion\SvnDiffDialog.ui'
#
# Created: Fri Apr 18 09:56:42 2014
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

class Ui_SvnDiffDialog(object):
    def setupUi(self, SvnDiffDialog):
        SvnDiffDialog.setObjectName(_fromUtf8("SvnDiffDialog"))
        SvnDiffDialog.resize(749, 646)
        self.vboxlayout = QtGui.QVBoxLayout(SvnDiffDialog)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.contentsGroup = QtGui.QGroupBox(SvnDiffDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.contentsGroup.sizePolicy().hasHeightForWidth())
        self.contentsGroup.setSizePolicy(sizePolicy)
        self.contentsGroup.setObjectName(_fromUtf8("contentsGroup"))
        self.vboxlayout1 = QtGui.QVBoxLayout(self.contentsGroup)
        self.vboxlayout1.setObjectName(_fromUtf8("vboxlayout1"))
        self.contents = QtGui.QTextEdit(self.contentsGroup)
        self.contents.setLineWrapMode(QtGui.QTextEdit.NoWrap)
        self.contents.setReadOnly(True)
        self.contents.setTabStopWidth(8)
        self.contents.setAcceptRichText(False)
        self.contents.setObjectName(_fromUtf8("contents"))
        self.vboxlayout1.addWidget(self.contents)
        self.vboxlayout.addWidget(self.contentsGroup)
        self.errorGroup = QtGui.QGroupBox(SvnDiffDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.errorGroup.sizePolicy().hasHeightForWidth())
        self.errorGroup.setSizePolicy(sizePolicy)
        self.errorGroup.setObjectName(_fromUtf8("errorGroup"))
        self.vboxlayout2 = QtGui.QVBoxLayout(self.errorGroup)
        self.vboxlayout2.setObjectName(_fromUtf8("vboxlayout2"))
        self.errors = QtGui.QTextEdit(self.errorGroup)
        self.errors.setReadOnly(True)
        self.errors.setAcceptRichText(False)
        self.errors.setObjectName(_fromUtf8("errors"))
        self.vboxlayout2.addWidget(self.errors)
        self.vboxlayout.addWidget(self.errorGroup)
        self.inputGroup = QtGui.QGroupBox(SvnDiffDialog)
        self.inputGroup.setObjectName(_fromUtf8("inputGroup"))
        self.gridlayout = QtGui.QGridLayout(self.inputGroup)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        spacerItem = QtGui.QSpacerItem(327, 29, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridlayout.addItem(spacerItem, 1, 1, 1, 1)
        self.sendButton = QtGui.QPushButton(self.inputGroup)
        self.sendButton.setObjectName(_fromUtf8("sendButton"))
        self.gridlayout.addWidget(self.sendButton, 1, 2, 1, 1)
        self.input = QtGui.QLineEdit(self.inputGroup)
        self.input.setObjectName(_fromUtf8("input"))
        self.gridlayout.addWidget(self.input, 0, 0, 1, 3)
        self.passwordCheckBox = QtGui.QCheckBox(self.inputGroup)
        self.passwordCheckBox.setObjectName(_fromUtf8("passwordCheckBox"))
        self.gridlayout.addWidget(self.passwordCheckBox, 1, 0, 1, 1)
        self.vboxlayout.addWidget(self.inputGroup)
        self.buttonBox = QtGui.QDialogButtonBox(SvnDiffDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close|QtGui.QDialogButtonBox.Save)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(SvnDiffDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), SvnDiffDialog.close)
        QtCore.QMetaObject.connectSlotsByName(SvnDiffDialog)
        SvnDiffDialog.setTabOrder(self.contents, self.errors)
        SvnDiffDialog.setTabOrder(self.errors, self.input)
        SvnDiffDialog.setTabOrder(self.input, self.passwordCheckBox)
        SvnDiffDialog.setTabOrder(self.passwordCheckBox, self.sendButton)
        SvnDiffDialog.setTabOrder(self.sendButton, self.buttonBox)

    def retranslateUi(self, SvnDiffDialog):
        SvnDiffDialog.setWindowTitle(_translate("SvnDiffDialog", "Subversion Diff", None))
        self.contentsGroup.setTitle(_translate("SvnDiffDialog", "Difference", None))
        self.contents.setWhatsThis(_translate("SvnDiffDialog", "<b>Subversion Diff</b><p>This shows the output of the svn diff command.</p>", None))
        self.errorGroup.setTitle(_translate("SvnDiffDialog", "Errors", None))
        self.inputGroup.setTitle(_translate("SvnDiffDialog", "Input", None))
        self.sendButton.setToolTip(_translate("SvnDiffDialog", "Press to send the input to the subversion process", None))
        self.sendButton.setText(_translate("SvnDiffDialog", "&Send", None))
        self.sendButton.setShortcut(_translate("SvnDiffDialog", "Alt+S", None))
        self.input.setToolTip(_translate("SvnDiffDialog", "Enter data to be sent to the subversion process", None))
        self.passwordCheckBox.setToolTip(_translate("SvnDiffDialog", "Select to switch the input field to password mode", None))
        self.passwordCheckBox.setText(_translate("SvnDiffDialog", "&Password Mode", None))
        self.passwordCheckBox.setShortcut(_translate("SvnDiffDialog", "Alt+P", None))

