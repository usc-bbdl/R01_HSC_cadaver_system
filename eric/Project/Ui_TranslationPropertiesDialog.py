# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Project\TranslationPropertiesDialog.ui'
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

class Ui_TranslationPropertiesDialog(object):
    def setupUi(self, TranslationPropertiesDialog):
        TranslationPropertiesDialog.setObjectName(_fromUtf8("TranslationPropertiesDialog"))
        TranslationPropertiesDialog.resize(592, 543)
        TranslationPropertiesDialog.setSizeGripEnabled(True)
        self._2 = QtGui.QVBoxLayout(TranslationPropertiesDialog)
        self._2.setObjectName(_fromUtf8("_2"))
        self._3 = QtGui.QGridLayout()
        self._3.setObjectName(_fromUtf8("_3"))
        self.transBinPathButton = QtGui.QPushButton(TranslationPropertiesDialog)
        self.transBinPathButton.setObjectName(_fromUtf8("transBinPathButton"))
        self._3.addWidget(self.transBinPathButton, 3, 1, 1, 1)
        self.transBinPathEdit = QtGui.QLineEdit(TranslationPropertiesDialog)
        self.transBinPathEdit.setObjectName(_fromUtf8("transBinPathEdit"))
        self._3.addWidget(self.transBinPathEdit, 3, 0, 1, 1)
        self.transPatternButton = QtGui.QPushButton(TranslationPropertiesDialog)
        self.transPatternButton.setObjectName(_fromUtf8("transPatternButton"))
        self._3.addWidget(self.transPatternButton, 1, 1, 1, 1)
        self.label = QtGui.QLabel(TranslationPropertiesDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self._3.addWidget(self.label, 2, 0, 1, 2)
        self.transPatternEdit = QtGui.QLineEdit(TranslationPropertiesDialog)
        self.transPatternEdit.setObjectName(_fromUtf8("transPatternEdit"))
        self._3.addWidget(self.transPatternEdit, 1, 0, 1, 1)
        self.textLabel1_3 = QtGui.QLabel(TranslationPropertiesDialog)
        self.textLabel1_3.setWordWrap(True)
        self.textLabel1_3.setObjectName(_fromUtf8("textLabel1_3"))
        self._3.addWidget(self.textLabel1_3, 0, 0, 1, 2)
        self._2.addLayout(self._3)
        self.exceptionsGroup = QtGui.QGroupBox(TranslationPropertiesDialog)
        self.exceptionsGroup.setObjectName(_fromUtf8("exceptionsGroup"))
        self._4 = QtGui.QGridLayout(self.exceptionsGroup)
        self._4.setObjectName(_fromUtf8("_4"))
        self.exceptDirButton = QtGui.QPushButton(self.exceptionsGroup)
        self.exceptDirButton.setObjectName(_fromUtf8("exceptDirButton"))
        self._4.addWidget(self.exceptDirButton, 2, 3, 1, 1)
        self.exceptFileButton = QtGui.QPushButton(self.exceptionsGroup)
        self.exceptFileButton.setObjectName(_fromUtf8("exceptFileButton"))
        self._4.addWidget(self.exceptFileButton, 2, 2, 1, 1)
        self.addExceptionButton = QtGui.QPushButton(self.exceptionsGroup)
        self.addExceptionButton.setEnabled(False)
        self.addExceptionButton.setObjectName(_fromUtf8("addExceptionButton"))
        self._4.addWidget(self.addExceptionButton, 2, 1, 1, 1)
        self.deleteExceptionButton = QtGui.QPushButton(self.exceptionsGroup)
        self.deleteExceptionButton.setEnabled(False)
        self.deleteExceptionButton.setObjectName(_fromUtf8("deleteExceptionButton"))
        self._4.addWidget(self.deleteExceptionButton, 2, 0, 1, 1)
        self.exceptionEdit = QtGui.QLineEdit(self.exceptionsGroup)
        self.exceptionEdit.setObjectName(_fromUtf8("exceptionEdit"))
        self._4.addWidget(self.exceptionEdit, 1, 0, 1, 4)
        self.exceptionsList = QtGui.QListWidget(self.exceptionsGroup)
        self.exceptionsList.setAlternatingRowColors(True)
        self.exceptionsList.setObjectName(_fromUtf8("exceptionsList"))
        self._4.addWidget(self.exceptionsList, 0, 0, 1, 4)
        self._2.addWidget(self.exceptionsGroup)
        self.buttonBox = QtGui.QDialogButtonBox(TranslationPropertiesDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self._2.addWidget(self.buttonBox)
        self.label.setBuddy(self.transBinPathEdit)
        self.textLabel1_3.setBuddy(self.transPatternEdit)

        self.retranslateUi(TranslationPropertiesDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), TranslationPropertiesDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), TranslationPropertiesDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(TranslationPropertiesDialog)
        TranslationPropertiesDialog.setTabOrder(self.transPatternEdit, self.transPatternButton)
        TranslationPropertiesDialog.setTabOrder(self.transPatternButton, self.transBinPathEdit)
        TranslationPropertiesDialog.setTabOrder(self.transBinPathEdit, self.transBinPathButton)
        TranslationPropertiesDialog.setTabOrder(self.transBinPathButton, self.exceptionsList)
        TranslationPropertiesDialog.setTabOrder(self.exceptionsList, self.exceptionEdit)
        TranslationPropertiesDialog.setTabOrder(self.exceptionEdit, self.deleteExceptionButton)
        TranslationPropertiesDialog.setTabOrder(self.deleteExceptionButton, self.addExceptionButton)
        TranslationPropertiesDialog.setTabOrder(self.addExceptionButton, self.exceptFileButton)
        TranslationPropertiesDialog.setTabOrder(self.exceptFileButton, self.exceptDirButton)

    def retranslateUi(self, TranslationPropertiesDialog):
        TranslationPropertiesDialog.setWindowTitle(_translate("TranslationPropertiesDialog", "Translation Properties", None))
        self.transBinPathButton.setToolTip(_translate("TranslationPropertiesDialog", "Show directory selection dialog", None))
        self.transBinPathButton.setWhatsThis(_translate("TranslationPropertiesDialog", "<b>Binary Translations Path</b>\n"
"<p>Select the directory for the binary translations via a directory selection dialog.</p>", None))
        self.transBinPathButton.setText(_translate("TranslationPropertiesDialog", "...", None))
        self.transBinPathEdit.setToolTip(_translate("TranslationPropertiesDialog", "Enter the path for the binary translation files (*.qm)", None))
        self.transBinPathEdit.setWhatsThis(_translate("TranslationPropertiesDialog", "<b>Binary Translations Path</b>\n"
"<p>Enter the directory for the binary translation files (*.qm). Leave it empty to store them together with the *.ts files.</p>", None))
        self.transPatternButton.setToolTip(_translate("TranslationPropertiesDialog", "Show directory selection dialog", None))
        self.transPatternButton.setWhatsThis(_translate("TranslationPropertiesDialog", "<b>Translation Pattern</b>\n"
"<p>Select a translation file via a file selection dialog.</p>", None))
        self.transPatternButton.setText(_translate("TranslationPropertiesDialog", "...", None))
        self.label.setText(_translate("TranslationPropertiesDialog", "&Binary Translations Path:", None))
        self.transPatternEdit.setToolTip(_translate("TranslationPropertiesDialog", "Enter the path pattern for the translation files", None))
        self.transPatternEdit.setWhatsThis(_translate("TranslationPropertiesDialog", "<b>Translation Pattern</b>\n"
"<p>Enter the path pattern for the translation files using %language% at the place of the language code (e.g. /path_to_eric/i18n/eric4_%language%.ts). This will result in translation files like /path_to_eric/i18n/eric_de.ts.</p>", None))
        self.textLabel1_3.setText(_translate("TranslationPropertiesDialog", "&Translation Path Pattern:\n"
"(Use \'%language%\' where the language code should be inserted, e.g. i18n/eric4_%language%.ts)", None))
        self.exceptionsGroup.setTitle(_translate("TranslationPropertiesDialog", "Exclude from translation", None))
        self.exceptDirButton.setToolTip(_translate("TranslationPropertiesDialog", "Press to select a directory via a selection dialog", None))
        self.exceptDirButton.setText(_translate("TranslationPropertiesDialog", "Select d&irectory...", None))
        self.exceptFileButton.setToolTip(_translate("TranslationPropertiesDialog", "Press to select a file via a selection dialog", None))
        self.exceptFileButton.setText(_translate("TranslationPropertiesDialog", "Select &file...", None))
        self.addExceptionButton.setToolTip(_translate("TranslationPropertiesDialog", "Press to add the entered path or file to the list", None))
        self.addExceptionButton.setText(_translate("TranslationPropertiesDialog", "&Add", None))
        self.deleteExceptionButton.setToolTip(_translate("TranslationPropertiesDialog", "Press to delete the selected entry from the list", None))
        self.deleteExceptionButton.setText(_translate("TranslationPropertiesDialog", "&Delete", None))
        self.exceptionEdit.setToolTip(_translate("TranslationPropertiesDialog", "Enter a path or file to be added", None))
        self.exceptionsList.setToolTip(_translate("TranslationPropertiesDialog", "List of paths or files to excude from translation", None))
        self.exceptionsList.setSortingEnabled(True)

