# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Project\AddLanguageDialog.ui'
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

class Ui_AddLanguageDialog(object):
    def setupUi(self, AddLanguageDialog):
        AddLanguageDialog.setObjectName(_fromUtf8("AddLanguageDialog"))
        AddLanguageDialog.resize(245, 77)
        AddLanguageDialog.setSizeGripEnabled(True)
        self.vboxlayout = QtGui.QVBoxLayout(AddLanguageDialog)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        self.languageLabel = QtGui.QLabel(AddLanguageDialog)
        self.languageLabel.setObjectName(_fromUtf8("languageLabel"))
        self.hboxlayout.addWidget(self.languageLabel)
        self.languageCombo = QtGui.QComboBox(AddLanguageDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.languageCombo.sizePolicy().hasHeightForWidth())
        self.languageCombo.setSizePolicy(sizePolicy)
        self.languageCombo.setEditable(True)
        self.languageCombo.setDuplicatesEnabled(False)
        self.languageCombo.setObjectName(_fromUtf8("languageCombo"))
        self.languageCombo.addItem(_fromUtf8(""))
        self.languageCombo.addItem(_fromUtf8(""))
        self.languageCombo.addItem(_fromUtf8(""))
        self.languageCombo.addItem(_fromUtf8(""))
        self.languageCombo.addItem(_fromUtf8(""))
        self.languageCombo.addItem(_fromUtf8(""))
        self.languageCombo.addItem(_fromUtf8(""))
        self.languageCombo.addItem(_fromUtf8(""))
        self.languageCombo.addItem(_fromUtf8(""))
        self.languageCombo.addItem(_fromUtf8(""))
        self.languageCombo.addItem(_fromUtf8(""))
        self.languageCombo.addItem(_fromUtf8(""))
        self.languageCombo.addItem(_fromUtf8(""))
        self.languageCombo.addItem(_fromUtf8(""))
        self.languageCombo.addItem(_fromUtf8(""))
        self.languageCombo.addItem(_fromUtf8(""))
        self.languageCombo.addItem(_fromUtf8(""))
        self.languageCombo.addItem(_fromUtf8(""))
        self.languageCombo.addItem(_fromUtf8(""))
        self.languageCombo.addItem(_fromUtf8(""))
        self.languageCombo.addItem(_fromUtf8(""))
        self.languageCombo.addItem(_fromUtf8(""))
        self.languageCombo.addItem(_fromUtf8(""))
        self.languageCombo.addItem(_fromUtf8(""))
        self.languageCombo.addItem(_fromUtf8(""))
        self.languageCombo.addItem(_fromUtf8(""))
        self.languageCombo.addItem(_fromUtf8(""))
        self.languageCombo.addItem(_fromUtf8(""))
        self.languageCombo.addItem(_fromUtf8(""))
        self.languageCombo.addItem(_fromUtf8(""))
        self.languageCombo.addItem(_fromUtf8(""))
        self.languageCombo.addItem(_fromUtf8(""))
        self.languageCombo.addItem(_fromUtf8(""))
        self.languageCombo.addItem(_fromUtf8(""))
        self.languageCombo.addItem(_fromUtf8(""))
        self.languageCombo.addItem(_fromUtf8(""))
        self.languageCombo.addItem(_fromUtf8(""))
        self.languageCombo.addItem(_fromUtf8(""))
        self.languageCombo.addItem(_fromUtf8(""))
        self.languageCombo.addItem(_fromUtf8(""))
        self.languageCombo.addItem(_fromUtf8(""))
        self.languageCombo.addItem(_fromUtf8(""))
        self.languageCombo.addItem(_fromUtf8(""))
        self.languageCombo.addItem(_fromUtf8(""))
        self.languageCombo.addItem(_fromUtf8(""))
        self.languageCombo.addItem(_fromUtf8(""))
        self.languageCombo.addItem(_fromUtf8(""))
        self.languageCombo.addItem(_fromUtf8(""))
        self.languageCombo.addItem(_fromUtf8(""))
        self.languageCombo.addItem(_fromUtf8(""))
        self.languageCombo.addItem(_fromUtf8(""))
        self.languageCombo.addItem(_fromUtf8(""))
        self.languageCombo.addItem(_fromUtf8(""))
        self.languageCombo.addItem(_fromUtf8(""))
        self.languageCombo.addItem(_fromUtf8(""))
        self.languageCombo.addItem(_fromUtf8(""))
        self.languageCombo.addItem(_fromUtf8(""))
        self.languageCombo.addItem(_fromUtf8(""))
        self.languageCombo.addItem(_fromUtf8(""))
        self.hboxlayout.addWidget(self.languageCombo)
        self.vboxlayout.addLayout(self.hboxlayout)
        self.buttonBox = QtGui.QDialogButtonBox(AddLanguageDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.vboxlayout.addWidget(self.buttonBox)
        self.languageLabel.setBuddy(self.languageCombo)

        self.retranslateUi(AddLanguageDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), AddLanguageDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), AddLanguageDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(AddLanguageDialog)

    def retranslateUi(self, AddLanguageDialog):
        AddLanguageDialog.setWindowTitle(_translate("AddLanguageDialog", "Add Language", None))
        AddLanguageDialog.setToolTip(_translate("AddLanguageDialog", "Add a language to the current project", None))
        AddLanguageDialog.setWhatsThis(_translate("AddLanguageDialog", "<b>Add Language Dialog</b>\n"
"<p>This dialog is used to add a language to the current project.</p>", None))
        self.languageLabel.setText(_translate("AddLanguageDialog", "&Language:", None))
        self.languageCombo.setToolTip(_translate("AddLanguageDialog", "Select a language to add to the current project", None))
        self.languageCombo.setWhatsThis(_translate("AddLanguageDialog", "<b>Language</b>\n"
"<p>Select a language to add to the current project.</p>", None))
        self.languageCombo.setItemText(0, _translate("AddLanguageDialog", "af", None))
        self.languageCombo.setItemText(1, _translate("AddLanguageDialog", "ar", None))
        self.languageCombo.setItemText(2, _translate("AddLanguageDialog", "bg", None))
        self.languageCombo.setItemText(3, _translate("AddLanguageDialog", "bo", None))
        self.languageCombo.setItemText(4, _translate("AddLanguageDialog", "br", None))
        self.languageCombo.setItemText(5, _translate("AddLanguageDialog", "bs", None))
        self.languageCombo.setItemText(6, _translate("AddLanguageDialog", "ca", None))
        self.languageCombo.setItemText(7, _translate("AddLanguageDialog", "cs", None))
        self.languageCombo.setItemText(8, _translate("AddLanguageDialog", "cy", None))
        self.languageCombo.setItemText(9, _translate("AddLanguageDialog", "da", None))
        self.languageCombo.setItemText(10, _translate("AddLanguageDialog", "de", None))
        self.languageCombo.setItemText(11, _translate("AddLanguageDialog", "el", None))
        self.languageCombo.setItemText(12, _translate("AddLanguageDialog", "en", None))
        self.languageCombo.setItemText(13, _translate("AddLanguageDialog", "en_GB", None))
        self.languageCombo.setItemText(14, _translate("AddLanguageDialog", "en_US", None))
        self.languageCombo.setItemText(15, _translate("AddLanguageDialog", "eo", None))
        self.languageCombo.setItemText(16, _translate("AddLanguageDialog", "es", None))
        self.languageCombo.setItemText(17, _translate("AddLanguageDialog", "et", None))
        self.languageCombo.setItemText(18, _translate("AddLanguageDialog", "eu", None))
        self.languageCombo.setItemText(19, _translate("AddLanguageDialog", "fi", None))
        self.languageCombo.setItemText(20, _translate("AddLanguageDialog", "fr", None))
        self.languageCombo.setItemText(21, _translate("AddLanguageDialog", "ga", None))
        self.languageCombo.setItemText(22, _translate("AddLanguageDialog", "gl", None))
        self.languageCombo.setItemText(23, _translate("AddLanguageDialog", "gu", None))
        self.languageCombo.setItemText(24, _translate("AddLanguageDialog", "he", None))
        self.languageCombo.setItemText(25, _translate("AddLanguageDialog", "hi", None))
        self.languageCombo.setItemText(26, _translate("AddLanguageDialog", "hu", None))
        self.languageCombo.setItemText(27, _translate("AddLanguageDialog", "id", None))
        self.languageCombo.setItemText(28, _translate("AddLanguageDialog", "is", None))
        self.languageCombo.setItemText(29, _translate("AddLanguageDialog", "it", None))
        self.languageCombo.setItemText(30, _translate("AddLanguageDialog", "ja", None))
        self.languageCombo.setItemText(31, _translate("AddLanguageDialog", "km", None))
        self.languageCombo.setItemText(32, _translate("AddLanguageDialog", "ko", None))
        self.languageCombo.setItemText(33, _translate("AddLanguageDialog", "lt", None))
        self.languageCombo.setItemText(34, _translate("AddLanguageDialog", "lv", None))
        self.languageCombo.setItemText(35, _translate("AddLanguageDialog", "mi", None))
        self.languageCombo.setItemText(36, _translate("AddLanguageDialog", "mk", None))
        self.languageCombo.setItemText(37, _translate("AddLanguageDialog", "mr", None))
        self.languageCombo.setItemText(38, _translate("AddLanguageDialog", "nl", None))
        self.languageCombo.setItemText(39, _translate("AddLanguageDialog", "no", None))
        self.languageCombo.setItemText(40, _translate("AddLanguageDialog", "no_NY", None))
        self.languageCombo.setItemText(41, _translate("AddLanguageDialog", "oc", None))
        self.languageCombo.setItemText(42, _translate("AddLanguageDialog", "pl", None))
        self.languageCombo.setItemText(43, _translate("AddLanguageDialog", "pt", None))
        self.languageCombo.setItemText(44, _translate("AddLanguageDialog", "pt_BR", None))
        self.languageCombo.setItemText(45, _translate("AddLanguageDialog", "ro", None))
        self.languageCombo.setItemText(46, _translate("AddLanguageDialog", "ru", None))
        self.languageCombo.setItemText(47, _translate("AddLanguageDialog", "sk", None))
        self.languageCombo.setItemText(48, _translate("AddLanguageDialog", "sl", None))
        self.languageCombo.setItemText(49, _translate("AddLanguageDialog", "sr", None))
        self.languageCombo.setItemText(50, _translate("AddLanguageDialog", "sv", None))
        self.languageCombo.setItemText(51, _translate("AddLanguageDialog", "ta", None))
        self.languageCombo.setItemText(52, _translate("AddLanguageDialog", "th", None))
        self.languageCombo.setItemText(53, _translate("AddLanguageDialog", "tr", None))
        self.languageCombo.setItemText(54, _translate("AddLanguageDialog", "uk", None))
        self.languageCombo.setItemText(55, _translate("AddLanguageDialog", "vn", None))
        self.languageCombo.setItemText(56, _translate("AddLanguageDialog", "wa", None))
        self.languageCombo.setItemText(57, _translate("AddLanguageDialog", "zh_CN.GB2312", None))
        self.languageCombo.setItemText(58, _translate("AddLanguageDialog", "zh_TW.Big5", None))
