# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Helpviewer\QtHelpFiltersDialog.ui'
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

class Ui_QtHelpFiltersDialog(object):
    def setupUi(self, QtHelpFiltersDialog):
        QtHelpFiltersDialog.setObjectName(_fromUtf8("QtHelpFiltersDialog"))
        QtHelpFiltersDialog.resize(570, 391)
        QtHelpFiltersDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtGui.QVBoxLayout(QtHelpFiltersDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(QtHelpFiltersDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(QtHelpFiltersDialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.filtersList = QtGui.QListWidget(QtHelpFiltersDialog)
        self.filtersList.setObjectName(_fromUtf8("filtersList"))
        self.gridLayout.addWidget(self.filtersList, 1, 0, 1, 2)
        self.attributesList = QtGui.QTreeWidget(QtHelpFiltersDialog)
        self.attributesList.setRootIsDecorated(False)
        self.attributesList.setObjectName(_fromUtf8("attributesList"))
        self.gridLayout.addWidget(self.attributesList, 1, 2, 1, 1)
        self.addButton = QtGui.QPushButton(QtHelpFiltersDialog)
        self.addButton.setObjectName(_fromUtf8("addButton"))
        self.gridLayout.addWidget(self.addButton, 2, 0, 1, 1)
        self.removeButton = QtGui.QPushButton(QtHelpFiltersDialog)
        self.removeButton.setObjectName(_fromUtf8("removeButton"))
        self.gridLayout.addWidget(self.removeButton, 2, 1, 1, 1)
        self.removeAttributeButton = QtGui.QPushButton(QtHelpFiltersDialog)
        self.removeAttributeButton.setObjectName(_fromUtf8("removeAttributeButton"))
        self.gridLayout.addWidget(self.removeAttributeButton, 2, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.buttonBox = QtGui.QDialogButtonBox(QtHelpFiltersDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(QtHelpFiltersDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), QtHelpFiltersDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(QtHelpFiltersDialog)
        QtHelpFiltersDialog.setTabOrder(self.filtersList, self.attributesList)
        QtHelpFiltersDialog.setTabOrder(self.attributesList, self.addButton)
        QtHelpFiltersDialog.setTabOrder(self.addButton, self.removeButton)
        QtHelpFiltersDialog.setTabOrder(self.removeButton, self.removeAttributeButton)
        QtHelpFiltersDialog.setTabOrder(self.removeAttributeButton, self.buttonBox)

    def retranslateUi(self, QtHelpFiltersDialog):
        QtHelpFiltersDialog.setWindowTitle(_translate("QtHelpFiltersDialog", "Manage QtHelp Filters", None))
        self.label.setText(_translate("QtHelpFiltersDialog", "Filters:", None))
        self.label_2.setText(_translate("QtHelpFiltersDialog", "Attributes:", None))
        self.attributesList.headerItem().setText(0, _translate("QtHelpFiltersDialog", "1", None))
        self.addButton.setToolTip(_translate("QtHelpFiltersDialog", "Press to add a new filter", None))
        self.addButton.setText(_translate("QtHelpFiltersDialog", "Add Filter ...", None))
        self.removeButton.setToolTip(_translate("QtHelpFiltersDialog", "Press to remove the selected filter", None))
        self.removeButton.setText(_translate("QtHelpFiltersDialog", "Remove Filter", None))
        self.removeAttributeButton.setToolTip(_translate("QtHelpFiltersDialog", "Press to remove the selected attribute", None))
        self.removeAttributeButton.setText(_translate("QtHelpFiltersDialog", "Remove Attribute", None))

