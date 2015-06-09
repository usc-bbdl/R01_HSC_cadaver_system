# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\DataViews\PyProfileDialog.ui'
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

class Ui_PyProfileDialog(object):
    def setupUi(self, PyProfileDialog):
        PyProfileDialog.setObjectName(_fromUtf8("PyProfileDialog"))
        PyProfileDialog.resize(832, 587)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(PyProfileDialog.sizePolicy().hasHeightForWidth())
        PyProfileDialog.setSizePolicy(sizePolicy)
        PyProfileDialog.setSizeGripEnabled(True)
        self.vboxlayout = QtGui.QVBoxLayout(PyProfileDialog)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.resultList = QtGui.QTreeWidget(PyProfileDialog)
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
        self.summaryList = QtGui.QTreeWidget(PyProfileDialog)
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
        self.checkProgress = QtGui.QProgressBar(PyProfileDialog)
        self.checkProgress.setProperty("value", 0)
        self.checkProgress.setOrientation(QtCore.Qt.Horizontal)
        self.checkProgress.setObjectName(_fromUtf8("checkProgress"))
        self.vboxlayout.addWidget(self.checkProgress)
        self.buttonBox = QtGui.QDialogButtonBox(PyProfileDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(PyProfileDialog)
        QtCore.QMetaObject.connectSlotsByName(PyProfileDialog)
        PyProfileDialog.setTabOrder(self.resultList, self.summaryList)

    def retranslateUi(self, PyProfileDialog):
        PyProfileDialog.setWindowTitle(_translate("PyProfileDialog", "Profile Results", None))
        PyProfileDialog.setWhatsThis(_translate("PyProfileDialog", "<b>Profile Results</b>\n"
"<p>This dialog shows the profile results.</p>", None))
        self.resultList.setWhatsThis(_translate("PyProfileDialog", "<b>Profile Results</b>\n"
"<p>This list shows the profile results. There are several actions available via the context menu.</p>", None))
        self.resultList.setSortingEnabled(True)
        self.resultList.headerItem().setText(0, _translate("PyProfileDialog", "Nr. Calls", None))
        self.resultList.headerItem().setText(1, _translate("PyProfileDialog", "Total Time", None))
        self.resultList.headerItem().setText(2, _translate("PyProfileDialog", "Tot. Time / Call", None))
        self.resultList.headerItem().setText(3, _translate("PyProfileDialog", "Cumulative Time", None))
        self.resultList.headerItem().setText(4, _translate("PyProfileDialog", "Cum. Time / Call", None))
        self.resultList.headerItem().setText(5, _translate("PyProfileDialog", "Filename", None))
        self.resultList.headerItem().setText(6, _translate("PyProfileDialog", "Line", None))
        self.resultList.headerItem().setText(7, _translate("PyProfileDialog", "Function", None))
        self.summaryList.setWhatsThis(_translate("PyProfileDialog", "<b>Summary</b>\n"
"<p>This shows some overall profile data. There are several actions available via the context menu.</p>", None))
        self.summaryList.headerItem().setText(0, _translate("PyProfileDialog", "Summary", None))
        self.summaryList.headerItem().setText(1, _translate("PyProfileDialog", "#", None))
        self.checkProgress.setToolTip(_translate("PyProfileDialog", "Shows the progress of the profile data calculation", None))

