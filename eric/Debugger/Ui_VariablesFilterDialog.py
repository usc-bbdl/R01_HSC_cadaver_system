# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Debugger\VariablesFilterDialog.ui'
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

class Ui_VariablesFilterDialog(object):
    def setupUi(self, VariablesFilterDialog):
        VariablesFilterDialog.setObjectName(_fromUtf8("VariablesFilterDialog"))
        VariablesFilterDialog.resize(386, 338)
        VariablesFilterDialog.setSizeGripEnabled(True)
        self.gridlayout = QtGui.QGridLayout(VariablesFilterDialog)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.buttonBox = QtGui.QDialogButtonBox(VariablesFilterDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridlayout.addWidget(self.buttonBox, 2, 0, 1, 2)
        self.localsLabel = QtGui.QLabel(VariablesFilterDialog)
        self.localsLabel.setObjectName(_fromUtf8("localsLabel"))
        self.gridlayout.addWidget(self.localsLabel, 0, 0, 1, 1)
        self.globalsLabel = QtGui.QLabel(VariablesFilterDialog)
        self.globalsLabel.setObjectName(_fromUtf8("globalsLabel"))
        self.gridlayout.addWidget(self.globalsLabel, 0, 1, 1, 1)
        self.localsList = QtGui.QListWidget(VariablesFilterDialog)
        self.localsList.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.localsList.setObjectName(_fromUtf8("localsList"))
        self.gridlayout.addWidget(self.localsList, 1, 0, 1, 1)
        self.globalsList = QtGui.QListWidget(VariablesFilterDialog)
        self.globalsList.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.globalsList.setObjectName(_fromUtf8("globalsList"))
        self.gridlayout.addWidget(self.globalsList, 1, 1, 1, 1)
        self.localsLabel.setBuddy(self.localsList)
        self.globalsLabel.setBuddy(self.globalsList)

        self.retranslateUi(VariablesFilterDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), VariablesFilterDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), VariablesFilterDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(VariablesFilterDialog)
        VariablesFilterDialog.setTabOrder(self.localsList, self.globalsList)

    def retranslateUi(self, VariablesFilterDialog):
        VariablesFilterDialog.setWindowTitle(_translate("VariablesFilterDialog", "Variables Type Filter", None))
        VariablesFilterDialog.setWhatsThis(_translate("VariablesFilterDialog", "<b>Filter Dialog</b>\n"
"<p> This dialog gives the user the possibility to select what kind of variables should <b>not</b> be shown during a debugging session.</p>", None))
        self.localsLabel.setText(_translate("VariablesFilterDialog", "&Locals Filter", None))
        self.globalsLabel.setText(_translate("VariablesFilterDialog", "&Globals Filter", None))
        self.localsList.setToolTip(_translate("VariablesFilterDialog", "Locals Filter List", None))
        self.localsList.setWhatsThis(_translate("VariablesFilterDialog", "<b>Locals Filter List</b>\n"
"<p>Select the variable types you want to be filtered out of the locals variables list.</p<", None))
        self.globalsList.setToolTip(_translate("VariablesFilterDialog", "Globals Filter List", None))
        self.globalsList.setWhatsThis(_translate("VariablesFilterDialog", "<b>Globals Filter List</b>\n"
"<p>Select the variable types you want to be filtered out of the globals variables list.</p<", None))

