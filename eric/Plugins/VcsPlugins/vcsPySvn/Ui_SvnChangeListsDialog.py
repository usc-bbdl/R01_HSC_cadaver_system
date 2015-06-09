# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Plugins\VcsPlugins\vcsPySvn\SvnChangeListsDialog.ui'
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
        SvnChangeListsDialog.setTabOrder(self.filesList, self.buttonBox)

    def retranslateUi(self, SvnChangeListsDialog):
        SvnChangeListsDialog.setWindowTitle(_translate("SvnChangeListsDialog", "Subversion Change Lists", None))
        self.label.setText(_translate("SvnChangeListsDialog", "Change Lists:", None))
        self.changeLists.setWhatsThis(_translate("SvnChangeListsDialog", "<b>Change Lists</b>\n"
"<p>Select a change list here to see the associated files in the list below.</p>", None))
        self.filesList.setWhatsThis(_translate("SvnChangeListsDialog", "<b>Files</b>\n"
"<p>This shows a list of files associated with the change list selected above.</p>", None))

