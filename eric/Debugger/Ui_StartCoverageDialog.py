# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Debugger\StartCoverageDialog.ui'
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

class Ui_StartCoverageDialog(object):
    def setupUi(self, StartCoverageDialog):
        StartCoverageDialog.setObjectName(_fromUtf8("StartCoverageDialog"))
        StartCoverageDialog.resize(488, 222)
        StartCoverageDialog.setSizeGripEnabled(True)
        self.gridLayout = QtGui.QGridLayout(StartCoverageDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.TextLabel1 = QtGui.QLabel(StartCoverageDialog)
        self.TextLabel1.setObjectName(_fromUtf8("TextLabel1"))
        self.gridLayout.addWidget(self.TextLabel1, 0, 0, 1, 1)
        self.cmdlineCombo = QtGui.QComboBox(StartCoverageDialog)
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
        self.TextLabel2 = QtGui.QLabel(StartCoverageDialog)
        self.TextLabel2.setObjectName(_fromUtf8("TextLabel2"))
        self.gridLayout.addWidget(self.TextLabel2, 1, 0, 1, 1)
        self.workdirCombo = QtGui.QComboBox(StartCoverageDialog)
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
        self.dirButton = QtGui.QPushButton(StartCoverageDialog)
        self.dirButton.setObjectName(_fromUtf8("dirButton"))
        self.gridLayout.addWidget(self.dirButton, 1, 3, 1, 1)
        self.textLabel1 = QtGui.QLabel(StartCoverageDialog)
        self.textLabel1.setObjectName(_fromUtf8("textLabel1"))
        self.gridLayout.addWidget(self.textLabel1, 2, 0, 1, 1)
        self.environmentCombo = QtGui.QComboBox(StartCoverageDialog)
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
        self.exceptionCheckBox = QtGui.QCheckBox(StartCoverageDialog)
        self.exceptionCheckBox.setChecked(True)
        self.exceptionCheckBox.setObjectName(_fromUtf8("exceptionCheckBox"))
        self.gridLayout.addWidget(self.exceptionCheckBox, 3, 0, 1, 2)
        self.clearShellCheckBox = QtGui.QCheckBox(StartCoverageDialog)
        self.clearShellCheckBox.setChecked(True)
        self.clearShellCheckBox.setObjectName(_fromUtf8("clearShellCheckBox"))
        self.gridLayout.addWidget(self.clearShellCheckBox, 3, 2, 1, 1)
        self.consoleCheckBox = QtGui.QCheckBox(StartCoverageDialog)
        self.consoleCheckBox.setObjectName(_fromUtf8("consoleCheckBox"))
        self.gridLayout.addWidget(self.consoleCheckBox, 4, 0, 1, 2)
        self.eraseCheckBox = QtGui.QCheckBox(StartCoverageDialog)
        self.eraseCheckBox.setObjectName(_fromUtf8("eraseCheckBox"))
        self.gridLayout.addWidget(self.eraseCheckBox, 5, 0, 1, 4)
        self.buttonBox = QtGui.QDialogButtonBox(StartCoverageDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 6, 0, 1, 4)
        self.TextLabel1.setBuddy(self.cmdlineCombo)
        self.TextLabel2.setBuddy(self.workdirCombo)
        self.textLabel1.setBuddy(self.environmentCombo)

        self.retranslateUi(StartCoverageDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), StartCoverageDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), StartCoverageDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(StartCoverageDialog)
        StartCoverageDialog.setTabOrder(self.cmdlineCombo, self.workdirCombo)
        StartCoverageDialog.setTabOrder(self.workdirCombo, self.dirButton)
        StartCoverageDialog.setTabOrder(self.dirButton, self.environmentCombo)
        StartCoverageDialog.setTabOrder(self.environmentCombo, self.exceptionCheckBox)
        StartCoverageDialog.setTabOrder(self.exceptionCheckBox, self.clearShellCheckBox)
        StartCoverageDialog.setTabOrder(self.clearShellCheckBox, self.consoleCheckBox)
        StartCoverageDialog.setTabOrder(self.consoleCheckBox, self.eraseCheckBox)
        StartCoverageDialog.setTabOrder(self.eraseCheckBox, self.buttonBox)

    def retranslateUi(self, StartCoverageDialog):
        StartCoverageDialog.setWindowTitle(_translate("StartCoverageDialog", "Start coverage run", None))
        self.TextLabel1.setText(_translate("StartCoverageDialog", "Command&line:", None))
        self.cmdlineCombo.setToolTip(_translate("StartCoverageDialog", "Enter the commandline parameters", None))
        self.cmdlineCombo.setWhatsThis(_translate("StartCoverageDialog", "<b>Commandline</b>\n"
"<p>Enter the commandline parameters in this field.</p>", None))
        self.TextLabel2.setText(_translate("StartCoverageDialog", "&Working directory:", None))
        self.workdirCombo.setToolTip(_translate("StartCoverageDialog", "Enter the working directory", None))
        self.workdirCombo.setWhatsThis(_translate("StartCoverageDialog", "<b>Working directory</b>\n"
"<p>Enter the working directory of the application to be debugged. Leave it empty to set the working directory to the executable directory.</p>", None))
        self.dirButton.setToolTip(_translate("StartCoverageDialog", "Select directory using a directory selection dialog", None))
        self.dirButton.setWhatsThis(_translate("StartCoverageDialog", "<b>Select directory</b>\n"
"<p>Select the working directory via a directory selection dialog.</p>", None))
        self.dirButton.setText(_translate("StartCoverageDialog", "...", None))
        self.textLabel1.setText(_translate("StartCoverageDialog", "&Environment:", None))
        self.environmentCombo.setToolTip(_translate("StartCoverageDialog", "Enter the environment variables to be set.", None))
        self.environmentCombo.setWhatsThis(_translate("StartCoverageDialog", "<b>Environment</b>\n"
"<p>Enter the environment variables to be set for the program. The individual settings must be separated by whitespace and be given in the form \'var=value\'. In order to add to an environment variable, enter it in the form \'var+=value\'.</p>\n"
"<p>Example: var1=1 var2=\"hello world\" var3+=\":/tmp\"</p>", None))
        self.exceptionCheckBox.setToolTip(_translate("StartCoverageDialog", "Uncheck to disable exception reporting", None))
        self.exceptionCheckBox.setWhatsThis(_translate("StartCoverageDialog", "<b>Report exceptions</b>\n"
"<p>Uncheck this in order to disable exception reporting.</p>", None))
        self.exceptionCheckBox.setText(_translate("StartCoverageDialog", "Report &exceptions", None))
        self.exceptionCheckBox.setShortcut(_translate("StartCoverageDialog", "Alt+E", None))
        self.clearShellCheckBox.setToolTip(_translate("StartCoverageDialog", "Select to clear the display of the interpreter window", None))
        self.clearShellCheckBox.setWhatsThis(_translate("StartCoverageDialog", "<b>Clear interpreter window</b><p>This clears the display of the interpreter window before starting the debug client.</p>", None))
        self.clearShellCheckBox.setText(_translate("StartCoverageDialog", "Clear &interpreter window", None))
        self.consoleCheckBox.setToolTip(_translate("StartCoverageDialog", "Select to start the debugger in a console window", None))
        self.consoleCheckBox.setWhatsThis(_translate("StartCoverageDialog", "<b>Start in console</b>\n"
"<p>Select to start the debugger in a console window. The console command has to be configured on the Debugger-&gt;General page</p>", None))
        self.consoleCheckBox.setText(_translate("StartCoverageDialog", "Start in console", None))
        self.eraseCheckBox.setToolTip(_translate("StartCoverageDialog", "Select this to erase the collected coverage information", None))
        self.eraseCheckBox.setWhatsThis(_translate("StartCoverageDialog", "<b>Erase coverage information</b>\n"
"<p>Select this to erase the collected coverage information before the next coverage run.</p>", None))
        self.eraseCheckBox.setText(_translate("StartCoverageDialog", "Erase &coverage information", None))
        self.eraseCheckBox.setShortcut(_translate("StartCoverageDialog", "Alt+C", None))

