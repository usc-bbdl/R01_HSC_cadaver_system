# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Preferences\ConfigurationPages\IconsPage.ui'
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

class Ui_IconsPage(object):
    def setupUi(self, IconsPage):
        IconsPage.setObjectName(_fromUtf8("IconsPage"))
        IconsPage.resize(539, 371)
        self.gridlayout = QtGui.QGridLayout(IconsPage)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.headerLabel = QtGui.QLabel(IconsPage)
        self.headerLabel.setObjectName(_fromUtf8("headerLabel"))
        self.gridlayout.addWidget(self.headerLabel, 0, 0, 1, 2)
        self.line10 = QtGui.QFrame(IconsPage)
        self.line10.setFrameShape(QtGui.QFrame.HLine)
        self.line10.setFrameShadow(QtGui.QFrame.Sunken)
        self.line10.setFrameShape(QtGui.QFrame.HLine)
        self.line10.setFrameShadow(QtGui.QFrame.Sunken)
        self.line10.setObjectName(_fromUtf8("line10"))
        self.gridlayout.addWidget(self.line10, 1, 0, 1, 2)
        self.TextLabel1_2_2_2_2 = QtGui.QLabel(IconsPage)
        self.TextLabel1_2_2_2_2.setObjectName(_fromUtf8("TextLabel1_2_2_2_2"))
        self.gridlayout.addWidget(self.TextLabel1_2_2_2_2, 2, 0, 1, 2)
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        self.deleteIconDirectoryButton = QtGui.QPushButton(IconsPage)
        self.deleteIconDirectoryButton.setEnabled(False)
        self.deleteIconDirectoryButton.setObjectName(_fromUtf8("deleteIconDirectoryButton"))
        self.hboxlayout.addWidget(self.deleteIconDirectoryButton)
        self.addIconDirectoryButton = QtGui.QPushButton(IconsPage)
        self.addIconDirectoryButton.setEnabled(False)
        self.addIconDirectoryButton.setObjectName(_fromUtf8("addIconDirectoryButton"))
        self.hboxlayout.addWidget(self.addIconDirectoryButton)
        self.iconDirectoryEdit = QtGui.QLineEdit(IconsPage)
        self.iconDirectoryEdit.setObjectName(_fromUtf8("iconDirectoryEdit"))
        self.hboxlayout.addWidget(self.iconDirectoryEdit)
        self.iconDirectoryButton = QtGui.QPushButton(IconsPage)
        self.iconDirectoryButton.setObjectName(_fromUtf8("iconDirectoryButton"))
        self.hboxlayout.addWidget(self.iconDirectoryButton)
        self.gridlayout.addLayout(self.hboxlayout, 4, 0, 1, 1)
        self.showIconsButton = QtGui.QPushButton(IconsPage)
        self.showIconsButton.setEnabled(False)
        self.showIconsButton.setObjectName(_fromUtf8("showIconsButton"))
        self.gridlayout.addWidget(self.showIconsButton, 4, 1, 1, 1)
        self.vboxlayout = QtGui.QVBoxLayout()
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        spacerItem = QtGui.QSpacerItem(20, 209, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vboxlayout.addItem(spacerItem)
        self.upButton = QtGui.QPushButton(IconsPage)
        self.upButton.setEnabled(False)
        self.upButton.setObjectName(_fromUtf8("upButton"))
        self.vboxlayout.addWidget(self.upButton)
        self.downButton = QtGui.QPushButton(IconsPage)
        self.downButton.setEnabled(False)
        self.downButton.setObjectName(_fromUtf8("downButton"))
        self.vboxlayout.addWidget(self.downButton)
        spacerItem1 = QtGui.QSpacerItem(20, 170, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vboxlayout.addItem(spacerItem1)
        self.gridlayout.addLayout(self.vboxlayout, 3, 1, 1, 1)
        self.iconDirectoryList = QtGui.QListWidget(IconsPage)
        self.iconDirectoryList.setAlternatingRowColors(True)
        self.iconDirectoryList.setObjectName(_fromUtf8("iconDirectoryList"))
        self.gridlayout.addWidget(self.iconDirectoryList, 3, 0, 1, 1)

        self.retranslateUi(IconsPage)
        QtCore.QMetaObject.connectSlotsByName(IconsPage)
        IconsPage.setTabOrder(self.iconDirectoryList, self.upButton)
        IconsPage.setTabOrder(self.upButton, self.downButton)
        IconsPage.setTabOrder(self.downButton, self.deleteIconDirectoryButton)
        IconsPage.setTabOrder(self.deleteIconDirectoryButton, self.iconDirectoryEdit)
        IconsPage.setTabOrder(self.iconDirectoryEdit, self.iconDirectoryButton)
        IconsPage.setTabOrder(self.iconDirectoryButton, self.showIconsButton)
        IconsPage.setTabOrder(self.showIconsButton, self.addIconDirectoryButton)

    def retranslateUi(self, IconsPage):
        self.headerLabel.setText(_translate("IconsPage", "<b>Configure icon directories</b>", None))
        self.TextLabel1_2_2_2_2.setText(_translate("IconsPage", "<font color=\"#FF0000\"><b>Note:</b> These settings are activated at the next startup of the application.</font>", None))
        self.deleteIconDirectoryButton.setToolTip(_translate("IconsPage", "Press to delete the selected directory from the list", None))
        self.deleteIconDirectoryButton.setText(_translate("IconsPage", "Delete", None))
        self.addIconDirectoryButton.setToolTip(_translate("IconsPage", "Press to add the entered directory to the list", None))
        self.addIconDirectoryButton.setText(_translate("IconsPage", "Add", None))
        self.iconDirectoryEdit.setToolTip(_translate("IconsPage", "Enter a directory to be added", None))
        self.iconDirectoryButton.setToolTip(_translate("IconsPage", "Press to select an icon directory via a selection dialog", None))
        self.iconDirectoryButton.setText(_translate("IconsPage", "...", None))
        self.showIconsButton.setText(_translate("IconsPage", "Show", None))
        self.upButton.setText(_translate("IconsPage", "Up", None))
        self.downButton.setText(_translate("IconsPage", "Down", None))
        self.iconDirectoryList.setToolTip(_translate("IconsPage", "List of icon directories", None))

