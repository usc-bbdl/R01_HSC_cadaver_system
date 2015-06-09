# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\SqlBrowser\SqlBrowserWidget.ui'
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

class Ui_SqlBrowserWidget(object):
    def setupUi(self, SqlBrowserWidget):
        SqlBrowserWidget.setObjectName(_fromUtf8("SqlBrowserWidget"))
        SqlBrowserWidget.resize(800, 550)
        self.verticalLayout_2 = QtGui.QVBoxLayout(SqlBrowserWidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.splitter = QtGui.QSplitter(SqlBrowserWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.connections = SqlConnectionWidget(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.connections.sizePolicy().hasHeightForWidth())
        self.connections.setSizePolicy(sizePolicy)
        self.connections.setObjectName(_fromUtf8("connections"))
        self.table = QtGui.QTableView(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table.sizePolicy().hasHeightForWidth())
        self.table.setSizePolicy(sizePolicy)
        self.table.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.table.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.table.setObjectName(_fromUtf8("table"))
        self.verticalLayout_2.addWidget(self.splitter)
        self.queryGroup = QtGui.QGroupBox(SqlBrowserWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.queryGroup.sizePolicy().hasHeightForWidth())
        self.queryGroup.setSizePolicy(sizePolicy)
        self.queryGroup.setMaximumSize(QtCore.QSize(16777215, 200))
        self.queryGroup.setObjectName(_fromUtf8("queryGroup"))
        self.verticalLayout = QtGui.QVBoxLayout(self.queryGroup)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.sqlEdit = QtGui.QPlainTextEdit(self.queryGroup)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sqlEdit.sizePolicy().hasHeightForWidth())
        self.sqlEdit.setSizePolicy(sizePolicy)
        self.sqlEdit.setMinimumSize(QtCore.QSize(0, 18))
        self.sqlEdit.setObjectName(_fromUtf8("sqlEdit"))
        self.verticalLayout.addWidget(self.sqlEdit)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.clearButton = QtGui.QPushButton(self.queryGroup)
        self.clearButton.setObjectName(_fromUtf8("clearButton"))
        self.horizontalLayout.addWidget(self.clearButton)
        self.executeButton = QtGui.QPushButton(self.queryGroup)
        self.executeButton.setObjectName(_fromUtf8("executeButton"))
        self.horizontalLayout.addWidget(self.executeButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addWidget(self.queryGroup)
        self.insertRowAction = QtGui.QAction(SqlBrowserWidget)
        self.insertRowAction.setEnabled(False)
        self.insertRowAction.setObjectName(_fromUtf8("insertRowAction"))
        self.deleteRowAction = QtGui.QAction(SqlBrowserWidget)
        self.deleteRowAction.setEnabled(False)
        self.deleteRowAction.setObjectName(_fromUtf8("deleteRowAction"))

        self.retranslateUi(SqlBrowserWidget)
        QtCore.QMetaObject.connectSlotsByName(SqlBrowserWidget)
        SqlBrowserWidget.setTabOrder(self.sqlEdit, self.clearButton)
        SqlBrowserWidget.setTabOrder(self.clearButton, self.executeButton)
        SqlBrowserWidget.setTabOrder(self.executeButton, self.connections)
        SqlBrowserWidget.setTabOrder(self.connections, self.table)

    def retranslateUi(self, SqlBrowserWidget):
        SqlBrowserWidget.setWindowTitle(_translate("SqlBrowserWidget", "eric4 SQL Browser", None))
        self.queryGroup.setTitle(_translate("SqlBrowserWidget", "SQL Query", None))
        self.sqlEdit.setToolTip(_translate("SqlBrowserWidget", "Enter the SQL query to be executed", None))
        self.clearButton.setToolTip(_translate("SqlBrowserWidget", "Press to clear the entry", None))
        self.clearButton.setText(_translate("SqlBrowserWidget", "&Clear", None))
        self.executeButton.setToolTip(_translate("SqlBrowserWidget", "Press to execute the query", None))
        self.executeButton.setText(_translate("SqlBrowserWidget", "&Execute", None))
        self.insertRowAction.setText(_translate("SqlBrowserWidget", "&Insert Row", None))
        self.insertRowAction.setToolTip(_translate("SqlBrowserWidget", "Inserts a new row", None))
        self.deleteRowAction.setText(_translate("SqlBrowserWidget", "&Delete Row", None))
        self.deleteRowAction.setStatusTip(_translate("SqlBrowserWidget", "Deletes the current row", None))

from SqlConnectionWidget import SqlConnectionWidget
