# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Project\LexerAssociationDialog.ui'
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

class Ui_LexerAssociationDialog(object):
    def setupUi(self, LexerAssociationDialog):
        LexerAssociationDialog.setObjectName(_fromUtf8("LexerAssociationDialog"))
        LexerAssociationDialog.resize(460, 418)
        LexerAssociationDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtGui.QVBoxLayout(LexerAssociationDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.editorLexerList = QtGui.QTreeWidget(LexerAssociationDialog)
        self.editorLexerList.setAlternatingRowColors(True)
        self.editorLexerList.setRootIsDecorated(False)
        self.editorLexerList.setObjectName(_fromUtf8("editorLexerList"))
        self.verticalLayout.addWidget(self.editorLexerList)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.textLabel2_6 = QtGui.QLabel(LexerAssociationDialog)
        self.textLabel2_6.setObjectName(_fromUtf8("textLabel2_6"))
        self.gridLayout.addWidget(self.textLabel2_6, 0, 0, 1, 1)
        self.editorFileExtEdit = QtGui.QLineEdit(LexerAssociationDialog)
        self.editorFileExtEdit.setObjectName(_fromUtf8("editorFileExtEdit"))
        self.gridLayout.addWidget(self.editorFileExtEdit, 0, 1, 1, 1)
        self.addLexerButton = QtGui.QPushButton(LexerAssociationDialog)
        self.addLexerButton.setObjectName(_fromUtf8("addLexerButton"))
        self.gridLayout.addWidget(self.addLexerButton, 0, 2, 1, 1)
        self.textLabel3_3 = QtGui.QLabel(LexerAssociationDialog)
        self.textLabel3_3.setObjectName(_fromUtf8("textLabel3_3"))
        self.gridLayout.addWidget(self.textLabel3_3, 1, 0, 1, 1)
        self.editorLexerCombo = QtGui.QComboBox(LexerAssociationDialog)
        self.editorLexerCombo.setObjectName(_fromUtf8("editorLexerCombo"))
        self.gridLayout.addWidget(self.editorLexerCombo, 1, 1, 1, 1)
        self.deleteLexerButton = QtGui.QPushButton(LexerAssociationDialog)
        self.deleteLexerButton.setObjectName(_fromUtf8("deleteLexerButton"))
        self.gridLayout.addWidget(self.deleteLexerButton, 1, 2, 1, 1)
        self.pygmentsLabel = QtGui.QLabel(LexerAssociationDialog)
        self.pygmentsLabel.setObjectName(_fromUtf8("pygmentsLabel"))
        self.gridLayout.addWidget(self.pygmentsLabel, 2, 0, 1, 1)
        self.pygmentsLexerCombo = QtGui.QComboBox(LexerAssociationDialog)
        self.pygmentsLexerCombo.setObjectName(_fromUtf8("pygmentsLexerCombo"))
        self.gridLayout.addWidget(self.pygmentsLexerCombo, 2, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.buttonBox = QtGui.QDialogButtonBox(LexerAssociationDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        self.textLabel2_6.setBuddy(self.editorFileExtEdit)
        self.textLabel3_3.setBuddy(self.editorLexerCombo)
        self.pygmentsLabel.setBuddy(self.pygmentsLexerCombo)

        self.retranslateUi(LexerAssociationDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), LexerAssociationDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), LexerAssociationDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(LexerAssociationDialog)
        LexerAssociationDialog.setTabOrder(self.editorLexerList, self.editorFileExtEdit)
        LexerAssociationDialog.setTabOrder(self.editorFileExtEdit, self.editorLexerCombo)
        LexerAssociationDialog.setTabOrder(self.editorLexerCombo, self.pygmentsLexerCombo)
        LexerAssociationDialog.setTabOrder(self.pygmentsLexerCombo, self.addLexerButton)
        LexerAssociationDialog.setTabOrder(self.addLexerButton, self.deleteLexerButton)
        LexerAssociationDialog.setTabOrder(self.deleteLexerButton, self.buttonBox)

    def retranslateUi(self, LexerAssociationDialog):
        LexerAssociationDialog.setWindowTitle(_translate("LexerAssociationDialog", "Project Lexer Associations", None))
        self.editorLexerList.setSortingEnabled(True)
        self.editorLexerList.headerItem().setText(0, _translate("LexerAssociationDialog", "Filename Pattern", None))
        self.editorLexerList.headerItem().setText(1, _translate("LexerAssociationDialog", "Lexer Language", None))
        self.textLabel2_6.setText(_translate("LexerAssociationDialog", "Filename &Pattern:", None))
        self.editorFileExtEdit.setToolTip(_translate("LexerAssociationDialog", "Enter the filename pattern to be associated", None))
        self.addLexerButton.setToolTip(_translate("LexerAssociationDialog", "Press to add or change the entered association", None))
        self.addLexerButton.setText(_translate("LexerAssociationDialog", "Add/&Change", None))
        self.textLabel3_3.setText(_translate("LexerAssociationDialog", "&Lexer Language:", None))
        self.editorLexerCombo.setToolTip(_translate("LexerAssociationDialog", "Select the lexer language to associate", None))
        self.deleteLexerButton.setToolTip(_translate("LexerAssociationDialog", "Press to delete the selected association", None))
        self.deleteLexerButton.setText(_translate("LexerAssociationDialog", "&Delete", None))
        self.pygmentsLabel.setText(_translate("LexerAssociationDialog", "Alternative Le&xer:", None))
        self.pygmentsLexerCombo.setToolTip(_translate("LexerAssociationDialog", "Select the alternative lexer to associate", None))

