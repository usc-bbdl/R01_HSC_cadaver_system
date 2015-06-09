# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Preferences\ConfigurationPages\QtPage.ui'
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

class Ui_QtPage(object):
    def setupUi(self, QtPage):
        QtPage.setObjectName(_fromUtf8("QtPage"))
        QtPage.resize(642, 614)
        self.verticalLayout = QtGui.QVBoxLayout(QtPage)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.headerLabel = QtGui.QLabel(QtPage)
        self.headerLabel.setObjectName(_fromUtf8("headerLabel"))
        self.verticalLayout.addWidget(self.headerLabel)
        self.line12 = QtGui.QFrame(QtPage)
        self.line12.setFrameShape(QtGui.QFrame.HLine)
        self.line12.setFrameShadow(QtGui.QFrame.Sunken)
        self.line12.setFrameShape(QtGui.QFrame.HLine)
        self.line12.setFrameShadow(QtGui.QFrame.Sunken)
        self.line12.setObjectName(_fromUtf8("line12"))
        self.verticalLayout.addWidget(self.line12)
        self.qt4Group = QtGui.QGroupBox(QtPage)
        self.qt4Group.setObjectName(_fromUtf8("qt4Group"))
        self._2 = QtGui.QGridLayout(self.qt4Group)
        self._2.setObjectName(_fromUtf8("_2"))
        self.TextLabel1_2_2_4 = QtGui.QLabel(self.qt4Group)
        self.TextLabel1_2_2_4.setObjectName(_fromUtf8("TextLabel1_2_2_4"))
        self._2.addWidget(self.TextLabel1_2_2_4, 0, 0, 1, 2)
        self.qt4Edit = QtGui.QLineEdit(self.qt4Group)
        self.qt4Edit.setObjectName(_fromUtf8("qt4Edit"))
        self._2.addWidget(self.qt4Edit, 1, 0, 1, 1)
        self.qt4Button = QtGui.QPushButton(self.qt4Group)
        self.qt4Button.setObjectName(_fromUtf8("qt4Button"))
        self._2.addWidget(self.qt4Button, 1, 1, 1, 1)
        self.verticalLayout.addWidget(self.qt4Group)
        self.groupBox_3 = QtGui.QGroupBox(QtPage)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.gridlayout = QtGui.QGridLayout(self.groupBox_3)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.qt4TransButton = QtGui.QPushButton(self.groupBox_3)
        self.qt4TransButton.setObjectName(_fromUtf8("qt4TransButton"))
        self.gridlayout.addWidget(self.qt4TransButton, 1, 1, 1, 1)
        self.qt4TransEdit = QtGui.QLineEdit(self.groupBox_3)
        self.qt4TransEdit.setObjectName(_fromUtf8("qt4TransEdit"))
        self.gridlayout.addWidget(self.qt4TransEdit, 1, 0, 1, 1)
        self.TextLabel1_2_2_5 = QtGui.QLabel(self.groupBox_3)
        self.TextLabel1_2_2_5.setObjectName(_fromUtf8("TextLabel1_2_2_5"))
        self.gridlayout.addWidget(self.TextLabel1_2_2_5, 0, 0, 1, 2)
        self.textLabel1_2_4 = QtGui.QLabel(self.groupBox_3)
        self.textLabel1_2_4.setWordWrap(True)
        self.textLabel1_2_4.setObjectName(_fromUtf8("textLabel1_2_4"))
        self.gridlayout.addWidget(self.textLabel1_2_4, 2, 0, 1, 2)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.groupBox_4 = QtGui.QGroupBox(QtPage)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.gridlayout1 = QtGui.QGridLayout(self.groupBox_4)
        self.gridlayout1.setObjectName(_fromUtf8("gridlayout1"))
        self.label = QtGui.QLabel(self.groupBox_4)
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridlayout1.addWidget(self.label, 0, 0, 1, 5)
        self.label_3 = QtGui.QLabel(self.groupBox_4)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridlayout1.addWidget(self.label_3, 1, 0, 1, 1)
        self.qt4PrefixEdit = QtGui.QLineEdit(self.groupBox_4)
        self.qt4PrefixEdit.setObjectName(_fromUtf8("qt4PrefixEdit"))
        self.gridlayout1.addWidget(self.qt4PrefixEdit, 1, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.groupBox_4)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridlayout1.addWidget(self.label_5, 1, 2, 1, 1)
        self.qt4PostfixEdit = QtGui.QLineEdit(self.groupBox_4)
        self.qt4PostfixEdit.setObjectName(_fromUtf8("qt4PostfixEdit"))
        self.gridlayout1.addWidget(self.qt4PostfixEdit, 1, 3, 1, 1)
        self.qt4SampleLabel = QtGui.QLabel(self.groupBox_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qt4SampleLabel.sizePolicy().hasHeightForWidth())
        self.qt4SampleLabel.setSizePolicy(sizePolicy)
        self.qt4SampleLabel.setObjectName(_fromUtf8("qt4SampleLabel"))
        self.gridlayout1.addWidget(self.qt4SampleLabel, 1, 4, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_4)
        spacerItem = QtGui.QSpacerItem(496, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(QtPage)
        QtCore.QMetaObject.connectSlotsByName(QtPage)
        QtPage.setTabOrder(self.qt4Edit, self.qt4Button)
        QtPage.setTabOrder(self.qt4Button, self.qt4TransEdit)
        QtPage.setTabOrder(self.qt4TransEdit, self.qt4TransButton)
        QtPage.setTabOrder(self.qt4TransButton, self.qt4PrefixEdit)
        QtPage.setTabOrder(self.qt4PrefixEdit, self.qt4PostfixEdit)

    def retranslateUi(self, QtPage):
        self.headerLabel.setText(_translate("QtPage", "<b>Configure Qt</b>", None))
        self.qt4Group.setTitle(_translate("QtPage", "Qt4 Directory", None))
        self.TextLabel1_2_2_4.setText(_translate("QtPage", "<font color=\"#FF0000\"><b>Note:</b> This setting is activated at the next startup of the application.</font>", None))
        self.qt4Edit.setToolTip(_translate("QtPage", "Enter the path of the Qt4 directory.", None))
        self.qt4Button.setToolTip(_translate("QtPage", "Press to select the Qt4 directory via a directory selection dialog", None))
        self.qt4Button.setText(_translate("QtPage", "...", None))
        self.groupBox_3.setTitle(_translate("QtPage", "Qt4 Translations Directory", None))
        self.qt4TransButton.setToolTip(_translate("QtPage", "Press to select the Qt4 translations directory via a directory selection dialog", None))
        self.qt4TransButton.setText(_translate("QtPage", "...", None))
        self.qt4TransEdit.setToolTip(_translate("QtPage", "Enter the path of the Qt4 translations directory.", None))
        self.TextLabel1_2_2_5.setText(_translate("QtPage", "<font color=\"#FF0000\"><b>Note:</b> This setting is activated at the next startup of the application.</font>", None))
        self.textLabel1_2_4.setText(_translate("QtPage", "<b>Note:</b> Leave this entry empty to use the QT4TRANSLATIONSDIR environment variable or the path compiled into the Qt4 library.", None))
        self.groupBox_4.setTitle(_translate("QtPage", "Qt Tools", None))
        self.label.setText(_translate("QtPage", "The tool executable is composed of the prefix, the tool name and the postfix. For win, the extension is added automatically.", None))
        self.label_3.setText(_translate("QtPage", "Qt4-Prefix:", None))
        self.qt4PrefixEdit.setToolTip(_translate("QtPage", "Enter the prefix for the Qt4 tools name", None))
        self.label_5.setText(_translate("QtPage", "Qt4-Postfix:", None))
        self.qt4PostfixEdit.setToolTip(_translate("QtPage", "Enter the postfix for the Qt4 tools name", None))
        self.qt4SampleLabel.setToolTip(_translate("QtPage", "This gives an example of the complete tool name", None))
        self.qt4SampleLabel.setText(_translate("QtPage", "designer", None))

