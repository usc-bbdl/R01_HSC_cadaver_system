# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\E4Network\E4NetworkMonitor.ui'
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

class Ui_E4NetworkMonitor(object):
    def setupUi(self, E4NetworkMonitor):
        E4NetworkMonitor.setObjectName(_fromUtf8("E4NetworkMonitor"))
        E4NetworkMonitor.resize(800, 600)
        E4NetworkMonitor.setSizeGripEnabled(True)
        self.verticalLayout_3 = QtGui.QVBoxLayout(E4NetworkMonitor)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(E4NetworkMonitor)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.searchEdit = QtGui.QLineEdit(E4NetworkMonitor)
        self.searchEdit.setObjectName(_fromUtf8("searchEdit"))
        self.horizontalLayout.addWidget(self.searchEdit)
        self.clearButton = QtGui.QToolButton(E4NetworkMonitor)
        self.clearButton.setObjectName(_fromUtf8("clearButton"))
        self.horizontalLayout.addWidget(self.clearButton)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.requestsList = E4TableView(E4NetworkMonitor)
        self.requestsList.setAlternatingRowColors(True)
        self.requestsList.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.requestsList.setShowGrid(False)
        self.requestsList.setSortingEnabled(False)
        self.requestsList.setObjectName(_fromUtf8("requestsList"))
        self.verticalLayout_3.addWidget(self.requestsList)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.removeButton = QtGui.QPushButton(E4NetworkMonitor)
        self.removeButton.setAutoDefault(False)
        self.removeButton.setObjectName(_fromUtf8("removeButton"))
        self.horizontalLayout_3.addWidget(self.removeButton)
        self.removeAllButton = QtGui.QPushButton(E4NetworkMonitor)
        self.removeAllButton.setAutoDefault(False)
        self.removeAllButton.setObjectName(_fromUtf8("removeAllButton"))
        self.horizontalLayout_3.addWidget(self.removeAllButton)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.splitter = QtGui.QSplitter(E4NetworkMonitor)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.layoutWidget = QtGui.QWidget(self.splitter)
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.requestHeadersList = QtGui.QTableView(self.layoutWidget)
        self.requestHeadersList.setAlternatingRowColors(True)
        self.requestHeadersList.setShowGrid(False)
        self.requestHeadersList.setSortingEnabled(False)
        self.requestHeadersList.setObjectName(_fromUtf8("requestHeadersList"))
        self.verticalLayout.addWidget(self.requestHeadersList)
        self.layoutWidget1 = QtGui.QWidget(self.splitter)
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_3 = QtGui.QLabel(self.layoutWidget1)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_2.addWidget(self.label_3)
        self.responseHeadersList = QtGui.QTableView(self.layoutWidget1)
        self.responseHeadersList.setAlternatingRowColors(True)
        self.responseHeadersList.setShowGrid(False)
        self.responseHeadersList.setSortingEnabled(False)
        self.responseHeadersList.setObjectName(_fromUtf8("responseHeadersList"))
        self.verticalLayout_2.addWidget(self.responseHeadersList)
        self.verticalLayout_3.addWidget(self.splitter)
        self.buttonBox = QtGui.QDialogButtonBox(E4NetworkMonitor)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_3.addWidget(self.buttonBox)

        self.retranslateUi(E4NetworkMonitor)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), E4NetworkMonitor.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), E4NetworkMonitor.reject)
        QtCore.QObject.connect(self.clearButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.searchEdit.clear)
        QtCore.QMetaObject.connectSlotsByName(E4NetworkMonitor)
        E4NetworkMonitor.setTabOrder(self.searchEdit, self.clearButton)
        E4NetworkMonitor.setTabOrder(self.clearButton, self.requestsList)
        E4NetworkMonitor.setTabOrder(self.requestsList, self.removeButton)
        E4NetworkMonitor.setTabOrder(self.removeButton, self.removeAllButton)
        E4NetworkMonitor.setTabOrder(self.removeAllButton, self.requestHeadersList)
        E4NetworkMonitor.setTabOrder(self.requestHeadersList, self.responseHeadersList)
        E4NetworkMonitor.setTabOrder(self.responseHeadersList, self.buttonBox)

    def retranslateUi(self, E4NetworkMonitor):
        E4NetworkMonitor.setWindowTitle(_translate("E4NetworkMonitor", "Network Monitor", None))
        self.label.setText(_translate("E4NetworkMonitor", "Network Requests", None))
        self.searchEdit.setToolTip(_translate("E4NetworkMonitor", "Enter search term for requests", None))
        self.clearButton.setText(_translate("E4NetworkMonitor", "...", None))
        self.removeButton.setToolTip(_translate("E4NetworkMonitor", "Press to remove the selected requests", None))
        self.removeButton.setText(_translate("E4NetworkMonitor", "&Remove", None))
        self.removeAllButton.setToolTip(_translate("E4NetworkMonitor", "Press to remove all requests", None))
        self.removeAllButton.setText(_translate("E4NetworkMonitor", "Remove &All", None))
        self.label_2.setText(_translate("E4NetworkMonitor", "Request Headers", None))
        self.label_3.setText(_translate("E4NetworkMonitor", "Response Headers", None))

from E4Gui.E4TableView import E4TableView
