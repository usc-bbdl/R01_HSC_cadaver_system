# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\DataViews\CodeMetricsDialog.ui'
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

class Ui_CodeMetricsDialog(object):
    def setupUi(self, CodeMetricsDialog):
        CodeMetricsDialog.setObjectName(_fromUtf8("CodeMetricsDialog"))
        CodeMetricsDialog.resize(832, 587)
        CodeMetricsDialog.setSizeGripEnabled(True)
        self.vboxlayout = QtGui.QVBoxLayout(CodeMetricsDialog)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.resultList = QtGui.QTreeWidget(CodeMetricsDialog)
        self.resultList.setAlternatingRowColors(True)
        self.resultList.setObjectName(_fromUtf8("resultList"))
        self.vboxlayout.addWidget(self.resultList)
        self.summaryList = QtGui.QTreeWidget(CodeMetricsDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.summaryList.sizePolicy().hasHeightForWidth())
        self.summaryList.setSizePolicy(sizePolicy)
        self.summaryList.setAlternatingRowColors(True)
        self.summaryList.setObjectName(_fromUtf8("summaryList"))
        self.vboxlayout.addWidget(self.summaryList)
        self.checkProgress = QtGui.QProgressBar(CodeMetricsDialog)
        self.checkProgress.setProperty("value", 0)
        self.checkProgress.setOrientation(QtCore.Qt.Horizontal)
        self.checkProgress.setObjectName(_fromUtf8("checkProgress"))
        self.vboxlayout.addWidget(self.checkProgress)
        self.buttonBox = QtGui.QDialogButtonBox(CodeMetricsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(CodeMetricsDialog)
        QtCore.QMetaObject.connectSlotsByName(CodeMetricsDialog)

    def retranslateUi(self, CodeMetricsDialog):
        CodeMetricsDialog.setWindowTitle(_translate("CodeMetricsDialog", "Code Metrics", None))
        CodeMetricsDialog.setWhatsThis(_translate("CodeMetricsDialog", "<b>Code Metrics</b>\n"
"<p>This dialog shows some code metrics.</p>", None))
        self.resultList.setWhatsThis(_translate("CodeMetricsDialog", "<b>Code metrics</b>\n"
"<p>This list shows some code metrics.</p>", None))
        self.resultList.headerItem().setText(0, _translate("CodeMetricsDialog", "Name", None))
        self.resultList.headerItem().setText(1, _translate("CodeMetricsDialog", "Start", None))
        self.resultList.headerItem().setText(2, _translate("CodeMetricsDialog", "End", None))
        self.resultList.headerItem().setText(3, _translate("CodeMetricsDialog", "Lines", None))
        self.resultList.headerItem().setText(4, _translate("CodeMetricsDialog", "Lines of code", None))
        self.resultList.headerItem().setText(5, _translate("CodeMetricsDialog", "Comments", None))
        self.resultList.headerItem().setText(6, _translate("CodeMetricsDialog", "Empty", None))
        self.summaryList.setWhatsThis(_translate("CodeMetricsDialog", "<b>Summary</b>\n"
"<p>This shows some overall code metrics.</p>", None))
        self.summaryList.headerItem().setText(0, _translate("CodeMetricsDialog", "Summary", None))
        self.summaryList.headerItem().setText(1, _translate("CodeMetricsDialog", "#", None))
        self.checkProgress.setToolTip(_translate("CodeMetricsDialog", "Shows the progress of the code metrics action", None))

