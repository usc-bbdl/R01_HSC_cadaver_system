# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\ViewManager\BookmarkedFilesDialog.ui'
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

class Ui_BookmarkedFilesDialog(object):
    def setupUi(self, BookmarkedFilesDialog):
        BookmarkedFilesDialog.setObjectName(_fromUtf8("BookmarkedFilesDialog"))
        BookmarkedFilesDialog.resize(475, 391)
        BookmarkedFilesDialog.setSizeGripEnabled(True)
        self.vboxlayout = QtGui.QVBoxLayout(BookmarkedFilesDialog)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.gridlayout = QtGui.QGridLayout()
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.filesList = QtGui.QListWidget(BookmarkedFilesDialog)
        self.filesList.setAlternatingRowColors(True)
        self.filesList.setObjectName(_fromUtf8("filesList"))
        self.gridlayout.addWidget(self.filesList, 0, 0, 6, 3)
        self.deleteButton = QtGui.QPushButton(BookmarkedFilesDialog)
        self.deleteButton.setEnabled(False)
        self.deleteButton.setObjectName(_fromUtf8("deleteButton"))
        self.gridlayout.addWidget(self.deleteButton, 2, 3, 1, 1)
        spacerItem = QtGui.QSpacerItem(87, 130, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridlayout.addItem(spacerItem, 5, 3, 1, 1)
        self.upButton = QtGui.QPushButton(BookmarkedFilesDialog)
        self.upButton.setEnabled(False)
        self.upButton.setObjectName(_fromUtf8("upButton"))
        self.gridlayout.addWidget(self.upButton, 3, 3, 1, 1)
        self.fileButton = QtGui.QPushButton(BookmarkedFilesDialog)
        self.fileButton.setObjectName(_fromUtf8("fileButton"))
        self.gridlayout.addWidget(self.fileButton, 6, 2, 1, 1)
        self.downButton = QtGui.QPushButton(BookmarkedFilesDialog)
        self.downButton.setEnabled(False)
        self.downButton.setObjectName(_fromUtf8("downButton"))
        self.gridlayout.addWidget(self.downButton, 4, 3, 1, 1)
        self.addButton = QtGui.QPushButton(BookmarkedFilesDialog)
        self.addButton.setEnabled(False)
        self.addButton.setObjectName(_fromUtf8("addButton"))
        self.gridlayout.addWidget(self.addButton, 0, 3, 1, 1)
        self.TextLabel1 = QtGui.QLabel(BookmarkedFilesDialog)
        self.TextLabel1.setObjectName(_fromUtf8("TextLabel1"))
        self.gridlayout.addWidget(self.TextLabel1, 6, 0, 1, 1)
        self.changeButton = QtGui.QPushButton(BookmarkedFilesDialog)
        self.changeButton.setEnabled(False)
        self.changeButton.setObjectName(_fromUtf8("changeButton"))
        self.gridlayout.addWidget(self.changeButton, 1, 3, 1, 1)
        self.fileEdit = QtGui.QLineEdit(BookmarkedFilesDialog)
        self.fileEdit.setObjectName(_fromUtf8("fileEdit"))
        self.gridlayout.addWidget(self.fileEdit, 6, 1, 1, 1)
        self.vboxlayout.addLayout(self.gridlayout)
        self.buttonBox = QtGui.QDialogButtonBox(BookmarkedFilesDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.vboxlayout.addWidget(self.buttonBox)
        self.TextLabel1.setBuddy(self.fileEdit)

        self.retranslateUi(BookmarkedFilesDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), BookmarkedFilesDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), BookmarkedFilesDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(BookmarkedFilesDialog)
        BookmarkedFilesDialog.setTabOrder(self.filesList, self.addButton)
        BookmarkedFilesDialog.setTabOrder(self.addButton, self.changeButton)
        BookmarkedFilesDialog.setTabOrder(self.changeButton, self.deleteButton)
        BookmarkedFilesDialog.setTabOrder(self.deleteButton, self.upButton)
        BookmarkedFilesDialog.setTabOrder(self.upButton, self.downButton)
        BookmarkedFilesDialog.setTabOrder(self.downButton, self.fileEdit)
        BookmarkedFilesDialog.setTabOrder(self.fileEdit, self.fileButton)

    def retranslateUi(self, BookmarkedFilesDialog):
        BookmarkedFilesDialog.setWindowTitle(_translate("BookmarkedFilesDialog", "Configure Bookmarked Files Menu", None))
        self.deleteButton.setToolTip(_translate("BookmarkedFilesDialog", "Delete the selected entry", None))
        self.deleteButton.setWhatsThis(_translate("BookmarkedFilesDialog", "<b>Delete</b>\n"
"<p>Delete the selected entry.</p>", None))
        self.deleteButton.setText(_translate("BookmarkedFilesDialog", "&Delete", None))
        self.deleteButton.setShortcut(_translate("BookmarkedFilesDialog", "Alt+D", None))
        self.upButton.setToolTip(_translate("BookmarkedFilesDialog", "Move up", None))
        self.upButton.setWhatsThis(_translate("BookmarkedFilesDialog", "<b>Move Up</b>\n"
"<p>Move the selected entry up.</p>", None))
        self.upButton.setText(_translate("BookmarkedFilesDialog", "&Up", None))
        self.upButton.setShortcut(_translate("BookmarkedFilesDialog", "Alt+U", None))
        self.fileButton.setToolTip(_translate("BookmarkedFilesDialog", "Select the file via a file selection dialog", None))
        self.fileButton.setWhatsThis(_translate("BookmarkedFilesDialog", "<b>File</b>\n"
"<p>Select the file to be bookmarked via a file selection dialog.</p>", None))
        self.fileButton.setText(_translate("BookmarkedFilesDialog", "...", None))
        self.downButton.setToolTip(_translate("BookmarkedFilesDialog", "Move down", None))
        self.downButton.setWhatsThis(_translate("BookmarkedFilesDialog", "<b>Move Down</b>\n"
"<p>Move the selected entry down.</p>", None))
        self.downButton.setText(_translate("BookmarkedFilesDialog", "&Down", None))
        self.downButton.setShortcut(_translate("BookmarkedFilesDialog", "Alt+D", None))
        self.addButton.setToolTip(_translate("BookmarkedFilesDialog", "Add a new bookmarked file", None))
        self.addButton.setWhatsThis(_translate("BookmarkedFilesDialog", "<b>Add</b>\n"
"<p>Add a new bookmarked file with the value entered below.</p>", None))
        self.addButton.setText(_translate("BookmarkedFilesDialog", "&Add", None))
        self.addButton.setShortcut(_translate("BookmarkedFilesDialog", "Alt+A", None))
        self.TextLabel1.setText(_translate("BookmarkedFilesDialog", "&File:", None))
        self.changeButton.setToolTip(_translate("BookmarkedFilesDialog", "Change the value of the selected entry", None))
        self.changeButton.setWhatsThis(_translate("BookmarkedFilesDialog", "<b>Change</b>\n"
"<p>Change the value of the selected entry.</p>", None))
        self.changeButton.setText(_translate("BookmarkedFilesDialog", "C&hange", None))
        self.changeButton.setShortcut(_translate("BookmarkedFilesDialog", "Alt+H", None))
        self.fileEdit.setToolTip(_translate("BookmarkedFilesDialog", "Enter the filename of the file", None))
        self.fileEdit.setWhatsThis(_translate("BookmarkedFilesDialog", "<b>File</b>\n"
"<p>Enter the filename of the bookmarked file.</p>", None))

