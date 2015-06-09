# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Preferences\ConfigurationPages\DebuggerRubyPage.ui'
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

class Ui_DebuggerRubyPage(object):
    def setupUi(self, DebuggerRubyPage):
        DebuggerRubyPage.setObjectName(_fromUtf8("DebuggerRubyPage"))
        DebuggerRubyPage.resize(400, 170)
        self.vboxlayout = QtGui.QVBoxLayout(DebuggerRubyPage)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.headerLabel = QtGui.QLabel(DebuggerRubyPage)
        self.headerLabel.setObjectName(_fromUtf8("headerLabel"))
        self.vboxlayout.addWidget(self.headerLabel)
        self.line11_2_2 = QtGui.QFrame(DebuggerRubyPage)
        self.line11_2_2.setFrameShape(QtGui.QFrame.HLine)
        self.line11_2_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line11_2_2.setFrameShape(QtGui.QFrame.HLine)
        self.line11_2_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line11_2_2.setObjectName(_fromUtf8("line11_2_2"))
        self.vboxlayout.addWidget(self.line11_2_2)
        self.groupBox = QtGui.QGroupBox(DebuggerRubyPage)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.hboxlayout = QtGui.QHBoxLayout(self.groupBox)
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        self.rubyInterpreterEdit = QtGui.QLineEdit(self.groupBox)
        self.rubyInterpreterEdit.setObjectName(_fromUtf8("rubyInterpreterEdit"))
        self.hboxlayout.addWidget(self.rubyInterpreterEdit)
        self.rubyInterpreterButton = QtGui.QPushButton(self.groupBox)
        self.rubyInterpreterButton.setObjectName(_fromUtf8("rubyInterpreterButton"))
        self.hboxlayout.addWidget(self.rubyInterpreterButton)
        self.vboxlayout.addWidget(self.groupBox)
        self.rbRedirectCheckBox = QtGui.QCheckBox(DebuggerRubyPage)
        self.rbRedirectCheckBox.setObjectName(_fromUtf8("rbRedirectCheckBox"))
        self.vboxlayout.addWidget(self.rbRedirectCheckBox)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vboxlayout.addItem(spacerItem)

        self.retranslateUi(DebuggerRubyPage)
        QtCore.QMetaObject.connectSlotsByName(DebuggerRubyPage)

    def retranslateUi(self, DebuggerRubyPage):
        self.headerLabel.setText(_translate("DebuggerRubyPage", "<b>Configure Ruby Debugger</b>", None))
        self.groupBox.setTitle(_translate("DebuggerRubyPage", "Ruby Interpreter for Debug Client", None))
        self.rubyInterpreterEdit.setToolTip(_translate("DebuggerRubyPage", "Enter the path of the Ruby interpreter to be used by the debug client.", None))
        self.rubyInterpreterButton.setToolTip(_translate("DebuggerRubyPage", "Press to select the Ruby interpreter via a file selection dialog", None))
        self.rubyInterpreterButton.setText(_translate("DebuggerRubyPage", "...", None))
        self.rbRedirectCheckBox.setToolTip(_translate("DebuggerRubyPage", "Select, to redirect stdin, stdout and stderr of the program being debugged to the eric4 IDE", None))
        self.rbRedirectCheckBox.setText(_translate("DebuggerRubyPage", "Redirect stdin/stdout/stderr", None))

