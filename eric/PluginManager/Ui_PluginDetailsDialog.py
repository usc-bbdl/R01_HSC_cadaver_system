# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\PluginManager\PluginDetailsDialog.ui'
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

class Ui_PluginDetailsDialog(object):
    def setupUi(self, PluginDetailsDialog):
        PluginDetailsDialog.setObjectName(_fromUtf8("PluginDetailsDialog"))
        PluginDetailsDialog.resize(563, 479)
        PluginDetailsDialog.setSizeGripEnabled(True)
        self.gridlayout = QtGui.QGridLayout(PluginDetailsDialog)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.label = QtGui.QLabel(PluginDetailsDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridlayout.addWidget(self.label, 0, 0, 1, 1)
        self.moduleNameEdit = QtGui.QLineEdit(PluginDetailsDialog)
        self.moduleNameEdit.setReadOnly(True)
        self.moduleNameEdit.setObjectName(_fromUtf8("moduleNameEdit"))
        self.gridlayout.addWidget(self.moduleNameEdit, 0, 1, 1, 2)
        self.label_2 = QtGui.QLabel(PluginDetailsDialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridlayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.moduleFileNameEdit = QtGui.QLineEdit(PluginDetailsDialog)
        self.moduleFileNameEdit.setReadOnly(True)
        self.moduleFileNameEdit.setObjectName(_fromUtf8("moduleFileNameEdit"))
        self.gridlayout.addWidget(self.moduleFileNameEdit, 1, 1, 1, 2)
        self.autoactivateCheckBox = QtGui.QCheckBox(PluginDetailsDialog)
        self.autoactivateCheckBox.setFocusPolicy(QtCore.Qt.NoFocus)
        self.autoactivateCheckBox.setObjectName(_fromUtf8("autoactivateCheckBox"))
        self.gridlayout.addWidget(self.autoactivateCheckBox, 2, 0, 1, 1)
        self.activeCheckBox = QtGui.QCheckBox(PluginDetailsDialog)
        self.activeCheckBox.setFocusPolicy(QtCore.Qt.NoFocus)
        self.activeCheckBox.setObjectName(_fromUtf8("activeCheckBox"))
        self.gridlayout.addWidget(self.activeCheckBox, 2, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridlayout.addItem(spacerItem, 2, 2, 1, 1)
        self.label_3 = QtGui.QLabel(PluginDetailsDialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridlayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.pluginNameEdit = QtGui.QLineEdit(PluginDetailsDialog)
        self.pluginNameEdit.setReadOnly(True)
        self.pluginNameEdit.setObjectName(_fromUtf8("pluginNameEdit"))
        self.gridlayout.addWidget(self.pluginNameEdit, 3, 1, 1, 2)
        self.label_4 = QtGui.QLabel(PluginDetailsDialog)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridlayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.versionEdit = QtGui.QLineEdit(PluginDetailsDialog)
        self.versionEdit.setReadOnly(True)
        self.versionEdit.setObjectName(_fromUtf8("versionEdit"))
        self.gridlayout.addWidget(self.versionEdit, 4, 1, 1, 2)
        self.label_5 = QtGui.QLabel(PluginDetailsDialog)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridlayout.addWidget(self.label_5, 5, 0, 1, 1)
        self.authorEdit = QtGui.QLineEdit(PluginDetailsDialog)
        self.authorEdit.setReadOnly(True)
        self.authorEdit.setObjectName(_fromUtf8("authorEdit"))
        self.gridlayout.addWidget(self.authorEdit, 5, 1, 1, 2)
        self.label_6 = QtGui.QLabel(PluginDetailsDialog)
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridlayout.addWidget(self.label_6, 6, 0, 1, 1)
        self.descriptionEdit = QtGui.QTextEdit(PluginDetailsDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.descriptionEdit.sizePolicy().hasHeightForWidth())
        self.descriptionEdit.setSizePolicy(sizePolicy)
        self.descriptionEdit.setReadOnly(True)
        self.descriptionEdit.setObjectName(_fromUtf8("descriptionEdit"))
        self.gridlayout.addWidget(self.descriptionEdit, 6, 1, 1, 2)
        self.label_7 = QtGui.QLabel(PluginDetailsDialog)
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridlayout.addWidget(self.label_7, 7, 0, 1, 1)
        self.errorEdit = QtGui.QTextEdit(PluginDetailsDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.errorEdit.sizePolicy().hasHeightForWidth())
        self.errorEdit.setSizePolicy(sizePolicy)
        self.errorEdit.setReadOnly(True)
        self.errorEdit.setObjectName(_fromUtf8("errorEdit"))
        self.gridlayout.addWidget(self.errorEdit, 7, 1, 1, 2)
        self.buttonBox = QtGui.QDialogButtonBox(PluginDetailsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridlayout.addWidget(self.buttonBox, 8, 0, 1, 3)

        self.retranslateUi(PluginDetailsDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), PluginDetailsDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), PluginDetailsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(PluginDetailsDialog)
        PluginDetailsDialog.setTabOrder(self.moduleNameEdit, self.moduleFileNameEdit)
        PluginDetailsDialog.setTabOrder(self.moduleFileNameEdit, self.pluginNameEdit)
        PluginDetailsDialog.setTabOrder(self.pluginNameEdit, self.versionEdit)
        PluginDetailsDialog.setTabOrder(self.versionEdit, self.authorEdit)
        PluginDetailsDialog.setTabOrder(self.authorEdit, self.descriptionEdit)
        PluginDetailsDialog.setTabOrder(self.descriptionEdit, self.errorEdit)
        PluginDetailsDialog.setTabOrder(self.errorEdit, self.buttonBox)

    def retranslateUi(self, PluginDetailsDialog):
        PluginDetailsDialog.setWindowTitle(_translate("PluginDetailsDialog", "Plugin Details", None))
        self.label.setText(_translate("PluginDetailsDialog", "Module name:", None))
        self.label_2.setText(_translate("PluginDetailsDialog", "Module filename:", None))
        self.autoactivateCheckBox.setText(_translate("PluginDetailsDialog", "Autoactivate", None))
        self.activeCheckBox.setText(_translate("PluginDetailsDialog", "Active", None))
        self.label_3.setText(_translate("PluginDetailsDialog", "Plugin name:", None))
        self.label_4.setText(_translate("PluginDetailsDialog", "Version:", None))
        self.label_5.setText(_translate("PluginDetailsDialog", "Author:", None))
        self.label_6.setText(_translate("PluginDetailsDialog", "Description:", None))
        self.label_7.setText(_translate("PluginDetailsDialog", "Error:", None))

