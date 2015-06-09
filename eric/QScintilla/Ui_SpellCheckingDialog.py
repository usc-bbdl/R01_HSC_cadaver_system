# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\QScintilla\SpellCheckingDialog.ui'
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

class Ui_SpellCheckingDialog(object):
    def setupUi(self, SpellCheckingDialog):
        SpellCheckingDialog.setObjectName(_fromUtf8("SpellCheckingDialog"))
        SpellCheckingDialog.resize(696, 366)
        SpellCheckingDialog.setSizeGripEnabled(True)
        self.gridLayout_2 = QtGui.QGridLayout(SpellCheckingDialog)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_2 = QtGui.QLabel(SpellCheckingDialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.languageLabel = QtGui.QLabel(SpellCheckingDialog)
        self.languageLabel.setText(_fromUtf8(""))
        self.languageLabel.setObjectName(_fromUtf8("languageLabel"))
        self.horizontalLayout.addWidget(self.languageLabel)
        spacerItem1 = QtGui.QSpacerItem(328, 17, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 2)
        self.line_2 = QtGui.QFrame(SpellCheckingDialog)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout_2.addWidget(self.line_2, 1, 0, 1, 2)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(SpellCheckingDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.contextLabel = QtGui.QLabel(SpellCheckingDialog)
        self.contextLabel.setFrameShape(QtGui.QFrame.Panel)
        self.contextLabel.setFrameShadow(QtGui.QFrame.Sunken)
        self.contextLabel.setText(_fromUtf8(""))
        self.contextLabel.setTextFormat(QtCore.Qt.RichText)
        self.contextLabel.setWordWrap(True)
        self.contextLabel.setObjectName(_fromUtf8("contextLabel"))
        self.gridLayout.addWidget(self.contextLabel, 1, 0, 1, 2)
        self.label_3 = QtGui.QLabel(SpellCheckingDialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.changeEdit = QtGui.QLineEdit(SpellCheckingDialog)
        self.changeEdit.setObjectName(_fromUtf8("changeEdit"))
        self.gridLayout.addWidget(self.changeEdit, 2, 1, 1, 1)
        self.label_4 = QtGui.QLabel(SpellCheckingDialog)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 2)
        self.suggestionsList = QtGui.QListWidget(SpellCheckingDialog)
        self.suggestionsList.setObjectName(_fromUtf8("suggestionsList"))
        self.gridLayout.addWidget(self.suggestionsList, 4, 0, 1, 2)
        self.gridLayout_2.addLayout(self.gridLayout, 2, 0, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.ignoreButton = QtGui.QPushButton(SpellCheckingDialog)
        self.ignoreButton.setObjectName(_fromUtf8("ignoreButton"))
        self.verticalLayout.addWidget(self.ignoreButton)
        self.ignoreAllButton = QtGui.QPushButton(SpellCheckingDialog)
        self.ignoreAllButton.setObjectName(_fromUtf8("ignoreAllButton"))
        self.verticalLayout.addWidget(self.ignoreAllButton)
        self.addButton = QtGui.QPushButton(SpellCheckingDialog)
        self.addButton.setObjectName(_fromUtf8("addButton"))
        self.verticalLayout.addWidget(self.addButton)
        self.line = QtGui.QFrame(SpellCheckingDialog)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.replaceButton = QtGui.QPushButton(SpellCheckingDialog)
        self.replaceButton.setObjectName(_fromUtf8("replaceButton"))
        self.verticalLayout.addWidget(self.replaceButton)
        self.replaceAllButton = QtGui.QPushButton(SpellCheckingDialog)
        self.replaceAllButton.setObjectName(_fromUtf8("replaceAllButton"))
        self.verticalLayout.addWidget(self.replaceAllButton)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.gridLayout_2.addLayout(self.verticalLayout, 2, 1, 1, 1)
        self.line_3 = QtGui.QFrame(SpellCheckingDialog)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.gridLayout_2.addWidget(self.line_3, 3, 0, 1, 2)
        self.buttonBox = QtGui.QDialogButtonBox(SpellCheckingDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout_2.addWidget(self.buttonBox, 4, 0, 1, 2)
        self.label_3.setBuddy(self.changeEdit)
        self.label_4.setBuddy(self.suggestionsList)

        self.retranslateUi(SpellCheckingDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), SpellCheckingDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), SpellCheckingDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SpellCheckingDialog)
        SpellCheckingDialog.setTabOrder(self.changeEdit, self.suggestionsList)
        SpellCheckingDialog.setTabOrder(self.suggestionsList, self.ignoreButton)
        SpellCheckingDialog.setTabOrder(self.ignoreButton, self.ignoreAllButton)
        SpellCheckingDialog.setTabOrder(self.ignoreAllButton, self.addButton)
        SpellCheckingDialog.setTabOrder(self.addButton, self.replaceButton)
        SpellCheckingDialog.setTabOrder(self.replaceButton, self.replaceAllButton)
        SpellCheckingDialog.setTabOrder(self.replaceAllButton, self.buttonBox)

    def retranslateUi(self, SpellCheckingDialog):
        SpellCheckingDialog.setWindowTitle(_translate("SpellCheckingDialog", "Check spelling", None))
        self.label_2.setText(_translate("SpellCheckingDialog", "Current language:", None))
        self.languageLabel.setToolTip(_translate("SpellCheckingDialog", "Shows the language used for spell checking", None))
        self.label.setText(_translate("SpellCheckingDialog", "Not found in dictionary", None))
        self.contextLabel.setToolTip(_translate("SpellCheckingDialog", "Shows the unrecognized word with some context", None))
        self.label_3.setText(_translate("SpellCheckingDialog", "Change &to:", None))
        self.label_4.setText(_translate("SpellCheckingDialog", "&Suggestions:", None))
        self.ignoreButton.setToolTip(_translate("SpellCheckingDialog", "Press to ignore once", None))
        self.ignoreButton.setText(_translate("SpellCheckingDialog", "&Ignore", None))
        self.ignoreAllButton.setToolTip(_translate("SpellCheckingDialog", "Press to always ignore", None))
        self.ignoreAllButton.setText(_translate("SpellCheckingDialog", "I&gnore All", None))
        self.addButton.setToolTip(_translate("SpellCheckingDialog", "Press to add to dictionary", None))
        self.addButton.setText(_translate("SpellCheckingDialog", "&Add to dictionary", None))
        self.replaceButton.setToolTip(_translate("SpellCheckingDialog", "Press to replace the word", None))
        self.replaceButton.setText(_translate("SpellCheckingDialog", "&Replace", None))
        self.replaceAllButton.setToolTip(_translate("SpellCheckingDialog", "Press to replace all occurrences", None))
        self.replaceAllButton.setText(_translate("SpellCheckingDialog", "Re&place All", None))

