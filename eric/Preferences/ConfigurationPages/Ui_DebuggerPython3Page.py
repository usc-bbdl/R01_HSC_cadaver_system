# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Preferences\ConfigurationPages\DebuggerPython3Page.ui'
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

class Ui_DebuggerPython3Page(object):
    def setupUi(self, DebuggerPython3Page):
        DebuggerPython3Page.setObjectName(_fromUtf8("DebuggerPython3Page"))
        DebuggerPython3Page.resize(453, 449)
        self.verticalLayout_2 = QtGui.QVBoxLayout(DebuggerPython3Page)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.headerLabel = QtGui.QLabel(DebuggerPython3Page)
        self.headerLabel.setObjectName(_fromUtf8("headerLabel"))
        self.verticalLayout_2.addWidget(self.headerLabel)
        self.line11_2 = QtGui.QFrame(DebuggerPython3Page)
        self.line11_2.setFrameShape(QtGui.QFrame.HLine)
        self.line11_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line11_2.setFrameShape(QtGui.QFrame.HLine)
        self.line11_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line11_2.setObjectName(_fromUtf8("line11_2"))
        self.verticalLayout_2.addWidget(self.line11_2)
        self.groupBox = QtGui.QGroupBox(DebuggerPython3Page)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridlayout = QtGui.QGridLayout(self.groupBox)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.interpreterEdit = QtGui.QLineEdit(self.groupBox)
        self.interpreterEdit.setObjectName(_fromUtf8("interpreterEdit"))
        self.gridlayout.addWidget(self.interpreterEdit, 0, 0, 1, 1)
        self.interpreterButton = QtGui.QPushButton(self.groupBox)
        self.interpreterButton.setObjectName(_fromUtf8("interpreterButton"))
        self.gridlayout.addWidget(self.interpreterButton, 0, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(DebuggerPython3Page)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridlayout1 = QtGui.QGridLayout(self.groupBox_2)
        self.gridlayout1.setObjectName(_fromUtf8("gridlayout1"))
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        self.debugClientEdit = QtGui.QLineEdit(self.groupBox_2)
        self.debugClientEdit.setEnabled(False)
        self.debugClientEdit.setObjectName(_fromUtf8("debugClientEdit"))
        self.hboxlayout.addWidget(self.debugClientEdit)
        self.debugClientButton = QtGui.QPushButton(self.groupBox_2)
        self.debugClientButton.setEnabled(False)
        self.debugClientButton.setObjectName(_fromUtf8("debugClientButton"))
        self.hboxlayout.addWidget(self.debugClientButton)
        self.gridlayout1.addLayout(self.hboxlayout, 1, 0, 1, 3)
        self.standardButton = QtGui.QRadioButton(self.groupBox_2)
        self.standardButton.setObjectName(_fromUtf8("standardButton"))
        self.gridlayout1.addWidget(self.standardButton, 0, 0, 1, 1)
        self.customButton = QtGui.QRadioButton(self.groupBox_2)
        self.customButton.setObjectName(_fromUtf8("customButton"))
        self.gridlayout1.addWidget(self.customButton, 0, 2, 1, 1)
        self.threadedButton = QtGui.QRadioButton(self.groupBox_2)
        self.threadedButton.setObjectName(_fromUtf8("threadedButton"))
        self.gridlayout1.addWidget(self.threadedButton, 0, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.groupBox_3 = QtGui.QGroupBox(DebuggerPython3Page)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.groupBox_3)
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.sourceExtensionsEdit = QtGui.QLineEdit(self.groupBox_3)
        self.sourceExtensionsEdit.setObjectName(_fromUtf8("sourceExtensionsEdit"))
        self.verticalLayout.addWidget(self.sourceExtensionsEdit)
        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.pyRedirectCheckBox = QtGui.QCheckBox(DebuggerPython3Page)
        self.pyRedirectCheckBox.setObjectName(_fromUtf8("pyRedirectCheckBox"))
        self.verticalLayout_2.addWidget(self.pyRedirectCheckBox)
        self.pyNoEncodingCheckBox = QtGui.QCheckBox(DebuggerPython3Page)
        self.pyNoEncodingCheckBox.setObjectName(_fromUtf8("pyNoEncodingCheckBox"))
        self.verticalLayout_2.addWidget(self.pyNoEncodingCheckBox)
        spacerItem = QtGui.QSpacerItem(435, 21, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)

        self.retranslateUi(DebuggerPython3Page)
        QtCore.QObject.connect(self.customButton, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.debugClientEdit.setEnabled)
        QtCore.QObject.connect(self.customButton, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.debugClientButton.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(DebuggerPython3Page)
        DebuggerPython3Page.setTabOrder(self.interpreterEdit, self.interpreterButton)
        DebuggerPython3Page.setTabOrder(self.interpreterButton, self.standardButton)
        DebuggerPython3Page.setTabOrder(self.standardButton, self.threadedButton)
        DebuggerPython3Page.setTabOrder(self.threadedButton, self.customButton)
        DebuggerPython3Page.setTabOrder(self.customButton, self.debugClientEdit)
        DebuggerPython3Page.setTabOrder(self.debugClientEdit, self.debugClientButton)
        DebuggerPython3Page.setTabOrder(self.debugClientButton, self.sourceExtensionsEdit)
        DebuggerPython3Page.setTabOrder(self.sourceExtensionsEdit, self.pyRedirectCheckBox)
        DebuggerPython3Page.setTabOrder(self.pyRedirectCheckBox, self.pyNoEncodingCheckBox)

    def retranslateUi(self, DebuggerPython3Page):
        self.headerLabel.setText(_translate("DebuggerPython3Page", "<b>Configure Python3 Debugger</b>", None))
        self.groupBox.setTitle(_translate("DebuggerPython3Page", "Python3 Interpreter for Debug Client", None))
        self.interpreterEdit.setToolTip(_translate("DebuggerPython3Page", "Enter the path of the Python3 interpreter to be used by the debug client.", None))
        self.interpreterButton.setToolTip(_translate("DebuggerPython3Page", "Press to select the Python3 interpreter via a file selection dialog", None))
        self.interpreterButton.setText(_translate("DebuggerPython3Page", "...", None))
        self.groupBox_2.setTitle(_translate("DebuggerPython3Page", "Debug Client Type", None))
        self.debugClientEdit.setToolTip(_translate("DebuggerPython3Page", "Enter the path of the Debug Client to be used.  Leave empty to use the default.", None))
        self.debugClientButton.setToolTip(_translate("DebuggerPython3Page", "Press to select the Debug Client via a file selection dialog", None))
        self.debugClientButton.setText(_translate("DebuggerPython3Page", "...", None))
        self.standardButton.setToolTip(_translate("DebuggerPython3Page", "Select the standard debug client", None))
        self.standardButton.setText(_translate("DebuggerPython3Page", "Standard", None))
        self.customButton.setToolTip(_translate("DebuggerPython3Page", "Select the custom selected debug client", None))
        self.customButton.setText(_translate("DebuggerPython3Page", "Custom", None))
        self.threadedButton.setToolTip(_translate("DebuggerPython3Page", "Select the multi threaded debug client", None))
        self.threadedButton.setText(_translate("DebuggerPython3Page", "Multi Threaded", None))
        self.groupBox_3.setTitle(_translate("DebuggerPython3Page", "Source association", None))
        self.label.setText(_translate("DebuggerPython3Page", "Enter the file extensions to be associated with the Python3 debugger separated by a space. They must not overlap with the ones for Python2.", None))
        self.pyRedirectCheckBox.setToolTip(_translate("DebuggerPython3Page", "Select, to redirect stdin, stdout and stderr of the program being debugged to the eric4 IDE", None))
        self.pyRedirectCheckBox.setText(_translate("DebuggerPython3Page", "Redirect stdin/stdout/stderr", None))
        self.pyNoEncodingCheckBox.setToolTip(_translate("DebuggerPython3Page", "Select to not set the debug client encoding", None))
        self.pyNoEncodingCheckBox.setText(_translate("DebuggerPython3Page", "Don\'t set the encoding of the debug client", None))

