# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Plugins\VcsPlugins\vcsPySvn\SvnRelocateDialog.ui'
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

class Ui_SvnRelocateDialog(object):
    def setupUi(self, SvnRelocateDialog):
        SvnRelocateDialog.setObjectName(_fromUtf8("SvnRelocateDialog"))
        SvnRelocateDialog.resize(531, 119)
        SvnRelocateDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtGui.QVBoxLayout(SvnRelocateDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridlayout = QtGui.QGridLayout()
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.currUrlLabel = QtGui.QLabel(SvnRelocateDialog)
        self.currUrlLabel.setFrameShape(QtGui.QFrame.StyledPanel)
        self.currUrlLabel.setText(_fromUtf8(""))
        self.currUrlLabel.setObjectName(_fromUtf8("currUrlLabel"))
        self.gridlayout.addWidget(self.currUrlLabel, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(SvnRelocateDialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridlayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.newUrlEdit = QtGui.QLineEdit(SvnRelocateDialog)
        self.newUrlEdit.setObjectName(_fromUtf8("newUrlEdit"))
        self.gridlayout.addWidget(self.newUrlEdit, 1, 1, 1, 1)
        self.label = QtGui.QLabel(SvnRelocateDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridlayout.addWidget(self.label, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridlayout)
        self.insideCheckBox = QtGui.QCheckBox(SvnRelocateDialog)
        self.insideCheckBox.setObjectName(_fromUtf8("insideCheckBox"))
        self.verticalLayout.addWidget(self.insideCheckBox)
        self.buttonBox = QtGui.QDialogButtonBox(SvnRelocateDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(SvnRelocateDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), SvnRelocateDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), SvnRelocateDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SvnRelocateDialog)
        SvnRelocateDialog.setTabOrder(self.newUrlEdit, self.insideCheckBox)
        SvnRelocateDialog.setTabOrder(self.insideCheckBox, self.buttonBox)

    def retranslateUi(self, SvnRelocateDialog):
        SvnRelocateDialog.setWindowTitle(_translate("SvnRelocateDialog", "Subversion Relocate", None))
        self.label_2.setText(_translate("SvnRelocateDialog", "New repository URL:", None))
        self.newUrlEdit.setToolTip(_translate("SvnRelocateDialog", "Enter the URL of the repository the working space should be relocated to", None))
        self.label.setText(_translate("SvnRelocateDialog", "Current repository URL:", None))
        self.insideCheckBox.setToolTip(_translate("SvnRelocateDialog", "Select, if the relocate should happen inside the repository", None))
        self.insideCheckBox.setText(_translate("SvnRelocateDialog", "Relocate inside repository (used, if the repository layout has changed)", None))

