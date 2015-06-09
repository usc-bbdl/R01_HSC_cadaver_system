# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\PluginManager\PluginRepositoryDialog.ui'
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

class Ui_PluginRepositoryDialog(object):
    def setupUi(self, PluginRepositoryDialog):
        PluginRepositoryDialog.setObjectName(_fromUtf8("PluginRepositoryDialog"))
        PluginRepositoryDialog.resize(800, 675)
        PluginRepositoryDialog.setProperty("sizeGripEnabled", True)
        self.verticalLayout = QtGui.QVBoxLayout(PluginRepositoryDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridlayout = QtGui.QGridLayout()
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.repositoryList = QtGui.QTreeWidget(PluginRepositoryDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(7)
        sizePolicy.setHeightForWidth(self.repositoryList.sizePolicy().hasHeightForWidth())
        self.repositoryList.setSizePolicy(sizePolicy)
        self.repositoryList.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.repositoryList.setRootIsDecorated(False)
        self.repositoryList.setItemsExpandable(False)
        self.repositoryList.setAllColumnsShowFocus(True)
        self.repositoryList.setObjectName(_fromUtf8("repositoryList"))
        self.gridlayout.addWidget(self.repositoryList, 0, 0, 1, 2)
        self.label_2 = QtGui.QLabel(PluginRepositoryDialog)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridlayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.descriptionEdit = QtGui.QTextEdit(PluginRepositoryDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.descriptionEdit.sizePolicy().hasHeightForWidth())
        self.descriptionEdit.setSizePolicy(sizePolicy)
        self.descriptionEdit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.descriptionEdit.setReadOnly(True)
        self.descriptionEdit.setObjectName(_fromUtf8("descriptionEdit"))
        self.gridlayout.addWidget(self.descriptionEdit, 1, 1, 1, 1)
        self.label_3 = QtGui.QLabel(PluginRepositoryDialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridlayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.authorEdit = QtGui.QLineEdit(PluginRepositoryDialog)
        self.authorEdit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.authorEdit.setReadOnly(True)
        self.authorEdit.setObjectName(_fromUtf8("authorEdit"))
        self.gridlayout.addWidget(self.authorEdit, 2, 1, 1, 1)
        self.label = QtGui.QLabel(PluginRepositoryDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridlayout.addWidget(self.label, 3, 0, 1, 1)
        self.urlEdit = QtGui.QLineEdit(PluginRepositoryDialog)
        self.urlEdit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.urlEdit.setReadOnly(True)
        self.urlEdit.setObjectName(_fromUtf8("urlEdit"))
        self.gridlayout.addWidget(self.urlEdit, 3, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridlayout)
        self.line = QtGui.QFrame(PluginRepositoryDialog)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.downloadProgress = QtGui.QProgressBar(PluginRepositoryDialog)
        self.downloadProgress.setProperty("value", 0)
        self.downloadProgress.setObjectName(_fromUtf8("downloadProgress"))
        self.verticalLayout.addWidget(self.downloadProgress)
        self.statusLabel = QtGui.QLabel(PluginRepositoryDialog)
        self.statusLabel.setText(_fromUtf8(""))
        self.statusLabel.setObjectName(_fromUtf8("statusLabel"))
        self.verticalLayout.addWidget(self.statusLabel)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_4 = QtGui.QLabel(PluginRepositoryDialog)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout.addWidget(self.label_4)
        self.repositoryUrlEdit = QtGui.QLineEdit(PluginRepositoryDialog)
        self.repositoryUrlEdit.setReadOnly(True)
        self.repositoryUrlEdit.setObjectName(_fromUtf8("repositoryUrlEdit"))
        self.horizontalLayout.addWidget(self.repositoryUrlEdit)
        self.repositoryUrlEditButton = QtGui.QPushButton(PluginRepositoryDialog)
        self.repositoryUrlEditButton.setCheckable(True)
        self.repositoryUrlEditButton.setObjectName(_fromUtf8("repositoryUrlEditButton"))
        self.horizontalLayout.addWidget(self.repositoryUrlEditButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.buttonBox = QtGui.QDialogButtonBox(PluginRepositoryDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(PluginRepositoryDialog)
        QtCore.QMetaObject.connectSlotsByName(PluginRepositoryDialog)
        PluginRepositoryDialog.setTabOrder(self.repositoryList, self.buttonBox)
        PluginRepositoryDialog.setTabOrder(self.buttonBox, self.repositoryUrlEdit)
        PluginRepositoryDialog.setTabOrder(self.repositoryUrlEdit, self.repositoryUrlEditButton)

    def retranslateUi(self, PluginRepositoryDialog):
        PluginRepositoryDialog.setWindowTitle(_translate("PluginRepositoryDialog", "Plugin Repository", None))
        self.repositoryList.setSortingEnabled(True)
        self.repositoryList.headerItem().setText(0, _translate("PluginRepositoryDialog", "Name", None))
        self.repositoryList.headerItem().setText(1, _translate("PluginRepositoryDialog", "Version", None))
        self.repositoryList.headerItem().setText(2, _translate("PluginRepositoryDialog", "Short Description", None))
        self.label_2.setText(_translate("PluginRepositoryDialog", "Description:", None))
        self.descriptionEdit.setToolTip(_translate("PluginRepositoryDialog", "Displays the description of the selected plugin", None))
        self.label_3.setText(_translate("PluginRepositoryDialog", "Author:", None))
        self.authorEdit.setToolTip(_translate("PluginRepositoryDialog", "Displays the author of the selected plugin", None))
        self.label.setText(_translate("PluginRepositoryDialog", "URL:", None))
        self.urlEdit.setToolTip(_translate("PluginRepositoryDialog", "Displays the download URL of the selected plugin", None))
        self.downloadProgress.setToolTip(_translate("PluginRepositoryDialog", "Shows the progress of the current download", None))
        self.label_4.setText(_translate("PluginRepositoryDialog", "Repository URL:", None))
        self.repositoryUrlEdit.setToolTip(_translate("PluginRepositoryDialog", "Shows the repository URL", None))
        self.repositoryUrlEditButton.setToolTip(_translate("PluginRepositoryDialog", "Press to edit the plugin repository URL", None))
        self.repositoryUrlEditButton.setText(_translate("PluginRepositoryDialog", "Edit URL", None))

