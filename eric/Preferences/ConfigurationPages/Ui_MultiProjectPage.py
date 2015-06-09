# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Preferences\ConfigurationPages\MultiProjectPage.ui'
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

class Ui_MultiProjectPage(object):
    def setupUi(self, MultiProjectPage):
        MultiProjectPage.setObjectName(_fromUtf8("MultiProjectPage"))
        MultiProjectPage.resize(494, 357)
        self.verticalLayout = QtGui.QVBoxLayout(MultiProjectPage)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.headerLabel = QtGui.QLabel(MultiProjectPage)
        self.headerLabel.setObjectName(_fromUtf8("headerLabel"))
        self.verticalLayout.addWidget(self.headerLabel)
        self.line8 = QtGui.QFrame(MultiProjectPage)
        self.line8.setFrameShape(QtGui.QFrame.HLine)
        self.line8.setFrameShadow(QtGui.QFrame.Sunken)
        self.line8.setFrameShape(QtGui.QFrame.HLine)
        self.line8.setFrameShadow(QtGui.QFrame.Sunken)
        self.line8.setObjectName(_fromUtf8("line8"))
        self.verticalLayout.addWidget(self.line8)
        self.groupBox_2 = QtGui.QGroupBox(MultiProjectPage)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.workspaceEdit = QtGui.QLineEdit(self.groupBox_2)
        self.workspaceEdit.setObjectName(_fromUtf8("workspaceEdit"))
        self.horizontalLayout.addWidget(self.workspaceEdit)
        self.workspaceButton = QtGui.QPushButton(self.groupBox_2)
        self.workspaceButton.setText(_fromUtf8("..."))
        self.workspaceButton.setObjectName(_fromUtf8("workspaceButton"))
        self.horizontalLayout.addWidget(self.workspaceButton)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox = QtGui.QGroupBox(MultiProjectPage)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.vboxlayout = QtGui.QVBoxLayout(self.groupBox)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.openMasterAutomaticallyCheckBox = QtGui.QCheckBox(self.groupBox)
        self.openMasterAutomaticallyCheckBox.setObjectName(_fromUtf8("openMasterAutomaticallyCheckBox"))
        self.vboxlayout.addWidget(self.openMasterAutomaticallyCheckBox)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_6 = QtGui.QGroupBox(MultiProjectPage)
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.vboxlayout1 = QtGui.QVBoxLayout(self.groupBox_6)
        self.vboxlayout1.setObjectName(_fromUtf8("vboxlayout1"))
        self.multiProjectTimestampCheckBox = QtGui.QCheckBox(self.groupBox_6)
        self.multiProjectTimestampCheckBox.setObjectName(_fromUtf8("multiProjectTimestampCheckBox"))
        self.vboxlayout1.addWidget(self.multiProjectTimestampCheckBox)
        self.verticalLayout.addWidget(self.groupBox_6)
        self.groupBox_7 = QtGui.QGroupBox(MultiProjectPage)
        self.groupBox_7.setObjectName(_fromUtf8("groupBox_7"))
        self.vboxlayout2 = QtGui.QVBoxLayout(self.groupBox_7)
        self.vboxlayout2.setObjectName(_fromUtf8("vboxlayout2"))
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        self.label = QtGui.QLabel(self.groupBox_7)
        self.label.setObjectName(_fromUtf8("label"))
        self.hboxlayout.addWidget(self.label)
        self.multiProjectRecentSpinBox = QtGui.QSpinBox(self.groupBox_7)
        self.multiProjectRecentSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.multiProjectRecentSpinBox.setMinimum(5)
        self.multiProjectRecentSpinBox.setMaximum(50)
        self.multiProjectRecentSpinBox.setObjectName(_fromUtf8("multiProjectRecentSpinBox"))
        self.hboxlayout.addWidget(self.multiProjectRecentSpinBox)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)
        self.vboxlayout2.addLayout(self.hboxlayout)
        self.verticalLayout.addWidget(self.groupBox_7)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)

        self.retranslateUi(MultiProjectPage)
        QtCore.QMetaObject.connectSlotsByName(MultiProjectPage)
        MultiProjectPage.setTabOrder(self.workspaceEdit, self.workspaceButton)
        MultiProjectPage.setTabOrder(self.workspaceButton, self.openMasterAutomaticallyCheckBox)
        MultiProjectPage.setTabOrder(self.openMasterAutomaticallyCheckBox, self.multiProjectTimestampCheckBox)
        MultiProjectPage.setTabOrder(self.multiProjectTimestampCheckBox, self.multiProjectRecentSpinBox)

    def retranslateUi(self, MultiProjectPage):
        self.headerLabel.setText(_translate("MultiProjectPage", "<b>Configure multiproject settings</b>", None))
        self.groupBox_2.setTitle(_translate("MultiProjectPage", "Workspace", None))
        self.workspaceEdit.setToolTip(_translate("MultiProjectPage", "Enter the name of the workspace directory", None))
        self.workspaceEdit.setWhatsThis(_translate("MultiProjectPage", "<b>Workspace Directory</b>\n"
"<p>Enter the directory of the workspace. This directory is used as the default for opening or saving new files or projects.</p>", None))
        self.workspaceButton.setToolTip(_translate("MultiProjectPage", "Select the workspace directory via a directory selection button", None))
        self.groupBox.setTitle(_translate("MultiProjectPage", "Master Project", None))
        self.openMasterAutomaticallyCheckBox.setToolTip(_translate("MultiProjectPage", "Select to open the master project automatically upon opening the multiproject", None))
        self.openMasterAutomaticallyCheckBox.setText(_translate("MultiProjectPage", "Open master project automatically", None))
        self.groupBox_6.setTitle(_translate("MultiProjectPage", "XML", None))
        self.multiProjectTimestampCheckBox.setToolTip(_translate("MultiProjectPage", "Select, if a timestamp should be written to all multiproject related XML files", None))
        self.multiProjectTimestampCheckBox.setText(_translate("MultiProjectPage", "Include timestamp in multiproject related XML files", None))
        self.groupBox_7.setTitle(_translate("MultiProjectPage", "Recent Multiprojects", None))
        self.label.setText(_translate("MultiProjectPage", "Number of recent multiprojects:", None))
        self.multiProjectRecentSpinBox.setToolTip(_translate("MultiProjectPage", "Enter the number of recent multiprojects to remember", None))

