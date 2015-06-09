# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Helpviewer\HelpTopicDialog.ui'
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

class Ui_HelpTopicDialog(object):
    def setupUi(self, HelpTopicDialog):
        HelpTopicDialog.setObjectName(_fromUtf8("HelpTopicDialog"))
        HelpTopicDialog.resize(500, 300)
        self.verticalLayout = QtGui.QVBoxLayout(HelpTopicDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(HelpTopicDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.topicsList = QtGui.QListWidget(HelpTopicDialog)
        self.topicsList.setObjectName(_fromUtf8("topicsList"))
        self.verticalLayout.addWidget(self.topicsList)
        self.buttonBox = QtGui.QDialogButtonBox(HelpTopicDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        self.label.setBuddy(self.topicsList)

        self.retranslateUi(HelpTopicDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), HelpTopicDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), HelpTopicDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(HelpTopicDialog)
        HelpTopicDialog.setTabOrder(self.topicsList, self.buttonBox)

    def retranslateUi(self, HelpTopicDialog):
        HelpTopicDialog.setWindowTitle(_translate("HelpTopicDialog", "Select Help Topic", None))
        self.label.setText(_translate("HelpTopicDialog", "&Topics:", None))

