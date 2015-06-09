# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Plugins\VcsPlugins\vcsSubversion\SvnChangeListsDialog.ui'
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

class Ui_SvnChangeListsDialog(object):
    def setupUi(self, SvnChangeListsDialog):
        SvnChangeListsDialog.setObjectName(_fromUtf8("SvnChangeListsDialog"))
        SvnChangeListsDialog.resize(519, 494)
        SvnChangeListsDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtGui.QVBoxLayout(SvnChangeListsDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(SvnChangeListsDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.changeLists = QtGui.QListWidget(SvnChangeListsDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.changeLists.sizePolicy().hasHeightForWidth())
        self.changeLists.setSizePolicy(sizePolicy)
        self.changeLists.setAlternatingRowColors(True)
        self.changeLists.setObjectName(_fromUtf8("changeLists"))
        self.verticalLayout.addWidget(self.changeLists)
        self.filesLabel = QtGui.QLabel(SvnChangeListsDialog)
        self.filesLabel.setText(_fromUtf8(""))
        self.filesLabel.setWordWrap(True)
        self.filesLabel.setObjectName(_fromUtf8("filesLabel"))
        self.verticalLayout.addWidget(self.filesLabel)
        self.filesList = QtGui.QListWidget(SvnChangeListsDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.filesList.sizePolicy().hasHeightForWidth())
        self.filesList.setSizePolicy(sizePolicy)
        self.filesList.setAlternatingRowColors(True)
        self.filesList.setObjectName(_fromUtf8("filesList"))
        self.verticalLayout.addWidget(self.filesList)
        self.errorGroup = QtGui.QGroupBox(SvnChangeListsDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.errorGroup.sizePolicy().hasHeightForWidth())
        self.errorGroup.setSizePolicy(sizePolicy)
        self.errorGroup.setObjectName(_fromUtf8("errorGroup"))
        self.vboxlayout = QtGui.QVBoxLayout(self.errorGroup)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.errors = QtGui.QTextEdit(self.errorGroup)
        self.errors.setReadOnly(True)
        self.errors.setAcceptRichText(False)
        self.errors.setObjectName(_fromUtf8("errors"))
        self.vboxlayout.addWidget(self.errors)
        self.verticalLayout.addWidget(self.errorGroup)
        self.inputGroup = QtGui.QGroupBox(SvnChangeListsDialog)
        self.inputGroup.setObjectName(_fromUtf8("inputGroup"))
        self._2 = QtGui.QGridLayout(self.inputGroup)
        self._2.setObjectName(_fromUtf8("_2"))
        spacerItem = QtGui.QSpacerItem(327, 29, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self._2.addItem(spacerItem, 1, 1, 1, 1)
        self.sendButton = QtGui.QPushButton(self.inputGroup)
        self.sendButton.setObjectName(_fromUtf8("sendButton"))
        self._2.addWidget(self.sendButton, 1, 2, 1, 1)
        self.input = QtGui.QLineEdit(self.inputGroup)
        self.input.setObjectName(_fromUtf8("input"))
        self._2.addWidget(self.input, 0, 0, 1, 3)
        self.passwordCheckBox = QtGui.QCheckBox(self.inputGroup)
        self.passwordCheckBox.setObjectName(_fromUtf8("passwordCheckBox"))
        self._2.addWidget(self.passwordCheckBox, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.inputGroup)
        self.buttonBox = QtGui.QDialogButtonBox(SvnChangeListsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(SvnChangeListsDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), SvnChangeListsDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), SvnChangeListsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SvnChangeListsDialog)
        SvnChangeListsDialog.setTabOrder(self.changeLists, self.filesList)
        SvnChangeListsDialog.setTabOrder(self.filesList, self.errors)
        SvnChangeListsDialog.setTabOrder(self.errors, self.input)
        SvnChangeListsDialog.setTabOrder(self.input, self.passwordCheckBox)
        SvnChangeListsDialog.setTabOrder(self.passwordCheckBox, self.sendButton)
        SvnChangeListsDialog.setTabOrder(self.sendButton, self.buttonBox)

    def retranslateUi(self, SvnChangeListsDialog):
        SvnChangeListsDialog.setWindowTitle(_translate("SvnChangeListsDialog", "Subversion Change Lists", None))
        self.label.setText(_translate("SvnChangeListsDialog", "Change Lists:", None))
        self.changeLists.setWhatsThis(_translate("SvnChangeListsDialog", "<b>Change Lists</b>\n"
"<p>Select a change list here to see the associated files in the list below.</p>", None))
        self.filesList.setWhatsThis(_translate("SvnChangeListsDialog", "<b>Files</b>\n"
"<p>This shows a list of files associated with the change list selected above.</p>", None))
        self.errorGroup.setTitle(_translate("SvnChangeListsDialog", "Errors", None))
        self.inputGroup.setTitle(_translate("SvnChangeListsDialog", "Input", None))
        self.sendButton.setToolTip(_translate("SvnChangeListsDialog", "Press to send the input to the subversion process", None))
        self.sendButton.setText(_translate("SvnChangeListsDialog", "&Send", None))
        self.sendButton.setShortcut(_translate("SvnChangeListsDialog", "Alt+S", None))
        self.input.setToolTip(_translate("SvnChangeListsDialog", "Enter data to be sent to the subversion process", None))
        self.passwordCheckBox.setToolTip(_translate("SvnChangeListsDialog", "Select to switch the input field to password mode", None))
        self.passwordCheckBox.setText(_translate("SvnChangeListsDialog", "&Password Mode", None))
        self.passwordCheckBox.setShortcut(_translate("SvnChangeListsDialog", "Alt+P", None))

