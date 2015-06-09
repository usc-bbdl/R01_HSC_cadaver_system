# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Preferences\ConfigurationPages\ProjectBrowserPage.ui'
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

class Ui_ProjectBrowserPage(object):
    def setupUi(self, ProjectBrowserPage):
        ProjectBrowserPage.setObjectName(_fromUtf8("ProjectBrowserPage"))
        ProjectBrowserPage.resize(617, 497)
        self.verticalLayout = QtGui.QVBoxLayout(ProjectBrowserPage)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.headerLabel = QtGui.QLabel(ProjectBrowserPage)
        self.headerLabel.setObjectName(_fromUtf8("headerLabel"))
        self.verticalLayout.addWidget(self.headerLabel)
        self.line8 = QtGui.QFrame(ProjectBrowserPage)
        self.line8.setFrameShape(QtGui.QFrame.HLine)
        self.line8.setFrameShadow(QtGui.QFrame.Sunken)
        self.line8.setFrameShape(QtGui.QFrame.HLine)
        self.line8.setFrameShadow(QtGui.QFrame.Sunken)
        self.line8.setObjectName(_fromUtf8("line8"))
        self.verticalLayout.addWidget(self.line8)
        self.groupBox = QtGui.QGroupBox(ProjectBrowserPage)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.pbHighlightedButton = QtGui.QPushButton(self.groupBox)
        self.pbHighlightedButton.setMinimumSize(QtCore.QSize(100, 0))
        self.pbHighlightedButton.setText(_fromUtf8(""))
        self.pbHighlightedButton.setObjectName(_fromUtf8("pbHighlightedButton"))
        self.horizontalLayout.addWidget(self.pbHighlightedButton)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addWidget(self.groupBox)
        self.pbGroup = QtGui.QGroupBox(ProjectBrowserPage)
        self.pbGroup.setObjectName(_fromUtf8("pbGroup"))
        self.vboxlayout = QtGui.QVBoxLayout(self.pbGroup)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        self.label_6 = QtGui.QLabel(self.pbGroup)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.hboxlayout.addWidget(self.label_6)
        self.projectTypeCombo = QtGui.QComboBox(self.pbGroup)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.projectTypeCombo.sizePolicy().hasHeightForWidth())
        self.projectTypeCombo.setSizePolicy(sizePolicy)
        self.projectTypeCombo.setObjectName(_fromUtf8("projectTypeCombo"))
        self.hboxlayout.addWidget(self.projectTypeCombo)
        self.vboxlayout.addLayout(self.hboxlayout)
        self.gridlayout = QtGui.QGridLayout()
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.sourcesBrowserCheckBox = QtGui.QCheckBox(self.pbGroup)
        self.sourcesBrowserCheckBox.setObjectName(_fromUtf8("sourcesBrowserCheckBox"))
        self.gridlayout.addWidget(self.sourcesBrowserCheckBox, 0, 0, 1, 1)
        self.translationsBrowserCheckBox = QtGui.QCheckBox(self.pbGroup)
        self.translationsBrowserCheckBox.setObjectName(_fromUtf8("translationsBrowserCheckBox"))
        self.gridlayout.addWidget(self.translationsBrowserCheckBox, 0, 1, 1, 1)
        self.formsBrowserCheckBox = QtGui.QCheckBox(self.pbGroup)
        self.formsBrowserCheckBox.setObjectName(_fromUtf8("formsBrowserCheckBox"))
        self.gridlayout.addWidget(self.formsBrowserCheckBox, 1, 0, 1, 1)
        self.interfacesBrowserCheckBox = QtGui.QCheckBox(self.pbGroup)
        self.interfacesBrowserCheckBox.setObjectName(_fromUtf8("interfacesBrowserCheckBox"))
        self.gridlayout.addWidget(self.interfacesBrowserCheckBox, 1, 1, 1, 1)
        self.resourcesBrowserCheckBox = QtGui.QCheckBox(self.pbGroup)
        self.resourcesBrowserCheckBox.setObjectName(_fromUtf8("resourcesBrowserCheckBox"))
        self.gridlayout.addWidget(self.resourcesBrowserCheckBox, 2, 0, 1, 1)
        self.othersBrowserCheckBox = QtGui.QCheckBox(self.pbGroup)
        self.othersBrowserCheckBox.setObjectName(_fromUtf8("othersBrowserCheckBox"))
        self.gridlayout.addWidget(self.othersBrowserCheckBox, 2, 1, 1, 1)
        self.vboxlayout.addLayout(self.gridlayout)
        self.verticalLayout.addWidget(self.pbGroup)
        self.followEditorCheckBox = QtGui.QCheckBox(ProjectBrowserPage)
        self.followEditorCheckBox.setObjectName(_fromUtf8("followEditorCheckBox"))
        self.verticalLayout.addWidget(self.followEditorCheckBox)
        self.hideGeneratedCheckBox = QtGui.QCheckBox(ProjectBrowserPage)
        self.hideGeneratedCheckBox.setObjectName(_fromUtf8("hideGeneratedCheckBox"))
        self.verticalLayout.addWidget(self.hideGeneratedCheckBox)
        spacerItem1 = QtGui.QSpacerItem(599, 21, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)

        self.retranslateUi(ProjectBrowserPage)
        QtCore.QMetaObject.connectSlotsByName(ProjectBrowserPage)
        ProjectBrowserPage.setTabOrder(self.pbHighlightedButton, self.projectTypeCombo)
        ProjectBrowserPage.setTabOrder(self.projectTypeCombo, self.sourcesBrowserCheckBox)
        ProjectBrowserPage.setTabOrder(self.sourcesBrowserCheckBox, self.formsBrowserCheckBox)
        ProjectBrowserPage.setTabOrder(self.formsBrowserCheckBox, self.resourcesBrowserCheckBox)
        ProjectBrowserPage.setTabOrder(self.resourcesBrowserCheckBox, self.translationsBrowserCheckBox)
        ProjectBrowserPage.setTabOrder(self.translationsBrowserCheckBox, self.interfacesBrowserCheckBox)
        ProjectBrowserPage.setTabOrder(self.interfacesBrowserCheckBox, self.othersBrowserCheckBox)
        ProjectBrowserPage.setTabOrder(self.othersBrowserCheckBox, self.followEditorCheckBox)
        ProjectBrowserPage.setTabOrder(self.followEditorCheckBox, self.hideGeneratedCheckBox)

    def retranslateUi(self, ProjectBrowserPage):
        self.headerLabel.setText(_translate("ProjectBrowserPage", "<b>Configure project viewer settings</b>", None))
        self.groupBox.setTitle(_translate("ProjectBrowserPage", "Colours", None))
        self.label.setText(_translate("ProjectBrowserPage", "Highlighted entries (Others):", None))
        self.pbHighlightedButton.setToolTip(_translate("ProjectBrowserPage", "Select the colour for highlighted entries in the Others viewer.", None))
        self.pbGroup.setTitle(_translate("ProjectBrowserPage", "Visible Project Browsers", None))
        self.label_6.setText(_translate("ProjectBrowserPage", "Projecttype:", None))
        self.projectTypeCombo.setToolTip(_translate("ProjectBrowserPage", "Select the project type to be configured", None))
        self.sourcesBrowserCheckBox.setToolTip(_translate("ProjectBrowserPage", "Select to show the sources browser", None))
        self.sourcesBrowserCheckBox.setText(_translate("ProjectBrowserPage", "Sources Browser", None))
        self.translationsBrowserCheckBox.setToolTip(_translate("ProjectBrowserPage", "Select to show the translations browser", None))
        self.translationsBrowserCheckBox.setText(_translate("ProjectBrowserPage", "Translations Browser", None))
        self.formsBrowserCheckBox.setToolTip(_translate("ProjectBrowserPage", "Select to show the forms browser", None))
        self.formsBrowserCheckBox.setText(_translate("ProjectBrowserPage", "Forms Browser", None))
        self.interfacesBrowserCheckBox.setToolTip(_translate("ProjectBrowserPage", "Select to show the interfaces (IDL) browser", None))
        self.interfacesBrowserCheckBox.setText(_translate("ProjectBrowserPage", "Interfaces (IDL) Browser", None))
        self.resourcesBrowserCheckBox.setToolTip(_translate("ProjectBrowserPage", "Select to show the resources browser", None))
        self.resourcesBrowserCheckBox.setText(_translate("ProjectBrowserPage", "Resources Browser", None))
        self.othersBrowserCheckBox.setToolTip(_translate("ProjectBrowserPage", "Select to show the browser for other files", None))
        self.othersBrowserCheckBox.setText(_translate("ProjectBrowserPage", "Others Browser", None))
        self.followEditorCheckBox.setToolTip(_translate("ProjectBrowserPage", "Select to make the project browsers highlight the file of the current editor.", None))
        self.followEditorCheckBox.setText(_translate("ProjectBrowserPage", "Highlight file of current editor", None))
        self.hideGeneratedCheckBox.setToolTip(_translate("ProjectBrowserPage", "Select to hide sources generated from form files", None))
        self.hideGeneratedCheckBox.setText(_translate("ProjectBrowserPage", "Hide generated form sources", None))

