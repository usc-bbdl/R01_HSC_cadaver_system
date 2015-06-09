# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Preferences\ConfigurationPages\EditorCalltipsQScintillaPage.ui'
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

class Ui_EditorCalltipsQScintillaPage(object):
    def setupUi(self, EditorCalltipsQScintillaPage):
        EditorCalltipsQScintillaPage.setObjectName(_fromUtf8("EditorCalltipsQScintillaPage"))
        EditorCalltipsQScintillaPage.resize(406, 369)
        self.vboxlayout = QtGui.QVBoxLayout(EditorCalltipsQScintillaPage)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.headerLabel = QtGui.QLabel(EditorCalltipsQScintillaPage)
        self.headerLabel.setObjectName(_fromUtf8("headerLabel"))
        self.vboxlayout.addWidget(self.headerLabel)
        self.line18 = QtGui.QFrame(EditorCalltipsQScintillaPage)
        self.line18.setFrameShape(QtGui.QFrame.HLine)
        self.line18.setFrameShadow(QtGui.QFrame.Sunken)
        self.line18.setFrameShape(QtGui.QFrame.HLine)
        self.line18.setFrameShadow(QtGui.QFrame.Sunken)
        self.line18.setObjectName(_fromUtf8("line18"))
        self.vboxlayout.addWidget(self.line18)
        self.groupBox = QtGui.QGroupBox(EditorCalltipsQScintillaPage)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.vboxlayout1 = QtGui.QVBoxLayout(self.groupBox)
        self.vboxlayout1.setObjectName(_fromUtf8("vboxlayout1"))
        self.ctNoContextButton = QtGui.QRadioButton(self.groupBox)
        self.ctNoContextButton.setObjectName(_fromUtf8("ctNoContextButton"))
        self.vboxlayout1.addWidget(self.ctNoContextButton)
        self.ctNoAutoCompletionButton = QtGui.QRadioButton(self.groupBox)
        self.ctNoAutoCompletionButton.setObjectName(_fromUtf8("ctNoAutoCompletionButton"))
        self.vboxlayout1.addWidget(self.ctNoAutoCompletionButton)
        self.ctContextButton = QtGui.QRadioButton(self.groupBox)
        self.ctContextButton.setObjectName(_fromUtf8("ctContextButton"))
        self.vboxlayout1.addWidget(self.ctContextButton)
        self.line = QtGui.QFrame(self.groupBox)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.vboxlayout1.addWidget(self.line)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.vboxlayout1.addWidget(self.label)
        self.vboxlayout.addWidget(self.groupBox)
        spacerItem = QtGui.QSpacerItem(388, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vboxlayout.addItem(spacerItem)

        self.retranslateUi(EditorCalltipsQScintillaPage)
        QtCore.QMetaObject.connectSlotsByName(EditorCalltipsQScintillaPage)
        EditorCalltipsQScintillaPage.setTabOrder(self.ctNoContextButton, self.ctNoAutoCompletionButton)
        EditorCalltipsQScintillaPage.setTabOrder(self.ctNoAutoCompletionButton, self.ctContextButton)

    def retranslateUi(self, EditorCalltipsQScintillaPage):
        self.headerLabel.setText(_translate("EditorCalltipsQScintillaPage", "<b>Configure QScintilla Calltips</b>", None))
        self.groupBox.setTitle(_translate("EditorCalltipsQScintillaPage", "Context display options", None))
        self.ctNoContextButton.setToolTip(_translate("EditorCalltipsQScintillaPage", "Select to display calltips without a context", None))
        self.ctNoContextButton.setText(_translate("EditorCalltipsQScintillaPage", "Don\'t show context information", None))
        self.ctNoAutoCompletionButton.setToolTip(_translate("EditorCalltipsQScintillaPage", "Select to display calltips with a context only if the user hasn\'t already implicitly identified the context using autocompletion", None))
        self.ctNoAutoCompletionButton.setText(_translate("EditorCalltipsQScintillaPage", "Show context information, if no prior autocompletion", None))
        self.ctContextButton.setToolTip(_translate("EditorCalltipsQScintillaPage", "Select to display calltips with a context", None))
        self.ctContextButton.setText(_translate("EditorCalltipsQScintillaPage", "Show context information", None))
        self.label.setText(_translate("EditorCalltipsQScintillaPage", "A context is any scope (e.g. a C++ namespace or a Python module) prior to the function/method name.", None))

