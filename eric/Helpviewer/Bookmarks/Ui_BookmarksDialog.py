# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Helpviewer\Bookmarks\BookmarksDialog.ui'
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

class Ui_BookmarksDialog(object):
    def setupUi(self, BookmarksDialog):
        BookmarksDialog.setObjectName(_fromUtf8("BookmarksDialog"))
        BookmarksDialog.resize(750, 450)
        BookmarksDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtGui.QVBoxLayout(BookmarksDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.searchEdit = QtGui.QLineEdit(BookmarksDialog)
        self.searchEdit.setObjectName(_fromUtf8("searchEdit"))
        self.horizontalLayout.addWidget(self.searchEdit)
        self.clearButton = QtGui.QToolButton(BookmarksDialog)
        self.clearButton.setText(_fromUtf8(""))
        self.clearButton.setObjectName(_fromUtf8("clearButton"))
        self.horizontalLayout.addWidget(self.clearButton)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.bookmarksTree = E4TreeView(BookmarksDialog)
        self.bookmarksTree.setDragDropMode(QtGui.QAbstractItemView.InternalMove)
        self.bookmarksTree.setAlternatingRowColors(True)
        self.bookmarksTree.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.bookmarksTree.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.bookmarksTree.setUniformRowHeights(True)
        self.bookmarksTree.setObjectName(_fromUtf8("bookmarksTree"))
        self.verticalLayout.addWidget(self.bookmarksTree)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.removeButton = QtGui.QPushButton(BookmarksDialog)
        self.removeButton.setAutoDefault(False)
        self.removeButton.setObjectName(_fromUtf8("removeButton"))
        self.horizontalLayout_3.addWidget(self.removeButton)
        self.addFolderButton = QtGui.QPushButton(BookmarksDialog)
        self.addFolderButton.setAutoDefault(False)
        self.addFolderButton.setObjectName(_fromUtf8("addFolderButton"))
        self.horizontalLayout_3.addWidget(self.addFolderButton)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.buttonBox = QtGui.QDialogButtonBox(BookmarksDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(BookmarksDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), BookmarksDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), BookmarksDialog.reject)
        QtCore.QObject.connect(self.clearButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.searchEdit.clear)
        QtCore.QMetaObject.connectSlotsByName(BookmarksDialog)
        BookmarksDialog.setTabOrder(self.searchEdit, self.clearButton)
        BookmarksDialog.setTabOrder(self.clearButton, self.bookmarksTree)
        BookmarksDialog.setTabOrder(self.bookmarksTree, self.removeButton)
        BookmarksDialog.setTabOrder(self.removeButton, self.addFolderButton)
        BookmarksDialog.setTabOrder(self.addFolderButton, self.buttonBox)

    def retranslateUi(self, BookmarksDialog):
        BookmarksDialog.setWindowTitle(_translate("BookmarksDialog", "Manage Bookmarks", None))
        self.searchEdit.setToolTip(_translate("BookmarksDialog", "Enter search term for bookmarks", None))
        self.clearButton.setToolTip(_translate("BookmarksDialog", "Press to clear the search edit", None))
        self.removeButton.setToolTip(_translate("BookmarksDialog", "Press to delete the selected entries", None))
        self.removeButton.setText(_translate("BookmarksDialog", "&Delete", None))
        self.addFolderButton.setToolTip(_translate("BookmarksDialog", "Press to add a new bookmarks folder", None))
        self.addFolderButton.setText(_translate("BookmarksDialog", "Add &Folder", None))

from E4Gui.E4TreeView import E4TreeView
