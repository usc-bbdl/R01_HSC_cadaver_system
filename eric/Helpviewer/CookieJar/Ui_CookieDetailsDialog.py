# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Helpviewer\CookieJar\CookieDetailsDialog.ui'
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

class Ui_CookieDetailsDialog(object):
    def setupUi(self, CookieDetailsDialog):
        CookieDetailsDialog.setObjectName(_fromUtf8("CookieDetailsDialog"))
        CookieDetailsDialog.resize(400, 300)
        CookieDetailsDialog.setSizeGripEnabled(True)
        self.gridLayout = QtGui.QGridLayout(CookieDetailsDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(CookieDetailsDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.domainEdit = QtGui.QLineEdit(CookieDetailsDialog)
        self.domainEdit.setReadOnly(True)
        self.domainEdit.setObjectName(_fromUtf8("domainEdit"))
        self.gridLayout.addWidget(self.domainEdit, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(CookieDetailsDialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.nameEdit = QtGui.QLineEdit(CookieDetailsDialog)
        self.nameEdit.setReadOnly(True)
        self.nameEdit.setObjectName(_fromUtf8("nameEdit"))
        self.gridLayout.addWidget(self.nameEdit, 1, 1, 1, 1)
        self.label_3 = QtGui.QLabel(CookieDetailsDialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.pathEdit = QtGui.QLineEdit(CookieDetailsDialog)
        self.pathEdit.setReadOnly(True)
        self.pathEdit.setObjectName(_fromUtf8("pathEdit"))
        self.gridLayout.addWidget(self.pathEdit, 2, 1, 1, 1)
        self.label_6 = QtGui.QLabel(CookieDetailsDialog)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)
        self.secureCheckBox = QtGui.QCheckBox(CookieDetailsDialog)
        self.secureCheckBox.setText(_fromUtf8(""))
        self.secureCheckBox.setCheckable(False)
        self.secureCheckBox.setObjectName(_fromUtf8("secureCheckBox"))
        self.gridLayout.addWidget(self.secureCheckBox, 3, 1, 1, 1)
        self.label_4 = QtGui.QLabel(CookieDetailsDialog)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.expirationEdit = QtGui.QLineEdit(CookieDetailsDialog)
        self.expirationEdit.setReadOnly(True)
        self.expirationEdit.setObjectName(_fromUtf8("expirationEdit"))
        self.gridLayout.addWidget(self.expirationEdit, 4, 1, 1, 1)
        self.label_5 = QtGui.QLabel(CookieDetailsDialog)
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)
        self.valueEdit = QtGui.QPlainTextEdit(CookieDetailsDialog)
        self.valueEdit.setReadOnly(True)
        self.valueEdit.setObjectName(_fromUtf8("valueEdit"))
        self.gridLayout.addWidget(self.valueEdit, 5, 1, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(CookieDetailsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 6, 0, 1, 2)

        self.retranslateUi(CookieDetailsDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), CookieDetailsDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), CookieDetailsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(CookieDetailsDialog)
        CookieDetailsDialog.setTabOrder(self.domainEdit, self.nameEdit)
        CookieDetailsDialog.setTabOrder(self.nameEdit, self.pathEdit)
        CookieDetailsDialog.setTabOrder(self.pathEdit, self.secureCheckBox)
        CookieDetailsDialog.setTabOrder(self.secureCheckBox, self.expirationEdit)
        CookieDetailsDialog.setTabOrder(self.expirationEdit, self.valueEdit)
        CookieDetailsDialog.setTabOrder(self.valueEdit, self.buttonBox)

    def retranslateUi(self, CookieDetailsDialog):
        CookieDetailsDialog.setWindowTitle(_translate("CookieDetailsDialog", "Cookie Details", None))
        self.label.setText(_translate("CookieDetailsDialog", "Domain:", None))
        self.label_2.setText(_translate("CookieDetailsDialog", "Name:", None))
        self.label_3.setText(_translate("CookieDetailsDialog", "Path:", None))
        self.label_6.setText(_translate("CookieDetailsDialog", "Secure:", None))
        self.label_4.setText(_translate("CookieDetailsDialog", "Expires:", None))
        self.label_5.setText(_translate("CookieDetailsDialog", "Contents:", None))

