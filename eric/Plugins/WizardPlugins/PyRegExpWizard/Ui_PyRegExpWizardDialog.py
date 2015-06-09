# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Plugins\WizardPlugins\PyRegExpWizard\PyRegExpWizardDialog.ui'
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

class Ui_PyRegExpWizardDialog(object):
    def setupUi(self, PyRegExpWizardDialog):
        PyRegExpWizardDialog.setObjectName(_fromUtf8("PyRegExpWizardDialog"))
        PyRegExpWizardDialog.resize(750, 700)
        PyRegExpWizardDialog.setProperty("sizeGripEnabled", True)
        self.verticalLayout = QtGui.QVBoxLayout(PyRegExpWizardDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.versionGroup = QtGui.QGroupBox(PyRegExpWizardDialog)
        self.versionGroup.setObjectName(_fromUtf8("versionGroup"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.versionGroup)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.py2Button = QtGui.QRadioButton(self.versionGroup)
        self.py2Button.setStatusTip(_fromUtf8(""))
        self.py2Button.setChecked(True)
        self.py2Button.setObjectName(_fromUtf8("py2Button"))
        self.horizontalLayout.addWidget(self.py2Button)
        self.py3Button = QtGui.QRadioButton(self.versionGroup)
        self.py3Button.setObjectName(_fromUtf8("py3Button"))
        self.horizontalLayout.addWidget(self.py3Button)
        spacerItem = QtGui.QSpacerItem(535, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addWidget(self.versionGroup)
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        self.variableLabel = QtGui.QLabel(PyRegExpWizardDialog)
        self.variableLabel.setObjectName(_fromUtf8("variableLabel"))
        self.hboxlayout.addWidget(self.variableLabel)
        self.variableLineEdit = QtGui.QLineEdit(PyRegExpWizardDialog)
        self.variableLineEdit.setObjectName(_fromUtf8("variableLineEdit"))
        self.hboxlayout.addWidget(self.variableLineEdit)
        self.verticalLayout.addLayout(self.hboxlayout)
        self.importCheckBox = QtGui.QCheckBox(PyRegExpWizardDialog)
        self.importCheckBox.setObjectName(_fromUtf8("importCheckBox"))
        self.verticalLayout.addWidget(self.importCheckBox)
        self.variableLine = QtGui.QFrame(PyRegExpWizardDialog)
        self.variableLine.setFrameShape(QtGui.QFrame.HLine)
        self.variableLine.setFrameShadow(QtGui.QFrame.Sunken)
        self.variableLine.setFrameShape(QtGui.QFrame.HLine)
        self.variableLine.setFrameShadow(QtGui.QFrame.Sunken)
        self.variableLine.setObjectName(_fromUtf8("variableLine"))
        self.verticalLayout.addWidget(self.variableLine)
        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setObjectName(_fromUtf8("hboxlayout1"))
        self.commentButton = QtGui.QToolButton(PyRegExpWizardDialog)
        self.commentButton.setObjectName(_fromUtf8("commentButton"))
        self.hboxlayout1.addWidget(self.commentButton)
        self.charButton = QtGui.QToolButton(PyRegExpWizardDialog)
        self.charButton.setObjectName(_fromUtf8("charButton"))
        self.hboxlayout1.addWidget(self.charButton)
        self.anycharButton = QtGui.QToolButton(PyRegExpWizardDialog)
        self.anycharButton.setObjectName(_fromUtf8("anycharButton"))
        self.hboxlayout1.addWidget(self.anycharButton)
        self.repeatButton = QtGui.QToolButton(PyRegExpWizardDialog)
        self.repeatButton.setObjectName(_fromUtf8("repeatButton"))
        self.hboxlayout1.addWidget(self.repeatButton)
        self.nonGroupButton = QtGui.QToolButton(PyRegExpWizardDialog)
        self.nonGroupButton.setObjectName(_fromUtf8("nonGroupButton"))
        self.hboxlayout1.addWidget(self.nonGroupButton)
        self.groupButton = QtGui.QToolButton(PyRegExpWizardDialog)
        self.groupButton.setObjectName(_fromUtf8("groupButton"))
        self.hboxlayout1.addWidget(self.groupButton)
        self.namedGroupButton = QtGui.QToolButton(PyRegExpWizardDialog)
        self.namedGroupButton.setObjectName(_fromUtf8("namedGroupButton"))
        self.hboxlayout1.addWidget(self.namedGroupButton)
        self.namedReferenceButton = QtGui.QToolButton(PyRegExpWizardDialog)
        self.namedReferenceButton.setObjectName(_fromUtf8("namedReferenceButton"))
        self.hboxlayout1.addWidget(self.namedReferenceButton)
        self.altnButton = QtGui.QToolButton(PyRegExpWizardDialog)
        self.altnButton.setObjectName(_fromUtf8("altnButton"))
        self.hboxlayout1.addWidget(self.altnButton)
        self.beglineButton = QtGui.QToolButton(PyRegExpWizardDialog)
        self.beglineButton.setObjectName(_fromUtf8("beglineButton"))
        self.hboxlayout1.addWidget(self.beglineButton)
        self.endlineButton = QtGui.QToolButton(PyRegExpWizardDialog)
        self.endlineButton.setObjectName(_fromUtf8("endlineButton"))
        self.hboxlayout1.addWidget(self.endlineButton)
        self.wordboundButton = QtGui.QToolButton(PyRegExpWizardDialog)
        self.wordboundButton.setObjectName(_fromUtf8("wordboundButton"))
        self.hboxlayout1.addWidget(self.wordboundButton)
        self.nonwordboundButton = QtGui.QToolButton(PyRegExpWizardDialog)
        self.nonwordboundButton.setObjectName(_fromUtf8("nonwordboundButton"))
        self.hboxlayout1.addWidget(self.nonwordboundButton)
        self.poslookaheadButton = QtGui.QToolButton(PyRegExpWizardDialog)
        self.poslookaheadButton.setObjectName(_fromUtf8("poslookaheadButton"))
        self.hboxlayout1.addWidget(self.poslookaheadButton)
        self.neglookaheadButton = QtGui.QToolButton(PyRegExpWizardDialog)
        self.neglookaheadButton.setObjectName(_fromUtf8("neglookaheadButton"))
        self.hboxlayout1.addWidget(self.neglookaheadButton)
        self.poslookbehindButton = QtGui.QToolButton(PyRegExpWizardDialog)
        self.poslookbehindButton.setObjectName(_fromUtf8("poslookbehindButton"))
        self.hboxlayout1.addWidget(self.poslookbehindButton)
        self.neglookbehindButton = QtGui.QToolButton(PyRegExpWizardDialog)
        self.neglookbehindButton.setObjectName(_fromUtf8("neglookbehindButton"))
        self.hboxlayout1.addWidget(self.neglookbehindButton)
        spacerItem1 = QtGui.QSpacerItem(16, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.hboxlayout1.addItem(spacerItem1)
        self.undoButton = QtGui.QToolButton(PyRegExpWizardDialog)
        self.undoButton.setObjectName(_fromUtf8("undoButton"))
        self.hboxlayout1.addWidget(self.undoButton)
        self.redoButton = QtGui.QToolButton(PyRegExpWizardDialog)
        self.redoButton.setObjectName(_fromUtf8("redoButton"))
        self.hboxlayout1.addWidget(self.redoButton)
        spacerItem2 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout1.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.hboxlayout1)
        self.gridlayout = QtGui.QGridLayout()
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.textLabel1 = QtGui.QLabel(PyRegExpWizardDialog)
        self.textLabel1.setAlignment(QtCore.Qt.AlignTop)
        self.textLabel1.setObjectName(_fromUtf8("textLabel1"))
        self.gridlayout.addWidget(self.textLabel1, 0, 0, 1, 1)
        self.regexpTextEdit = QtGui.QTextEdit(PyRegExpWizardDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.regexpTextEdit.sizePolicy().hasHeightForWidth())
        self.regexpTextEdit.setSizePolicy(sizePolicy)
        self.regexpTextEdit.setAcceptRichText(False)
        self.regexpTextEdit.setObjectName(_fromUtf8("regexpTextEdit"))
        self.gridlayout.addWidget(self.regexpTextEdit, 0, 1, 1, 1)
        self.resultTable = QtGui.QTableWidget(PyRegExpWizardDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.resultTable.sizePolicy().hasHeightForWidth())
        self.resultTable.setSizePolicy(sizePolicy)
        self.resultTable.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.resultTable.setObjectName(_fromUtf8("resultTable"))
        self.resultTable.setColumnCount(0)
        self.resultTable.setRowCount(0)
        self.gridlayout.addWidget(self.resultTable, 3, 0, 1, 2)
        self.gridlayout1 = QtGui.QGridLayout()
        self.gridlayout1.setObjectName(_fromUtf8("gridlayout1"))
        self.multilineCheckBox = QtGui.QCheckBox(PyRegExpWizardDialog)
        self.multilineCheckBox.setObjectName(_fromUtf8("multilineCheckBox"))
        self.gridlayout1.addWidget(self.multilineCheckBox, 0, 1, 1, 1)
        self.unicodeCheckBox = QtGui.QCheckBox(PyRegExpWizardDialog)
        self.unicodeCheckBox.setObjectName(_fromUtf8("unicodeCheckBox"))
        self.gridlayout1.addWidget(self.unicodeCheckBox, 1, 2, 1, 1)
        self.verboseCheckBox = QtGui.QCheckBox(PyRegExpWizardDialog)
        self.verboseCheckBox.setObjectName(_fromUtf8("verboseCheckBox"))
        self.gridlayout1.addWidget(self.verboseCheckBox, 1, 0, 1, 1)
        self.caseSensitiveCheckBox = QtGui.QCheckBox(PyRegExpWizardDialog)
        self.caseSensitiveCheckBox.setChecked(True)
        self.caseSensitiveCheckBox.setObjectName(_fromUtf8("caseSensitiveCheckBox"))
        self.gridlayout1.addWidget(self.caseSensitiveCheckBox, 0, 0, 1, 1)
        self.localeCheckBox = QtGui.QCheckBox(PyRegExpWizardDialog)
        self.localeCheckBox.setObjectName(_fromUtf8("localeCheckBox"))
        self.gridlayout1.addWidget(self.localeCheckBox, 1, 1, 1, 1)
        self.dotallCheckBox = QtGui.QCheckBox(PyRegExpWizardDialog)
        self.dotallCheckBox.setObjectName(_fromUtf8("dotallCheckBox"))
        self.gridlayout1.addWidget(self.dotallCheckBox, 0, 2, 1, 1)
        self.gridlayout.addLayout(self.gridlayout1, 2, 0, 1, 2)
        self.textLabel2 = QtGui.QLabel(PyRegExpWizardDialog)
        self.textLabel2.setAlignment(QtCore.Qt.AlignTop)
        self.textLabel2.setObjectName(_fromUtf8("textLabel2"))
        self.gridlayout.addWidget(self.textLabel2, 1, 0, 1, 1)
        self.textTextEdit = QtGui.QTextEdit(PyRegExpWizardDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.textTextEdit.sizePolicy().hasHeightForWidth())
        self.textTextEdit.setSizePolicy(sizePolicy)
        self.textTextEdit.setAcceptRichText(False)
        self.textTextEdit.setObjectName(_fromUtf8("textTextEdit"))
        self.gridlayout.addWidget(self.textTextEdit, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridlayout)
        self.buttonBox = QtGui.QDialogButtonBox(PyRegExpWizardDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Close|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(PyRegExpWizardDialog)
        QtCore.QMetaObject.connectSlotsByName(PyRegExpWizardDialog)
        PyRegExpWizardDialog.setTabOrder(self.py2Button, self.py3Button)
        PyRegExpWizardDialog.setTabOrder(self.py3Button, self.variableLineEdit)
        PyRegExpWizardDialog.setTabOrder(self.variableLineEdit, self.importCheckBox)
        PyRegExpWizardDialog.setTabOrder(self.importCheckBox, self.commentButton)
        PyRegExpWizardDialog.setTabOrder(self.commentButton, self.charButton)
        PyRegExpWizardDialog.setTabOrder(self.charButton, self.anycharButton)
        PyRegExpWizardDialog.setTabOrder(self.anycharButton, self.repeatButton)
        PyRegExpWizardDialog.setTabOrder(self.repeatButton, self.nonGroupButton)
        PyRegExpWizardDialog.setTabOrder(self.nonGroupButton, self.groupButton)
        PyRegExpWizardDialog.setTabOrder(self.groupButton, self.namedGroupButton)
        PyRegExpWizardDialog.setTabOrder(self.namedGroupButton, self.namedReferenceButton)
        PyRegExpWizardDialog.setTabOrder(self.namedReferenceButton, self.altnButton)
        PyRegExpWizardDialog.setTabOrder(self.altnButton, self.beglineButton)
        PyRegExpWizardDialog.setTabOrder(self.beglineButton, self.endlineButton)
        PyRegExpWizardDialog.setTabOrder(self.endlineButton, self.wordboundButton)
        PyRegExpWizardDialog.setTabOrder(self.wordboundButton, self.nonwordboundButton)
        PyRegExpWizardDialog.setTabOrder(self.nonwordboundButton, self.poslookaheadButton)
        PyRegExpWizardDialog.setTabOrder(self.poslookaheadButton, self.neglookaheadButton)
        PyRegExpWizardDialog.setTabOrder(self.neglookaheadButton, self.poslookbehindButton)
        PyRegExpWizardDialog.setTabOrder(self.poslookbehindButton, self.neglookbehindButton)
        PyRegExpWizardDialog.setTabOrder(self.neglookbehindButton, self.undoButton)
        PyRegExpWizardDialog.setTabOrder(self.undoButton, self.redoButton)
        PyRegExpWizardDialog.setTabOrder(self.redoButton, self.regexpTextEdit)
        PyRegExpWizardDialog.setTabOrder(self.regexpTextEdit, self.textTextEdit)
        PyRegExpWizardDialog.setTabOrder(self.textTextEdit, self.caseSensitiveCheckBox)
        PyRegExpWizardDialog.setTabOrder(self.caseSensitiveCheckBox, self.verboseCheckBox)
        PyRegExpWizardDialog.setTabOrder(self.verboseCheckBox, self.multilineCheckBox)
        PyRegExpWizardDialog.setTabOrder(self.multilineCheckBox, self.localeCheckBox)
        PyRegExpWizardDialog.setTabOrder(self.localeCheckBox, self.dotallCheckBox)
        PyRegExpWizardDialog.setTabOrder(self.dotallCheckBox, self.unicodeCheckBox)
        PyRegExpWizardDialog.setTabOrder(self.unicodeCheckBox, self.resultTable)
        PyRegExpWizardDialog.setTabOrder(self.resultTable, self.buttonBox)

    def retranslateUi(self, PyRegExpWizardDialog):
        PyRegExpWizardDialog.setWindowTitle(_translate("PyRegExpWizardDialog", "Python re Wizard", None))
        self.versionGroup.setTitle(_translate("PyRegExpWizardDialog", "Python Version", None))
        self.py2Button.setText(_translate("PyRegExpWizardDialog", "Python 2", None))
        self.py3Button.setText(_translate("PyRegExpWizardDialog", "Python 3", None))
        self.variableLabel.setText(_translate("PyRegExpWizardDialog", "Variable Name:", None))
        self.importCheckBox.setText(_translate("PyRegExpWizardDialog", "Include import statement", None))
        self.commentButton.setToolTip(_translate("PyRegExpWizardDialog", "<b>Comment: (?#)</b>\n"
"<p>Insert some comment inside your regexp.</p>", None))
        self.commentButton.setWhatsThis(_translate("PyRegExpWizardDialog", "<b>Comment: (?#)</b>\n"
"<p>Insert some comment inside your regexp.The regex engine ignores everything after the (?# until the first closing round bracket. \n"
"The following example could clarify the regexp which match a valid date: </p>\n"
"<p>(?#year)(19|20)\\d\\d[- /.](?#month)(0[1-9]|1[012])[- /.](?#day)(0[1-9]|[12][0-9]|3[01])</p>", None))
        self.commentButton.setText(_translate("PyRegExpWizardDialog", "...", None))
        self.charButton.setToolTip(_translate("PyRegExpWizardDialog", "<b>Single character of a range (e.g. [abcd])</b><p>Select a single character of a range via a specific dialog.</p>", None))
        self.charButton.setWhatsThis(_translate("PyRegExpWizardDialog", "<b>Single character of a range (e.g. [abcd])</b><p>Select a single character of a range via a specific dialog. This dialog will help to edit the range of characters and add some specific conditions.</p>s", None))
        self.charButton.setText(_translate("PyRegExpWizardDialog", "...", None))
        self.anycharButton.setToolTip(_translate("PyRegExpWizardDialog", "<b>Any character: \'.\'</b>\n"
"<p>Select to insert a dot (.) in your regexp.</p>", None))
        self.anycharButton.setWhatsThis(_translate("PyRegExpWizardDialog", "<b>Any character: \'.\'</b>\n"
"<p>Select to insert a dot (.) in your regexp. The dot matches a single character, except line break characters (by default). \n"
"E.g. \'gr.y\' matches \'gray\', \'grey\', \'gr%y\', etc. Use the dot sparingly. Often, a character class or negated\n"
"character class is faster and more precise.</p>", None))
        self.anycharButton.setText(_translate("PyRegExpWizardDialog", "...", None))
        self.repeatButton.setToolTip(_translate("PyRegExpWizardDialog", "<b>Repeat contents</b>\n"
"<p>Select a repetition condition via a specific dialog. This dialog will help to specify the allowed range for repetitions.</p>", None))
        self.repeatButton.setWhatsThis(_translate("PyRegExpWizardDialog", "<b>Repeat contents</b>\n"
"<p>Select a repetition condition via a specific dialog. This dialog will help to specify the allowed range for repetitions.</p>", None))
        self.repeatButton.setText(_translate("PyRegExpWizardDialog", "...", None))
        self.nonGroupButton.setToolTip(_translate("PyRegExpWizardDialog", "<b>Non capturing parentheses: (?:)</b>\n"
"<p>Select to insert some non capturing brackets.</p>", None))
        self.nonGroupButton.setWhatsThis(_translate("PyRegExpWizardDialog", "<b>Non capturing parentheses: (?:)</b>\n"
"<p>Select to insert some non capturing brackets. It can be used to apply a regexp quantifier (eg. \'?\' or \'+\') to the entire\n"
"group of characters inside the brakets. E.g. the regex \'Set(?:Value)?\' matches \'Set\' or \'SetValue\'. The \'?:\' inside the brakets\n"
"means that the content of the match (called the backreference) is not stored for further use.</p>", None))
        self.nonGroupButton.setText(_translate("PyRegExpWizardDialog", "...", None))
        self.groupButton.setToolTip(_translate("PyRegExpWizardDialog", "<b>Group: ()</b>\n"
"<p>Select to insert some capturing brackets.</p>", None))
        self.groupButton.setWhatsThis(_translate("PyRegExpWizardDialog", "<b>Group: ()</b>\n"
"<p>Select to insert some capturing brackets. They can be used to apply a regexp quantifier (e.g. \'?\' or \'+\') to the entire group of \n"
"characters inside the brakets. E.g. the regex \'Set(Value)?\' matches \'Set\' or \'SetValue\'. Contrary to non-capturing parentheses, \n"
"the backreference matched inside the brakets is stored for further use (i.e. \'Value\' in the second example above). \n"
"One can access the backereference with the \'\\1\' expression. </p>\n"
"<p>E.g. \'([a-c])x\\1x\\1\' will match \'axaxa\', \'bxbxb\' and \'cxcxc\'.</p>", None))
        self.groupButton.setText(_translate("PyRegExpWizardDialog", "...", None))
        self.namedGroupButton.setToolTip(_translate("PyRegExpWizardDialog", "<b>Named group: (?P&lt;<i>groupname</i>&gt;)</b>\n"
"<p>Select to insert some named group brackets.</p>", None))
        self.namedGroupButton.setWhatsThis(_translate("PyRegExpWizardDialog", "<b>Named group: (?P&lt;<i>groupname</i>&gt;)</b>\n"
"<p>Select to insert some named group brackets. Usage is similar to standard group parentheses as the matched \n"
"backreference is also stored for further usage. The difference is that a name is given to the match. This is useful when \n"
"the work to do on the match becomes a bit complicated. One can access the backreference via the group name (i.e (?P=<i>groupname</i>)).\n"
"E.g. (?P<foo>[abc])x(?P=foo)x(?P=foo)x matches \'axaxax\',\'bxbxbx\' or \'cxcxcx\' (\'foo\' is the group name)</p>", None))
        self.namedGroupButton.setText(_translate("PyRegExpWizardDialog", "...", None))
        self.namedReferenceButton.setToolTip(_translate("PyRegExpWizardDialog", "<b>Reference named group: (?P=<i>groupname</i>)</b>\n"
"<p>Select to insert a reference to named group previously declared.</p>", None))
        self.namedReferenceButton.setWhatsThis(_translate("PyRegExpWizardDialog", "<b>Reference named group: (?P=<i>groupname</i>)</b>\n"
"<p>Select to insert a reference to named group previously declared. Each reference group refers to the match\n"
" found by the corresponding named group. In the following example, (?P=foo) may refer to the charaters \'a\',\'b\' or \'c\'.</p>\n"
"<p>E.g. (?P<foo>[abc])x(?P=foo)x(?P=foo)x matches \'axaxax\',\'bxbxbx\' or \'cxcxcx\'.</p>", None))
        self.namedReferenceButton.setText(_translate("PyRegExpWizardDialog", "...", None))
        self.altnButton.setToolTip(_translate("PyRegExpWizardDialog", "<b>Alternatives: \'|\'</b>\n"
"<p>Select to insert the alternation symbol \'|\'. </p>", None))
        self.altnButton.setWhatsThis(_translate("PyRegExpWizardDialog", "<b>Alternatives: \'|\'</b>\n"
"<p>Select to insert the alternation symbol \'|\'. The alternation is used to match a single regular expression out of \n"
"several possible regular expressions. E.g. \'cat|dog|mouse|fish\' matches words containing the word \'cat\', \'dog\',\'mouse\' or \'fish\'.\n"
"Be aware that in the above example, the alternatives refer to whole or part of words. If you want to match exactly the\n"
" words \'cat\', \'dog\', ... you should express the fact that you only want to match complete words: \'\\b(cat|dog|mouse|fish)\\b\'</p>", None))
        self.altnButton.setText(_translate("PyRegExpWizardDialog", "...", None))
        self.beglineButton.setToolTip(_translate("PyRegExpWizardDialog", "<b>Begin of line: \'^\'</b>\n"
"<p>Select to insert the start line character (^).</p>", None))
        self.beglineButton.setWhatsThis(_translate("PyRegExpWizardDialog", "<b>Begin of line: \'^\'</b>\n"
"<p>Select to insert the start line character (^). It is used to find some expressions at the begining of lines.\n"
"E.g. \'^[A-Z]\' match lines starting with a capitalized character. </p>", None))
        self.beglineButton.setText(_translate("PyRegExpWizardDialog", "...", None))
        self.endlineButton.setToolTip(_translate("PyRegExpWizardDialog", "<b>End of line: \'$\'</b>\n"
"<p>Select to insert the end of line character ($).</p>", None))
        self.endlineButton.setWhatsThis(_translate("PyRegExpWizardDialog", "<b>End of line: \'$\'</b>\n"
"<p>Select to insert the end of line character ($). It is used to find some expressions at the end of lines.</p>", None))
        self.endlineButton.setText(_translate("PyRegExpWizardDialog", "...", None))
        self.wordboundButton.setToolTip(_translate("PyRegExpWizardDialog", "<b>Word boundary</b>\n"
"<p>Select to insert the word boudary character (\\b).</p>", None))
        self.wordboundButton.setWhatsThis(_translate("PyRegExpWizardDialog", "<b>Word boundary</b>\n"
"<p>Select to insert the word boudary character (\\b). This character is used to express the fact that word \n"
"must begin or end at this position. E.g. \'\\bcat\\b\' matches exactly the word \'cat\' while \'concatenation\' is ignored.</p>", None))
        self.wordboundButton.setText(_translate("PyRegExpWizardDialog", "...", None))
        self.nonwordboundButton.setToolTip(_translate("PyRegExpWizardDialog", "<b>Non word boundary</b>\n"
"<p>Select to insert the word boudary character (\\B). \\B is the negated version of \\b.</p>", None))
        self.nonwordboundButton.setWhatsThis(_translate("PyRegExpWizardDialog", "<b>Non word boundary</b>\n"
"<p>Select to insert the word boudary character (\\B). \\B is the negated version of \\b. \\B matches at every position where \\b \n"
"does not. Effectively, \\B matches at any position between two word characters as well as at any position between two non-word characters.</p>", None))
        self.nonwordboundButton.setText(_translate("PyRegExpWizardDialog", "...", None))
        self.poslookaheadButton.setToolTip(_translate("PyRegExpWizardDialog", "<b>Positive lookahead: (?=<i>regexpr</i>)</b>\n"
"<p>Select to insert the positive lookhead brackets.</p>", None))
        self.poslookaheadButton.setWhatsThis(_translate("PyRegExpWizardDialog", "<b>Positive lookahead: (?=<i>regexpr</i>)</b>\n"
"<p>Select to insert the positive lookhead brackets. Basically, positive lookhead is used to match a character only if followed by another one.\n"
"Writting \'q(?=u)\' means that you want to match the \'q\' character only if it is followed by \'u\'. In this statement \'u\' is a trivial \n"
"regexp which may be replaced by a more complex expression; q(?=[abc])\' will match a \'q\' if followed by either \'a\', \'b\' or \'c\'.</p>", None))
        self.poslookaheadButton.setText(_translate("PyRegExpWizardDialog", "...", None))
        self.neglookaheadButton.setToolTip(_translate("PyRegExpWizardDialog", "<b>Negative lookahead: (?!<i>regexpr</i>)</b>\n"
"<p>Select to insert the negative lookhead brackets.</p>", None))
        self.neglookaheadButton.setWhatsThis(_translate("PyRegExpWizardDialog", "<b>Negative lookahead: (?!<i>regexpr</i>)</b>\n"
"<p>Select to insert the negative lookhead brackets. Basically, negative lookhead is used to match a character only if it is not\n"
"followed by a another one. Writting \'q(?!u)\' means that you want to match \'q\' only if it is not followed by \'u\'. In this statement, \'u\' is a\n"
"trivial regexp which may be replaced by a more complex expression; \'q(?![abc])\' will match a \'q\' if it is followed by anything else than \'a\', \'b\' or \'c\'.</p>", None))
        self.neglookaheadButton.setText(_translate("PyRegExpWizardDialog", "...", None))
        self.poslookbehindButton.setToolTip(_translate("PyRegExpWizardDialog", "<b>Positive lookbehind: (?&lt;=<i>regexpr</i>)</b>\n"
"<p>Select to insert the positive lookbehind brackets.</p>", None))
        self.poslookbehindButton.setWhatsThis(_translate("PyRegExpWizardDialog", "<b>Positive lookbehind: (?&lt;=<i>regexpr</i>)</b>\n"
"<p>Select to insert the positive lookbehind brackets. Lookbehind has the same effect as lookahead, but works backwards. \n"
"It is used to match a character only if preceded by another one. Writting \'(?&lt;=u)q\' means that you want to match the \'q\' character \n"
"only if it is preceded by \'u\'. As with lookhead, \'u\' may be replaced by a more complex expression; \'(?&lt;=[abc])q\' will match a \'q\' if preceded by either \'a\', \'b\' or \'c\'.</p>", None))
        self.poslookbehindButton.setText(_translate("PyRegExpWizardDialog", "...", None))
        self.neglookbehindButton.setToolTip(_translate("PyRegExpWizardDialog", "<b>Negative lookbehind (?&lt;!<i>regexpr</i>)</b>\n"
"<p>Select to insert the negative lookbehind brackets.</p>", None))
        self.neglookbehindButton.setWhatsThis(_translate("PyRegExpWizardDialog", "<b>Negative lookbehind (?&lt;!<i>regexpr</i>)</b>\n"
"<p>Select to insert the negative lookbehind brackets. Lookbehind has the same effect as lookahead, \n"
"but works backwards. It is used to match a character only if not preceded by another one. Writting \'(?&lt;!u)q\' means that you want to match the \'q\' \n"
"character only if it is not preceded by \'u\'. As other lookaround, \'u\' may be replaced by a more complex \n"
"expression; \'(?&lt;![abc])q\' will match a \'q\' only if not preceded by either \'a\', \'b\' nor \'c\'.</p>", None))
        self.neglookbehindButton.setText(_translate("PyRegExpWizardDialog", "...", None))
        self.undoButton.setToolTip(_translate("PyRegExpWizardDialog", "<b>Undo last edit</b>", None))
        self.undoButton.setText(_translate("PyRegExpWizardDialog", "...", None))
        self.redoButton.setToolTip(_translate("PyRegExpWizardDialog", "<b>Redo last edit</b>", None))
        self.redoButton.setText(_translate("PyRegExpWizardDialog", "...", None))
        self.textLabel1.setText(_translate("PyRegExpWizardDialog", "Regexp:", None))
        self.multilineCheckBox.setToolTip(_translate("PyRegExpWizardDialog", "\"^\" matches beginning of line, \"$\" matches end of line", None))
        self.multilineCheckBox.setText(_translate("PyRegExpWizardDialog", "Match Linebreaks", None))
        self.unicodeCheckBox.setText(_translate("PyRegExpWizardDialog", "Unicode", None))
        self.verboseCheckBox.setText(_translate("PyRegExpWizardDialog", "Verbose Regexp", None))
        self.caseSensitiveCheckBox.setText(_translate("PyRegExpWizardDialog", "Case Sensitive", None))
        self.localeCheckBox.setText(_translate("PyRegExpWizardDialog", "Observe Locale", None))
        self.dotallCheckBox.setToolTip(_translate("PyRegExpWizardDialog", "\".\" matches linebreaks as well", None))
        self.dotallCheckBox.setText(_translate("PyRegExpWizardDialog", "Dot matches Linebreak", None))
        self.textLabel2.setText(_translate("PyRegExpWizardDialog", "Text:", None))

