# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Plugins\VcsPlugins\vcsPySvn\SvnStatusDialog.ui'
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

class Ui_SvnStatusDialog(object):
    def setupUi(self, SvnStatusDialog):
        SvnStatusDialog.setObjectName(_fromUtf8("SvnStatusDialog"))
        SvnStatusDialog.resize(955, 646)
        self.verticalLayout = QtGui.QVBoxLayout(SvnStatusDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label = QtGui.QLabel(SvnStatusDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.statusFilterCombo = QtGui.QComboBox(SvnStatusDialog)
        self.statusFilterCombo.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.statusFilterCombo.setObjectName(_fromUtf8("statusFilterCombo"))
        self.horizontalLayout_2.addWidget(self.statusFilterCombo)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.statusList = QtGui.QTreeWidget(SvnStatusDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(self.statusList.sizePolicy().hasHeightForWidth())
        self.statusList.setSizePolicy(sizePolicy)
        self.statusList.setAlternatingRowColors(True)
        self.statusList.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.statusList.setRootIsDecorated(False)
        self.statusList.setItemsExpandable(False)
        self.statusList.setObjectName(_fromUtf8("statusList"))
        self.verticalLayout.addWidget(self.statusList)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.commitButton = QtGui.QPushButton(SvnStatusDialog)
        self.commitButton.setObjectName(_fromUtf8("commitButton"))
        self.horizontalLayout.addWidget(self.commitButton)
        self.line = QtGui.QFrame(SvnStatusDialog)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.horizontalLayout.addWidget(self.line)
        self.addButton = QtGui.QPushButton(SvnStatusDialog)
        self.addButton.setObjectName(_fromUtf8("addButton"))
        self.horizontalLayout.addWidget(self.addButton)
        self.diffButton = QtGui.QPushButton(SvnStatusDialog)
        self.diffButton.setObjectName(_fromUtf8("diffButton"))
        self.horizontalLayout.addWidget(self.diffButton)
        self.revertButton = QtGui.QPushButton(SvnStatusDialog)
        self.revertButton.setObjectName(_fromUtf8("revertButton"))
        self.horizontalLayout.addWidget(self.revertButton)
        self.restoreButton = QtGui.QPushButton(SvnStatusDialog)
        self.restoreButton.setObjectName(_fromUtf8("restoreButton"))
        self.horizontalLayout.addWidget(self.restoreButton)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.errorGroup = QtGui.QGroupBox(SvnStatusDialog)
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
        self.buttonBox = QtGui.QDialogButtonBox(SvnStatusDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        self.label.setBuddy(self.statusFilterCombo)

        self.retranslateUi(SvnStatusDialog)
        QtCore.QMetaObject.connectSlotsByName(SvnStatusDialog)
        SvnStatusDialog.setTabOrder(self.statusFilterCombo, self.statusList)
        SvnStatusDialog.setTabOrder(self.statusList, self.commitButton)
        SvnStatusDialog.setTabOrder(self.commitButton, self.addButton)
        SvnStatusDialog.setTabOrder(self.addButton, self.diffButton)
        SvnStatusDialog.setTabOrder(self.diffButton, self.revertButton)
        SvnStatusDialog.setTabOrder(self.revertButton, self.restoreButton)
        SvnStatusDialog.setTabOrder(self.restoreButton, self.errors)
        SvnStatusDialog.setTabOrder(self.errors, self.buttonBox)

    def retranslateUi(self, SvnStatusDialog):
        SvnStatusDialog.setWindowTitle(_translate("SvnStatusDialog", "Subversion Status", None))
        SvnStatusDialog.setWhatsThis(_translate("SvnStatusDialog", "<b>Subversion Status</b>\n"
"<p>This dialog shows the status of the selected file or project.</p>", None))
        self.label.setText(_translate("SvnStatusDialog", "&Filter on Status:", None))
        self.statusFilterCombo.setToolTip(_translate("SvnStatusDialog", "Select the status of entries to be shown", None))
        self.statusList.setSortingEnabled(True)
        self.statusList.headerItem().setText(0, _translate("SvnStatusDialog", "Commit", None))
        self.statusList.headerItem().setText(1, _translate("SvnStatusDialog", "Changelist", None))
        self.statusList.headerItem().setText(2, _translate("SvnStatusDialog", "Status", None))
        self.statusList.headerItem().setText(3, _translate("SvnStatusDialog", "Prop. Status", None))
        self.statusList.headerItem().setText(4, _translate("SvnStatusDialog", "Locked", None))
        self.statusList.headerItem().setText(5, _translate("SvnStatusDialog", "History", None))
        self.statusList.headerItem().setText(6, _translate("SvnStatusDialog", "Switched", None))
        self.statusList.headerItem().setText(7, _translate("SvnStatusDialog", "Lock Info", None))
        self.statusList.headerItem().setText(8, _translate("SvnStatusDialog", "Up to date", None))
        self.statusList.headerItem().setText(9, _translate("SvnStatusDialog", "Revision", None))
        self.statusList.headerItem().setText(10, _translate("SvnStatusDialog", "Last Change", None))
        self.statusList.headerItem().setText(11, _translate("SvnStatusDialog", "Author", None))
        self.statusList.headerItem().setText(12, _translate("SvnStatusDialog", "Path", None))
        self.commitButton.setToolTip(_translate("SvnStatusDialog", "Commit the selected changes", None))
        self.commitButton.setText(_translate("SvnStatusDialog", "&Commit", None))
        self.addButton.setToolTip(_translate("SvnStatusDialog", "Add the selected entries to the repository", None))
        self.addButton.setText(_translate("SvnStatusDialog", "&Add", None))
        self.diffButton.setToolTip(_translate("SvnStatusDialog", "Show differences of the selected entries to the repository", None))
        self.diffButton.setText(_translate("SvnStatusDialog", "&Differences", None))
        self.revertButton.setToolTip(_translate("SvnStatusDialog", "Revert the selected entries to the last revision in the repository", None))
        self.revertButton.setText(_translate("SvnStatusDialog", "Re&vert", None))
        self.restoreButton.setToolTip(_translate("SvnStatusDialog", "Restore the selected missing entries from the repository", None))
        self.restoreButton.setText(_translate("SvnStatusDialog", "&Restore", None))
        self.errorGroup.setTitle(_translate("SvnStatusDialog", "Errors", None))

