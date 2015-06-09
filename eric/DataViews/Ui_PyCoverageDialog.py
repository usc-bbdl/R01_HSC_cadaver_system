# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\DataViews\PyCoverageDialog.ui'
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

class Ui_PyCoverageDialog(object):
    def setupUi(self, PyCoverageDialog):
        PyCoverageDialog.setObjectName(_fromUtf8("PyCoverageDialog"))
        PyCoverageDialog.resize(832, 585)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(PyCoverageDialog.sizePolicy().hasHeightForWidth())
        PyCoverageDialog.setSizePolicy(sizePolicy)
        PyCoverageDialog.setSizeGripEnabled(True)
        self.vboxlayout = QtGui.QVBoxLayout(PyCoverageDialog)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        self.textLabel1_2 = QtGui.QLabel(PyCoverageDialog)
        self.textLabel1_2.setObjectName(_fromUtf8("textLabel1_2"))
        self.hboxlayout.addWidget(self.textLabel1_2)
        self.excludeCombo = QtGui.QComboBox(PyCoverageDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.excludeCombo.sizePolicy().hasHeightForWidth())
        self.excludeCombo.setSizePolicy(sizePolicy)
        self.excludeCombo.setEditable(True)
        self.excludeCombo.setInsertPolicy(QtGui.QComboBox.InsertAtTop)
        self.excludeCombo.setAutoCompletion(True)
        self.excludeCombo.setDuplicatesEnabled(False)
        self.excludeCombo.setObjectName(_fromUtf8("excludeCombo"))
        self.hboxlayout.addWidget(self.excludeCombo)
        self.reloadButton = QtGui.QPushButton(PyCoverageDialog)
        self.reloadButton.setObjectName(_fromUtf8("reloadButton"))
        self.hboxlayout.addWidget(self.reloadButton)
        self.vboxlayout.addLayout(self.hboxlayout)
        self.resultList = QtGui.QTreeWidget(PyCoverageDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.resultList.sizePolicy().hasHeightForWidth())
        self.resultList.setSizePolicy(sizePolicy)
        self.resultList.setAlternatingRowColors(True)
        self.resultList.setRootIsDecorated(False)
        self.resultList.setItemsExpandable(False)
        self.resultList.setObjectName(_fromUtf8("resultList"))
        self.vboxlayout.addWidget(self.resultList)
        self.textLabel1 = QtGui.QLabel(PyCoverageDialog)
        self.textLabel1.setObjectName(_fromUtf8("textLabel1"))
        self.vboxlayout.addWidget(self.textLabel1)
        self.summaryList = QtGui.QTreeWidget(PyCoverageDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.summaryList.sizePolicy().hasHeightForWidth())
        self.summaryList.setSizePolicy(sizePolicy)
        self.summaryList.setAlternatingRowColors(True)
        self.summaryList.setRootIsDecorated(False)
        self.summaryList.setItemsExpandable(False)
        self.summaryList.setObjectName(_fromUtf8("summaryList"))
        self.vboxlayout.addWidget(self.summaryList)
        self.checkProgress = QtGui.QProgressBar(PyCoverageDialog)
        self.checkProgress.setProperty("value", 0)
        self.checkProgress.setOrientation(QtCore.Qt.Horizontal)
        self.checkProgress.setObjectName(_fromUtf8("checkProgress"))
        self.vboxlayout.addWidget(self.checkProgress)
        self.buttonBox = QtGui.QDialogButtonBox(PyCoverageDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.vboxlayout.addWidget(self.buttonBox)
        self.textLabel1_2.setBuddy(self.excludeCombo)

        self.retranslateUi(PyCoverageDialog)
        QtCore.QMetaObject.connectSlotsByName(PyCoverageDialog)
        PyCoverageDialog.setTabOrder(self.excludeCombo, self.reloadButton)
        PyCoverageDialog.setTabOrder(self.reloadButton, self.resultList)
        PyCoverageDialog.setTabOrder(self.resultList, self.summaryList)

    def retranslateUi(self, PyCoverageDialog):
        PyCoverageDialog.setWindowTitle(_translate("PyCoverageDialog", "Python Code Coverage", None))
        PyCoverageDialog.setWhatsThis(_translate("PyCoverageDialog", "<b>Python Code Coverage</b>\n"
"<p>This dialog shows the collected code coverage data.</p>", None))
        self.textLabel1_2.setText(_translate("PyCoverageDialog", "E&xclude pattern:", None))
        self.excludeCombo.setToolTip(_translate("PyCoverageDialog", "Enter a regexp pattern marking lines to exclude from coverage", None))
        self.excludeCombo.setWhatsThis(_translate("PyCoverageDialog", "<b>Exclude pattern</b>\n"
"<p>Enter a regular expression pattern. Lines matching this pattern are excluded from the coverage analysis. The default pattern is \'#pragma[: ]+[nN][oO] [cC][oO][vV][eE][rR]\'. If the pattern is found on a line containing the colon that introduces a suite of statements, the entire suite is excluded.</p>", None))
        self.reloadButton.setText(_translate("PyCoverageDialog", "&Reload", None))
        self.reloadButton.setShortcut(_translate("PyCoverageDialog", "Alt+R", None))
        self.resultList.setWhatsThis(_translate("PyCoverageDialog", "<b>Python Code Coverage</b>\n"
"<p>This list shows the collected code coverage data. There are several actions available via the context menu.</p>", None))
        self.resultList.headerItem().setText(0, _translate("PyCoverageDialog", "Name", None))
        self.resultList.headerItem().setText(1, _translate("PyCoverageDialog", "Statements", None))
        self.resultList.headerItem().setText(2, _translate("PyCoverageDialog", "Executed", None))
        self.resultList.headerItem().setText(3, _translate("PyCoverageDialog", "Coverage", None))
        self.resultList.headerItem().setText(4, _translate("PyCoverageDialog", "Excluded", None))
        self.resultList.headerItem().setText(5, _translate("PyCoverageDialog", "Missing", None))
        self.textLabel1.setText(_translate("PyCoverageDialog", "Summary", None))
        self.summaryList.setWhatsThis(_translate("PyCoverageDialog", "<b>Summary</b>\n"
"<p>This shows some overall code coverage information.</p>", None))
        self.summaryList.headerItem().setText(0, _translate("PyCoverageDialog", "Statements", None))
        self.summaryList.headerItem().setText(1, _translate("PyCoverageDialog", "Executed", None))
        self.summaryList.headerItem().setText(2, _translate("PyCoverageDialog", "Coverage", None))
        self.checkProgress.setToolTip(_translate("PyCoverageDialog", "Shows the progress of the code coverage action", None))

