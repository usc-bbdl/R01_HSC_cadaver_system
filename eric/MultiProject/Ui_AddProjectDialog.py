# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\MultiProject\AddProjectDialog.ui'
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

class Ui_AddProjectDialog(object):
    def setupUi(self, AddProjectDialog):
        AddProjectDialog.setObjectName(_fromUtf8("AddProjectDialog"))
        AddProjectDialog.resize(569, 378)
        AddProjectDialog.setSizeGripEnabled(True)
        self.vboxlayout = QtGui.QVBoxLayout(AddProjectDialog)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.gridlayout = QtGui.QGridLayout()
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.label = QtGui.QLabel(AddProjectDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridlayout.addWidget(self.label, 0, 0, 1, 1)
        self.nameEdit = QtGui.QLineEdit(AddProjectDialog)
        self.nameEdit.setObjectName(_fromUtf8("nameEdit"))
        self.gridlayout.addWidget(self.nameEdit, 0, 1, 1, 2)
        self.label_2 = QtGui.QLabel(AddProjectDialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridlayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.filenameEdit = QtGui.QLineEdit(AddProjectDialog)
        self.filenameEdit.setObjectName(_fromUtf8("filenameEdit"))
        self.gridlayout.addWidget(self.filenameEdit, 1, 1, 1, 1)
        self.fileButton = QtGui.QPushButton(AddProjectDialog)
        self.fileButton.setObjectName(_fromUtf8("fileButton"))
        self.gridlayout.addWidget(self.fileButton, 1, 2, 1, 1)
        self.label_3 = QtGui.QLabel(AddProjectDialog)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridlayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.descriptionEdit = QtGui.QTextEdit(AddProjectDialog)
        self.descriptionEdit.setTabChangesFocus(True)
        self.descriptionEdit.setAcceptRichText(False)
        self.descriptionEdit.setObjectName(_fromUtf8("descriptionEdit"))
        self.gridlayout.addWidget(self.descriptionEdit, 2, 1, 1, 2)
        self.masterCheckBox = QtGui.QCheckBox(AddProjectDialog)
        self.masterCheckBox.setObjectName(_fromUtf8("masterCheckBox"))
        self.gridlayout.addWidget(self.masterCheckBox, 3, 0, 1, 3)
        self.vboxlayout.addLayout(self.gridlayout)
        self.buttonBox = QtGui.QDialogButtonBox(AddProjectDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.vboxlayout.addWidget(self.buttonBox)
        self.label.setBuddy(self.nameEdit)
        self.label_2.setBuddy(self.filenameEdit)
        self.label_3.setBuddy(self.descriptionEdit)

        self.retranslateUi(AddProjectDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), AddProjectDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), AddProjectDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(AddProjectDialog)
        AddProjectDialog.setTabOrder(self.nameEdit, self.filenameEdit)
        AddProjectDialog.setTabOrder(self.filenameEdit, self.fileButton)
        AddProjectDialog.setTabOrder(self.fileButton, self.descriptionEdit)
        AddProjectDialog.setTabOrder(self.descriptionEdit, self.masterCheckBox)
        AddProjectDialog.setTabOrder(self.masterCheckBox, self.buttonBox)

    def retranslateUi(self, AddProjectDialog):
        AddProjectDialog.setWindowTitle(_translate("AddProjectDialog", "Add Project", None))
        self.label.setText(_translate("AddProjectDialog", "&Name:", None))
        self.nameEdit.setToolTip(_translate("AddProjectDialog", "Enter the name of the project", None))
        self.label_2.setText(_translate("AddProjectDialog", "Project&file:", None))
        self.filenameEdit.setToolTip(_translate("AddProjectDialog", "Enter the name of the project file", None))
        self.fileButton.setToolTip(_translate("AddProjectDialog", "Select the project file via a file selection dialog", None))
        self.fileButton.setText(_translate("AddProjectDialog", "...", None))
        self.label_3.setText(_translate("AddProjectDialog", "&Description:", None))
        self.descriptionEdit.setToolTip(_translate("AddProjectDialog", "Enter a short description for the project", None))
        self.masterCheckBox.setToolTip(_translate("AddProjectDialog", "Select to make this project the master project", None))
        self.masterCheckBox.setText(_translate("AddProjectDialog", "Is &master project", None))

