# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Plugins\VcsPlugins\vcsPySvn\ConfigurationPage\SubversionPage.ui'
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

class Ui_SubversionPage(object):
    def setupUi(self, SubversionPage):
        SubversionPage.setObjectName(_fromUtf8("SubversionPage"))
        SubversionPage.resize(402, 354)
        self.vboxlayout = QtGui.QVBoxLayout(SubversionPage)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.headerLabel = QtGui.QLabel(SubversionPage)
        self.headerLabel.setObjectName(_fromUtf8("headerLabel"))
        self.vboxlayout.addWidget(self.headerLabel)
        self.line15 = QtGui.QFrame(SubversionPage)
        self.line15.setFrameShape(QtGui.QFrame.HLine)
        self.line15.setFrameShadow(QtGui.QFrame.Sunken)
        self.line15.setFrameShape(QtGui.QFrame.HLine)
        self.line15.setFrameShadow(QtGui.QFrame.Sunken)
        self.line15.setObjectName(_fromUtf8("line15"))
        self.vboxlayout.addWidget(self.line15)
        self.groupBox = QtGui.QGroupBox(SubversionPage)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.hboxlayout = QtGui.QHBoxLayout(self.groupBox)
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.hboxlayout.addWidget(self.label)
        self.logSpinBox = QtGui.QSpinBox(self.groupBox)
        self.logSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.logSpinBox.setMaximum(999999)
        self.logSpinBox.setObjectName(_fromUtf8("logSpinBox"))
        self.hboxlayout.addWidget(self.logSpinBox)
        spacerItem = QtGui.QSpacerItem(41, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)
        self.vboxlayout.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(SubversionPage)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.hboxlayout1 = QtGui.QHBoxLayout(self.groupBox_2)
        self.hboxlayout1.setObjectName(_fromUtf8("hboxlayout1"))
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.hboxlayout1.addWidget(self.label_2)
        self.commitSpinBox = QtGui.QSpinBox(self.groupBox_2)
        self.commitSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.commitSpinBox.setMinimum(1)
        self.commitSpinBox.setMaximum(100)
        self.commitSpinBox.setObjectName(_fromUtf8("commitSpinBox"))
        self.hboxlayout1.addWidget(self.commitSpinBox)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout1.addItem(spacerItem1)
        self.vboxlayout.addWidget(self.groupBox_2)
        self.configButton = QtGui.QPushButton(SubversionPage)
        self.configButton.setObjectName(_fromUtf8("configButton"))
        self.vboxlayout.addWidget(self.configButton)
        self.serversButton = QtGui.QPushButton(SubversionPage)
        self.serversButton.setObjectName(_fromUtf8("serversButton"))
        self.vboxlayout.addWidget(self.serversButton)
        spacerItem2 = QtGui.QSpacerItem(388, 31, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vboxlayout.addItem(spacerItem2)

        self.retranslateUi(SubversionPage)
        QtCore.QMetaObject.connectSlotsByName(SubversionPage)

    def retranslateUi(self, SubversionPage):
        self.headerLabel.setText(_translate("SubversionPage", "<b>Configure Subversion Interface</b>", None))
        self.groupBox.setTitle(_translate("SubversionPage", "Log", None))
        self.label.setText(_translate("SubversionPage", "No. of log messages shown:", None))
        self.logSpinBox.setToolTip(_translate("SubversionPage", "Enter the number of log messages to be shown", None))
        self.groupBox_2.setTitle(_translate("SubversionPage", "Commit", None))
        self.label_2.setText(_translate("SubversionPage", "No. of commit messages to remember:", None))
        self.commitSpinBox.setToolTip(_translate("SubversionPage", "Enter the number of commit messages to remember", None))
        self.configButton.setToolTip(_translate("SubversionPage", "Edit the subversion config file", None))
        self.configButton.setText(_translate("SubversionPage", "Edit config file", None))
        self.serversButton.setToolTip(_translate("SubversionPage", "Edit the subversion servers file", None))
        self.serversButton.setText(_translate("SubversionPage", "Edit servers file", None))

