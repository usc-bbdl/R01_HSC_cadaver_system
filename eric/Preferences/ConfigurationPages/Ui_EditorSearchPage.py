# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Preferences\ConfigurationPages\EditorSearchPage.ui'
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

class Ui_EditorSearchPage(object):
    def setupUi(self, EditorSearchPage):
        EditorSearchPage.setObjectName(_fromUtf8("EditorSearchPage"))
        EditorSearchPage.resize(576, 596)
        self.vboxlayout = QtGui.QVBoxLayout(EditorSearchPage)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.headerLabel = QtGui.QLabel(EditorSearchPage)
        self.headerLabel.setObjectName(_fromUtf8("headerLabel"))
        self.vboxlayout.addWidget(self.headerLabel)
        self.line3 = QtGui.QFrame(EditorSearchPage)
        self.line3.setFrameShape(QtGui.QFrame.HLine)
        self.line3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line3.setFrameShape(QtGui.QFrame.HLine)
        self.line3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line3.setObjectName(_fromUtf8("line3"))
        self.vboxlayout.addWidget(self.line3)
        self.groupBox_4 = QtGui.QGroupBox(EditorSearchPage)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.vboxlayout1 = QtGui.QVBoxLayout(self.groupBox_4)
        self.vboxlayout1.setObjectName(_fromUtf8("vboxlayout1"))
        self.occurrencesMarkersEnabledCheckBox = QtGui.QCheckBox(self.groupBox_4)
        self.occurrencesMarkersEnabledCheckBox.setObjectName(_fromUtf8("occurrencesMarkersEnabledCheckBox"))
        self.vboxlayout1.addWidget(self.occurrencesMarkersEnabledCheckBox)
        self.searchMarkersEnabledCheckBox = QtGui.QCheckBox(self.groupBox_4)
        self.searchMarkersEnabledCheckBox.setObjectName(_fromUtf8("searchMarkersEnabledCheckBox"))
        self.vboxlayout1.addWidget(self.searchMarkersEnabledCheckBox)
        self.quicksearchMarkersEnabledCheckBox = QtGui.QCheckBox(self.groupBox_4)
        self.quicksearchMarkersEnabledCheckBox.setObjectName(_fromUtf8("quicksearchMarkersEnabledCheckBox"))
        self.vboxlayout1.addWidget(self.quicksearchMarkersEnabledCheckBox)
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        self.label = QtGui.QLabel(self.groupBox_4)
        self.label.setObjectName(_fromUtf8("label"))
        self.hboxlayout.addWidget(self.label)
        self.markOccurrencesTimeoutSpinBox = QtGui.QSpinBox(self.groupBox_4)
        self.markOccurrencesTimeoutSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.markOccurrencesTimeoutSpinBox.setButtonSymbols(QtGui.QAbstractSpinBox.PlusMinus)
        self.markOccurrencesTimeoutSpinBox.setCorrectionMode(QtGui.QAbstractSpinBox.CorrectToNearestValue)
        self.markOccurrencesTimeoutSpinBox.setMinimum(100)
        self.markOccurrencesTimeoutSpinBox.setMaximum(5000)
        self.markOccurrencesTimeoutSpinBox.setSingleStep(100)
        self.markOccurrencesTimeoutSpinBox.setObjectName(_fromUtf8("markOccurrencesTimeoutSpinBox"))
        self.hboxlayout.addWidget(self.markOccurrencesTimeoutSpinBox)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)
        self.vboxlayout1.addLayout(self.hboxlayout)
        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setObjectName(_fromUtf8("hboxlayout1"))
        self.TextLabel2_2_2_2_2_2 = QtGui.QLabel(self.groupBox_4)
        self.TextLabel2_2_2_2_2_2.setObjectName(_fromUtf8("TextLabel2_2_2_2_2_2"))
        self.hboxlayout1.addWidget(self.TextLabel2_2_2_2_2_2)
        self.searchMarkerButton = QtGui.QPushButton(self.groupBox_4)
        self.searchMarkerButton.setMinimumSize(QtCore.QSize(100, 0))
        self.searchMarkerButton.setText(_fromUtf8(""))
        self.searchMarkerButton.setObjectName(_fromUtf8("searchMarkerButton"))
        self.hboxlayout1.addWidget(self.searchMarkerButton)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout1.addItem(spacerItem1)
        self.vboxlayout1.addLayout(self.hboxlayout1)
        self.vboxlayout.addWidget(self.groupBox_4)
        spacerItem2 = QtGui.QSpacerItem(558, 231, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vboxlayout.addItem(spacerItem2)

        self.retranslateUi(EditorSearchPage)
        QtCore.QMetaObject.connectSlotsByName(EditorSearchPage)
        EditorSearchPage.setTabOrder(self.occurrencesMarkersEnabledCheckBox, self.searchMarkersEnabledCheckBox)
        EditorSearchPage.setTabOrder(self.searchMarkersEnabledCheckBox, self.quicksearchMarkersEnabledCheckBox)
        EditorSearchPage.setTabOrder(self.quicksearchMarkersEnabledCheckBox, self.markOccurrencesTimeoutSpinBox)
        EditorSearchPage.setTabOrder(self.markOccurrencesTimeoutSpinBox, self.searchMarkerButton)

    def retranslateUi(self, EditorSearchPage):
        self.headerLabel.setText(_translate("EditorSearchPage", "<b>Configure editor search options</b>", None))
        self.groupBox_4.setTitle(_translate("EditorSearchPage", "Search Markers", None))
        self.occurrencesMarkersEnabledCheckBox.setToolTip(_translate("EditorSearchPage", "Select, whether markers for all occurrences of the current word shall be shown", None))
        self.occurrencesMarkersEnabledCheckBox.setText(_translate("EditorSearchPage", "Highlight all occurrences of current word", None))
        self.searchMarkersEnabledCheckBox.setToolTip(_translate("EditorSearchPage", "Select, whether search markers shall be shown for a standard search", None))
        self.searchMarkersEnabledCheckBox.setText(_translate("EditorSearchPage", "Highlight all occurrences of search text", None))
        self.quicksearchMarkersEnabledCheckBox.setToolTip(_translate("EditorSearchPage", "Select, whether search markers shall be shown for a quicksearch", None))
        self.quicksearchMarkersEnabledCheckBox.setText(_translate("EditorSearchPage", "Highlight all occurrences of quicksearch text", None))
        self.label.setText(_translate("EditorSearchPage", "Timeout for current word highlighting:", None))
        self.markOccurrencesTimeoutSpinBox.setToolTip(_translate("EditorSearchPage", "Enter the time in milliseconds after which occurrences of the current word shall be highlighted", None))
        self.markOccurrencesTimeoutSpinBox.setSuffix(_translate("EditorSearchPage", " ms", None))
        self.TextLabel2_2_2_2_2_2.setText(_translate("EditorSearchPage", "Marker Colour:", None))
        self.searchMarkerButton.setToolTip(_translate("EditorSearchPage", "Select the colour for the search markers.", None))

