# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Helpviewer\SearchWidget.ui'
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

class Ui_SearchWidget(object):
    def setupUi(self, SearchWidget):
        SearchWidget.setObjectName(_fromUtf8("SearchWidget"))
        SearchWidget.resize(718, 25)
        self.horizontalLayout = QtGui.QHBoxLayout(SearchWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.closeButton = QtGui.QToolButton(SearchWidget)
        self.closeButton.setText(_fromUtf8(""))
        self.closeButton.setObjectName(_fromUtf8("closeButton"))
        self.horizontalLayout.addWidget(self.closeButton)
        self.label = QtGui.QLabel(SearchWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.findtextCombo = QtGui.QComboBox(SearchWidget)
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
        self.horizontalLayout.addWidget(self.findtextCombo)
        self.findPrevButton = QtGui.QToolButton(SearchWidget)
        self.findPrevButton.setObjectName(_fromUtf8("findPrevButton"))
        self.horizontalLayout.addWidget(self.findPrevButton)
        self.findNextButton = QtGui.QToolButton(SearchWidget)
        self.findNextButton.setObjectName(_fromUtf8("findNextButton"))
        self.horizontalLayout.addWidget(self.findNextButton)
        self.caseCheckBox = QtGui.QCheckBox(SearchWidget)
        self.caseCheckBox.setObjectName(_fromUtf8("caseCheckBox"))
        self.horizontalLayout.addWidget(self.caseCheckBox)
        self.wrapCheckBox = QtGui.QCheckBox(SearchWidget)
        self.wrapCheckBox.setObjectName(_fromUtf8("wrapCheckBox"))
        self.horizontalLayout.addWidget(self.wrapCheckBox)
        self.infoLine = QtGui.QFrame(SearchWidget)
        self.infoLine.setFrameShape(QtGui.QFrame.VLine)
        self.infoLine.setFrameShadow(QtGui.QFrame.Sunken)
        self.infoLine.setObjectName(_fromUtf8("infoLine"))
        self.horizontalLayout.addWidget(self.infoLine)
        self.infoLabel = QtGui.QLabel(SearchWidget)
        self.infoLabel.setMinimumSize(QtCore.QSize(200, 0))
        self.infoLabel.setText(_fromUtf8(""))
        self.infoLabel.setObjectName(_fromUtf8("infoLabel"))
        self.horizontalLayout.addWidget(self.infoLabel)

        self.retranslateUi(SearchWidget)
        QtCore.QMetaObject.connectSlotsByName(SearchWidget)
        SearchWidget.setTabOrder(self.findtextCombo, self.caseCheckBox)
        SearchWidget.setTabOrder(self.caseCheckBox, self.wrapCheckBox)
        SearchWidget.setTabOrder(self.wrapCheckBox, self.findNextButton)
        SearchWidget.setTabOrder(self.findNextButton, self.findPrevButton)
        SearchWidget.setTabOrder(self.findPrevButton, self.closeButton)

    def retranslateUi(self, SearchWidget):
        SearchWidget.setWindowTitle(_translate("SearchWidget", "Find", None))
        self.closeButton.setToolTip(_translate("SearchWidget", "Press to close the window", None))
        self.label.setText(_translate("SearchWidget", "Find:", None))
        self.findPrevButton.setToolTip(_translate("SearchWidget", "Press to find the previous occurrence", None))
        self.findNextButton.setToolTip(_translate("SearchWidget", "Press to find the next occurrence", None))
        self.caseCheckBox.setText(_translate("SearchWidget", "Match case", None))
        self.wrapCheckBox.setText(_translate("SearchWidget", "Wrap around", None))

