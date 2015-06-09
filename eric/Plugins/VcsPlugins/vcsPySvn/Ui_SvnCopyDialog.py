# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Plugins\VcsPlugins\vcsPySvn\SvnCopyDialog.ui'
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

class Ui_SvnCopyDialog(object):
    def setupUi(self, SvnCopyDialog):
        SvnCopyDialog.setObjectName(_fromUtf8("SvnCopyDialog"))
        SvnCopyDialog.resize(409, 135)
        SvnCopyDialog.setSizeGripEnabled(True)
        self.vboxlayout = QtGui.QVBoxLayout(SvnCopyDialog)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.gridlayout = QtGui.QGridLayout()
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.dirButton = QtGui.QPushButton(SvnCopyDialog)
        self.dirButton.setObjectName(_fromUtf8("dirButton"))
        self.gridlayout.addWidget(self.dirButton, 1, 2, 1, 1)
        self.textLabel1 = QtGui.QLabel(SvnCopyDialog)
        self.textLabel1.setObjectName(_fromUtf8("textLabel1"))
        self.gridlayout.addWidget(self.textLabel1, 0, 0, 1, 1)
        self.sourceEdit = QtGui.QLineEdit(SvnCopyDialog)
        self.sourceEdit.setReadOnly(True)
        self.sourceEdit.setObjectName(_fromUtf8("sourceEdit"))
        self.gridlayout.addWidget(self.sourceEdit, 0, 1, 1, 1)
        self.targetEdit = QtGui.QLineEdit(SvnCopyDialog)
        self.targetEdit.setObjectName(_fromUtf8("targetEdit"))
        self.gridlayout.addWidget(self.targetEdit, 1, 1, 1, 1)
        self.textLabel2 = QtGui.QLabel(SvnCopyDialog)
        self.textLabel2.setObjectName(_fromUtf8("textLabel2"))
        self.gridlayout.addWidget(self.textLabel2, 1, 0, 1, 1)
        self.vboxlayout.addLayout(self.gridlayout)
        self.forceCheckBox = QtGui.QCheckBox(SvnCopyDialog)
        self.forceCheckBox.setObjectName(_fromUtf8("forceCheckBox"))
        self.vboxlayout.addWidget(self.forceCheckBox)
        self.buttonBox = QtGui.QDialogButtonBox(SvnCopyDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(SvnCopyDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), SvnCopyDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), SvnCopyDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SvnCopyDialog)
        SvnCopyDialog.setTabOrder(self.sourceEdit, self.targetEdit)
        SvnCopyDialog.setTabOrder(self.targetEdit, self.dirButton)
        SvnCopyDialog.setTabOrder(self.dirButton, self.forceCheckBox)
        SvnCopyDialog.setTabOrder(self.forceCheckBox, self.buttonBox)

    def retranslateUi(self, SvnCopyDialog):
        SvnCopyDialog.setWindowTitle(_translate("SvnCopyDialog", "Subversion Copy", None))
        self.dirButton.setToolTip(_translate("SvnCopyDialog", "Press to open a selection dialog", None))
        self.dirButton.setWhatsThis(_translate("SvnCopyDialog", "<b>Target name</b>\n"
"<p>Select the target name for the operation via a selection dialog.</p>", None))
        self.dirButton.setText(_translate("SvnCopyDialog", "...", None))
        self.textLabel1.setText(_translate("SvnCopyDialog", "Source:", None))
        self.sourceEdit.setToolTip(_translate("SvnCopyDialog", "Shows the name of the source", None))
        self.sourceEdit.setWhatsThis(_translate("SvnCopyDialog", "<b>Source name</b>\n"
"<p>This field shows the name of the source.</p>", None))
        self.targetEdit.setToolTip(_translate("SvnCopyDialog", "Enter the target name", None))
        self.targetEdit.setWhatsThis(_translate("SvnCopyDialog", "<b>Target name</b>\n"
"<p>Enter the new name in this field. The target must be the new name or an absolute path.</p>", None))
        self.textLabel2.setText(_translate("SvnCopyDialog", "Target:", None))
        self.forceCheckBox.setToolTip(_translate("SvnCopyDialog", "Select to force the operation", None))
        self.forceCheckBox.setText(_translate("SvnCopyDialog", "Enforce operation", None))

