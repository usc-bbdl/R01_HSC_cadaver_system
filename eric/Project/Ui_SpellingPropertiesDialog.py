# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Project\SpellingPropertiesDialog.ui'
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

class Ui_SpellingPropertiesDialog(object):
    def setupUi(self, SpellingPropertiesDialog):
        SpellingPropertiesDialog.setObjectName(_fromUtf8("SpellingPropertiesDialog"))
        SpellingPropertiesDialog.resize(600, 187)
        SpellingPropertiesDialog.setSizeGripEnabled(True)
        self.gridLayout = QtGui.QGridLayout(SpellingPropertiesDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.textLabel1_3 = QtGui.QLabel(SpellingPropertiesDialog)
        self.textLabel1_3.setObjectName(_fromUtf8("textLabel1_3"))
        self.gridLayout.addWidget(self.textLabel1_3, 0, 0, 1, 1)
        self.spellingComboBox = QtGui.QComboBox(SpellingPropertiesDialog)
        self.spellingComboBox.setObjectName(_fromUtf8("spellingComboBox"))
        self.gridLayout.addWidget(self.spellingComboBox, 1, 0, 1, 1)
        self.label = QtGui.QLabel(SpellingPropertiesDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.pwlEdit = QtGui.QLineEdit(SpellingPropertiesDialog)
        self.pwlEdit.setObjectName(_fromUtf8("pwlEdit"))
        self.gridLayout.addWidget(self.pwlEdit, 3, 0, 1, 1)
        self.pwlButton = QtGui.QPushButton(SpellingPropertiesDialog)
        self.pwlButton.setObjectName(_fromUtf8("pwlButton"))
        self.gridLayout.addWidget(self.pwlButton, 3, 1, 1, 1)
        self.label_2 = QtGui.QLabel(SpellingPropertiesDialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)
        self.pelEdit = QtGui.QLineEdit(SpellingPropertiesDialog)
        self.pelEdit.setObjectName(_fromUtf8("pelEdit"))
        self.gridLayout.addWidget(self.pelEdit, 5, 0, 1, 1)
        self.pelButton = QtGui.QPushButton(SpellingPropertiesDialog)
        self.pelButton.setObjectName(_fromUtf8("pelButton"))
        self.gridLayout.addWidget(self.pelButton, 5, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 2, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 6, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(SpellingPropertiesDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 7, 0, 1, 2)
        self.textLabel1_3.setBuddy(self.spellingComboBox)
        self.label.setBuddy(self.pwlEdit)
        self.label_2.setBuddy(self.pelEdit)

        self.retranslateUi(SpellingPropertiesDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), SpellingPropertiesDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), SpellingPropertiesDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SpellingPropertiesDialog)
        SpellingPropertiesDialog.setTabOrder(self.spellingComboBox, self.pwlEdit)
        SpellingPropertiesDialog.setTabOrder(self.pwlEdit, self.pwlButton)
        SpellingPropertiesDialog.setTabOrder(self.pwlButton, self.pelEdit)
        SpellingPropertiesDialog.setTabOrder(self.pelEdit, self.pelButton)
        SpellingPropertiesDialog.setTabOrder(self.pelButton, self.buttonBox)

    def retranslateUi(self, SpellingPropertiesDialog):
        SpellingPropertiesDialog.setWindowTitle(_translate("SpellingPropertiesDialog", "Spelling Properties", None))
        self.textLabel1_3.setText(_translate("SpellingPropertiesDialog", "Project &Language:", None))
        self.spellingComboBox.setToolTip(_translate("SpellingPropertiesDialog", "Select the project\'s language", None))
        self.label.setText(_translate("SpellingPropertiesDialog", "Project &Word List:", None))
        self.pwlEdit.setToolTip(_translate("SpellingPropertiesDialog", "Enter the filename of the project word list", None))
        self.pwlButton.setToolTip(_translate("SpellingPropertiesDialog", "Select the project word list file via a file selection dialog", None))
        self.pwlButton.setText(_translate("SpellingPropertiesDialog", "...", None))
        self.label_2.setText(_translate("SpellingPropertiesDialog", "Project E&xclude List:", None))
        self.pelEdit.setToolTip(_translate("SpellingPropertiesDialog", "Enter the filename of the project exclude list", None))
        self.pelButton.setToolTip(_translate("SpellingPropertiesDialog", "Select the project exclude list file via a file selection dialog", None))
        self.pelButton.setText(_translate("SpellingPropertiesDialog", "...", None))

