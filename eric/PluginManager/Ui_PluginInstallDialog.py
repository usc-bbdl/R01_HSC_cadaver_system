# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\PluginManager\PluginInstallDialog.ui'
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

class Ui_PluginInstallDialog(object):
    def setupUi(self, PluginInstallDialog):
        PluginInstallDialog.setObjectName(_fromUtf8("PluginInstallDialog"))
        PluginInstallDialog.resize(611, 362)
        self.vboxlayout = QtGui.QVBoxLayout(PluginInstallDialog)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.wizard = QtGui.QStackedWidget(PluginInstallDialog)
        self.wizard.setObjectName(_fromUtf8("wizard"))
        self.selectionPage = QtGui.QWidget()
        self.selectionPage.setObjectName(_fromUtf8("selectionPage"))
        self.gridlayout = QtGui.QGridLayout(self.selectionPage)
        self.gridlayout.setMargin(0)
        self.gridlayout.setVerticalSpacing(6)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.label = QtGui.QLabel(self.selectionPage)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridlayout.addWidget(self.label, 0, 0, 1, 2)
        self.archivesList = QtGui.QListWidget(self.selectionPage)
        self.archivesList.setAlternatingRowColors(True)
        self.archivesList.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.archivesList.setObjectName(_fromUtf8("archivesList"))
        self.gridlayout.addWidget(self.archivesList, 1, 0, 3, 1)
        self.addArchivesButton = QtGui.QPushButton(self.selectionPage)
        self.addArchivesButton.setObjectName(_fromUtf8("addArchivesButton"))
        self.gridlayout.addWidget(self.addArchivesButton, 1, 1, 1, 1)
        self.removeArchivesButton = QtGui.QPushButton(self.selectionPage)
        self.removeArchivesButton.setEnabled(False)
        self.removeArchivesButton.setObjectName(_fromUtf8("removeArchivesButton"))
        self.gridlayout.addWidget(self.removeArchivesButton, 2, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 101, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridlayout.addItem(spacerItem, 3, 1, 1, 1)
        self.wizard.addWidget(self.selectionPage)
        self.destinationPage = QtGui.QWidget()
        self.destinationPage.setObjectName(_fromUtf8("destinationPage"))
        self.vboxlayout1 = QtGui.QVBoxLayout(self.destinationPage)
        self.vboxlayout1.setMargin(0)
        self.vboxlayout1.setObjectName(_fromUtf8("vboxlayout1"))
        self.label_2 = QtGui.QLabel(self.destinationPage)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.vboxlayout1.addWidget(self.label_2)
        self.destinationCombo = QtGui.QComboBox(self.destinationPage)
        self.destinationCombo.setObjectName(_fromUtf8("destinationCombo"))
        self.vboxlayout1.addWidget(self.destinationCombo)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vboxlayout1.addItem(spacerItem1)
        self.wizard.addWidget(self.destinationPage)
        self.summaryPage = QtGui.QWidget()
        self.summaryPage.setObjectName(_fromUtf8("summaryPage"))
        self.vboxlayout2 = QtGui.QVBoxLayout(self.summaryPage)
        self.vboxlayout2.setMargin(0)
        self.vboxlayout2.setObjectName(_fromUtf8("vboxlayout2"))
        self.label_3 = QtGui.QLabel(self.summaryPage)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.vboxlayout2.addWidget(self.label_3)
        self.summaryEdit = QtGui.QTextEdit(self.summaryPage)
        self.summaryEdit.setReadOnly(True)
        self.summaryEdit.setObjectName(_fromUtf8("summaryEdit"))
        self.vboxlayout2.addWidget(self.summaryEdit)
        self.progress = QtGui.QProgressBar(self.summaryPage)
        self.progress.setProperty("value", 0)
        self.progress.setObjectName(_fromUtf8("progress"))
        self.vboxlayout2.addWidget(self.progress)
        self.wizard.addWidget(self.summaryPage)
        self.vboxlayout.addWidget(self.wizard)
        self.buttonBox = QtGui.QDialogButtonBox(PluginInstallDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(PluginInstallDialog)
        self.wizard.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(PluginInstallDialog)
        PluginInstallDialog.setTabOrder(self.addArchivesButton, self.archivesList)
        PluginInstallDialog.setTabOrder(self.archivesList, self.removeArchivesButton)
        PluginInstallDialog.setTabOrder(self.removeArchivesButton, self.destinationCombo)
        PluginInstallDialog.setTabOrder(self.destinationCombo, self.summaryEdit)
        PluginInstallDialog.setTabOrder(self.summaryEdit, self.buttonBox)

    def retranslateUi(self, PluginInstallDialog):
        PluginInstallDialog.setWindowTitle(_translate("PluginInstallDialog", "Plugin Installation", None))
        self.label.setText(_translate("PluginInstallDialog", "<b>Enter the plugin archives to install</b>", None))
        self.archivesList.setSortingEnabled(True)
        self.addArchivesButton.setToolTip(_translate("PluginInstallDialog", "Add plugin ZIP-archives via a file selection dialog", None))
        self.addArchivesButton.setText(_translate("PluginInstallDialog", "Add ...", None))
        self.removeArchivesButton.setToolTip(_translate("PluginInstallDialog", "Remove the selected entries from the list of plugin archives to be installed", None))
        self.removeArchivesButton.setText(_translate("PluginInstallDialog", "Remove", None))
        self.label_2.setText(_translate("PluginInstallDialog", "<b>Select the destination plugin directory</b>", None))
        self.destinationCombo.setToolTip(_translate("PluginInstallDialog", "Select the destination plugin area", None))
        self.label_3.setText(_translate("PluginInstallDialog", "<b>Installation Summary</b>", None))
        self.summaryEdit.setToolTip(_translate("PluginInstallDialog", "This shows the summary of the installation data", None))

