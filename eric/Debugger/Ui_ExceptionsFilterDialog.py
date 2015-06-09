# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Debugger\ExceptionsFilterDialog.ui'
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

class Ui_ExceptionsFilterDialog(object):
    def setupUi(self, ExceptionsFilterDialog):
        ExceptionsFilterDialog.setObjectName(_fromUtf8("ExceptionsFilterDialog"))
        ExceptionsFilterDialog.resize(464, 385)
        ExceptionsFilterDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtGui.QVBoxLayout(ExceptionsFilterDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.exceptionList = QtGui.QListWidget(ExceptionsFilterDialog)
        self.exceptionList.setAlternatingRowColors(True)
        self.exceptionList.setObjectName(_fromUtf8("exceptionList"))
        self.verticalLayout.addWidget(self.exceptionList)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.addButton = QtGui.QPushButton(ExceptionsFilterDialog)
        self.addButton.setEnabled(False)
        self.addButton.setObjectName(_fromUtf8("addButton"))
        self.horizontalLayout.addWidget(self.addButton)
        self.exceptionEdit = QtGui.QLineEdit(ExceptionsFilterDialog)
        self.exceptionEdit.setObjectName(_fromUtf8("exceptionEdit"))
        self.horizontalLayout.addWidget(self.exceptionEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.deleteButton = QtGui.QPushButton(ExceptionsFilterDialog)
        self.deleteButton.setEnabled(False)
        self.deleteButton.setObjectName(_fromUtf8("deleteButton"))
        self.horizontalLayout_2.addWidget(self.deleteButton)
        self.deleteAllButton = QtGui.QPushButton(ExceptionsFilterDialog)
        self.deleteAllButton.setObjectName(_fromUtf8("deleteAllButton"))
        self.horizontalLayout_2.addWidget(self.deleteAllButton)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.buttonBox = QtGui.QDialogButtonBox(ExceptionsFilterDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(ExceptionsFilterDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ExceptionsFilterDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ExceptionsFilterDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ExceptionsFilterDialog)
        ExceptionsFilterDialog.setTabOrder(self.exceptionList, self.exceptionEdit)
        ExceptionsFilterDialog.setTabOrder(self.exceptionEdit, self.addButton)
        ExceptionsFilterDialog.setTabOrder(self.addButton, self.deleteButton)
        ExceptionsFilterDialog.setTabOrder(self.deleteButton, self.deleteAllButton)
        ExceptionsFilterDialog.setTabOrder(self.deleteAllButton, self.buttonBox)

    def retranslateUi(self, ExceptionsFilterDialog):
        ExceptionsFilterDialog.setWindowTitle(_translate("ExceptionsFilterDialog", "Exceptions Filter", None))
        ExceptionsFilterDialog.setWhatsThis(_translate("ExceptionsFilterDialog", "<b>Exception Filter</b>\n"
"<p>This dialog is used to enter the exception types, that shall be highlighted during a debugging session. If this list is empty, all exception types will be highlighted. If the exception reporting flag in the \"Start Debugging\" dialog is unchecked, no exception will be reported at all.</p>\n"
"<p>Please note, that unhandled exceptions are always highlighted independent of these settings.</p>", None))
        self.exceptionList.setToolTip(_translate("ExceptionsFilterDialog", "List of exceptions that shall be highlighted", None))
        self.addButton.setToolTip(_translate("ExceptionsFilterDialog", "Press to add the entered exception to the list", None))
        self.addButton.setText(_translate("ExceptionsFilterDialog", "Add", None))
        self.exceptionEdit.setToolTip(_translate("ExceptionsFilterDialog", "Enter an exception type that shall be highlighted", None))
        self.deleteButton.setToolTip(_translate("ExceptionsFilterDialog", "Press to delete the selected exception from the list", None))
        self.deleteButton.setText(_translate("ExceptionsFilterDialog", "Delete", None))
        self.deleteAllButton.setToolTip(_translate("ExceptionsFilterDialog", "Press to delete all exceptions from the list", None))
        self.deleteAllButton.setText(_translate("ExceptionsFilterDialog", "Delete All", None))

