# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Preferences\ConfigurationPages\ViewmanagerPage.ui'
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

class Ui_ViewmanagerPage(object):
    def setupUi(self, ViewmanagerPage):
        ViewmanagerPage.setObjectName(_fromUtf8("ViewmanagerPage"))
        ViewmanagerPage.resize(406, 315)
        self.vboxlayout = QtGui.QVBoxLayout(ViewmanagerPage)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.headerLabel = QtGui.QLabel(ViewmanagerPage)
        self.headerLabel.setObjectName(_fromUtf8("headerLabel"))
        self.vboxlayout.addWidget(self.headerLabel)
        self.line9_2 = QtGui.QFrame(ViewmanagerPage)
        self.line9_2.setFrameShape(QtGui.QFrame.HLine)
        self.line9_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line9_2.setFrameShape(QtGui.QFrame.HLine)
        self.line9_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line9_2.setObjectName(_fromUtf8("line9_2"))
        self.vboxlayout.addWidget(self.line9_2)
        self.TextLabel1_2_2_2_3 = QtGui.QLabel(ViewmanagerPage)
        self.TextLabel1_2_2_2_3.setObjectName(_fromUtf8("TextLabel1_2_2_2_3"))
        self.vboxlayout.addWidget(self.TextLabel1_2_2_2_3)
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        self.windowLabel = QtGui.QLabel(ViewmanagerPage)
        self.windowLabel.setObjectName(_fromUtf8("windowLabel"))
        self.hboxlayout.addWidget(self.windowLabel)
        self.windowComboBox = QtGui.QComboBox(ViewmanagerPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.windowComboBox.sizePolicy().hasHeightForWidth())
        self.windowComboBox.setSizePolicy(sizePolicy)
        self.windowComboBox.setObjectName(_fromUtf8("windowComboBox"))
        self.hboxlayout.addWidget(self.windowComboBox)
        self.vboxlayout.addLayout(self.hboxlayout)
        self.previewPixmap = QtGui.QLabel(ViewmanagerPage)
        self.previewPixmap.setScaledContents(False)
        self.previewPixmap.setAlignment(QtCore.Qt.AlignCenter)
        self.previewPixmap.setObjectName(_fromUtf8("previewPixmap"))
        self.vboxlayout.addWidget(self.previewPixmap)
        self.line = QtGui.QFrame(ViewmanagerPage)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.vboxlayout.addWidget(self.line)
        self.tabViewGroupBox = QtGui.QGroupBox(ViewmanagerPage)
        self.tabViewGroupBox.setEnabled(False)
        self.tabViewGroupBox.setObjectName(_fromUtf8("tabViewGroupBox"))
        self.vboxlayout1 = QtGui.QVBoxLayout(self.tabViewGroupBox)
        self.vboxlayout1.setObjectName(_fromUtf8("vboxlayout1"))
        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setObjectName(_fromUtf8("hboxlayout1"))
        self.filenameLengthLabel = QtGui.QLabel(self.tabViewGroupBox)
        self.filenameLengthLabel.setObjectName(_fromUtf8("filenameLengthLabel"))
        self.hboxlayout1.addWidget(self.filenameLengthLabel)
        self.filenameLengthSpinBox = QtGui.QSpinBox(self.tabViewGroupBox)
        self.filenameLengthSpinBox.setMinimum(1)
        self.filenameLengthSpinBox.setMaximum(100)
        self.filenameLengthSpinBox.setProperty("value", 40)
        self.filenameLengthSpinBox.setObjectName(_fromUtf8("filenameLengthSpinBox"))
        self.hboxlayout1.addWidget(self.filenameLengthSpinBox)
        spacerItem = QtGui.QSpacerItem(81, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout1.addItem(spacerItem)
        self.vboxlayout1.addLayout(self.hboxlayout1)
        self.filenameOnlyCheckBox = QtGui.QCheckBox(self.tabViewGroupBox)
        self.filenameOnlyCheckBox.setObjectName(_fromUtf8("filenameOnlyCheckBox"))
        self.vboxlayout1.addWidget(self.filenameOnlyCheckBox)
        self.vboxlayout.addWidget(self.tabViewGroupBox)
        self.groupBox_7 = QtGui.QGroupBox(ViewmanagerPage)
        self.groupBox_7.setObjectName(_fromUtf8("groupBox_7"))
        self.hboxlayout2 = QtGui.QHBoxLayout(self.groupBox_7)
        self.hboxlayout2.setObjectName(_fromUtf8("hboxlayout2"))
        self.label = QtGui.QLabel(self.groupBox_7)
        self.label.setObjectName(_fromUtf8("label"))
        self.hboxlayout2.addWidget(self.label)
        self.recentFilesSpinBox = QtGui.QSpinBox(self.groupBox_7)
        self.recentFilesSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.recentFilesSpinBox.setMinimum(5)
        self.recentFilesSpinBox.setMaximum(50)
        self.recentFilesSpinBox.setObjectName(_fromUtf8("recentFilesSpinBox"))
        self.hboxlayout2.addWidget(self.recentFilesSpinBox)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout2.addItem(spacerItem1)
        self.vboxlayout.addWidget(self.groupBox_7)
        spacerItem2 = QtGui.QSpacerItem(388, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vboxlayout.addItem(spacerItem2)
        self.windowLabel.setBuddy(self.windowComboBox)

        self.retranslateUi(ViewmanagerPage)
        QtCore.QMetaObject.connectSlotsByName(ViewmanagerPage)

    def retranslateUi(self, ViewmanagerPage):
        self.headerLabel.setText(_translate("ViewmanagerPage", "<b>Configure viewmanager</b>", None))
        self.TextLabel1_2_2_2_3.setText(_translate("ViewmanagerPage", "<font color=\"#FF0000\"><b>Note:</b> This setting is activated at the next startup of the application.</font>", None))
        self.windowLabel.setText(_translate("ViewmanagerPage", "Window view:", None))
        self.windowComboBox.setToolTip(_translate("ViewmanagerPage", "Select the window view type.", None))
        self.windowComboBox.setWhatsThis(_translate("ViewmanagerPage", "The kind of window view can be selected from this list. The picture below gives an example of the selected view type.", None))
        self.previewPixmap.setToolTip(_translate("ViewmanagerPage", "Preview of selected window view", None))
        self.previewPixmap.setWhatsThis(_translate("ViewmanagerPage", "This displays a small preview of the selected window view. This is the way the source windows are displayed in the application.", None))
        self.tabViewGroupBox.setTitle(_translate("ViewmanagerPage", "Tabbed View", None))
        self.filenameLengthLabel.setText(_translate("ViewmanagerPage", "Filename Length of Tab:", None))
        self.filenameLengthSpinBox.setToolTip(_translate("ViewmanagerPage", "Enter the number of characters to be shown in the tab.", None))
        self.filenameOnlyCheckBox.setToolTip(_translate("ViewmanagerPage", "Select to display the filename only", None))
        self.filenameOnlyCheckBox.setText(_translate("ViewmanagerPage", "Show filename only", None))
        self.groupBox_7.setTitle(_translate("ViewmanagerPage", "Recent Files", None))
        self.label.setText(_translate("ViewmanagerPage", "Number of recent files:", None))
        self.recentFilesSpinBox.setToolTip(_translate("ViewmanagerPage", "Enter the number of recent files to remember", None))

