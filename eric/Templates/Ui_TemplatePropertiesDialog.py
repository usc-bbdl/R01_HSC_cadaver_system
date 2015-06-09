# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Templates\TemplatePropertiesDialog.ui'
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

class Ui_TemplatePropertiesDialog(object):
    def setupUi(self, TemplatePropertiesDialog):
        TemplatePropertiesDialog.setObjectName(_fromUtf8("TemplatePropertiesDialog"))
        TemplatePropertiesDialog.resize(448, 323)
        TemplatePropertiesDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtGui.QVBoxLayout(TemplatePropertiesDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.textLabel1 = QtGui.QLabel(TemplatePropertiesDialog)
        self.textLabel1.setObjectName(_fromUtf8("textLabel1"))
        self.gridLayout.addWidget(self.textLabel1, 0, 0, 1, 1)
        self.nameEdit = QtGui.QLineEdit(TemplatePropertiesDialog)
        self.nameEdit.setObjectName(_fromUtf8("nameEdit"))
        self.gridLayout.addWidget(self.nameEdit, 0, 1, 1, 1)
        self.descriptionLabel = QtGui.QLabel(TemplatePropertiesDialog)
        self.descriptionLabel.setObjectName(_fromUtf8("descriptionLabel"))
        self.gridLayout.addWidget(self.descriptionLabel, 1, 0, 1, 1)
        self.descriptionEdit = QtGui.QLineEdit(TemplatePropertiesDialog)
        self.descriptionEdit.setObjectName(_fromUtf8("descriptionEdit"))
        self.gridLayout.addWidget(self.descriptionEdit, 1, 1, 1, 1)
        self.groupLabel = QtGui.QLabel(TemplatePropertiesDialog)
        self.groupLabel.setObjectName(_fromUtf8("groupLabel"))
        self.gridLayout.addWidget(self.groupLabel, 2, 0, 1, 1)
        self.groupCombo = QtGui.QComboBox(TemplatePropertiesDialog)
        self.groupCombo.setToolTip(_fromUtf8(""))
        self.groupCombo.setObjectName(_fromUtf8("groupCombo"))
        self.gridLayout.addWidget(self.groupCombo, 2, 1, 1, 1)
        self.templateLabel = QtGui.QLabel(TemplatePropertiesDialog)
        self.templateLabel.setAlignment(QtCore.Qt.AlignTop)
        self.templateLabel.setObjectName(_fromUtf8("templateLabel"))
        self.gridLayout.addWidget(self.templateLabel, 3, 0, 1, 1)
        self.templateEdit = QtGui.QTextEdit(TemplatePropertiesDialog)
        self.templateEdit.setLineWrapMode(QtGui.QTextEdit.NoWrap)
        self.templateEdit.setAcceptRichText(False)
        self.templateEdit.setObjectName(_fromUtf8("templateEdit"))
        self.gridLayout.addWidget(self.templateEdit, 3, 1, 3, 1)
        self.helpButton = QtGui.QPushButton(TemplatePropertiesDialog)
        self.helpButton.setObjectName(_fromUtf8("helpButton"))
        self.gridLayout.addWidget(self.helpButton, 4, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(84, 98, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 5, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.buttonBox = QtGui.QDialogButtonBox(TemplatePropertiesDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(TemplatePropertiesDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), TemplatePropertiesDialog.reject)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), TemplatePropertiesDialog.accept)
        QtCore.QMetaObject.connectSlotsByName(TemplatePropertiesDialog)
        TemplatePropertiesDialog.setTabOrder(self.nameEdit, self.descriptionEdit)
        TemplatePropertiesDialog.setTabOrder(self.descriptionEdit, self.groupCombo)
        TemplatePropertiesDialog.setTabOrder(self.groupCombo, self.templateEdit)
        TemplatePropertiesDialog.setTabOrder(self.templateEdit, self.helpButton)
        TemplatePropertiesDialog.setTabOrder(self.helpButton, self.buttonBox)

    def retranslateUi(self, TemplatePropertiesDialog):
        TemplatePropertiesDialog.setWindowTitle(_translate("TemplatePropertiesDialog", "Template Properties", None))
        self.textLabel1.setText(_translate("TemplatePropertiesDialog", "Name:", None))
        self.nameEdit.setToolTip(_translate("TemplatePropertiesDialog", "Enter the name of the template/group. Templates are autocompleted upon this name.", None))
        self.descriptionLabel.setText(_translate("TemplatePropertiesDialog", "Description:", None))
        self.descriptionEdit.setToolTip(_translate("TemplatePropertiesDialog", "Enter a description for the template", None))
        self.groupLabel.setText(_translate("TemplatePropertiesDialog", "Group:", None))
        self.templateLabel.setText(_translate("TemplatePropertiesDialog", "Template:", None))
        self.templateEdit.setToolTip(_translate("TemplatePropertiesDialog", "Enter the text of the template", None))
        self.templateEdit.setWhatsThis(_translate("TemplatePropertiesDialog", "<b>Template Text</b>\n"
"<p>Enter the template text in this area. Every occurrence of $VAR$ will be replaced\n"
"by the associated text when the template is applied.  Predefined variables may be used in the template. The separator character might\n"
"be changed via the preferences dialog.</p>\n"
"<p>Press the help button for more information.</p>", None))
        self.helpButton.setText(_translate("TemplatePropertiesDialog", "&Help", None))
        self.helpButton.setShortcut(_translate("TemplatePropertiesDialog", "Alt+H", None))

