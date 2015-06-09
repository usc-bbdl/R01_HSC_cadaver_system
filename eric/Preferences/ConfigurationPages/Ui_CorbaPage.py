# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Preferences\ConfigurationPages\CorbaPage.ui'
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

class Ui_CorbaPage(object):
    def setupUi(self, CorbaPage):
        CorbaPage.setObjectName(_fromUtf8("CorbaPage"))
        CorbaPage.resize(589, 490)
        self.vboxlayout = QtGui.QVBoxLayout(CorbaPage)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.headerLabel = QtGui.QLabel(CorbaPage)
        self.headerLabel.setObjectName(_fromUtf8("headerLabel"))
        self.vboxlayout.addWidget(self.headerLabel)
        self.line13 = QtGui.QFrame(CorbaPage)
        self.line13.setFrameShape(QtGui.QFrame.HLine)
        self.line13.setFrameShadow(QtGui.QFrame.Sunken)
        self.line13.setFrameShape(QtGui.QFrame.HLine)
        self.line13.setFrameShadow(QtGui.QFrame.Sunken)
        self.line13.setObjectName(_fromUtf8("line13"))
        self.vboxlayout.addWidget(self.line13)
        self.groupBox = QtGui.QGroupBox(CorbaPage)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridlayout = QtGui.QGridLayout(self.groupBox)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.idlButton = QtGui.QPushButton(self.groupBox)
        self.idlButton.setObjectName(_fromUtf8("idlButton"))
        self.gridlayout.addWidget(self.idlButton, 0, 1, 1, 1)
        self.idlEdit = QtGui.QLineEdit(self.groupBox)
        self.idlEdit.setObjectName(_fromUtf8("idlEdit"))
        self.gridlayout.addWidget(self.idlEdit, 0, 0, 1, 1)
        self.textLabel1_4 = QtGui.QLabel(self.groupBox)
        self.textLabel1_4.setObjectName(_fromUtf8("textLabel1_4"))
        self.gridlayout.addWidget(self.textLabel1_4, 1, 0, 1, 2)
        self.vboxlayout.addWidget(self.groupBox)
        spacerItem = QtGui.QSpacerItem(20, 81, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vboxlayout.addItem(spacerItem)

        self.retranslateUi(CorbaPage)
        QtCore.QMetaObject.connectSlotsByName(CorbaPage)
        CorbaPage.setTabOrder(self.idlEdit, self.idlButton)

    def retranslateUi(self, CorbaPage):
        self.headerLabel.setText(_translate("CorbaPage", "<b>Configure CORBA support</b>", None))
        self.groupBox.setTitle(_translate("CorbaPage", "IDL Compiler", None))
        self.idlButton.setToolTip(_translate("CorbaPage", "Press to select the IDL compiler via a file selection dialog.", None))
        self.idlButton.setText(_translate("CorbaPage", "...", None))
        self.idlEdit.setToolTip(_translate("CorbaPage", "Enter the path to the IDL compiler.", None))
        self.textLabel1_4.setText(_translate("CorbaPage", "<b>Note:</b> Leave this entry empty to use the default value (omniidl or omniidl.exe).", None))

