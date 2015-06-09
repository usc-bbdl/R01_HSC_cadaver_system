# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Plugins\VcsPlugins\vcsPySvn\SvnOptionsDialog.ui'
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

class Ui_SvnOptionsDialog(object):
    def setupUi(self, SvnOptionsDialog):
        SvnOptionsDialog.setObjectName(_fromUtf8("SvnOptionsDialog"))
        SvnOptionsDialog.resize(565, 165)
        SvnOptionsDialog.setSizeGripEnabled(True)
        self.vboxlayout = QtGui.QVBoxLayout(SvnOptionsDialog)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.gridlayout = QtGui.QGridLayout()
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.TextLabel5 = QtGui.QLabel(SvnOptionsDialog)
        self.TextLabel5.setObjectName(_fromUtf8("TextLabel5"))
        self.gridlayout.addWidget(self.TextLabel5, 2, 0, 1, 1)
        self.layoutCheckBox = QtGui.QCheckBox(SvnOptionsDialog)
        self.layoutCheckBox.setChecked(True)
        self.layoutCheckBox.setObjectName(_fromUtf8("layoutCheckBox"))
        self.gridlayout.addWidget(self.layoutCheckBox, 3, 0, 1, 2)
        self.protocolCombo = QtGui.QComboBox(SvnOptionsDialog)
        self.protocolCombo.setObjectName(_fromUtf8("protocolCombo"))
        self.gridlayout.addWidget(self.protocolCombo, 0, 1, 1, 1)
        self.vcsUrlButton = QtGui.QPushButton(SvnOptionsDialog)
        self.vcsUrlButton.setObjectName(_fromUtf8("vcsUrlButton"))
        self.gridlayout.addWidget(self.vcsUrlButton, 1, 2, 1, 1)
        self.vcsUrlLabel = QtGui.QLabel(SvnOptionsDialog)
        self.vcsUrlLabel.setObjectName(_fromUtf8("vcsUrlLabel"))
        self.gridlayout.addWidget(self.vcsUrlLabel, 1, 0, 1, 1)
        self.vcsLogEdit = QtGui.QLineEdit(SvnOptionsDialog)
        self.vcsLogEdit.setObjectName(_fromUtf8("vcsLogEdit"))
        self.gridlayout.addWidget(self.vcsLogEdit, 2, 1, 1, 1)
        self.textLabel1 = QtGui.QLabel(SvnOptionsDialog)
        self.textLabel1.setObjectName(_fromUtf8("textLabel1"))
        self.gridlayout.addWidget(self.textLabel1, 0, 0, 1, 1)
        self.vcsUrlEdit = QtGui.QLineEdit(SvnOptionsDialog)
        self.vcsUrlEdit.setObjectName(_fromUtf8("vcsUrlEdit"))
        self.gridlayout.addWidget(self.vcsUrlEdit, 1, 1, 1, 1)
        self.vboxlayout.addLayout(self.gridlayout)
        self.buttonBox = QtGui.QDialogButtonBox(SvnOptionsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.vboxlayout.addWidget(self.buttonBox)
        self.TextLabel5.setBuddy(self.vcsLogEdit)
        self.vcsUrlLabel.setBuddy(self.vcsUrlEdit)
        self.textLabel1.setBuddy(self.protocolCombo)

        self.retranslateUi(SvnOptionsDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), SvnOptionsDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), SvnOptionsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SvnOptionsDialog)
        SvnOptionsDialog.setTabOrder(self.protocolCombo, self.vcsUrlEdit)
        SvnOptionsDialog.setTabOrder(self.vcsUrlEdit, self.vcsUrlButton)
        SvnOptionsDialog.setTabOrder(self.vcsUrlButton, self.vcsLogEdit)
        SvnOptionsDialog.setTabOrder(self.vcsLogEdit, self.layoutCheckBox)

    def retranslateUi(self, SvnOptionsDialog):
        SvnOptionsDialog.setWindowTitle(_translate("SvnOptionsDialog", "Repository Infos", None))
        SvnOptionsDialog.setWhatsThis(_translate("SvnOptionsDialog", "<b>Repository Infos Dialog</b>\n"
"<p>Enter the various infos into the entry fields. These values are used to generate a new project in the repository. If the checkbox is selected, the URL must end in the project name. A directory tree with project/tags, project/branches and project/trunk will be generated in the repository. If the checkbox is not selected, the URL must contain the complete path in the repository.</p>\n"
"<p>For remote repositories the URL must contain the hostname.</p>", None))
        self.TextLabel5.setText(_translate("SvnOptionsDialog", "Log &Message:", None))
        self.layoutCheckBox.setToolTip(_translate("SvnOptionsDialog", "Select, if the standard repository layout (projectdir/trunk, projectdir/tags, projectdir/branches) should be generated", None))
        self.layoutCheckBox.setText(_translate("SvnOptionsDialog", "Create standard repository &layout", None))
        self.layoutCheckBox.setShortcut(_translate("SvnOptionsDialog", "Alt+L", None))
        self.protocolCombo.setToolTip(_translate("SvnOptionsDialog", "Select the protocol to access the repository", None))
        self.vcsUrlButton.setToolTip(_translate("SvnOptionsDialog", "Select the repository url via a directory selection dialog or the repository browser", None))
        self.vcsUrlButton.setText(_translate("SvnOptionsDialog", "...", None))
        self.vcsUrlLabel.setText(_translate("SvnOptionsDialog", "&URL:", None))
        self.vcsLogEdit.setToolTip(_translate("SvnOptionsDialog", "Enter the log message for the new project.", None))
        self.vcsLogEdit.setWhatsThis(_translate("SvnOptionsDialog", "<b>Log Message</b>\n"
"<p>Enter the log message to be used for the new project.</p>", None))
        self.vcsLogEdit.setText(_translate("SvnOptionsDialog", "new project started", None))
        self.textLabel1.setText(_translate("SvnOptionsDialog", "&Protocol:", None))
        self.vcsUrlEdit.setToolTip(_translate("SvnOptionsDialog", "Enter the url path of the module in the repository (without protocol part)", None))
        self.vcsUrlEdit.setWhatsThis(_translate("SvnOptionsDialog", "<b>URL</b><p>Enter the URL to the module. For a repository with standard layout, this must not contain the trunk, tags or branches part.</p>", None))

