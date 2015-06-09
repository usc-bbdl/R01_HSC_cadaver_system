# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\QScintilla\ReplaceWidget.ui'
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

class Ui_ReplaceWidget(object):
    def setupUi(self, ReplaceWidget):
        ReplaceWidget.setObjectName(_fromUtf8("ReplaceWidget"))
        ReplaceWidget.resize(724, 69)
        self.gridLayout = QtGui.QGridLayout(ReplaceWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.closeButton = QtGui.QToolButton(ReplaceWidget)
        self.closeButton.setText(_fromUtf8(""))
        self.closeButton.setObjectName(_fromUtf8("closeButton"))
        self.gridLayout.addWidget(self.closeButton, 0, 0, 1, 1)
        self.label = QtGui.QLabel(ReplaceWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.findtextCombo = QtGui.QComboBox(ReplaceWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.findtextCombo.sizePolicy().hasHeightForWidth())
        self.findtextCombo.setSizePolicy(sizePolicy)
        self.findtextCombo.setEditable(True)
        self.findtextCombo.setInsertPolicy(QtGui.QComboBox.InsertAtTop)
        self.findtextCombo.setAutoCompletion(False)
        self.findtextCombo.setDuplicatesEnabled(False)
        self.findtextCombo.setObjectName(_fromUtf8("findtextCombo"))
        self.gridLayout.addWidget(self.findtextCombo, 0, 2, 1, 1)
        self.findPrevButton = QtGui.QToolButton(ReplaceWidget)
        self.findPrevButton.setObjectName(_fromUtf8("findPrevButton"))
        self.gridLayout.addWidget(self.findPrevButton, 0, 3, 1, 1)
        self.findNextButton = QtGui.QToolButton(ReplaceWidget)
        self.findNextButton.setObjectName(_fromUtf8("findNextButton"))
        self.gridLayout.addWidget(self.findNextButton, 0, 4, 1, 1)
        self.caseCheckBox = QtGui.QCheckBox(ReplaceWidget)
        self.caseCheckBox.setObjectName(_fromUtf8("caseCheckBox"))
        self.gridLayout.addWidget(self.caseCheckBox, 0, 6, 1, 1)
        self.wordCheckBox = QtGui.QCheckBox(ReplaceWidget)
        self.wordCheckBox.setObjectName(_fromUtf8("wordCheckBox"))
        self.gridLayout.addWidget(self.wordCheckBox, 0, 7, 1, 1)
        self.regexpCheckBox = QtGui.QCheckBox(ReplaceWidget)
        self.regexpCheckBox.setObjectName(_fromUtf8("regexpCheckBox"))
        self.gridLayout.addWidget(self.regexpCheckBox, 0, 8, 1, 1)
        self.label_2 = QtGui.QLabel(ReplaceWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)
        self.replacetextCombo = QtGui.QComboBox(ReplaceWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.replacetextCombo.sizePolicy().hasHeightForWidth())
        self.replacetextCombo.setSizePolicy(sizePolicy)
        self.replacetextCombo.setEditable(True)
        self.replacetextCombo.setInsertPolicy(QtGui.QComboBox.InsertAtTop)
        self.replacetextCombo.setAutoCompletion(False)
        self.replacetextCombo.setDuplicatesEnabled(False)
        self.replacetextCombo.setObjectName(_fromUtf8("replacetextCombo"))
        self.gridLayout.addWidget(self.replacetextCombo, 1, 2, 1, 1)
        self.replaceButton = QtGui.QToolButton(ReplaceWidget)
        self.replaceButton.setObjectName(_fromUtf8("replaceButton"))
        self.gridLayout.addWidget(self.replaceButton, 1, 3, 1, 1)
        self.replaceSearchButton = QtGui.QToolButton(ReplaceWidget)
        self.replaceSearchButton.setObjectName(_fromUtf8("replaceSearchButton"))
        self.gridLayout.addWidget(self.replaceSearchButton, 1, 4, 1, 1)
        self.replaceAllButton = QtGui.QToolButton(ReplaceWidget)
        self.replaceAllButton.setObjectName(_fromUtf8("replaceAllButton"))
        self.gridLayout.addWidget(self.replaceAllButton, 1, 5, 1, 1)
        self.wrapCheckBox = QtGui.QCheckBox(ReplaceWidget)
        self.wrapCheckBox.setObjectName(_fromUtf8("wrapCheckBox"))
        self.gridLayout.addWidget(self.wrapCheckBox, 1, 6, 1, 1)
        self.selectionCheckBox = QtGui.QCheckBox(ReplaceWidget)
        self.selectionCheckBox.setObjectName(_fromUtf8("selectionCheckBox"))
        self.gridLayout.addWidget(self.selectionCheckBox, 1, 7, 1, 1)

        self.retranslateUi(ReplaceWidget)
        QtCore.QMetaObject.connectSlotsByName(ReplaceWidget)
        ReplaceWidget.setTabOrder(self.findtextCombo, self.replacetextCombo)
        ReplaceWidget.setTabOrder(self.replacetextCombo, self.caseCheckBox)
        ReplaceWidget.setTabOrder(self.caseCheckBox, self.wordCheckBox)
        ReplaceWidget.setTabOrder(self.wordCheckBox, self.regexpCheckBox)
        ReplaceWidget.setTabOrder(self.regexpCheckBox, self.wrapCheckBox)
        ReplaceWidget.setTabOrder(self.wrapCheckBox, self.selectionCheckBox)
        ReplaceWidget.setTabOrder(self.selectionCheckBox, self.findNextButton)
        ReplaceWidget.setTabOrder(self.findNextButton, self.findPrevButton)
        ReplaceWidget.setTabOrder(self.findPrevButton, self.replaceButton)
        ReplaceWidget.setTabOrder(self.replaceButton, self.replaceSearchButton)
        ReplaceWidget.setTabOrder(self.replaceSearchButton, self.replaceAllButton)
        ReplaceWidget.setTabOrder(self.replaceAllButton, self.closeButton)

    def retranslateUi(self, ReplaceWidget):
        ReplaceWidget.setWindowTitle(_translate("ReplaceWidget", "Find and Replace", None))
        self.closeButton.setToolTip(_translate("ReplaceWidget", "Press to close the window", None))
        self.label.setText(_translate("ReplaceWidget", "Find:", None))
        self.findPrevButton.setToolTip(_translate("ReplaceWidget", "Press to find the previous occurrence", None))
        self.findNextButton.setToolTip(_translate("ReplaceWidget", "Press to find the next occurrence", None))
        self.caseCheckBox.setText(_translate("ReplaceWidget", "Match case", None))
        self.wordCheckBox.setText(_translate("ReplaceWidget", "Whole word", None))
        self.regexpCheckBox.setText(_translate("ReplaceWidget", "Regexp", None))
        self.label_2.setText(_translate("ReplaceWidget", "Replace:", None))
        self.replaceButton.setToolTip(_translate("ReplaceWidget", "Press to replace the selection", None))
        self.replaceSearchButton.setToolTip(_translate("ReplaceWidget", "Press to replace the selection and search for the next occurence", None))
        self.replaceAllButton.setToolTip(_translate("ReplaceWidget", "Press to replace all occurrences", None))
        self.wrapCheckBox.setText(_translate("ReplaceWidget", "Wrap around", None))
        self.selectionCheckBox.setText(_translate("ReplaceWidget", "Selection only", None))

