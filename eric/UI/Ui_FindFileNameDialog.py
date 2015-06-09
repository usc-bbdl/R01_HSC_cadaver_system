# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\UI\FindFileNameDialog.ui'
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

class Ui_FindFileNameDialog(object):
    def setupUi(self, FindFileNameDialog):
        FindFileNameDialog.setObjectName(_fromUtf8("FindFileNameDialog"))
        FindFileNameDialog.resize(599, 478)
        self.vboxlayout = QtGui.QVBoxLayout(FindFileNameDialog)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.textLabel1 = QtGui.QLabel(FindFileNameDialog)
        self.textLabel1.setObjectName(_fromUtf8("textLabel1"))
        self.vboxlayout.addWidget(self.textLabel1)
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        self.fileNameEdit = QtGui.QLineEdit(FindFileNameDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(9)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fileNameEdit.sizePolicy().hasHeightForWidth())
        self.fileNameEdit.setSizePolicy(sizePolicy)
        self.fileNameEdit.setObjectName(_fromUtf8("fileNameEdit"))
        self.hboxlayout.addWidget(self.fileNameEdit)
        self.extsepLabel = QtGui.QLabel(FindFileNameDialog)
        self.extsepLabel.setObjectName(_fromUtf8("extsepLabel"))
        self.hboxlayout.addWidget(self.extsepLabel)
        self.fileExtEdit = QtGui.QLineEdit(FindFileNameDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fileExtEdit.sizePolicy().hasHeightForWidth())
        self.fileExtEdit.setSizePolicy(sizePolicy)
        self.fileExtEdit.setObjectName(_fromUtf8("fileExtEdit"))
        self.hboxlayout.addWidget(self.fileExtEdit)
        self.vboxlayout.addLayout(self.hboxlayout)
        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setObjectName(_fromUtf8("hboxlayout1"))
        self.searchDirCheckBox = QtGui.QCheckBox(FindFileNameDialog)
        self.searchDirCheckBox.setEnabled(False)
        self.searchDirCheckBox.setObjectName(_fromUtf8("searchDirCheckBox"))
        self.hboxlayout1.addWidget(self.searchDirCheckBox)
        self.searchDirEdit = QtGui.QLineEdit(FindFileNameDialog)
        self.searchDirEdit.setObjectName(_fromUtf8("searchDirEdit"))
        self.hboxlayout1.addWidget(self.searchDirEdit)
        self.searchDirButton = QtGui.QPushButton(FindFileNameDialog)
        self.searchDirButton.setObjectName(_fromUtf8("searchDirButton"))
        self.hboxlayout1.addWidget(self.searchDirButton)
        self.vboxlayout.addLayout(self.hboxlayout1)
        self.hboxlayout2 = QtGui.QHBoxLayout()
        self.hboxlayout2.setObjectName(_fromUtf8("hboxlayout2"))
        self.projectCheckBox = QtGui.QCheckBox(FindFileNameDialog)
        self.projectCheckBox.setObjectName(_fromUtf8("projectCheckBox"))
        self.hboxlayout2.addWidget(self.projectCheckBox)
        self.syspathCheckBox = QtGui.QCheckBox(FindFileNameDialog)
        self.syspathCheckBox.setObjectName(_fromUtf8("syspathCheckBox"))
        self.hboxlayout2.addWidget(self.syspathCheckBox)
        self.vboxlayout.addLayout(self.hboxlayout2)
        self.fileList = QtGui.QTreeWidget(FindFileNameDialog)
        self.fileList.setRootIsDecorated(False)
        self.fileList.setObjectName(_fromUtf8("fileList"))
        self.vboxlayout.addWidget(self.fileList)
        self.buttonBox = QtGui.QDialogButtonBox(FindFileNameDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close|QtGui.QDialogButtonBox.Open)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(FindFileNameDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), FindFileNameDialog.close)
        QtCore.QMetaObject.connectSlotsByName(FindFileNameDialog)
        FindFileNameDialog.setTabOrder(self.fileNameEdit, self.fileExtEdit)
        FindFileNameDialog.setTabOrder(self.fileExtEdit, self.searchDirEdit)
        FindFileNameDialog.setTabOrder(self.searchDirEdit, self.searchDirButton)
        FindFileNameDialog.setTabOrder(self.searchDirButton, self.searchDirCheckBox)
        FindFileNameDialog.setTabOrder(self.searchDirCheckBox, self.projectCheckBox)
        FindFileNameDialog.setTabOrder(self.projectCheckBox, self.syspathCheckBox)
        FindFileNameDialog.setTabOrder(self.syspathCheckBox, self.fileList)

    def retranslateUi(self, FindFileNameDialog):
        FindFileNameDialog.setWindowTitle(_translate("FindFileNameDialog", "Find File", None))
        self.textLabel1.setText(_translate("FindFileNameDialog", "Enter filename (? matches any single character, * matches everything)", None))
        self.fileNameEdit.setToolTip(_translate("FindFileNameDialog", "Enter file name to search for ", None))
        self.extsepLabel.setText(_translate("FindFileNameDialog", ".", None))
        self.fileExtEdit.setToolTip(_translate("FindFileNameDialog", "Enter file extension to search for", None))
        self.searchDirCheckBox.setToolTip(_translate("FindFileNameDialog", "Enabled to include the entered directory into the search", None))
        self.searchDirCheckBox.setText(_translate("FindFileNameDialog", "Search Path:", None))
        self.searchDirEdit.setToolTip(_translate("FindFileNameDialog", "Enter the directory, the file should be searched in", None))
        self.searchDirButton.setToolTip(_translate("FindFileNameDialog", "Press to select the directory, the file should be searched in", None))
        self.searchDirButton.setText(_translate("FindFileNameDialog", "...", None))
        self.projectCheckBox.setToolTip(_translate("FindFileNameDialog", "Select to search in the project path", None))
        self.projectCheckBox.setText(_translate("FindFileNameDialog", "Search in &project", None))
        self.projectCheckBox.setShortcut(_translate("FindFileNameDialog", "Alt+P", None))
        self.syspathCheckBox.setToolTip(_translate("FindFileNameDialog", "Select to search in sys.path", None))
        self.syspathCheckBox.setText(_translate("FindFileNameDialog", "Search in &sys.path", None))
        self.syspathCheckBox.setShortcut(_translate("FindFileNameDialog", "Alt+S", None))
        self.fileList.setSortingEnabled(True)
        self.fileList.headerItem().setText(0, _translate("FindFileNameDialog", "Filename", None))
        self.fileList.headerItem().setText(1, _translate("FindFileNameDialog", "Path", None))

