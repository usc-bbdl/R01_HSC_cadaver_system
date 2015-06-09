# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Preferences\ConfigurationPages\EditorHighlightersPage.ui'
#
# Created: Fri Apr 18 09:56:42 2014
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

class Ui_EditorHighlightersPage(object):
    def setupUi(self, EditorHighlightersPage):
        EditorHighlightersPage.setObjectName(_fromUtf8("EditorHighlightersPage"))
        EditorHighlightersPage.resize(400, 361)
        self.verticalLayout = QtGui.QVBoxLayout(EditorHighlightersPage)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.headerLabel = QtGui.QLabel(EditorHighlightersPage)
        self.headerLabel.setObjectName(_fromUtf8("headerLabel"))
        self.verticalLayout.addWidget(self.headerLabel)
        self.line19 = QtGui.QFrame(EditorHighlightersPage)
        self.line19.setFrameShape(QtGui.QFrame.HLine)
        self.line19.setFrameShadow(QtGui.QFrame.Sunken)
        self.line19.setFrameShape(QtGui.QFrame.HLine)
        self.line19.setFrameShadow(QtGui.QFrame.Sunken)
        self.line19.setObjectName(_fromUtf8("line19"))
        self.verticalLayout.addWidget(self.line19)
        self.editorLexerList = QtGui.QTreeWidget(EditorHighlightersPage)
        self.editorLexerList.setAlternatingRowColors(True)
        self.editorLexerList.setRootIsDecorated(False)
        self.editorLexerList.setObjectName(_fromUtf8("editorLexerList"))
        self.verticalLayout.addWidget(self.editorLexerList)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.textLabel2_6 = QtGui.QLabel(EditorHighlightersPage)
        self.textLabel2_6.setObjectName(_fromUtf8("textLabel2_6"))
        self.gridLayout.addWidget(self.textLabel2_6, 0, 0, 1, 1)
        self.editorFileExtEdit = QtGui.QLineEdit(EditorHighlightersPage)
        self.editorFileExtEdit.setObjectName(_fromUtf8("editorFileExtEdit"))
        self.gridLayout.addWidget(self.editorFileExtEdit, 0, 1, 1, 1)
        self.addLexerButton = QtGui.QPushButton(EditorHighlightersPage)
        self.addLexerButton.setObjectName(_fromUtf8("addLexerButton"))
        self.gridLayout.addWidget(self.addLexerButton, 0, 2, 1, 1)
        self.textLabel3_3 = QtGui.QLabel(EditorHighlightersPage)
        self.textLabel3_3.setObjectName(_fromUtf8("textLabel3_3"))
        self.gridLayout.addWidget(self.textLabel3_3, 1, 0, 1, 1)
        self.editorLexerCombo = QtGui.QComboBox(EditorHighlightersPage)
        self.editorLexerCombo.setObjectName(_fromUtf8("editorLexerCombo"))
        self.gridLayout.addWidget(self.editorLexerCombo, 1, 1, 1, 1)
        self.deleteLexerButton = QtGui.QPushButton(EditorHighlightersPage)
        self.deleteLexerButton.setObjectName(_fromUtf8("deleteLexerButton"))
        self.gridLayout.addWidget(self.deleteLexerButton, 1, 2, 1, 1)
        self.pygmentsLabel = QtGui.QLabel(EditorHighlightersPage)
        self.pygmentsLabel.setObjectName(_fromUtf8("pygmentsLabel"))
        self.gridLayout.addWidget(self.pygmentsLabel, 2, 0, 1, 1)
        self.pygmentsLexerCombo = QtGui.QComboBox(EditorHighlightersPage)
        self.pygmentsLexerCombo.setObjectName(_fromUtf8("pygmentsLexerCombo"))
        self.gridLayout.addWidget(self.pygmentsLexerCombo, 2, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(EditorHighlightersPage)
        QtCore.QMetaObject.connectSlotsByName(EditorHighlightersPage)
        EditorHighlightersPage.setTabOrder(self.editorLexerList, self.editorFileExtEdit)
        EditorHighlightersPage.setTabOrder(self.editorFileExtEdit, self.editorLexerCombo)
        EditorHighlightersPage.setTabOrder(self.editorLexerCombo, self.pygmentsLexerCombo)
        EditorHighlightersPage.setTabOrder(self.pygmentsLexerCombo, self.addLexerButton)
        EditorHighlightersPage.setTabOrder(self.addLexerButton, self.deleteLexerButton)

    def retranslateUi(self, EditorHighlightersPage):
        self.headerLabel.setText(_translate("EditorHighlightersPage", "<b>Configure syntax highlighters</b>", None))
        self.editorLexerList.setSortingEnabled(True)
        self.editorLexerList.headerItem().setText(0, _translate("EditorHighlightersPage", "Filename Pattern", None))
        self.editorLexerList.headerItem().setText(1, _translate("EditorHighlightersPage", "Lexer Language", None))
        self.textLabel2_6.setText(_translate("EditorHighlightersPage", "Filename Pattern:", None))
        self.editorFileExtEdit.setToolTip(_translate("EditorHighlightersPage", "Enter the filename pattern to be associated", None))
        self.addLexerButton.setToolTip(_translate("EditorHighlightersPage", "Press to add or change the entered association", None))
        self.addLexerButton.setText(_translate("EditorHighlightersPage", "Add/Change", None))
        self.textLabel3_3.setText(_translate("EditorHighlightersPage", "Lexer Language:", None))
        self.editorLexerCombo.setToolTip(_translate("EditorHighlightersPage", "Select the lexer language to associate", None))
        self.deleteLexerButton.setToolTip(_translate("EditorHighlightersPage", "Press to delete the selected association", None))
        self.deleteLexerButton.setText(_translate("EditorHighlightersPage", "Delete", None))
        self.pygmentsLabel.setText(_translate("EditorHighlightersPage", "Alternative Lexer:", None))
        self.pygmentsLexerCombo.setToolTip(_translate("EditorHighlightersPage", "Select the alternative lexer to associate", None))

