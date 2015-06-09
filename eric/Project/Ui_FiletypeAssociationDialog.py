# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Project\FiletypeAssociationDialog.ui'
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

class Ui_FiletypeAssociationDialog(object):
    def setupUi(self, FiletypeAssociationDialog):
        FiletypeAssociationDialog.setObjectName(_fromUtf8("FiletypeAssociationDialog"))
        FiletypeAssociationDialog.resize(600, 573)
        FiletypeAssociationDialog.setSizeGripEnabled(True)
        self._2 = QtGui.QVBoxLayout(FiletypeAssociationDialog)
        self._2.setObjectName(_fromUtf8("_2"))
        self.filetypeAssociationList = QtGui.QTreeWidget(FiletypeAssociationDialog)
        self.filetypeAssociationList.setAlternatingRowColors(True)
        self.filetypeAssociationList.setRootIsDecorated(False)
        self.filetypeAssociationList.setItemsExpandable(False)
        self.filetypeAssociationList.setObjectName(_fromUtf8("filetypeAssociationList"))
        self._2.addWidget(self.filetypeAssociationList)
        self._3 = QtGui.QGridLayout()
        self._3.setObjectName(_fromUtf8("_3"))
        self.deleteAssociationButton = QtGui.QPushButton(FiletypeAssociationDialog)
        self.deleteAssociationButton.setEnabled(False)
        self.deleteAssociationButton.setObjectName(_fromUtf8("deleteAssociationButton"))
        self._3.addWidget(self.deleteAssociationButton, 1, 2, 1, 1)
        self.filetypeCombo = QtGui.QComboBox(FiletypeAssociationDialog)
        self.filetypeCombo.setObjectName(_fromUtf8("filetypeCombo"))
        self._3.addWidget(self.filetypeCombo, 1, 1, 1, 1)
        self.textLabel3_3 = QtGui.QLabel(FiletypeAssociationDialog)
        self.textLabel3_3.setObjectName(_fromUtf8("textLabel3_3"))
        self._3.addWidget(self.textLabel3_3, 1, 0, 1, 1)
        self.filePatternEdit = QtGui.QLineEdit(FiletypeAssociationDialog)
        self.filePatternEdit.setObjectName(_fromUtf8("filePatternEdit"))
        self._3.addWidget(self.filePatternEdit, 0, 1, 1, 1)
        self.textLabel2_6 = QtGui.QLabel(FiletypeAssociationDialog)
        self.textLabel2_6.setObjectName(_fromUtf8("textLabel2_6"))
        self._3.addWidget(self.textLabel2_6, 0, 0, 1, 1)
        self.addAssociationButton = QtGui.QPushButton(FiletypeAssociationDialog)
        self.addAssociationButton.setEnabled(False)
        self.addAssociationButton.setObjectName(_fromUtf8("addAssociationButton"))
        self._3.addWidget(self.addAssociationButton, 0, 2, 1, 1)
        self._2.addLayout(self._3)
        self.buttonBox = QtGui.QDialogButtonBox(FiletypeAssociationDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self._2.addWidget(self.buttonBox)

        self.retranslateUi(FiletypeAssociationDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), FiletypeAssociationDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), FiletypeAssociationDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(FiletypeAssociationDialog)
        FiletypeAssociationDialog.setTabOrder(self.filetypeAssociationList, self.filePatternEdit)
        FiletypeAssociationDialog.setTabOrder(self.filePatternEdit, self.filetypeCombo)
        FiletypeAssociationDialog.setTabOrder(self.filetypeCombo, self.addAssociationButton)
        FiletypeAssociationDialog.setTabOrder(self.addAssociationButton, self.deleteAssociationButton)

    def retranslateUi(self, FiletypeAssociationDialog):
        FiletypeAssociationDialog.setWindowTitle(_translate("FiletypeAssociationDialog", "Filetype Associations", None))
        self.filetypeAssociationList.setSortingEnabled(True)
        self.filetypeAssociationList.headerItem().setText(0, _translate("FiletypeAssociationDialog", "Filename Pattern", None))
        self.filetypeAssociationList.headerItem().setText(1, _translate("FiletypeAssociationDialog", "Filetype", None))
        self.deleteAssociationButton.setToolTip(_translate("FiletypeAssociationDialog", "Press to delete the selected association", None))
        self.deleteAssociationButton.setText(_translate("FiletypeAssociationDialog", "Delete", None))
        self.filetypeCombo.setToolTip(_translate("FiletypeAssociationDialog", "Select the filetype to associate", None))
        self.textLabel3_3.setText(_translate("FiletypeAssociationDialog", "Filetype:", None))
        self.filePatternEdit.setToolTip(_translate("FiletypeAssociationDialog", "Enter the filename pattern to be associated", None))
        self.textLabel2_6.setText(_translate("FiletypeAssociationDialog", "Filename Pattern:", None))
        self.addAssociationButton.setToolTip(_translate("FiletypeAssociationDialog", "Press to add or change the entered association", None))
        self.addAssociationButton.setText(_translate("FiletypeAssociationDialog", "Add/Change", None))

