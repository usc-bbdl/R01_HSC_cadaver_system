# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Plugins\WizardPlugins\QRegExpWizard\QRegExpWizardDialog.ui'
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

class Ui_QRegExpWizardDialog(object):
    def setupUi(self, QRegExpWizardDialog):
        QRegExpWizardDialog.setObjectName(_fromUtf8("QRegExpWizardDialog"))
        QRegExpWizardDialog.resize(749, 600)
        QRegExpWizardDialog.setProperty("sizeGripEnabled", True)
        self.vboxlayout = QtGui.QVBoxLayout(QRegExpWizardDialog)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        self.variableLabel = QtGui.QLabel(QRegExpWizardDialog)
        self.variableLabel.setObjectName(_fromUtf8("variableLabel"))
        self.hboxlayout.addWidget(self.variableLabel)
        self.variableLineEdit = QtGui.QLineEdit(QRegExpWizardDialog)
        self.variableLineEdit.setObjectName(_fromUtf8("variableLineEdit"))
        self.hboxlayout.addWidget(self.variableLineEdit)
        self.vboxlayout.addLayout(self.hboxlayout)
        self.variableLine = QtGui.QFrame(QRegExpWizardDialog)
        self.variableLine.setFrameShape(QtGui.QFrame.HLine)
        self.variableLine.setFrameShadow(QtGui.QFrame.Sunken)
        self.variableLine.setObjectName(_fromUtf8("variableLine"))
        self.vboxlayout.addWidget(self.variableLine)
        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setObjectName(_fromUtf8("hboxlayout1"))
        self.charButton = QtGui.QToolButton(QRegExpWizardDialog)
        self.charButton.setObjectName(_fromUtf8("charButton"))
        self.hboxlayout1.addWidget(self.charButton)
        self.anycharButton = QtGui.QToolButton(QRegExpWizardDialog)
        self.anycharButton.setObjectName(_fromUtf8("anycharButton"))
        self.hboxlayout1.addWidget(self.anycharButton)
        self.repeatButton = QtGui.QToolButton(QRegExpWizardDialog)
        self.repeatButton.setObjectName(_fromUtf8("repeatButton"))
        self.hboxlayout1.addWidget(self.repeatButton)
        self.nonGroupButton = QtGui.QToolButton(QRegExpWizardDialog)
        self.nonGroupButton.setObjectName(_fromUtf8("nonGroupButton"))
        self.hboxlayout1.addWidget(self.nonGroupButton)
        self.groupButton = QtGui.QToolButton(QRegExpWizardDialog)
        self.groupButton.setObjectName(_fromUtf8("groupButton"))
        self.hboxlayout1.addWidget(self.groupButton)
        self.altnButton = QtGui.QToolButton(QRegExpWizardDialog)
        self.altnButton.setObjectName(_fromUtf8("altnButton"))
        self.hboxlayout1.addWidget(self.altnButton)
        self.beglineButton = QtGui.QToolButton(QRegExpWizardDialog)
        self.beglineButton.setObjectName(_fromUtf8("beglineButton"))
        self.hboxlayout1.addWidget(self.beglineButton)
        self.endlineButton = QtGui.QToolButton(QRegExpWizardDialog)
        self.endlineButton.setObjectName(_fromUtf8("endlineButton"))
        self.hboxlayout1.addWidget(self.endlineButton)
        self.wordboundButton = QtGui.QToolButton(QRegExpWizardDialog)
        self.wordboundButton.setObjectName(_fromUtf8("wordboundButton"))
        self.hboxlayout1.addWidget(self.wordboundButton)
        self.nonwordboundButton = QtGui.QToolButton(QRegExpWizardDialog)
        self.nonwordboundButton.setObjectName(_fromUtf8("nonwordboundButton"))
        self.hboxlayout1.addWidget(self.nonwordboundButton)
        self.poslookaheadButton = QtGui.QToolButton(QRegExpWizardDialog)
        self.poslookaheadButton.setObjectName(_fromUtf8("poslookaheadButton"))
        self.hboxlayout1.addWidget(self.poslookaheadButton)
        self.neglookaheadButton = QtGui.QToolButton(QRegExpWizardDialog)
        self.neglookaheadButton.setObjectName(_fromUtf8("neglookaheadButton"))
        self.hboxlayout1.addWidget(self.neglookaheadButton)
        spacerItem = QtGui.QSpacerItem(16, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.hboxlayout1.addItem(spacerItem)
        self.undoButton = QtGui.QToolButton(QRegExpWizardDialog)
        self.undoButton.setObjectName(_fromUtf8("undoButton"))
        self.hboxlayout1.addWidget(self.undoButton)
        self.redoButton = QtGui.QToolButton(QRegExpWizardDialog)
        self.redoButton.setObjectName(_fromUtf8("redoButton"))
        self.hboxlayout1.addWidget(self.redoButton)
        spacerItem1 = QtGui.QSpacerItem(81, 24, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout1.addItem(spacerItem1)
        self.vboxlayout.addLayout(self.hboxlayout1)
        self.gridlayout = QtGui.QGridLayout()
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.textLabel1 = QtGui.QLabel(QRegExpWizardDialog)
        self.textLabel1.setObjectName(_fromUtf8("textLabel1"))
        self.gridlayout.addWidget(self.textLabel1, 0, 0, 1, 1)
        self.textLabel2 = QtGui.QLabel(QRegExpWizardDialog)
        self.textLabel2.setAlignment(QtCore.Qt.AlignTop)
        self.textLabel2.setObjectName(_fromUtf8("textLabel2"))
        self.gridlayout.addWidget(self.textLabel2, 1, 0, 1, 1)
        self.regexpLineEdit = QtGui.QLineEdit(QRegExpWizardDialog)
        self.regexpLineEdit.setObjectName(_fromUtf8("regexpLineEdit"))
        self.gridlayout.addWidget(self.regexpLineEdit, 0, 1, 1, 1)
        self.textTextEdit = QtGui.QTextEdit(QRegExpWizardDialog)
        self.textTextEdit.setObjectName(_fromUtf8("textTextEdit"))
        self.gridlayout.addWidget(self.textTextEdit, 1, 1, 1, 1)
        self.vboxlayout.addLayout(self.gridlayout)
        self.hboxlayout2 = QtGui.QHBoxLayout()
        self.hboxlayout2.setObjectName(_fromUtf8("hboxlayout2"))
        self.caseSensitiveCheckBox = QtGui.QCheckBox(QRegExpWizardDialog)
        self.caseSensitiveCheckBox.setChecked(True)
        self.caseSensitiveCheckBox.setObjectName(_fromUtf8("caseSensitiveCheckBox"))
        self.hboxlayout2.addWidget(self.caseSensitiveCheckBox)
        self.minimalCheckBox = QtGui.QCheckBox(QRegExpWizardDialog)
        self.minimalCheckBox.setObjectName(_fromUtf8("minimalCheckBox"))
        self.hboxlayout2.addWidget(self.minimalCheckBox)
        self.wildcardCheckBox = QtGui.QCheckBox(QRegExpWizardDialog)
        self.wildcardCheckBox.setObjectName(_fromUtf8("wildcardCheckBox"))
        self.hboxlayout2.addWidget(self.wildcardCheckBox)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout2.addItem(spacerItem2)
        self.vboxlayout.addLayout(self.hboxlayout2)
        self.resultTable = QtGui.QTableWidget(QRegExpWizardDialog)
        self.resultTable.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.resultTable.setObjectName(_fromUtf8("resultTable"))
        self.resultTable.setColumnCount(0)
        self.resultTable.setRowCount(0)
        self.vboxlayout.addWidget(self.resultTable)
        self.buttonBox = QtGui.QDialogButtonBox(QRegExpWizardDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Close|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.vboxlayout.addWidget(self.buttonBox)
        self.variableLabel.setBuddy(self.variableLineEdit)
        self.textLabel1.setBuddy(self.regexpLineEdit)
        self.textLabel2.setBuddy(self.textTextEdit)

        self.retranslateUi(QRegExpWizardDialog)
        QtCore.QObject.connect(self.undoButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.regexpLineEdit.undo)
        QtCore.QObject.connect(self.redoButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.regexpLineEdit.redo)
        QtCore.QMetaObject.connectSlotsByName(QRegExpWizardDialog)
        QRegExpWizardDialog.setTabOrder(self.variableLineEdit, self.regexpLineEdit)
        QRegExpWizardDialog.setTabOrder(self.regexpLineEdit, self.textTextEdit)
        QRegExpWizardDialog.setTabOrder(self.textTextEdit, self.caseSensitiveCheckBox)
        QRegExpWizardDialog.setTabOrder(self.caseSensitiveCheckBox, self.minimalCheckBox)
        QRegExpWizardDialog.setTabOrder(self.minimalCheckBox, self.wildcardCheckBox)
        QRegExpWizardDialog.setTabOrder(self.wildcardCheckBox, self.resultTable)
        QRegExpWizardDialog.setTabOrder(self.resultTable, self.charButton)
        QRegExpWizardDialog.setTabOrder(self.charButton, self.anycharButton)
        QRegExpWizardDialog.setTabOrder(self.anycharButton, self.repeatButton)
        QRegExpWizardDialog.setTabOrder(self.repeatButton, self.nonGroupButton)
        QRegExpWizardDialog.setTabOrder(self.nonGroupButton, self.groupButton)
        QRegExpWizardDialog.setTabOrder(self.groupButton, self.altnButton)
        QRegExpWizardDialog.setTabOrder(self.altnButton, self.beglineButton)
        QRegExpWizardDialog.setTabOrder(self.beglineButton, self.endlineButton)
        QRegExpWizardDialog.setTabOrder(self.endlineButton, self.wordboundButton)
        QRegExpWizardDialog.setTabOrder(self.wordboundButton, self.nonwordboundButton)
        QRegExpWizardDialog.setTabOrder(self.nonwordboundButton, self.poslookaheadButton)
        QRegExpWizardDialog.setTabOrder(self.poslookaheadButton, self.neglookaheadButton)
        QRegExpWizardDialog.setTabOrder(self.neglookaheadButton, self.undoButton)
        QRegExpWizardDialog.setTabOrder(self.undoButton, self.redoButton)

    def retranslateUi(self, QRegExpWizardDialog):
        QRegExpWizardDialog.setWindowTitle(_translate("QRegExpWizardDialog", "QRegExp Wizard", None))
        self.variableLabel.setText(_translate("QRegExpWizardDialog", "&Variable Name:", None))
        self.charButton.setToolTip(_translate("QRegExpWizardDialog", "<b>Single character of a range (e.g. [abcd])</b><p>Select a single character of a range via a specific dialog.</p>", None))
        self.charButton.setWhatsThis(_translate("QRegExpWizardDialog", "<b>Single character of a range (e.g. [abcd])</b><p>Select a single character of a range via a specific dialog. This dialog will help to edit the range of characters and add some specific conditions.</p>s", None))
        self.charButton.setText(_translate("QRegExpWizardDialog", "...", None))
        self.anycharButton.setToolTip(_translate("QRegExpWizardDialog", "<b>Any character: \'.\'</b>\n"
"<p>Select to insert a dot (.) in your regexp.</p>", None))
        self.anycharButton.setWhatsThis(_translate("QRegExpWizardDialog", "<b>Any character: \'.\'</b>\n"
"<p>Select to insert a dot (.) in your regexp. The dot matches a single character, except line break characters (by default). \n"
"E.g. \'gr.y\' matches \'gray\', \'grey\', \'gr%y\', etc. Use the dot sparingly. Often, a character class or negated\n"
"character class is faster and more precise.</p>", None))
        self.anycharButton.setText(_translate("QRegExpWizardDialog", "...", None))
        self.repeatButton.setToolTip(_translate("QRegExpWizardDialog", "<b>Repeat contents</b>\n"
"<p>Select a repetition condition via a specific dialog. This dialog will help to specify the allowed range for repetitions.</p>", None))
        self.repeatButton.setWhatsThis(_translate("QRegExpWizardDialog", "<b>Repeat contents</b>\n"
"<p>Select a repetition condition via a specific dialog. This dialog will help to specify the allowed range for repetitions.</p>", None))
        self.repeatButton.setText(_translate("QRegExpWizardDialog", "...", None))
        self.nonGroupButton.setToolTip(_translate("QRegExpWizardDialog", "<b>Non capturing parentheses: (?:)</b>\n"
"<p>Select to insert some non capturing brackets.</p>", None))
        self.nonGroupButton.setWhatsThis(_translate("QRegExpWizardDialog", "<b>Non capturing parentheses: (?:)</b>\n"
"<p>Select to insert some non capturing brackets. It can be used to apply a regexp quantifier (eg. \'?\' or \'+\') to the entire\n"
"group of characters inside the brakets. E.g. the regex \'Set(?:Value)?\' matches \'Set\' or \'SetValue\'. The \'?:\' inside the brakets\n"
"means that the content of the match (called the backreference) is not stored for further use.</p>", None))
        self.nonGroupButton.setText(_translate("QRegExpWizardDialog", "...", None))
        self.groupButton.setToolTip(_translate("QRegExpWizardDialog", "<b>Group: ()</b>\n"
"<p>Select to insert some capturing brackets.</p>", None))
        self.groupButton.setWhatsThis(_translate("QRegExpWizardDialog", "<b>Group: ()</b>\n"
"<p>Select to insert some capturing brackets. They can be used to apply a regexp quantifier (e.g. \'?\' or \'+\') to the entire group of \n"
"characters inside the brakets. E.g. the regex \'Set(Value)?\' matches \'Set\' or \'SetValue\'. Contrary to non-capturing parentheses, \n"
"the backreference matched inside the brakets is stored for further use (i.e. \'Value\' in the second example above). \n"
"One can access the backereference with the \'\\1\' expression. </p>\n"
"<p>E.g. \'([a-c])x\\1x\\1\' will match \'axaxa\', \'bxbxb\' and \'cxcxc\'.</p>", None))
        self.groupButton.setText(_translate("QRegExpWizardDialog", "...", None))
        self.altnButton.setToolTip(_translate("QRegExpWizardDialog", "<b>Alternatives: \'|\'</b>\n"
"<p>Select to insert the alternation symbol \'|\'. </p>", None))
        self.altnButton.setWhatsThis(_translate("QRegExpWizardDialog", "<b>Alternatives: \'|\'</b>\n"
"<p>Select to insert the alternation symbol \'|\'. The alternation is used to match a single regular expression out of \n"
"several possible regular expressions. E.g. \'cat|dog|mouse|fish\' matches words containing the word \'cat\', \'dog\',\'mouse\' or \'fish\'.\n"
"Be aware that in the above example, the alternatives refer to whole or part of words. If you want to match exactly the\n"
" words \'cat\', \'dog\', ... you should express the fact that you only want to match complete words: \'\\b(cat|dog|mouse|fish)\\b\'</p>", None))
        self.altnButton.setText(_translate("QRegExpWizardDialog", "...", None))
        self.beglineButton.setToolTip(_translate("QRegExpWizardDialog", "<b>Begin of line: \'^\'</b>\n"
"<p>Select to insert the start line character (^).</p>", None))
        self.beglineButton.setWhatsThis(_translate("QRegExpWizardDialog", "<b>Begin of line: \'^\'</b>\n"
"<p>Select to insert the start line character (^). It is used to find some expressions at the begining of lines.\n"
"E.g. \'^[A-Z]\' match lines starting with a capitalized character. </p>", None))
        self.beglineButton.setText(_translate("QRegExpWizardDialog", "...", None))
        self.endlineButton.setToolTip(_translate("QRegExpWizardDialog", "<b>End of line: \'$\'</b>\n"
"<p>Select to insert the end of line character ($).</p>", None))
        self.endlineButton.setWhatsThis(_translate("QRegExpWizardDialog", "<b>End of line: \'$\'</b>\n"
"<p>Select to insert the end of line character ($). It is used to find some expressions at the end of lines.</p>", None))
        self.endlineButton.setText(_translate("QRegExpWizardDialog", "...", None))
        self.wordboundButton.setToolTip(_translate("QRegExpWizardDialog", "<b>Word boundary</b>\n"
"<p>Select to insert the word boudary character (\\b).</p>", None))
        self.wordboundButton.setWhatsThis(_translate("QRegExpWizardDialog", "<b>Word boundary</b>\n"
"<p>Select to insert the word boudary character (\\b). This character is used to express the fact that word \n"
"must begin or end at this position. E.g. \'\\bcat\\b\' matches exactly the word \'cat\' while \'concatenation\' is ignored.</p>", None))
        self.wordboundButton.setText(_translate("QRegExpWizardDialog", "...", None))
        self.nonwordboundButton.setToolTip(_translate("QRegExpWizardDialog", "<b>Non word boundary</b>\n"
"<p>Select to insert the word boudary character (\\B). \\B is the negated version of \\b.</p>", None))
        self.nonwordboundButton.setWhatsThis(_translate("QRegExpWizardDialog", "<b>Non word boundary</b>\n"
"<p>Select to insert the word boudary character (\\B). \\B is the negated version of \\b. \\B matches at every position where \\b \n"
"does not. Effectively, \\B matches at any position between two word characters as well as at any position between two non-word characters.</p>", None))
        self.nonwordboundButton.setText(_translate("QRegExpWizardDialog", "...", None))
        self.poslookaheadButton.setToolTip(_translate("QRegExpWizardDialog", "<b>Positive lookahead: (?=<i>regexpr</i>)</b>\n"
"<p>Select to insert the positive lookhead brackets.</p>", None))
        self.poslookaheadButton.setWhatsThis(_translate("QRegExpWizardDialog", "<b>Positive lookahead: (?=<i>regexpr</i>)</b>\n"
"<p>Select to insert the positive lookhead brackets. Basically, positive lookhead is used to match a character only if followed by another one.\n"
"Writting \'q(?=u)\' means that you want to match the \'q\' character only if it is followed by \'u\'. In this statement \'u\' is a trivial \n"
"regexp which may be replaced by a more complex expression; q(?=[abc])\' will match a \'q\' if followed by either \'a\', \'b\' or \'c\'.</p>", None))
        self.poslookaheadButton.setText(_translate("QRegExpWizardDialog", "...", None))
        self.neglookaheadButton.setToolTip(_translate("QRegExpWizardDialog", "<b>Negative lookahead: (?!<i>regexpr</i>)</b>\n"
"<p>Select to insert the negative lookhead brackets.</p>", None))
        self.neglookaheadButton.setWhatsThis(_translate("QRegExpWizardDialog", "<b>Negative lookahead: (?!<i>regexpr</i>)</b>\n"
"<p>Select to insert the negative lookhead brackets. Basically, negative lookhead is used to match a character only if it is not\n"
"followed by a another one. Writting \'q(?!u)\' means that you want to match \'q\' only if it is not followed by \'u\'. In this statement, \'u\' is a\n"
"trivial regexp which may be replaced by a more complex expression; \'q(?![abc])\' will match a \'q\' if it is followed by anything else than \'a\', \'b\' or \'c\'.</p>", None))
        self.neglookaheadButton.setText(_translate("QRegExpWizardDialog", "...", None))
        self.undoButton.setToolTip(_translate("QRegExpWizardDialog", "<b>Undo last edit</b>", None))
        self.undoButton.setText(_translate("QRegExpWizardDialog", "...", None))
        self.redoButton.setToolTip(_translate("QRegExpWizardDialog", "<b>Redo last edit</b>", None))
        self.redoButton.setText(_translate("QRegExpWizardDialog", "...", None))
        self.textLabel1.setText(_translate("QRegExpWizardDialog", "&Regexp:", None))
        self.textLabel2.setText(_translate("QRegExpWizardDialog", "&Text:", None))
        self.caseSensitiveCheckBox.setText(_translate("QRegExpWizardDialog", "Case &Sensitive", None))
        self.caseSensitiveCheckBox.setShortcut(_translate("QRegExpWizardDialog", "Alt+S", None))
        self.minimalCheckBox.setText(_translate("QRegExpWizardDialog", "&Minimal", None))
        self.minimalCheckBox.setShortcut(_translate("QRegExpWizardDialog", "Alt+M", None))
        self.wildcardCheckBox.setText(_translate("QRegExpWizardDialog", "&Wildcard", None))
        self.wildcardCheckBox.setShortcut(_translate("QRegExpWizardDialog", "Alt+W", None))

