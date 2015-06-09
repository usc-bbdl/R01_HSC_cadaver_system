# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Preferences\ConfigurationPages\TemplatesPage.ui'
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

class Ui_TemplatesPage(object):
    def setupUi(self, TemplatesPage):
        TemplatesPage.setObjectName(_fromUtf8("TemplatesPage"))
        TemplatesPage.resize(532, 374)
        self.vboxlayout = QtGui.QVBoxLayout(TemplatesPage)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.headerLabel = QtGui.QLabel(TemplatesPage)
        self.headerLabel.setObjectName(_fromUtf8("headerLabel"))
        self.vboxlayout.addWidget(self.headerLabel)
        self.line11_2_2_2_2_2 = QtGui.QFrame(TemplatesPage)
        self.line11_2_2_2_2_2.setFrameShape(QtGui.QFrame.HLine)
        self.line11_2_2_2_2_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line11_2_2_2_2_2.setFrameShape(QtGui.QFrame.HLine)
        self.line11_2_2_2_2_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line11_2_2_2_2_2.setObjectName(_fromUtf8("line11_2_2_2_2_2"))
        self.vboxlayout.addWidget(self.line11_2_2_2_2_2)
        self.groupBox = QtGui.QGroupBox(TemplatesPage)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.vboxlayout1 = QtGui.QVBoxLayout(self.groupBox)
        self.vboxlayout1.setObjectName(_fromUtf8("vboxlayout1"))
        self.templatesAutoOpenGroupsCheckBox = QtGui.QCheckBox(self.groupBox)
        self.templatesAutoOpenGroupsCheckBox.setObjectName(_fromUtf8("templatesAutoOpenGroupsCheckBox"))
        self.vboxlayout1.addWidget(self.templatesAutoOpenGroupsCheckBox)
        self.vboxlayout.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(TemplatesPage)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.vboxlayout2 = QtGui.QVBoxLayout(self.groupBox_2)
        self.vboxlayout2.setObjectName(_fromUtf8("vboxlayout2"))
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        self.textLabel1_19 = QtGui.QLabel(self.groupBox_2)
        self.textLabel1_19.setObjectName(_fromUtf8("textLabel1_19"))
        self.hboxlayout.addWidget(self.textLabel1_19)
        self.templatesSeparatorCharEdit = QtGui.QLineEdit(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.templatesSeparatorCharEdit.sizePolicy().hasHeightForWidth())
        self.templatesSeparatorCharEdit.setSizePolicy(sizePolicy)
        self.templatesSeparatorCharEdit.setMaxLength(1)
        self.templatesSeparatorCharEdit.setObjectName(_fromUtf8("templatesSeparatorCharEdit"))
        self.hboxlayout.addWidget(self.templatesSeparatorCharEdit)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)
        self.vboxlayout2.addLayout(self.hboxlayout)
        self.groupBox_3 = QtGui.QGroupBox(self.groupBox_2)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.vboxlayout3 = QtGui.QVBoxLayout(self.groupBox_3)
        self.vboxlayout3.setObjectName(_fromUtf8("vboxlayout3"))
        self.templatesMultiDialogButton = QtGui.QRadioButton(self.groupBox_3)
        self.templatesMultiDialogButton.setObjectName(_fromUtf8("templatesMultiDialogButton"))
        self.vboxlayout3.addWidget(self.templatesMultiDialogButton)
        self.templatesSingleDialogButton = QtGui.QRadioButton(self.groupBox_3)
        self.templatesSingleDialogButton.setObjectName(_fromUtf8("templatesSingleDialogButton"))
        self.vboxlayout3.addWidget(self.templatesSingleDialogButton)
        self.vboxlayout2.addWidget(self.groupBox_3)
        self.vboxlayout.addWidget(self.groupBox_2)
        self.groupBox_4 = QtGui.QGroupBox(TemplatesPage)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.vboxlayout4 = QtGui.QVBoxLayout(self.groupBox_4)
        self.vboxlayout4.setObjectName(_fromUtf8("vboxlayout4"))
        self.templatesToolTipCheckBox = QtGui.QCheckBox(self.groupBox_4)
        self.templatesToolTipCheckBox.setObjectName(_fromUtf8("templatesToolTipCheckBox"))
        self.vboxlayout4.addWidget(self.templatesToolTipCheckBox)
        self.vboxlayout.addWidget(self.groupBox_4)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vboxlayout.addItem(spacerItem1)

        self.retranslateUi(TemplatesPage)
        QtCore.QMetaObject.connectSlotsByName(TemplatesPage)
        TemplatesPage.setTabOrder(self.templatesAutoOpenGroupsCheckBox, self.templatesSeparatorCharEdit)
        TemplatesPage.setTabOrder(self.templatesSeparatorCharEdit, self.templatesMultiDialogButton)
        TemplatesPage.setTabOrder(self.templatesMultiDialogButton, self.templatesSingleDialogButton)
        TemplatesPage.setTabOrder(self.templatesSingleDialogButton, self.templatesToolTipCheckBox)

    def retranslateUi(self, TemplatesPage):
        self.headerLabel.setText(_translate("TemplatesPage", "<b>Configure Templates</b>", None))
        self.groupBox.setTitle(_translate("TemplatesPage", "Groups", None))
        self.templatesAutoOpenGroupsCheckBox.setToolTip(_translate("TemplatesPage", "Select, if groups having entries should be opened automatically", None))
        self.templatesAutoOpenGroupsCheckBox.setText(_translate("TemplatesPage", "Expand groups automatically", None))
        self.groupBox_2.setTitle(_translate("TemplatesPage", "Variables", None))
        self.textLabel1_19.setText(_translate("TemplatesPage", "Separator:", None))
        self.templatesSeparatorCharEdit.setToolTip(_translate("TemplatesPage", "Enter the character that encloses variables", None))
        self.groupBox_3.setTitle(_translate("TemplatesPage", "Input method for variables", None))
        self.templatesMultiDialogButton.setToolTip(_translate("TemplatesPage", "Select, if a new dialog should be opened for every template variable", None))
        self.templatesMultiDialogButton.setText(_translate("TemplatesPage", "One dialog per template variable", None))
        self.templatesSingleDialogButton.setToolTip(_translate("TemplatesPage", "Select, if only one dialog for all template variables should be shown", None))
        self.templatesSingleDialogButton.setText(_translate("TemplatesPage", "One dialog for all template variables", None))
        self.groupBox_4.setTitle(_translate("TemplatesPage", "Tooltips", None))
        self.templatesToolTipCheckBox.setToolTip(_translate("TemplatesPage", "Select, if the template text should be shown in a tooltip", None))
        self.templatesToolTipCheckBox.setText(_translate("TemplatesPage", "Show template text in tooltip", None))

