# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Preferences\ConfigurationPages\EditorCalltipsPage.ui'
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

class Ui_EditorCalltipsPage(object):
    def setupUi(self, EditorCalltipsPage):
        EditorCalltipsPage.setObjectName(_fromUtf8("EditorCalltipsPage"))
        EditorCalltipsPage.resize(406, 369)
        self.verticalLayout_2 = QtGui.QVBoxLayout(EditorCalltipsPage)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.headerLabel = QtGui.QLabel(EditorCalltipsPage)
        self.headerLabel.setObjectName(_fromUtf8("headerLabel"))
        self.verticalLayout_2.addWidget(self.headerLabel)
        self.line18 = QtGui.QFrame(EditorCalltipsPage)
        self.line18.setFrameShape(QtGui.QFrame.HLine)
        self.line18.setFrameShadow(QtGui.QFrame.Sunken)
        self.line18.setFrameShape(QtGui.QFrame.HLine)
        self.line18.setFrameShadow(QtGui.QFrame.Sunken)
        self.line18.setObjectName(_fromUtf8("line18"))
        self.verticalLayout_2.addWidget(self.line18)
        self.ctEnabledCheckBox = QtGui.QCheckBox(EditorCalltipsPage)
        self.ctEnabledCheckBox.setObjectName(_fromUtf8("ctEnabledCheckBox"))
        self.verticalLayout_2.addWidget(self.ctEnabledCheckBox)
        self.frame = QtGui.QFrame(EditorCalltipsPage)
        self.frame.setEnabled(False)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.textLabel2 = QtGui.QLabel(self.frame)
        self.textLabel2.setObjectName(_fromUtf8("textLabel2"))
        self.horizontalLayout.addWidget(self.textLabel2)
        self.ctVisibleSlider = QtGui.QSlider(self.frame)
        self.ctVisibleSlider.setMaximum(20)
        self.ctVisibleSlider.setOrientation(QtCore.Qt.Horizontal)
        self.ctVisibleSlider.setTickInterval(1)
        self.ctVisibleSlider.setObjectName(_fromUtf8("ctVisibleSlider"))
        self.horizontalLayout.addWidget(self.ctVisibleSlider)
        self.lCDNumber5 = QtGui.QLCDNumber(self.frame)
        self.lCDNumber5.setDigitCount(2)
        self.lCDNumber5.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lCDNumber5.setObjectName(_fromUtf8("lCDNumber5"))
        self.horizontalLayout.addWidget(self.lCDNumber5)
        self.verticalLayout_2.addWidget(self.frame)
        self.groupBox_2 = QtGui.QGroupBox(EditorCalltipsPage)
        self.groupBox_2.setEnabled(False)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.hboxlayout = QtGui.QHBoxLayout(self.groupBox_2)
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        self.TextLabel2_2_2_2 = QtGui.QLabel(self.groupBox_2)
        self.TextLabel2_2_2_2.setObjectName(_fromUtf8("TextLabel2_2_2_2"))
        self.hboxlayout.addWidget(self.TextLabel2_2_2_2)
        self.calltipsBackgroundButton = QtGui.QPushButton(self.groupBox_2)
        self.calltipsBackgroundButton.setMinimumSize(QtCore.QSize(100, 0))
        self.calltipsBackgroundButton.setText(_fromUtf8(""))
        self.calltipsBackgroundButton.setObjectName(_fromUtf8("calltipsBackgroundButton"))
        self.hboxlayout.addWidget(self.calltipsBackgroundButton)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.groupBox = QtGui.QGroupBox(EditorCalltipsPage)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.ctScintillaCheckBox = QtGui.QCheckBox(self.groupBox)
        self.ctScintillaCheckBox.setObjectName(_fromUtf8("ctScintillaCheckBox"))
        self.verticalLayout.addWidget(self.ctScintillaCheckBox)
        self.verticalLayout_2.addWidget(self.groupBox)
        spacerItem1 = QtGui.QSpacerItem(388, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)

        self.retranslateUi(EditorCalltipsPage)
        QtCore.QObject.connect(self.ctEnabledCheckBox, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.groupBox_2.setEnabled)
        QtCore.QObject.connect(self.ctEnabledCheckBox, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.frame.setEnabled)
        QtCore.QObject.connect(self.ctVisibleSlider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.lCDNumber5.display)
        QtCore.QMetaObject.connectSlotsByName(EditorCalltipsPage)
        EditorCalltipsPage.setTabOrder(self.ctEnabledCheckBox, self.ctVisibleSlider)
        EditorCalltipsPage.setTabOrder(self.ctVisibleSlider, self.calltipsBackgroundButton)
        EditorCalltipsPage.setTabOrder(self.calltipsBackgroundButton, self.ctScintillaCheckBox)

    def retranslateUi(self, EditorCalltipsPage):
        self.headerLabel.setText(_translate("EditorCalltipsPage", "<b>Configure Calltips</b>", None))
        self.ctEnabledCheckBox.setToolTip(_translate("EditorCalltipsPage", "Select this to enable calltips", None))
        self.ctEnabledCheckBox.setText(_translate("EditorCalltipsPage", "Calltips Enabled", None))
        self.textLabel2.setText(_translate("EditorCalltipsPage", "Visible calltips:", None))
        self.ctVisibleSlider.setToolTip(_translate("EditorCalltipsPage", "Move to set the maximum number of calltips shown (0 = all available)", None))
        self.lCDNumber5.setToolTip(_translate("EditorCalltipsPage", "Displays the maximum number of calltips to be shown", None))
        self.groupBox_2.setTitle(_translate("EditorCalltipsPage", "Colours", None))
        self.TextLabel2_2_2_2.setText(_translate("EditorCalltipsPage", "Background colour:", None))
        self.calltipsBackgroundButton.setToolTip(_translate("EditorCalltipsPage", "Select the background colour for calltips.", None))
        self.groupBox.setTitle(_translate("EditorCalltipsPage", "Plug-In Behavior", None))
        self.ctScintillaCheckBox.setToolTip(_translate("EditorCalltipsPage", "Select to show QScintilla provided calltips, if the selected plugin fails", None))
        self.ctScintillaCheckBox.setWhatsThis(_translate("EditorCalltipsPage", "Qscintilla provided calltips are shown, if this option is enabled and calltips shall be provided by a plug-in (see calltips sub-page of the plug-in) and the plugin-in doesn\'t deliver any calltips.", None))
        self.ctScintillaCheckBox.setText(_translate("EditorCalltipsPage", "Show QScintilla calltips, if plug-in fails", None))

