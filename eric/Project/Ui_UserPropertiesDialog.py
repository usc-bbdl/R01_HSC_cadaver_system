# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Project\UserPropertiesDialog.ui'
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

class Ui_UserPropertiesDialog(object):
    def setupUi(self, UserPropertiesDialog):
        UserPropertiesDialog.setObjectName(_fromUtf8("UserPropertiesDialog"))
        UserPropertiesDialog.resize(543, 309)
        UserPropertiesDialog.setSizeGripEnabled(True)
        self._2 = QtGui.QVBoxLayout(UserPropertiesDialog)
        self._2.setObjectName(_fromUtf8("_2"))
        self.groupBox_2 = QtGui.QGroupBox(UserPropertiesDialog)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self._3 = QtGui.QHBoxLayout(self.groupBox_2)
        self._3.setObjectName(_fromUtf8("_3"))
        self.vcsStatusMonitorIntervalSpinBox = QtGui.QSpinBox(self.groupBox_2)
        self.vcsStatusMonitorIntervalSpinBox.setMaximum(3600)
        self.vcsStatusMonitorIntervalSpinBox.setObjectName(_fromUtf8("vcsStatusMonitorIntervalSpinBox"))
        self._3.addWidget(self.vcsStatusMonitorIntervalSpinBox)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self._3.addItem(spacerItem)
        self._2.addWidget(self.groupBox_2)
        self.vcsGroup = QtGui.QGroupBox(UserPropertiesDialog)
        self.vcsGroup.setObjectName(_fromUtf8("vcsGroup"))
        self._4 = QtGui.QVBoxLayout(self.vcsGroup)
        self._4.setObjectName(_fromUtf8("_4"))
        self.vcsInterfaceCombo = QtGui.QComboBox(self.vcsGroup)
        self.vcsInterfaceCombo.setObjectName(_fromUtf8("vcsInterfaceCombo"))
        self._4.addWidget(self.vcsInterfaceCombo)
        self.vcsInterfaceDefaultCheckBox = QtGui.QCheckBox(self.vcsGroup)
        self.vcsInterfaceDefaultCheckBox.setObjectName(_fromUtf8("vcsInterfaceDefaultCheckBox"))
        self._4.addWidget(self.vcsInterfaceDefaultCheckBox)
        self._2.addWidget(self.vcsGroup)
        spacerItem1 = QtGui.QSpacerItem(525, 41, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self._2.addItem(spacerItem1)
        self.buttonBox = QtGui.QDialogButtonBox(UserPropertiesDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self._2.addWidget(self.buttonBox)

        self.retranslateUi(UserPropertiesDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), UserPropertiesDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), UserPropertiesDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(UserPropertiesDialog)
        UserPropertiesDialog.setTabOrder(self.vcsStatusMonitorIntervalSpinBox, self.vcsInterfaceCombo)
        UserPropertiesDialog.setTabOrder(self.vcsInterfaceCombo, self.vcsInterfaceDefaultCheckBox)
        UserPropertiesDialog.setTabOrder(self.vcsInterfaceDefaultCheckBox, self.buttonBox)

    def retranslateUi(self, UserPropertiesDialog):
        UserPropertiesDialog.setWindowTitle(_translate("UserPropertiesDialog", "User Project Properties", None))
        UserPropertiesDialog.setWhatsThis(_translate("UserPropertiesDialog", "<b>User Project Properties</b>\n"
"<p>This dialog is used to show and edit the user specific project properties.</p>", None))
        self.groupBox_2.setTitle(_translate("UserPropertiesDialog", "VCS Status Monitor", None))
        self.vcsStatusMonitorIntervalSpinBox.setToolTip(_translate("UserPropertiesDialog", "Select the interval in seconds for VCS status updates (0 to disable)", None))
        self.vcsStatusMonitorIntervalSpinBox.setSuffix(_translate("UserPropertiesDialog", " sec", None))
        self.vcsGroup.setTitle(_translate("UserPropertiesDialog", "VCS Interface", None))
        self.vcsInterfaceCombo.setToolTip(_translate("UserPropertiesDialog", "Select the vcs interface to be used", None))
        self.vcsInterfaceDefaultCheckBox.setToolTip(_translate("UserPropertiesDialog", "Select to make the interface selection the default for the project", None))
        self.vcsInterfaceDefaultCheckBox.setText(_translate("UserPropertiesDialog", "Make interface selection the default", None))

