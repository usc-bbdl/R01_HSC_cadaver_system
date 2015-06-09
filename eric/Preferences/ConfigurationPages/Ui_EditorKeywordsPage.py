# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Preferences\ConfigurationPages\EditorKeywordsPage.ui'
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

class Ui_EditorKeywordsPage(object):
    def setupUi(self, EditorKeywordsPage):
        EditorKeywordsPage.setObjectName(_fromUtf8("EditorKeywordsPage"))
        EditorKeywordsPage.resize(462, 422)
        self.verticalLayout = QtGui.QVBoxLayout(EditorKeywordsPage)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.headerLabel = QtGui.QLabel(EditorKeywordsPage)
        self.headerLabel.setObjectName(_fromUtf8("headerLabel"))
        self.verticalLayout.addWidget(self.headerLabel)
        self.line5 = QtGui.QFrame(EditorKeywordsPage)
        self.line5.setFrameShape(QtGui.QFrame.HLine)
        self.line5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line5.setFrameShape(QtGui.QFrame.HLine)
        self.line5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line5.setObjectName(_fromUtf8("line5"))
        self.verticalLayout.addWidget(self.line5)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.TextLabel1_3_3 = QtGui.QLabel(EditorKeywordsPage)
        self.TextLabel1_3_3.setToolTip(_fromUtf8(""))
        self.TextLabel1_3_3.setObjectName(_fromUtf8("TextLabel1_3_3"))
        self.horizontalLayout.addWidget(self.TextLabel1_3_3)
        self.languageCombo = QtGui.QComboBox(EditorKeywordsPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.languageCombo.sizePolicy().hasHeightForWidth())
        self.languageCombo.setSizePolicy(sizePolicy)
        self.languageCombo.setObjectName(_fromUtf8("languageCombo"))
        self.horizontalLayout.addWidget(self.languageCombo)
        self.label = QtGui.QLabel(EditorKeywordsPage)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.setSpinBox = QtGui.QSpinBox(EditorKeywordsPage)
        self.setSpinBox.setMinimum(1)
        self.setSpinBox.setMaximum(9)
        self.setSpinBox.setObjectName(_fromUtf8("setSpinBox"))
        self.horizontalLayout.addWidget(self.setSpinBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.keywordsEdit = QtGui.QPlainTextEdit(EditorKeywordsPage)
        self.keywordsEdit.setObjectName(_fromUtf8("keywordsEdit"))
        self.verticalLayout.addWidget(self.keywordsEdit)

        self.retranslateUi(EditorKeywordsPage)
        QtCore.QMetaObject.connectSlotsByName(EditorKeywordsPage)
        EditorKeywordsPage.setTabOrder(self.languageCombo, self.setSpinBox)
        EditorKeywordsPage.setTabOrder(self.setSpinBox, self.keywordsEdit)

    def retranslateUi(self, EditorKeywordsPage):
        self.headerLabel.setText(_translate("EditorKeywordsPage", "<b>Configure syntax highlighter keywords</b>", None))
        self.TextLabel1_3_3.setText(_translate("EditorKeywordsPage", "Language:", None))
        self.languageCombo.setToolTip(_translate("EditorKeywordsPage", "Select the language to be configured.", None))
        self.label.setText(_translate("EditorKeywordsPage", "Set:", None))
        self.keywordsEdit.setToolTip(_translate("EditorKeywordsPage", "Enter the keywords separated by a blank", None))

