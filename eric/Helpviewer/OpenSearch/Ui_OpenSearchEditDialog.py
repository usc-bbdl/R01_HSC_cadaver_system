# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Helpviewer\OpenSearch\OpenSearchEditDialog.ui'
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

class Ui_OpenSearchEditDialog(object):
    def setupUi(self, OpenSearchEditDialog):
        OpenSearchEditDialog.setObjectName(_fromUtf8("OpenSearchEditDialog"))
        OpenSearchEditDialog.resize(690, 218)
        OpenSearchEditDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtGui.QVBoxLayout(OpenSearchEditDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_2 = QtGui.QLabel(OpenSearchEditDialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.nameEdit = QtGui.QLineEdit(OpenSearchEditDialog)
        self.nameEdit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.nameEdit.setReadOnly(True)
        self.nameEdit.setObjectName(_fromUtf8("nameEdit"))
        self.gridLayout.addWidget(self.nameEdit, 0, 1, 1, 1)
        self.label_3 = QtGui.QLabel(OpenSearchEditDialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.descriptionEdit = QtGui.QLineEdit(OpenSearchEditDialog)
        self.descriptionEdit.setObjectName(_fromUtf8("descriptionEdit"))
        self.gridLayout.addWidget(self.descriptionEdit, 1, 1, 1, 1)
        self.label_5 = QtGui.QLabel(OpenSearchEditDialog)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.imageEdit = QtGui.QLineEdit(OpenSearchEditDialog)
        self.imageEdit.setObjectName(_fromUtf8("imageEdit"))
        self.gridLayout.addWidget(self.imageEdit, 2, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.label_4 = QtGui.QLabel(OpenSearchEditDialog)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.searchEdit = QtGui.QLineEdit(OpenSearchEditDialog)
        self.searchEdit.setObjectName(_fromUtf8("searchEdit"))
        self.verticalLayout.addWidget(self.searchEdit)
        self.label_6 = QtGui.QLabel(OpenSearchEditDialog)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout.addWidget(self.label_6)
        self.suggestionsEdit = QtGui.QLineEdit(OpenSearchEditDialog)
        self.suggestionsEdit.setObjectName(_fromUtf8("suggestionsEdit"))
        self.verticalLayout.addWidget(self.suggestionsEdit)
        self.buttonBox = QtGui.QDialogButtonBox(OpenSearchEditDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        self.label_2.setBuddy(self.nameEdit)
        self.label_3.setBuddy(self.descriptionEdit)
        self.label_5.setBuddy(self.imageEdit)
        self.label_4.setBuddy(self.searchEdit)
        self.label_6.setBuddy(self.suggestionsEdit)

        self.retranslateUi(OpenSearchEditDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), OpenSearchEditDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), OpenSearchEditDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(OpenSearchEditDialog)
        OpenSearchEditDialog.setTabOrder(self.nameEdit, self.descriptionEdit)
        OpenSearchEditDialog.setTabOrder(self.descriptionEdit, self.imageEdit)
        OpenSearchEditDialog.setTabOrder(self.imageEdit, self.searchEdit)
        OpenSearchEditDialog.setTabOrder(self.searchEdit, self.suggestionsEdit)
        OpenSearchEditDialog.setTabOrder(self.suggestionsEdit, self.buttonBox)

    def retranslateUi(self, OpenSearchEditDialog):
        OpenSearchEditDialog.setWindowTitle(_translate("OpenSearchEditDialog", "Edit search engine data", None))
        self.label_2.setText(_translate("OpenSearchEditDialog", "&Name:", None))
        self.nameEdit.setToolTip(_translate("OpenSearchEditDialog", "Shows the name of the search engine", None))
        self.label_3.setText(_translate("OpenSearchEditDialog", "&Description:", None))
        self.descriptionEdit.setToolTip(_translate("OpenSearchEditDialog", "Enter a description", None))
        self.label_5.setText(_translate("OpenSearchEditDialog", "&Image URL:", None))
        self.imageEdit.setToolTip(_translate("OpenSearchEditDialog", "Enter the URL of the image", None))
        self.label_4.setText(_translate("OpenSearchEditDialog", "&Search URL Template:", None))
        self.searchEdit.setToolTip(_translate("OpenSearchEditDialog", "Enter the template of the search URL", None))
        self.label_6.setText(_translate("OpenSearchEditDialog", "Su&ggestions URL Template:", None))
        self.suggestionsEdit.setToolTip(_translate("OpenSearchEditDialog", "Enter the template of the suggestions URL", None))

