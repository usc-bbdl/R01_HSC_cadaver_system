# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Plugins\VcsPlugins\vcsPySvn\SvnNewProjectOptionsDialog.ui'
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

class Ui_SvnNewProjectOptionsDialog(object):
    def setupUi(self, SvnNewProjectOptionsDialog):
        SvnNewProjectOptionsDialog.setObjectName(_fromUtf8("SvnNewProjectOptionsDialog"))
        SvnNewProjectOptionsDialog.resize(562, 200)
        SvnNewProjectOptionsDialog.setSizeGripEnabled(True)
        self.vboxlayout = QtGui.QVBoxLayout(SvnNewProjectOptionsDialog)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.gridlayout = QtGui.QGridLayout()
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.vcsTagEdit = QtGui.QLineEdit(SvnNewProjectOptionsDialog)
        self.vcsTagEdit.setObjectName(_fromUtf8("vcsTagEdit"))
        self.gridlayout.addWidget(self.vcsTagEdit, 2, 1, 1, 1)
        self.projectDirButton = QtGui.QPushButton(SvnNewProjectOptionsDialog)
        self.projectDirButton.setObjectName(_fromUtf8("projectDirButton"))
        self.gridlayout.addWidget(self.projectDirButton, 3, 2, 1, 1)
        self.protocolCombo = QtGui.QComboBox(SvnNewProjectOptionsDialog)
        self.protocolCombo.setObjectName(_fromUtf8("protocolCombo"))
        self.gridlayout.addWidget(self.protocolCombo, 0, 1, 1, 1)
        self.textLabel1 = QtGui.QLabel(SvnNewProjectOptionsDialog)
        self.textLabel1.setObjectName(_fromUtf8("textLabel1"))
        self.gridlayout.addWidget(self.textLabel1, 0, 0, 1, 1)
        self.vcsUrlEdit = QtGui.QLineEdit(SvnNewProjectOptionsDialog)
        self.vcsUrlEdit.setObjectName(_fromUtf8("vcsUrlEdit"))
        self.gridlayout.addWidget(self.vcsUrlEdit, 1, 1, 1, 1)
        self.vcsUrlLabel = QtGui.QLabel(SvnNewProjectOptionsDialog)
        self.vcsUrlLabel.setObjectName(_fromUtf8("vcsUrlLabel"))
        self.gridlayout.addWidget(self.vcsUrlLabel, 1, 0, 1, 1)
        self.vcsProjectDirEdit = QtGui.QLineEdit(SvnNewProjectOptionsDialog)
        self.vcsProjectDirEdit.setObjectName(_fromUtf8("vcsProjectDirEdit"))
        self.gridlayout.addWidget(self.vcsProjectDirEdit, 3, 1, 1, 1)
        self.layoutCheckBox = QtGui.QCheckBox(SvnNewProjectOptionsDialog)
        self.layoutCheckBox.setChecked(True)
        self.layoutCheckBox.setObjectName(_fromUtf8("layoutCheckBox"))
        self.gridlayout.addWidget(self.layoutCheckBox, 4, 0, 1, 2)
        self.vcsUrlButton = QtGui.QPushButton(SvnNewProjectOptionsDialog)
        self.vcsUrlButton.setObjectName(_fromUtf8("vcsUrlButton"))
        self.gridlayout.addWidget(self.vcsUrlButton, 1, 2, 1, 1)
        self.TextLabel4 = QtGui.QLabel(SvnNewProjectOptionsDialog)
        self.TextLabel4.setObjectName(_fromUtf8("TextLabel4"))
        self.gridlayout.addWidget(self.TextLabel4, 3, 0, 1, 1)
        self.vcsTagLabel = QtGui.QLabel(SvnNewProjectOptionsDialog)
        self.vcsTagLabel.setObjectName(_fromUtf8("vcsTagLabel"))
        self.gridlayout.addWidget(self.vcsTagLabel, 2, 0, 1, 1)
        self.vboxlayout.addLayout(self.gridlayout)
        self.buttonBox = QtGui.QDialogButtonBox(SvnNewProjectOptionsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.vboxlayout.addWidget(self.buttonBox)
        self.textLabel1.setBuddy(self.protocolCombo)
        self.vcsUrlLabel.setBuddy(self.vcsUrlEdit)
        self.TextLabel4.setBuddy(self.vcsProjectDirEdit)
        self.vcsTagLabel.setBuddy(self.vcsTagEdit)

        self.retranslateUi(SvnNewProjectOptionsDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), SvnNewProjectOptionsDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), SvnNewProjectOptionsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SvnNewProjectOptionsDialog)
        SvnNewProjectOptionsDialog.setTabOrder(self.protocolCombo, self.vcsUrlEdit)
        SvnNewProjectOptionsDialog.setTabOrder(self.vcsUrlEdit, self.vcsUrlButton)
        SvnNewProjectOptionsDialog.setTabOrder(self.vcsUrlButton, self.vcsTagEdit)
        SvnNewProjectOptionsDialog.setTabOrder(self.vcsTagEdit, self.vcsProjectDirEdit)
        SvnNewProjectOptionsDialog.setTabOrder(self.vcsProjectDirEdit, self.projectDirButton)
        SvnNewProjectOptionsDialog.setTabOrder(self.projectDirButton, self.layoutCheckBox)

    def retranslateUi(self, SvnNewProjectOptionsDialog):
        SvnNewProjectOptionsDialog.setWindowTitle(_translate("SvnNewProjectOptionsDialog", "New Project from Repository", None))
        SvnNewProjectOptionsDialog.setWhatsThis(_translate("SvnNewProjectOptionsDialog", "<b>New Project from Repository Dialog</b>\n"
"<p>Enter the various repository infos into the entry fields. These values are used, when the new project is retrieved from the repository. If the checkbox is selected, the URL must end in the project name. A repository layout with project/tags, project/branches and project/trunk will be assumed. In this case, you may enter a tag or branch, which must look like tags/tagname or branches/branchname. If the checkbox is not selected, the URL must contain the complete path in the repository.</p>\n"
"<p>For remote repositories the URL must contain the hostname.</p>", None))
        self.vcsTagEdit.setToolTip(_translate("SvnNewProjectOptionsDialog", "Enter the tag the new project should be generated from", None))
        self.vcsTagEdit.setWhatsThis(_translate("SvnNewProjectOptionsDialog", "<b>Tag in VCS</b>\n"
"<p>Enter the tag name the new project shall be generated from. Leave empty to retrieve the latest data from the repository.</p>", None))
        self.projectDirButton.setToolTip(_translate("SvnNewProjectOptionsDialog", "Select the project directory via a directory selection dialog", None))
        self.projectDirButton.setText(_translate("SvnNewProjectOptionsDialog", "...", None))
        self.protocolCombo.setToolTip(_translate("SvnNewProjectOptionsDialog", "Select the protocol to access the repository", None))
        self.textLabel1.setText(_translate("SvnNewProjectOptionsDialog", "&Protocol:", None))
        self.vcsUrlEdit.setToolTip(_translate("SvnNewProjectOptionsDialog", "Enter the url path of the module in the repository (without protocol part)", None))
        self.vcsUrlEdit.setWhatsThis(_translate("SvnNewProjectOptionsDialog", "<b>URL</b><p>Enter the URL to the module. For a repository with standard layout, this must not contain the trunk, tags or branches part.</p>", None))
        self.vcsUrlLabel.setText(_translate("SvnNewProjectOptionsDialog", "&URL:", None))
        self.vcsProjectDirEdit.setToolTip(_translate("SvnNewProjectOptionsDialog", "Enter the directory of the new project.", None))
        self.vcsProjectDirEdit.setWhatsThis(_translate("SvnNewProjectOptionsDialog", "<b>Project Directory</b>\n"
"<p>Enter the directory of the new project. It will be retrieved from \n"
"the repository and be placed in this directory.</p>", None))
        self.layoutCheckBox.setToolTip(_translate("SvnNewProjectOptionsDialog", "Select to indicate, that the repository has a standard layout (projectdir/trunk, projectdir/tags, projectdir/branches)", None))
        self.layoutCheckBox.setText(_translate("SvnNewProjectOptionsDialog", "Repository has standard &layout", None))
        self.layoutCheckBox.setShortcut(_translate("SvnNewProjectOptionsDialog", "Alt+L", None))
        self.vcsUrlButton.setToolTip(_translate("SvnNewProjectOptionsDialog", "Select the repository url via a directory selection dialog or the repository browser", None))
        self.vcsUrlButton.setText(_translate("SvnNewProjectOptionsDialog", "...", None))
        self.TextLabel4.setText(_translate("SvnNewProjectOptionsDialog", "Project &Directory:", None))
        self.vcsTagLabel.setText(_translate("SvnNewProjectOptionsDialog", "&Tag:", None))

