# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Helpviewer\HelpLanguagesDialog.ui'
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

class Ui_HelpLanguagesDialog(object):
    def setupUi(self, HelpLanguagesDialog):
        HelpLanguagesDialog.setObjectName(_fromUtf8("HelpLanguagesDialog"))
        HelpLanguagesDialog.resize(400, 300)
        self.gridLayout = QtGui.QGridLayout(HelpLanguagesDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(HelpLanguagesDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.languagesList = QtGui.QListView(HelpLanguagesDialog)
        self.languagesList.setObjectName(_fromUtf8("languagesList"))
        self.gridLayout.addWidget(self.languagesList, 1, 0, 4, 1)
        self.upButton = QtGui.QPushButton(HelpLanguagesDialog)
        self.upButton.setObjectName(_fromUtf8("upButton"))
        self.gridLayout.addWidget(self.upButton, 1, 1, 1, 1)
        self.downButton = QtGui.QPushButton(HelpLanguagesDialog)
        self.downButton.setObjectName(_fromUtf8("downButton"))
        self.gridLayout.addWidget(self.downButton, 2, 1, 1, 1)
        self.removeButton = QtGui.QPushButton(HelpLanguagesDialog)
        self.removeButton.setObjectName(_fromUtf8("removeButton"))
        self.gridLayout.addWidget(self.removeButton, 3, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 77, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 4, 1, 1, 1)
        self.addCombo = QtGui.QComboBox(HelpLanguagesDialog)
        self.addCombo.setObjectName(_fromUtf8("addCombo"))
        self.gridLayout.addWidget(self.addCombo, 5, 0, 1, 1)
        self.addButton = QtGui.QPushButton(HelpLanguagesDialog)
        self.addButton.setObjectName(_fromUtf8("addButton"))
        self.gridLayout.addWidget(self.addButton, 5, 1, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(HelpLanguagesDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 6, 0, 1, 2)

        self.retranslateUi(HelpLanguagesDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), HelpLanguagesDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), HelpLanguagesDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(HelpLanguagesDialog)
        HelpLanguagesDialog.setTabOrder(self.languagesList, self.upButton)
        HelpLanguagesDialog.setTabOrder(self.upButton, self.downButton)
        HelpLanguagesDialog.setTabOrder(self.downButton, self.removeButton)
        HelpLanguagesDialog.setTabOrder(self.removeButton, self.addCombo)
        HelpLanguagesDialog.setTabOrder(self.addCombo, self.addButton)
        HelpLanguagesDialog.setTabOrder(self.addButton, self.buttonBox)

    def retranslateUi(self, HelpLanguagesDialog):
        HelpLanguagesDialog.setWindowTitle(_translate("HelpLanguagesDialog", "Languages", None))
        self.label.setText(_translate("HelpLanguagesDialog", "Languages in order of preference:", None))
        self.upButton.setText(_translate("HelpLanguagesDialog", "&Up", None))
        self.downButton.setText(_translate("HelpLanguagesDialog", "&Down", None))
        self.removeButton.setText(_translate("HelpLanguagesDialog", "&Remove", None))
        self.addButton.setText(_translate("HelpLanguagesDialog", "&Add", None))

