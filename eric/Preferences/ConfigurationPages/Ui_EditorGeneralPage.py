# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Preferences\ConfigurationPages\EditorGeneralPage.ui'
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

class Ui_EditorGeneralPage(object):
    def setupUi(self, EditorGeneralPage):
        EditorGeneralPage.setObjectName(_fromUtf8("EditorGeneralPage"))
        EditorGeneralPage.resize(553, 593)
        self.verticalLayout = QtGui.QVBoxLayout(EditorGeneralPage)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.headerLabel = QtGui.QLabel(EditorGeneralPage)
        self.headerLabel.setObjectName(_fromUtf8("headerLabel"))
        self.verticalLayout.addWidget(self.headerLabel)
        self.line2 = QtGui.QFrame(EditorGeneralPage)
        self.line2.setFrameShape(QtGui.QFrame.HLine)
        self.line2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line2.setFrameShape(QtGui.QFrame.HLine)
        self.line2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line2.setObjectName(_fromUtf8("line2"))
        self.verticalLayout.addWidget(self.line2)
        self.groupBox_5 = QtGui.QGroupBox(EditorGeneralPage)
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.vboxlayout = QtGui.QVBoxLayout(self.groupBox_5)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.gridlayout = QtGui.QGridLayout()
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.TextLabel13_3 = QtGui.QLabel(self.groupBox_5)
        self.TextLabel13_3.setObjectName(_fromUtf8("TextLabel13_3"))
        self.gridlayout.addWidget(self.TextLabel13_3, 0, 0, 1, 1)
        self.tabwidthSlider = QtGui.QSlider(self.groupBox_5)
        self.tabwidthSlider.setMinimum(1)
        self.tabwidthSlider.setMaximum(20)
        self.tabwidthSlider.setProperty("value", 4)
        self.tabwidthSlider.setOrientation(QtCore.Qt.Horizontal)
        self.tabwidthSlider.setTickInterval(1)
        self.tabwidthSlider.setObjectName(_fromUtf8("tabwidthSlider"))
        self.gridlayout.addWidget(self.tabwidthSlider, 0, 1, 1, 1)
        self.tabwidthLCD = QtGui.QLCDNumber(self.groupBox_5)
        self.tabwidthLCD.setDigitCount(2)
        self.tabwidthLCD.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.tabwidthLCD.setProperty("value", 4.0)
        self.tabwidthLCD.setObjectName(_fromUtf8("tabwidthLCD"))
        self.gridlayout.addWidget(self.tabwidthLCD, 0, 2, 1, 1)
        self.TextLabel13_2_3 = QtGui.QLabel(self.groupBox_5)
        self.TextLabel13_2_3.setObjectName(_fromUtf8("TextLabel13_2_3"))
        self.gridlayout.addWidget(self.TextLabel13_2_3, 1, 0, 1, 1)
        self.indentwidthSlider = QtGui.QSlider(self.groupBox_5)
        self.indentwidthSlider.setMinimum(1)
        self.indentwidthSlider.setMaximum(20)
        self.indentwidthSlider.setProperty("value", 4)
        self.indentwidthSlider.setOrientation(QtCore.Qt.Horizontal)
        self.indentwidthSlider.setTickInterval(1)
        self.indentwidthSlider.setObjectName(_fromUtf8("indentwidthSlider"))
        self.gridlayout.addWidget(self.indentwidthSlider, 1, 1, 1, 1)
        self.indentwidthLCD = QtGui.QLCDNumber(self.groupBox_5)
        self.indentwidthLCD.setDigitCount(2)
        self.indentwidthLCD.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.indentwidthLCD.setProperty("value", 4.0)
        self.indentwidthLCD.setObjectName(_fromUtf8("indentwidthLCD"))
        self.gridlayout.addWidget(self.indentwidthLCD, 1, 2, 1, 1)
        self.vboxlayout.addLayout(self.gridlayout)
        self.gridlayout1 = QtGui.QGridLayout()
        self.gridlayout1.setObjectName(_fromUtf8("gridlayout1"))
        self.indentguidesCheckBox = QtGui.QCheckBox(self.groupBox_5)
        self.indentguidesCheckBox.setObjectName(_fromUtf8("indentguidesCheckBox"))
        self.gridlayout1.addWidget(self.indentguidesCheckBox, 0, 0, 1, 1)
        self.tabforindentationCheckBox = QtGui.QCheckBox(self.groupBox_5)
        self.tabforindentationCheckBox.setObjectName(_fromUtf8("tabforindentationCheckBox"))
        self.gridlayout1.addWidget(self.tabforindentationCheckBox, 0, 1, 1, 1)
        self.autoindentCheckBox = QtGui.QCheckBox(self.groupBox_5)
        self.autoindentCheckBox.setObjectName(_fromUtf8("autoindentCheckBox"))
        self.gridlayout1.addWidget(self.autoindentCheckBox, 1, 0, 1, 1)
        self.converttabsCheckBox = QtGui.QCheckBox(self.groupBox_5)
        self.converttabsCheckBox.setObjectName(_fromUtf8("converttabsCheckBox"))
        self.gridlayout1.addWidget(self.converttabsCheckBox, 1, 1, 1, 1)
        self.tabindentsCheckBox = QtGui.QCheckBox(self.groupBox_5)
        self.tabindentsCheckBox.setObjectName(_fromUtf8("tabindentsCheckBox"))
        self.gridlayout1.addWidget(self.tabindentsCheckBox, 2, 0, 1, 1)
        self.vboxlayout.addLayout(self.gridlayout1)
        self.verticalLayout.addWidget(self.groupBox_5)
        self.groupBox = QtGui.QGroupBox(EditorGeneralPage)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.comment0CheckBox = QtGui.QCheckBox(self.groupBox)
        self.comment0CheckBox.setObjectName(_fromUtf8("comment0CheckBox"))
        self.gridLayout.addWidget(self.comment0CheckBox, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        spacerItem = QtGui.QSpacerItem(535, 101, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.TextLabel13_3.setBuddy(self.tabwidthSlider)
        self.TextLabel13_2_3.setBuddy(self.indentwidthSlider)

        self.retranslateUi(EditorGeneralPage)
        QtCore.QObject.connect(self.tabwidthSlider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.tabwidthLCD.display)
        QtCore.QObject.connect(self.indentwidthSlider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.indentwidthLCD.display)
        QtCore.QMetaObject.connectSlotsByName(EditorGeneralPage)
        EditorGeneralPage.setTabOrder(self.tabwidthSlider, self.indentwidthSlider)
        EditorGeneralPage.setTabOrder(self.indentwidthSlider, self.indentguidesCheckBox)
        EditorGeneralPage.setTabOrder(self.indentguidesCheckBox, self.autoindentCheckBox)
        EditorGeneralPage.setTabOrder(self.autoindentCheckBox, self.tabindentsCheckBox)
        EditorGeneralPage.setTabOrder(self.tabindentsCheckBox, self.tabforindentationCheckBox)
        EditorGeneralPage.setTabOrder(self.tabforindentationCheckBox, self.converttabsCheckBox)

    def retranslateUi(self, EditorGeneralPage):
        self.headerLabel.setText(_translate("EditorGeneralPage", "<b>Configure general editor settings</b>", None))
        self.groupBox_5.setTitle(_translate("EditorGeneralPage", "Tabs && Indentation", None))
        self.TextLabel13_3.setText(_translate("EditorGeneralPage", "Tab width:", None))
        self.tabwidthSlider.setToolTip(_translate("EditorGeneralPage", "Move to set the tab width.", None))
        self.tabwidthLCD.setToolTip(_translate("EditorGeneralPage", "Displays the selected tab width.", None))
        self.TextLabel13_2_3.setText(_translate("EditorGeneralPage", "Indentation width:", None))
        self.indentwidthSlider.setToolTip(_translate("EditorGeneralPage", "Move to set the indentation width.", None))
        self.indentwidthLCD.setToolTip(_translate("EditorGeneralPage", "Displays the selected indentation width.", None))
        self.indentguidesCheckBox.setToolTip(_translate("EditorGeneralPage", "Select whether indentation guides should be shown.", None))
        self.indentguidesCheckBox.setText(_translate("EditorGeneralPage", "Show Indentation Guides", None))
        self.tabforindentationCheckBox.setToolTip(_translate("EditorGeneralPage", "Select whether tab characters are used for indentations.", None))
        self.tabforindentationCheckBox.setText(_translate("EditorGeneralPage", "Use tabs for indentations", None))
        self.autoindentCheckBox.setToolTip(_translate("EditorGeneralPage", "Select whether autoindentation shall be enabled", None))
        self.autoindentCheckBox.setText(_translate("EditorGeneralPage", "Auto indentation", None))
        self.converttabsCheckBox.setToolTip(_translate("EditorGeneralPage", "Select whether tabs shall be converted upon opening the file", None))
        self.converttabsCheckBox.setText(_translate("EditorGeneralPage", "Convert tabs upon open", None))
        self.tabindentsCheckBox.setToolTip(_translate("EditorGeneralPage", "Select whether pressing the tab key indents.", None))
        self.tabindentsCheckBox.setText(_translate("EditorGeneralPage", "Tab key indents", None))
        self.groupBox.setTitle(_translate("EditorGeneralPage", "Comments", None))
        self.comment0CheckBox.setToolTip(_translate("EditorGeneralPage", "Select to insert the comment sign at column 0", None))
        self.comment0CheckBox.setWhatsThis(_translate("EditorGeneralPage", "<b>Insert comment at column 0</b><p>Select to insert the comment sign at column 0. Otherwise, the comment sign is inserted at the first non-whitespace position.</p>", None))
        self.comment0CheckBox.setText(_translate("EditorGeneralPage", "Insert comment at column 0", None))

