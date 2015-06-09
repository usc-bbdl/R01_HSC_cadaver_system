# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Debugger\StartProfileDialog.ui'
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

class Ui_StartProfileDialog(object):
    def setupUi(self, StartProfileDialog):
        StartProfileDialog.setObjectName(_fromUtf8("StartProfileDialog"))
        StartProfileDialog.resize(488, 183)
        StartProfileDialog.setSizeGripEnabled(True)
        self.gridLayout = QtGui.QGridLayout(StartProfileDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.TextLabel1 = QtGui.QLabel(StartProfileDialog)
        self.TextLabel1.setObjectName(_fromUtf8("TextLabel1"))
        self.gridLayout.addWidget(self.TextLabel1, 0, 0, 1, 1)
        self.cmdlineCombo = QtGui.QComboBox(StartProfileDialog)
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
        self.TextLabel2 = QtGui.QLabel(StartProfileDialog)
        self.TextLabel2.setObjectName(_fromUtf8("TextLabel2"))
        self.gridLayout.addWidget(self.TextLabel2, 1, 0, 1, 1)
        self.workdirCombo = QtGui.QComboBox(StartProfileDialog)
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
        self.dirButton = QtGui.QPushButton(StartProfileDialog)
        self.dirButton.setObjectName(_fromUtf8("dirButton"))
        self.gridLayout.addWidget(self.dirButton, 1, 3, 1, 1)
        self.textLabel1 = QtGui.QLabel(StartProfileDialog)
        self.textLabel1.setObjectName(_fromUtf8("textLabel1"))
        self.gridLayout.addWidget(self.textLabel1, 2, 0, 1, 1)
        self.environmentCombo = QtGui.QComboBox(StartProfileDialog)
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
        self.exceptionCheckBox = QtGui.QCheckBox(StartProfileDialog)
        self.exceptionCheckBox.setChecked(True)
        self.exceptionCheckBox.setObjectName(_fromUtf8("exceptionCheckBox"))
        self.gridLayout.addWidget(self.exceptionCheckBox, 3, 0, 1, 2)
        self.clearShellCheckBox = QtGui.QCheckBox(StartProfileDialog)
        self.clearShellCheckBox.setChecked(True)
        self.clearShellCheckBox.setObjectName(_fromUtf8("clearShellCheckBox"))
        self.gridLayout.addWidget(self.clearShellCheckBox, 3, 2, 1, 2)
        self.consoleCheckBox = QtGui.QCheckBox(StartProfileDialog)
        self.consoleCheckBox.setObjectName(_fromUtf8("consoleCheckBox"))
        self.gridLayout.addWidget(self.consoleCheckBox, 4, 0, 1, 2)
        self.eraseCheckBox = QtGui.QCheckBox(StartProfileDialog)
        self.eraseCheckBox.setObjectName(_fromUtf8("eraseCheckBox"))
        self.gridLayout.addWidget(self.eraseCheckBox, 4, 2, 1, 2)
        self.buttonBox = QtGui.QDialogButtonBox(StartProfileDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 5, 0, 1, 4)
        self.TextLabel1.setBuddy(self.cmdlineCombo)
        self.TextLabel2.setBuddy(self.workdirCombo)
        self.textLabel1.setBuddy(self.environmentCombo)

        self.retranslateUi(StartProfileDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), StartProfileDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), StartProfileDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(StartProfileDialog)
        StartProfileDialog.setTabOrder(self.cmdlineCombo, self.workdirCombo)
        StartProfileDialog.setTabOrder(self.workdirCombo, self.dirButton)
        StartProfileDialog.setTabOrder(self.dirButton, self.environmentCombo)
        StartProfileDialog.setTabOrder(self.environmentCombo, self.exceptionCheckBox)
        StartProfileDialog.setTabOrder(self.exceptionCheckBox, self.clearShellCheckBox)
        StartProfileDialog.setTabOrder(self.clearShellCheckBox, self.consoleCheckBox)
        StartProfileDialog.setTabOrder(self.consoleCheckBox, self.eraseCheckBox)
        StartProfileDialog.setTabOrder(self.eraseCheckBox, self.buttonBox)

    def retranslateUi(self, StartProfileDialog):
        StartProfileDialog.setWindowTitle(_translate("StartProfileDialog", "Start profiling", None))
        self.TextLabel1.setText(_translate("StartProfileDialog", "Command&line:", None))
        self.cmdlineCombo.setToolTip(_translate("StartProfileDialog", "Enter the commandline parameters", None))
        self.cmdlineCombo.setWhatsThis(_translate("StartProfileDialog", "<b>Commandline</b>\n"
"<p>Enter the commandline parameters in this field.</p>", None))
        self.TextLabel2.setText(_translate("StartProfileDialog", "&Working directory:", None))
        self.workdirCombo.setToolTip(_translate("StartProfileDialog", "Enter the working directory", None))
        self.workdirCombo.setWhatsThis(_translate("StartProfileDialog", "<b>Working directory</b>\n"
"<p>Enter the working directory of the application to be debugged. Leave it empty to set the working directory to the executable directory.</p>", None))
        self.dirButton.setToolTip(_translate("StartProfileDialog", "Select directory using a directory selection dialog", None))
        self.dirButton.setWhatsThis(_translate("StartProfileDialog", "<b>Select directory</b>\n"
"<p>Select the working directory via a directory selection dialog.</p>", None))
        self.dirButton.setText(_translate("StartProfileDialog", "...", None))
        self.textLabel1.setText(_translate("StartProfileDialog", "&Environment:", None))
        self.environmentCombo.setToolTip(_translate("StartProfileDialog", "Enter the environment variables to be set.", None))
        self.environmentCombo.setWhatsThis(_translate("StartProfileDialog", "<b>Environment</b>\n"
"<p>Enter the environment variables to be set for the program. The individual settings must be separated by whitespace and be given in the form \'var=value\'. In order to add to an environment variable, enter it in the form \'var+=value\'.</p>\n"
"<p>Example: var1=1 var2=\"hello world\" var3+=\":/tmp\"</p>", None))
        self.exceptionCheckBox.setToolTip(_translate("StartProfileDialog", "Uncheck to disable exception reporting", None))
        self.exceptionCheckBox.setWhatsThis(_translate("StartProfileDialog", "<b>Report exceptions</b>\n"
"<p>Uncheck this in order to disable exception reporting.</p>", None))
        self.exceptionCheckBox.setText(_translate("StartProfileDialog", "Report &exceptions", None))
        self.exceptionCheckBox.setShortcut(_translate("StartProfileDialog", "Alt+E", None))
        self.clearShellCheckBox.setToolTip(_translate("StartProfileDialog", "Select to clear the display of the interpreter window", None))
        self.clearShellCheckBox.setWhatsThis(_translate("StartProfileDialog", "<b>Clear interpreter window</b><p>This clears the display of the interpreter window before starting the debug client.</p>", None))
        self.clearShellCheckBox.setText(_translate("StartProfileDialog", "Clear &interpreter window", None))
        self.consoleCheckBox.setToolTip(_translate("StartProfileDialog", "Select to start the debugger in a console window", None))
        self.consoleCheckBox.setWhatsThis(_translate("StartProfileDialog", "<b>Start in console</b>\n"
"<p>Select to start the debugger in a console window. The console command has to be configured on the Debugger-&gt;General page</p>", None))
        self.consoleCheckBox.setText(_translate("StartProfileDialog", "Start in console", None))
        self.eraseCheckBox.setToolTip(_translate("StartProfileDialog", "Select this to erase the collected timing data", None))
        self.eraseCheckBox.setWhatsThis(_translate("StartProfileDialog", "<b>Erase timing data</b>\n"
"<p>Select this to erase the collected timing data before the next profiling run.</p>", None))
        self.eraseCheckBox.setText(_translate("StartProfileDialog", "Erase &timing data", None))
        self.eraseCheckBox.setShortcut(_translate("StartProfileDialog", "Alt+C", None))

