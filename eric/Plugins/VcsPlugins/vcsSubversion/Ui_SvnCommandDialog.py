# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Plugins\VcsPlugins\vcsSubversion\SvnCommandDialog.ui'
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

class Ui_SvnCommandDialog(object):
    def setupUi(self, SvnCommandDialog):
        SvnCommandDialog.setObjectName(_fromUtf8("SvnCommandDialog"))
        SvnCommandDialog.resize(628, 137)
        self.vboxlayout = QtGui.QVBoxLayout(SvnCommandDialog)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.gridlayout = QtGui.QGridLayout()
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.textLabel1 = QtGui.QLabel(SvnCommandDialog)
        self.textLabel1.setToolTip(_fromUtf8(""))
        self.textLabel1.setObjectName(_fromUtf8("textLabel1"))
        self.gridlayout.addWidget(self.textLabel1, 0, 0, 1, 1)
        self.commandCombo = QtGui.QComboBox(SvnCommandDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.commandCombo.sizePolicy().hasHeightForWidth())
        self.commandCombo.setSizePolicy(sizePolicy)
        self.commandCombo.setEditable(True)
        self.commandCombo.setInsertPolicy(QtGui.QComboBox.InsertAtTop)
        self.commandCombo.setAutoCompletion(True)
        self.commandCombo.setDuplicatesEnabled(False)
        self.commandCombo.setObjectName(_fromUtf8("commandCombo"))
        self.gridlayout.addWidget(self.commandCombo, 0, 1, 1, 2)
        self.dirButton = QtGui.QPushButton(SvnCommandDialog)
        self.dirButton.setObjectName(_fromUtf8("dirButton"))
        self.gridlayout.addWidget(self.dirButton, 1, 2, 1, 1)
        self.workdirCombo = QtGui.QComboBox(SvnCommandDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.workdirCombo.sizePolicy().hasHeightForWidth())
        self.workdirCombo.setSizePolicy(sizePolicy)
        self.workdirCombo.setEditable(True)
        self.workdirCombo.setInsertPolicy(QtGui.QComboBox.InsertAtTop)
        self.workdirCombo.setAutoCompletion(True)
        self.workdirCombo.setDuplicatesEnabled(False)
        self.workdirCombo.setObjectName(_fromUtf8("workdirCombo"))
        self.gridlayout.addWidget(self.workdirCombo, 1, 1, 1, 1)
        self.textLabel2 = QtGui.QLabel(SvnCommandDialog)
        self.textLabel2.setObjectName(_fromUtf8("textLabel2"))
        self.gridlayout.addWidget(self.textLabel2, 1, 0, 1, 1)
        self.textLabel3 = QtGui.QLabel(SvnCommandDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textLabel3.sizePolicy().hasHeightForWidth())
        self.textLabel3.setSizePolicy(sizePolicy)
        self.textLabel3.setObjectName(_fromUtf8("textLabel3"))
        self.gridlayout.addWidget(self.textLabel3, 2, 0, 1, 1)
        self.projectDirLabel = QtGui.QLabel(SvnCommandDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.projectDirLabel.sizePolicy().hasHeightForWidth())
        self.projectDirLabel.setSizePolicy(sizePolicy)
        self.projectDirLabel.setObjectName(_fromUtf8("projectDirLabel"))
        self.gridlayout.addWidget(self.projectDirLabel, 2, 1, 1, 2)
        self.vboxlayout.addLayout(self.gridlayout)
        self.buttonBox = QtGui.QDialogButtonBox(SvnCommandDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(SvnCommandDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), SvnCommandDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), SvnCommandDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SvnCommandDialog)
        SvnCommandDialog.setTabOrder(self.commandCombo, self.workdirCombo)
        SvnCommandDialog.setTabOrder(self.workdirCombo, self.dirButton)
        SvnCommandDialog.setTabOrder(self.dirButton, self.buttonBox)

    def retranslateUi(self, SvnCommandDialog):
        SvnCommandDialog.setWindowTitle(_translate("SvnCommandDialog", "Subversion Command", None))
        self.textLabel1.setText(_translate("SvnCommandDialog", "Subversion Command:", None))
        self.commandCombo.setToolTip(_translate("SvnCommandDialog", "Enter the Subversion command to be executed with all necessary parameters", None))
        self.commandCombo.setWhatsThis(_translate("SvnCommandDialog", "<b>Subversion Command</b>\n"
"<p>Enter the Subversion command to be executed including all necessary \n"
"parameters. If a parameter of the commandline includes a space you have to \n"
"surround this parameter by single or double quotes. Do not include the name \n"
"of the subversion client executable (i.e. svn).</p>", None))
        self.dirButton.setToolTip(_translate("SvnCommandDialog", "Select the working directory via a directory selection dialog", None))
        self.dirButton.setWhatsThis(_translate("SvnCommandDialog", "<b>Working directory</b>\n"
"<p>Select the working directory for the Subversion command via a directory selection dialog.</p>", None))
        self.dirButton.setText(_translate("SvnCommandDialog", "...", None))
        self.workdirCombo.setToolTip(_translate("SvnCommandDialog", "Enter the working directory for the Subversion command", None))
        self.workdirCombo.setWhatsThis(_translate("SvnCommandDialog", "<b>Working directory</b>\n"
"<p>Enter the working directory for the Subversion command.\n"
"This is an optional entry. The button to the right will open a \n"
"directory selection dialog.</p>", None))
        self.textLabel2.setText(_translate("SvnCommandDialog", "Working Directory:<br>(optional)", None))
        self.textLabel3.setText(_translate("SvnCommandDialog", "Project Directory:", None))
        self.projectDirLabel.setToolTip(_translate("SvnCommandDialog", "This shows the root directory of the current project.", None))
        self.projectDirLabel.setText(_translate("SvnCommandDialog", "project directory", None))

