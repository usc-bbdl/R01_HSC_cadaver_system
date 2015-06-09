# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Project\NewDialogClassDialog.ui'
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

class Ui_NewDialogClassDialog(object):
    def setupUi(self, NewDialogClassDialog):
        NewDialogClassDialog.setObjectName(_fromUtf8("NewDialogClassDialog"))
        NewDialogClassDialog.resize(600, 139)
        NewDialogClassDialog.setSizeGripEnabled(True)
        self._2 = QtGui.QVBoxLayout(NewDialogClassDialog)
        self._2.setObjectName(_fromUtf8("_2"))
        self._3 = QtGui.QGridLayout()
        self._3.setObjectName(_fromUtf8("_3"))
        self.pathnameEdit = QtGui.QLineEdit(NewDialogClassDialog)
        self.pathnameEdit.setObjectName(_fromUtf8("pathnameEdit"))
        self._3.addWidget(self.pathnameEdit, 2, 1, 1, 1)
        self.label = QtGui.QLabel(NewDialogClassDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self._3.addWidget(self.label, 0, 0, 1, 1)
        self.pathButton = QtGui.QPushButton(NewDialogClassDialog)
        self.pathButton.setObjectName(_fromUtf8("pathButton"))
        self._3.addWidget(self.pathButton, 2, 2, 1, 1)
        self.label_2 = QtGui.QLabel(NewDialogClassDialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self._3.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtGui.QLabel(NewDialogClassDialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self._3.addWidget(self.label_3, 2, 0, 1, 1)
        self.classnameEdit = QtGui.QLineEdit(NewDialogClassDialog)
        self.classnameEdit.setObjectName(_fromUtf8("classnameEdit"))
        self._3.addWidget(self.classnameEdit, 0, 1, 1, 2)
        self.filenameEdit = QtGui.QLineEdit(NewDialogClassDialog)
        self.filenameEdit.setObjectName(_fromUtf8("filenameEdit"))
        self._3.addWidget(self.filenameEdit, 1, 1, 1, 2)
        self._2.addLayout(self._3)
        self.buttonBox = QtGui.QDialogButtonBox(NewDialogClassDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self._2.addWidget(self.buttonBox)
        self.label.setBuddy(self.classnameEdit)
        self.label_2.setBuddy(self.filenameEdit)
        self.label_3.setBuddy(self.pathnameEdit)

        self.retranslateUi(NewDialogClassDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), NewDialogClassDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), NewDialogClassDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(NewDialogClassDialog)
        NewDialogClassDialog.setTabOrder(self.classnameEdit, self.filenameEdit)
        NewDialogClassDialog.setTabOrder(self.filenameEdit, self.pathnameEdit)
        NewDialogClassDialog.setTabOrder(self.pathnameEdit, self.pathButton)
        NewDialogClassDialog.setTabOrder(self.pathButton, self.buttonBox)

    def retranslateUi(self, NewDialogClassDialog):
        NewDialogClassDialog.setWindowTitle(_translate("NewDialogClassDialog", "New Dialog Class", None))
        self.pathnameEdit.setToolTip(_translate("NewDialogClassDialog", "Enter the path of the file for the forms code", None))
        self.label.setText(_translate("NewDialogClassDialog", "&Classname:", None))
        self.pathButton.setToolTip(_translate("NewDialogClassDialog", "Select the source file path via a directory selection dialog", None))
        self.pathButton.setText(_translate("NewDialogClassDialog", "...", None))
        self.label_2.setText(_translate("NewDialogClassDialog", "&Filename:", None))
        self.label_3.setText(_translate("NewDialogClassDialog", "&Path:", None))
        self.classnameEdit.setToolTip(_translate("NewDialogClassDialog", "Enter the name of the new class", None))
        self.filenameEdit.setToolTip(_translate("NewDialogClassDialog", "Enter the name of the file for the forms code", None))

