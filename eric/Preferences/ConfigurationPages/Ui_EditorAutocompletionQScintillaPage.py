# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Preferences\ConfigurationPages\EditorAutocompletionQScintillaPage.ui'
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

class Ui_EditorAutocompletionQScintillaPage(object):
    def setupUi(self, EditorAutocompletionQScintillaPage):
        EditorAutocompletionQScintillaPage.setObjectName(_fromUtf8("EditorAutocompletionQScintillaPage"))
        EditorAutocompletionQScintillaPage.resize(506, 257)
        self.gridLayout = QtGui.QGridLayout(EditorAutocompletionQScintillaPage)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.headerLabel = QtGui.QLabel(EditorAutocompletionQScintillaPage)
        self.headerLabel.setObjectName(_fromUtf8("headerLabel"))
        self.gridLayout.addWidget(self.headerLabel, 0, 0, 1, 2)
        self.line6 = QtGui.QFrame(EditorAutocompletionQScintillaPage)
        self.line6.setFrameShape(QtGui.QFrame.HLine)
        self.line6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line6.setFrameShape(QtGui.QFrame.HLine)
        self.line6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line6.setObjectName(_fromUtf8("line6"))
        self.gridLayout.addWidget(self.line6, 1, 0, 1, 2)
        self.acShowSingleCheckBox = QtGui.QCheckBox(EditorAutocompletionQScintillaPage)
        self.acShowSingleCheckBox.setObjectName(_fromUtf8("acShowSingleCheckBox"))
        self.gridLayout.addWidget(self.acShowSingleCheckBox, 2, 0, 1, 1)
        self.acFillupsCheckBox = QtGui.QCheckBox(EditorAutocompletionQScintillaPage)
        self.acFillupsCheckBox.setObjectName(_fromUtf8("acFillupsCheckBox"))
        self.gridLayout.addWidget(self.acFillupsCheckBox, 2, 1, 1, 1)
        self.groupBox = QtGui.QGroupBox(EditorAutocompletionQScintillaPage)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.hboxlayout = QtGui.QHBoxLayout(self.groupBox)
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        self.acSourceDocumentRadioButton = QtGui.QRadioButton(self.groupBox)
        self.acSourceDocumentRadioButton.setObjectName(_fromUtf8("acSourceDocumentRadioButton"))
        self.hboxlayout.addWidget(self.acSourceDocumentRadioButton)
        self.acSourceAPIsRadioButton = QtGui.QRadioButton(self.groupBox)
        self.acSourceAPIsRadioButton.setObjectName(_fromUtf8("acSourceAPIsRadioButton"))
        self.hboxlayout.addWidget(self.acSourceAPIsRadioButton)
        self.acSourceAllRadioButton = QtGui.QRadioButton(self.groupBox)
        self.acSourceAllRadioButton.setObjectName(_fromUtf8("acSourceAllRadioButton"))
        self.hboxlayout.addWidget(self.acSourceAllRadioButton)
        self.gridLayout.addWidget(self.groupBox, 3, 0, 1, 2)
        spacerItem = QtGui.QSpacerItem(456, 51, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 4, 0, 1, 2)

        self.retranslateUi(EditorAutocompletionQScintillaPage)
        QtCore.QMetaObject.connectSlotsByName(EditorAutocompletionQScintillaPage)
        EditorAutocompletionQScintillaPage.setTabOrder(self.acShowSingleCheckBox, self.acFillupsCheckBox)
        EditorAutocompletionQScintillaPage.setTabOrder(self.acFillupsCheckBox, self.acSourceDocumentRadioButton)
        EditorAutocompletionQScintillaPage.setTabOrder(self.acSourceDocumentRadioButton, self.acSourceAPIsRadioButton)
        EditorAutocompletionQScintillaPage.setTabOrder(self.acSourceAPIsRadioButton, self.acSourceAllRadioButton)

    def retranslateUi(self, EditorAutocompletionQScintillaPage):
        self.headerLabel.setText(_translate("EditorAutocompletionQScintillaPage", "<b>Configure QScintilla Autocompletion</b>", None))
        self.acShowSingleCheckBox.setToolTip(_translate("EditorAutocompletionQScintillaPage", "Select this, if single entries shall be inserted automatically", None))
        self.acShowSingleCheckBox.setText(_translate("EditorAutocompletionQScintillaPage", "Show single", None))
        self.acFillupsCheckBox.setToolTip(_translate("EditorAutocompletionQScintillaPage", "Select to enable the use of fill-up characters to autocomplete the current word", None))
        self.acFillupsCheckBox.setWhatsThis(_translate("EditorAutocompletionQScintillaPage", "<b>Use fill-up characters</b><p>Select to enable the use of fill-up characters to autocomplete the current word. A fill-up character is one that, when entered while an auto-completion list is being displayed, causes the currently selected item from the list to be added to the text followed by the fill-up character.</p>", None))
        self.acFillupsCheckBox.setText(_translate("EditorAutocompletionQScintillaPage", "Use fill-up characters", None))
        self.groupBox.setTitle(_translate("EditorAutocompletionQScintillaPage", "Source", None))
        self.acSourceDocumentRadioButton.setToolTip(_translate("EditorAutocompletionQScintillaPage", "Select this to get autocompletion from current document", None))
        self.acSourceDocumentRadioButton.setText(_translate("EditorAutocompletionQScintillaPage", "from Document", None))
        self.acSourceAPIsRadioButton.setToolTip(_translate("EditorAutocompletionQScintillaPage", "Select this to get autocompletion from installed APIs", None))
        self.acSourceAPIsRadioButton.setText(_translate("EditorAutocompletionQScintillaPage", "from API files", None))
        self.acSourceAllRadioButton.setToolTip(_translate("EditorAutocompletionQScintillaPage", "Select this to get autocompletion from current document and installed APIs", None))
        self.acSourceAllRadioButton.setText(_translate("EditorAutocompletionQScintillaPage", "from Document and API files", None))

