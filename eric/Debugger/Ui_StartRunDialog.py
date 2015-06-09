# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Debugger\StartRunDialog.ui'
#
# Created: Fri Apr 18 09:56:41 2014
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

class Ui_StartRunDialog(object):
    def setupUi(self, StartRunDialog):
        StartRunDialog.setObjectName(_fromUtf8("StartRunDialog"))
        StartRunDialog.resize(488, 257)
        StartRunDialog.setSizeGripEnabled(True)
        self.gridLayout = QtGui.QGridLayout(StartRunDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.TextLabel1 = QtGui.QLabel(StartRunDialog)
        self.TextLabel1.setObjectName(_fromUtf8("TextLabel1"))
        self.gridLayout.addWidget(self.TextLabel1, 0, 0, 1, 1)
        self.cmdlineCombo = QtGui.QComboBox(StartRunDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmdlineCombo.sizePolicy().hasHeightForWidth())
        self.cmdlineCombo.setSizePolicy(sizePolicy)
        self.cmdlineCombo.setEditable(True)
        self.cmdlineCombo.setInsertPolicy(QtGui.QComboBox.InsertAtTop)
        self.cmdlineCombo.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToMinimumContentsLengthWithIcon)
        self.cmdlineCombo.setAutoCompletion(True)
        self.cmdlineCombo.setDuplicatesEnabled(False)
        self.cmdlineCombo.setObjectName(_fromUtf8("cmdlineCombo"))
        self.gridLayout.addWidget(self.cmdlineCombo, 0, 1, 1, 3)
        self.TextLabel2 = QtGui.QLabel(StartRunDialog)
        self.TextLabel2.setObjectName(_fromUtf8("TextLabel2"))
        self.gridLayout.addWidget(self.TextLabel2, 1, 0, 1, 1)
        self.workdirCombo = QtGui.QComboBox(StartRunDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.workdirCombo.sizePolicy().hasHeightForWidth())
        self.workdirCombo.setSizePolicy(sizePolicy)
        self.workdirCombo.setEditable(True)
        self.workdirCombo.setInsertPolicy(QtGui.QComboBox.InsertAtTop)
        self.workdirCombo.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToMinimumContentsLengthWithIcon)
        self.workdirCombo.setAutoCompletion(True)
        self.workdirCombo.setDuplicatesEnabled(False)
        self.workdirCombo.setObjectName(_fromUtf8("workdirCombo"))
        self.gridLayout.addWidget(self.workdirCombo, 1, 1, 1, 2)
        self.dirButton = QtGui.QPushButton(StartRunDialog)
        self.dirButton.setObjectName(_fromUtf8("dirButton"))
        self.gridLayout.addWidget(self.dirButton, 1, 3, 1, 1)
        self.textLabel1 = QtGui.QLabel(StartRunDialog)
        self.textLabel1.setObjectName(_fromUtf8("textLabel1"))
        self.gridLayout.addWidget(self.textLabel1, 2, 0, 1, 1)
        self.environmentCombo = QtGui.QComboBox(StartRunDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.environmentCombo.sizePolicy().hasHeightForWidth())
        self.environmentCombo.setSizePolicy(sizePolicy)
        self.environmentCombo.setEditable(True)
        self.environmentCombo.setInsertPolicy(QtGui.QComboBox.InsertAtTop)
        self.environmentCombo.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToMinimumContentsLengthWithIcon)
        self.environmentCombo.setAutoCompletion(True)
        self.environmentCombo.setDuplicatesEnabled(False)
        self.environmentCombo.setObjectName(_fromUtf8("environmentCombo"))
        self.gridLayout.addWidget(self.environmentCombo, 2, 1, 1, 3)
        self.exceptionCheckBox = QtGui.QCheckBox(StartRunDialog)
        self.exceptionCheckBox.setChecked(True)
        self.exceptionCheckBox.setObjectName(_fromUtf8("exceptionCheckBox"))
        self.gridLayout.addWidget(self.exceptionCheckBox, 3, 0, 1, 2)
        self.clearShellCheckBox = QtGui.QCheckBox(StartRunDialog)
        self.clearShellCheckBox.setChecked(True)
        self.clearShellCheckBox.setObjectName(_fromUtf8("clearShellCheckBox"))
        self.gridLayout.addWidget(self.clearShellCheckBox, 3, 2, 1, 2)
        self.consoleCheckBox = QtGui.QCheckBox(StartRunDialog)
        self.consoleCheckBox.setObjectName(_fromUtf8("consoleCheckBox"))
        self.gridLayout.addWidget(self.consoleCheckBox, 4, 0, 1, 1)
        self.groupBox = QtGui.QGroupBox(StartRunDialog)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.forkModeCheckBox = QtGui.QCheckBox(self.groupBox)
        self.forkModeCheckBox.setObjectName(_fromUtf8("forkModeCheckBox"))
        self.horizontalLayout.addWidget(self.forkModeCheckBox)
        self.forkChildCheckBox = QtGui.QCheckBox(self.groupBox)
        self.forkChildCheckBox.setEnabled(False)
        self.forkChildCheckBox.setObjectName(_fromUtf8("forkChildCheckBox"))
        self.horizontalLayout.addWidget(self.forkChildCheckBox)
        self.gridLayout.addWidget(self.groupBox, 5, 0, 1, 4)
        self.buttonBox = QtGui.QDialogButtonBox(StartRunDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 6, 0, 1, 4)
        self.TextLabel1.setBuddy(self.cmdlineCombo)
        self.TextLabel2.setBuddy(self.workdirCombo)
        self.textLabel1.setBuddy(self.environmentCombo)

        self.retranslateUi(StartRunDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), StartRunDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), StartRunDialog.reject)
        QtCore.QObject.connect(self.forkModeCheckBox, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.forkChildCheckBox.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(StartRunDialog)
        StartRunDialog.setTabOrder(self.cmdlineCombo, self.workdirCombo)
        StartRunDialog.setTabOrder(self.workdirCombo, self.dirButton)
        StartRunDialog.setTabOrder(self.dirButton, self.environmentCombo)
        StartRunDialog.setTabOrder(self.environmentCombo, self.exceptionCheckBox)
        StartRunDialog.setTabOrder(self.exceptionCheckBox, self.clearShellCheckBox)
        StartRunDialog.setTabOrder(self.clearShellCheckBox, self.consoleCheckBox)
        StartRunDialog.setTabOrder(self.consoleCheckBox, self.forkModeCheckBox)
        StartRunDialog.setTabOrder(self.forkModeCheckBox, self.forkChildCheckBox)
        StartRunDialog.setTabOrder(self.forkChildCheckBox, self.buttonBox)

    def retranslateUi(self, StartRunDialog):
        StartRunDialog.setWindowTitle(_translate("StartRunDialog", "Start running", None))
        self.TextLabel1.setText(_translate("StartRunDialog", "Command&line:", None))
        self.cmdlineCombo.setToolTip(_translate("StartRunDialog", "Enter the commandline parameters", None))
        self.cmdlineCombo.setWhatsThis(_translate("StartRunDialog", "<b>Commandline</b>\n"
"<p>Enter the commandline parameters in this field.</p>", None))
        self.TextLabel2.setText(_translate("StartRunDialog", "&Working directory:", None))
        self.workdirCombo.setToolTip(_translate("StartRunDialog", "Enter the working directory", None))
        self.workdirCombo.setWhatsThis(_translate("StartRunDialog", "<b>Working directory</b>\n"
"<p>Enter the working directory of the application to be debugged. Leave it empty to set the working directory to the executable directory.</p>", None))
        self.dirButton.setToolTip(_translate("StartRunDialog", "Select directory using a directory selection dialog", None))
        self.dirButton.setWhatsThis(_translate("StartRunDialog", "<b>Select directory</b>\n"
"<p>Select the working directory via a directory selection dialog.</p>", None))
        self.dirButton.setText(_translate("StartRunDialog", "...", None))
        self.textLabel1.setText(_translate("StartRunDialog", "&Environment:", None))
        self.environmentCombo.setToolTip(_translate("StartRunDialog", "Enter the environment variables to be set.", None))
        self.environmentCombo.setWhatsThis(_translate("StartRunDialog", "<b>Environment</b>\n"
"<p>Enter the environment variables to be set for the program. The individual settings must be separated by whitespace and be given in the form \'var=value\'. In order to add to an environment variable, enter it in the form \'var+=value\'.</p>\n"
"<p>Example: var1=1 var2=\"hello world\" var3+=\":/tmp\"</p>", None))
        self.exceptionCheckBox.setToolTip(_translate("StartRunDialog", "Uncheck to disable exception reporting", None))
        self.exceptionCheckBox.setWhatsThis(_translate("StartRunDialog", "<b>Report exceptions</b>\n"
"<p>Uncheck this in order to disable exception reporting.</p>", None))
        self.exceptionCheckBox.setText(_translate("StartRunDialog", "Report &exceptions", None))
        self.exceptionCheckBox.setShortcut(_translate("StartRunDialog", "Alt+E", None))
        self.clearShellCheckBox.setToolTip(_translate("StartRunDialog", "Select to clear the display of the interpreter window", None))
        self.clearShellCheckBox.setWhatsThis(_translate("StartRunDialog", "<b>Clear interpreter window</b><p>This clears the display of the interpreter window before starting the debug client.</p>", None))
        self.clearShellCheckBox.setText(_translate("StartRunDialog", "Clear &interpreter window", None))
        self.consoleCheckBox.setToolTip(_translate("StartRunDialog", "Select to start the debugger in a console window", None))
        self.consoleCheckBox.setWhatsThis(_translate("StartRunDialog", "<b>Start in console</b>\n"
"<p>Select to start the debugger in a console window. The console command has to be configured on the Debugger-&gt;General page</p>", None))
        self.consoleCheckBox.setText(_translate("StartRunDialog", "Start in console", None))
        self.groupBox.setTitle(_translate("StartRunDialog", "Forking", None))
        self.forkModeCheckBox.setToolTip(_translate("StartRunDialog", "Select to go through the fork without asking", None))
        self.forkModeCheckBox.setWhatsThis(_translate("StartRunDialog", "<b>Fork without pausing</b>\n"
"<p>Select to go through the fork without asking making the forking decision based on the Parent/Child selection.</p>", None))
        self.forkModeCheckBox.setText(_translate("StartRunDialog", "Fork without pausing", None))
        self.forkChildCheckBox.setToolTip(_translate("StartRunDialog", "Select to debug the child process after forking", None))
        self.forkChildCheckBox.setWhatsThis(_translate("StartRunDialog", "<b>Debug Child Process</b>\n"
"<p>Select to debug the child process after forking. If it is not selected, the parent process will be debugged. This has no effect, if forking without pausing is not selected.</p>", None))
        self.forkChildCheckBox.setText(_translate("StartRunDialog", "Debug Child Process", None))

