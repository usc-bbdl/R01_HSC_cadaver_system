# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Project\DebuggerPropertiesDialog.ui'
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

class Ui_DebuggerPropertiesDialog(object):
    def setupUi(self, DebuggerPropertiesDialog):
        DebuggerPropertiesDialog.setObjectName(_fromUtf8("DebuggerPropertiesDialog"))
        DebuggerPropertiesDialog.resize(592, 589)
        DebuggerPropertiesDialog.setSizeGripEnabled(True)
        self._2 = QtGui.QVBoxLayout(DebuggerPropertiesDialog)
        self._2.setObjectName(_fromUtf8("_2"))
        self.groupBox = QtGui.QGroupBox(DebuggerPropertiesDialog)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self._4 = QtGui.QHBoxLayout(self.groupBox)
        self._4.setObjectName(_fromUtf8("_4"))
        self.debugClientEdit = QtGui.QLineEdit(self.groupBox)
        self.debugClientEdit.setObjectName(_fromUtf8("debugClientEdit"))
        self._4.addWidget(self.debugClientEdit)
        self.debugClientButton = QtGui.QPushButton(self.groupBox)
        self.debugClientButton.setObjectName(_fromUtf8("debugClientButton"))
        self._4.addWidget(self.debugClientButton)
        self._2.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(DebuggerPropertiesDialog)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self._5 = QtGui.QHBoxLayout(self.groupBox_2)
        self._5.setObjectName(_fromUtf8("_5"))
        self.interpreterEdit = QtGui.QLineEdit(self.groupBox_2)
        self.interpreterEdit.setObjectName(_fromUtf8("interpreterEdit"))
        self._5.addWidget(self.interpreterEdit)
        self.interpreterButton = QtGui.QPushButton(self.groupBox_2)
        self.interpreterButton.setObjectName(_fromUtf8("interpreterButton"))
        self._5.addWidget(self.interpreterButton)
        self._2.addWidget(self.groupBox_2)
        self.groupBox_3 = QtGui.QGroupBox(DebuggerPropertiesDialog)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self._6 = QtGui.QGridLayout(self.groupBox_3)
        self._6.setObjectName(_fromUtf8("_6"))
        self.debugEnvironmentOverrideCheckBox = QtGui.QCheckBox(self.groupBox_3)
        self.debugEnvironmentOverrideCheckBox.setObjectName(_fromUtf8("debugEnvironmentOverrideCheckBox"))
        self._6.addWidget(self.debugEnvironmentOverrideCheckBox, 0, 0, 1, 2)
        self.debugEnvironmentEdit = QtGui.QLineEdit(self.groupBox_3)
        self.debugEnvironmentEdit.setObjectName(_fromUtf8("debugEnvironmentEdit"))
        self._6.addWidget(self.debugEnvironmentEdit, 1, 1, 1, 1)
        self.textLabel1_16 = QtGui.QLabel(self.groupBox_3)
        self.textLabel1_16.setObjectName(_fromUtf8("textLabel1_16"))
        self._6.addWidget(self.textLabel1_16, 1, 0, 1, 1)
        self._2.addWidget(self.groupBox_3)
        self.remoteDebuggerGroup = QtGui.QGroupBox(DebuggerPropertiesDialog)
        self.remoteDebuggerGroup.setCheckable(True)
        self.remoteDebuggerGroup.setObjectName(_fromUtf8("remoteDebuggerGroup"))
        self._7 = QtGui.QGridLayout(self.remoteDebuggerGroup)
        self._7.setObjectName(_fromUtf8("_7"))
        self.pathTranslationGroup = QtGui.QGroupBox(self.remoteDebuggerGroup)
        self.pathTranslationGroup.setCheckable(True)
        self.pathTranslationGroup.setObjectName(_fromUtf8("pathTranslationGroup"))
        self.gridlayout = QtGui.QGridLayout(self.pathTranslationGroup)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.textLabel2_9 = QtGui.QLabel(self.pathTranslationGroup)
        self.textLabel2_9.setObjectName(_fromUtf8("textLabel2_9"))
        self.gridlayout.addWidget(self.textLabel2_9, 1, 0, 1, 1)
        self.translationLocalEdit = QtGui.QLineEdit(self.pathTranslationGroup)
        self.translationLocalEdit.setObjectName(_fromUtf8("translationLocalEdit"))
        self.gridlayout.addWidget(self.translationLocalEdit, 1, 1, 1, 1)
        self.translationRemoteEdit = QtGui.QLineEdit(self.pathTranslationGroup)
        self.translationRemoteEdit.setObjectName(_fromUtf8("translationRemoteEdit"))
        self.gridlayout.addWidget(self.translationRemoteEdit, 0, 1, 1, 1)
        self.textLabel1_18 = QtGui.QLabel(self.pathTranslationGroup)
        self.textLabel1_18.setObjectName(_fromUtf8("textLabel1_18"))
        self.gridlayout.addWidget(self.textLabel1_18, 0, 0, 1, 1)
        self._7.addWidget(self.pathTranslationGroup, 2, 0, 1, 2)
        self.hostLabel = QtGui.QLabel(self.remoteDebuggerGroup)
        self.hostLabel.setObjectName(_fromUtf8("hostLabel"))
        self._7.addWidget(self.hostLabel, 0, 0, 1, 1)
        self.remoteCommandEdit = QtGui.QLineEdit(self.remoteDebuggerGroup)
        self.remoteCommandEdit.setObjectName(_fromUtf8("remoteCommandEdit"))
        self._7.addWidget(self.remoteCommandEdit, 1, 1, 1, 1)
        self.execLabel = QtGui.QLabel(self.remoteDebuggerGroup)
        self.execLabel.setObjectName(_fromUtf8("execLabel"))
        self._7.addWidget(self.execLabel, 1, 0, 1, 1)
        self.remoteHostEdit = QtGui.QLineEdit(self.remoteDebuggerGroup)
        self.remoteHostEdit.setObjectName(_fromUtf8("remoteHostEdit"))
        self._7.addWidget(self.remoteHostEdit, 0, 1, 1, 1)
        self._2.addWidget(self.remoteDebuggerGroup)
        self.consoleDebuggerGroup = QtGui.QGroupBox(DebuggerPropertiesDialog)
        self.consoleDebuggerGroup.setCheckable(True)
        self.consoleDebuggerGroup.setObjectName(_fromUtf8("consoleDebuggerGroup"))
        self._3 = QtGui.QHBoxLayout(self.consoleDebuggerGroup)
        self._3.setObjectName(_fromUtf8("_3"))
        self.textLabel1_17 = QtGui.QLabel(self.consoleDebuggerGroup)
        self.textLabel1_17.setObjectName(_fromUtf8("textLabel1_17"))
        self._3.addWidget(self.textLabel1_17)
        self.consoleCommandEdit = QtGui.QLineEdit(self.consoleDebuggerGroup)
        self.consoleCommandEdit.setObjectName(_fromUtf8("consoleCommandEdit"))
        self._3.addWidget(self.consoleCommandEdit)
        self._2.addWidget(self.consoleDebuggerGroup)
        self.redirectCheckBox = QtGui.QCheckBox(DebuggerPropertiesDialog)
        self.redirectCheckBox.setObjectName(_fromUtf8("redirectCheckBox"))
        self._2.addWidget(self.redirectCheckBox)
        self.noEncodingCheckBox = QtGui.QCheckBox(DebuggerPropertiesDialog)
        self.noEncodingCheckBox.setObjectName(_fromUtf8("noEncodingCheckBox"))
        self._2.addWidget(self.noEncodingCheckBox)
        self.buttonBox = QtGui.QDialogButtonBox(DebuggerPropertiesDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self._2.addWidget(self.buttonBox)

        self.retranslateUi(DebuggerPropertiesDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), DebuggerPropertiesDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), DebuggerPropertiesDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(DebuggerPropertiesDialog)
        DebuggerPropertiesDialog.setTabOrder(self.debugClientEdit, self.debugClientButton)
        DebuggerPropertiesDialog.setTabOrder(self.debugClientButton, self.interpreterEdit)
        DebuggerPropertiesDialog.setTabOrder(self.interpreterEdit, self.interpreterButton)
        DebuggerPropertiesDialog.setTabOrder(self.interpreterButton, self.debugEnvironmentOverrideCheckBox)
        DebuggerPropertiesDialog.setTabOrder(self.debugEnvironmentOverrideCheckBox, self.debugEnvironmentEdit)
        DebuggerPropertiesDialog.setTabOrder(self.debugEnvironmentEdit, self.remoteDebuggerGroup)
        DebuggerPropertiesDialog.setTabOrder(self.remoteDebuggerGroup, self.remoteHostEdit)
        DebuggerPropertiesDialog.setTabOrder(self.remoteHostEdit, self.remoteCommandEdit)
        DebuggerPropertiesDialog.setTabOrder(self.remoteCommandEdit, self.pathTranslationGroup)
        DebuggerPropertiesDialog.setTabOrder(self.pathTranslationGroup, self.translationRemoteEdit)
        DebuggerPropertiesDialog.setTabOrder(self.translationRemoteEdit, self.translationLocalEdit)
        DebuggerPropertiesDialog.setTabOrder(self.translationLocalEdit, self.consoleDebuggerGroup)
        DebuggerPropertiesDialog.setTabOrder(self.consoleDebuggerGroup, self.consoleCommandEdit)
        DebuggerPropertiesDialog.setTabOrder(self.consoleCommandEdit, self.redirectCheckBox)

    def retranslateUi(self, DebuggerPropertiesDialog):
        DebuggerPropertiesDialog.setWindowTitle(_translate("DebuggerPropertiesDialog", "Debugger Properties", None))
        self.groupBox.setTitle(_translate("DebuggerPropertiesDialog", "Debug Client", None))
        self.debugClientEdit.setToolTip(_translate("DebuggerPropertiesDialog", "Enter the path of the Debug Client to be used.  Leave empty to use the default.", None))
        self.debugClientButton.setToolTip(_translate("DebuggerPropertiesDialog", "Press to select the Debug Client via a file selection dialog", None))
        self.debugClientButton.setText(_translate("DebuggerPropertiesDialog", "...", None))
        self.groupBox_2.setTitle(_translate("DebuggerPropertiesDialog", "Interpreter for Debug Client", None))
        self.interpreterEdit.setToolTip(_translate("DebuggerPropertiesDialog", "Enter the path of the interpreter to be used by the debug client.", None))
        self.interpreterButton.setToolTip(_translate("DebuggerPropertiesDialog", "Press to select the interpreter via a file selection dialog", None))
        self.interpreterButton.setText(_translate("DebuggerPropertiesDialog", "...", None))
        self.groupBox_3.setTitle(_translate("DebuggerPropertiesDialog", "Environment for Debug Client", None))
        self.debugEnvironmentOverrideCheckBox.setToolTip(_translate("DebuggerPropertiesDialog", "Select, if the environment of the debug client should be replaced", None))
        self.debugEnvironmentOverrideCheckBox.setText(_translate("DebuggerPropertiesDialog", "Replace Environment", None))
        self.debugEnvironmentEdit.setToolTip(_translate("DebuggerPropertiesDialog", "Enter the environment variables to be set.", None))
        self.debugEnvironmentEdit.setWhatsThis(_translate("DebuggerPropertiesDialog", "<b>Environment</b>\n"
"<p>Enter the environment variables to be set for the debugger. The individual settings must be separate by whitespace and be given in the form \'var=value\'.</p>\n"
"<p>Example: var1=1 var2=\"hello world\"</p>", None))
        self.textLabel1_16.setText(_translate("DebuggerPropertiesDialog", "Environment:", None))
        self.remoteDebuggerGroup.setToolTip(_translate("DebuggerPropertiesDialog", "Select, if the debugger should be run remotely", None))
        self.remoteDebuggerGroup.setTitle(_translate("DebuggerPropertiesDialog", "Remote Debugger", None))
        self.pathTranslationGroup.setToolTip(_translate("DebuggerPropertiesDialog", "Select, if path translation for remote debugging should be done", None))
        self.pathTranslationGroup.setTitle(_translate("DebuggerPropertiesDialog", "Perform Path Translation", None))
        self.textLabel2_9.setText(_translate("DebuggerPropertiesDialog", "Local Path:", None))
        self.translationLocalEdit.setToolTip(_translate("DebuggerPropertiesDialog", "Enter the local path", None))
        self.translationRemoteEdit.setToolTip(_translate("DebuggerPropertiesDialog", "Enter the remote path", None))
        self.textLabel1_18.setText(_translate("DebuggerPropertiesDialog", "Remote Path:", None))
        self.hostLabel.setText(_translate("DebuggerPropertiesDialog", "Remote Host:", None))
        self.remoteCommandEdit.setToolTip(_translate("DebuggerPropertiesDialog", "Enter the remote execution command.", None))
        self.remoteCommandEdit.setWhatsThis(_translate("DebuggerPropertiesDialog", "<b>Remote Execution</b>\n"
"<p>Enter the remote execution command (e.g. ssh). This command is used to log into the remote host and execute the remote debugger.</p>", None))
        self.execLabel.setText(_translate("DebuggerPropertiesDialog", "Remote Execution:", None))
        self.remoteHostEdit.setToolTip(_translate("DebuggerPropertiesDialog", "Enter the hostname of the remote machine.", None))
        self.remoteHostEdit.setWhatsThis(_translate("DebuggerPropertiesDialog", "<b>Remote Host</b>\n"
"<p>Enter the hostname of the remote machine.</p>", None))
        self.consoleDebuggerGroup.setToolTip(_translate("DebuggerPropertiesDialog", "Select, if the debugger should be executed in a console window", None))
        self.consoleDebuggerGroup.setTitle(_translate("DebuggerPropertiesDialog", "Console Debugger", None))
        self.textLabel1_17.setText(_translate("DebuggerPropertiesDialog", "Console Command:", None))
        self.consoleCommandEdit.setToolTip(_translate("DebuggerPropertiesDialog", "Enter the console command (e.g. xterm -e)", None))
        self.consoleCommandEdit.setWhatsThis(_translate("DebuggerPropertiesDialog", "<b>Console Command</b>\n"
"<p>Enter the console command (e.g. xterm -e). This command is used to open a command window for the debugger.</p>", None))
        self.redirectCheckBox.setToolTip(_translate("DebuggerPropertiesDialog", "Select to redirect stdin, stdout and stderr of the program being debugged to the eric4 IDE", None))
        self.redirectCheckBox.setText(_translate("DebuggerPropertiesDialog", "Redirect stdin/stdout/stderr", None))
        self.noEncodingCheckBox.setToolTip(_translate("DebuggerPropertiesDialog", "Select to not set the debug client encoding", None))
        self.noEncodingCheckBox.setText(_translate("DebuggerPropertiesDialog", "Don\'t set the encoding of the debug client", None))

