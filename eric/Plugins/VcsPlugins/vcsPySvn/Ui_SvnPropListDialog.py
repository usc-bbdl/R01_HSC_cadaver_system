# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Plugins\VcsPlugins\vcsPySvn\SvnPropListDialog.ui'
#
# Created: Fri Apr 18 09:56:42 2014
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

class Ui_SvnPropListDialog(object):
    def setupUi(self, SvnPropListDialog):
        SvnPropListDialog.setObjectName(_fromUtf8("SvnPropListDialog"))
        SvnPropListDialog.resize(826, 569)
        self.verticalLayout_2 = QtGui.QVBoxLayout(SvnPropListDialog)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.propsList = QtGui.QTreeWidget(SvnPropListDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.propsList.sizePolicy().hasHeightForWidth())
        self.propsList.setSizePolicy(sizePolicy)
        self.propsList.setAlternatingRowColors(True)
        self.propsList.setRootIsDecorated(False)
        self.propsList.setItemsExpandable(False)
        self.propsList.setObjectName(_fromUtf8("propsList"))
        self.verticalLayout_2.addWidget(self.propsList)
        self.errorGroup = QtGui.QGroupBox(SvnPropListDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.errorGroup.sizePolicy().hasHeightForWidth())
        self.errorGroup.setSizePolicy(sizePolicy)
        self.errorGroup.setObjectName(_fromUtf8("errorGroup"))
        self.verticalLayout = QtGui.QVBoxLayout(self.errorGroup)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.errors = QtGui.QTextEdit(self.errorGroup)
        self.errors.setObjectName(_fromUtf8("errors"))
        self.verticalLayout.addWidget(self.errors)
        self.verticalLayout_2.addWidget(self.errorGroup)
        self.buttonBox = QtGui.QDialogButtonBox(SvnPropListDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(SvnPropListDialog)
        QtCore.QMetaObject.connectSlotsByName(SvnPropListDialog)
        SvnPropListDialog.setTabOrder(self.propsList, self.errors)

    def retranslateUi(self, SvnPropListDialog):
        SvnPropListDialog.setWindowTitle(_translate("SvnPropListDialog", "Subversion List Properties", None))
        SvnPropListDialog.setWhatsThis(_translate("SvnPropListDialog", "<b>Subversion List Prperties</b>\n"
"<p>This dialog shows the properties of the selected file or project.</p>", None))
        self.propsList.setWhatsThis(_translate("SvnPropListDialog", "<b>Properties List</b>\n"
"<p>This shows the properties of the selected file or project.</p>", None))
        self.propsList.setSortingEnabled(True)
        self.propsList.headerItem().setText(0, _translate("SvnPropListDialog", "Path", None))
        self.propsList.headerItem().setText(1, _translate("SvnPropListDialog", "Name", None))
        self.propsList.headerItem().setText(2, _translate("SvnPropListDialog", "Value", None))
        self.errorGroup.setTitle(_translate("SvnPropListDialog", "Errors", None))
        self.errors.setWhatsThis(_translate("SvnPropListDialog", "<b>Subversion proplist errors</b>\n"
"<p>This shows possible error messages of the subversion proplist command.</p>", None))

