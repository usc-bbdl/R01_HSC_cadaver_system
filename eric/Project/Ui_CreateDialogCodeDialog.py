# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Project\CreateDialogCodeDialog.ui'
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

class Ui_CreateDialogCodeDialog(object):
    def setupUi(self, CreateDialogCodeDialog):
        CreateDialogCodeDialog.setObjectName(_fromUtf8("CreateDialogCodeDialog"))
        CreateDialogCodeDialog.resize(584, 466)
        CreateDialogCodeDialog.setSizeGripEnabled(True)
        self.vboxlayout = QtGui.QVBoxLayout(CreateDialogCodeDialog)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.gridlayout = QtGui.QGridLayout()
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.label_2 = QtGui.QLabel(CreateDialogCodeDialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridlayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.newButton = QtGui.QPushButton(CreateDialogCodeDialog)
        self.newButton.setObjectName(_fromUtf8("newButton"))
        self.gridlayout.addWidget(self.newButton, 0, 2, 1, 2)
        self.label = QtGui.QLabel(CreateDialogCodeDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridlayout.addWidget(self.label, 0, 0, 1, 1)
        self.clearFilterButton = QtGui.QToolButton(CreateDialogCodeDialog)
        self.clearFilterButton.setText(_fromUtf8(""))
        self.clearFilterButton.setObjectName(_fromUtf8("clearFilterButton"))
        self.gridlayout.addWidget(self.clearFilterButton, 2, 3, 1, 1)
        self.classNameCombo = QtGui.QComboBox(CreateDialogCodeDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.classNameCombo.sizePolicy().hasHeightForWidth())
        self.classNameCombo.setSizePolicy(sizePolicy)
        self.classNameCombo.setObjectName(_fromUtf8("classNameCombo"))
        self.gridlayout.addWidget(self.classNameCombo, 0, 1, 1, 1)
        self.filenameEdit = QtGui.QLineEdit(CreateDialogCodeDialog)
        self.filenameEdit.setReadOnly(True)
        self.filenameEdit.setObjectName(_fromUtf8("filenameEdit"))
        self.gridlayout.addWidget(self.filenameEdit, 1, 1, 1, 3)
        self.filterEdit = QtGui.QLineEdit(CreateDialogCodeDialog)
        self.filterEdit.setObjectName(_fromUtf8("filterEdit"))
        self.gridlayout.addWidget(self.filterEdit, 2, 1, 1, 2)
        self.label_3 = QtGui.QLabel(CreateDialogCodeDialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridlayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.vboxlayout.addLayout(self.gridlayout)
        self.slotsView = QtGui.QTreeView(CreateDialogCodeDialog)
        self.slotsView.setSortingEnabled(True)
        self.slotsView.setObjectName(_fromUtf8("slotsView"))
        self.vboxlayout.addWidget(self.slotsView)
        self.buttonBox = QtGui.QDialogButtonBox(CreateDialogCodeDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.vboxlayout.addWidget(self.buttonBox)
        self.label_2.setBuddy(self.filenameEdit)
        self.label.setBuddy(self.classNameCombo)
        self.label_3.setBuddy(self.filterEdit)

        self.retranslateUi(CreateDialogCodeDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), CreateDialogCodeDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(CreateDialogCodeDialog)
        CreateDialogCodeDialog.setTabOrder(self.classNameCombo, self.newButton)
        CreateDialogCodeDialog.setTabOrder(self.newButton, self.filenameEdit)
        CreateDialogCodeDialog.setTabOrder(self.filenameEdit, self.filterEdit)
        CreateDialogCodeDialog.setTabOrder(self.filterEdit, self.clearFilterButton)
        CreateDialogCodeDialog.setTabOrder(self.clearFilterButton, self.slotsView)
        CreateDialogCodeDialog.setTabOrder(self.slotsView, self.buttonBox)

    def retranslateUi(self, CreateDialogCodeDialog):
        CreateDialogCodeDialog.setWindowTitle(_translate("CreateDialogCodeDialog", "Forms code generator", None))
        self.label_2.setText(_translate("CreateDialogCodeDialog", "&Filename:", None))
        self.newButton.setToolTip(_translate("CreateDialogCodeDialog", "Press to generate a new forms class", None))
        self.newButton.setText(_translate("CreateDialogCodeDialog", "&New...", None))
        self.label.setText(_translate("CreateDialogCodeDialog", "&Classname:", None))
        self.classNameCombo.setToolTip(_translate("CreateDialogCodeDialog", "Select the class that should get the forms code", None))
        self.filenameEdit.setToolTip(_translate("CreateDialogCodeDialog", "Displays the name of the file containing the code", None))
        self.filterEdit.setToolTip(_translate("CreateDialogCodeDialog", "Enter a regular expression to filter the list below", None))
        self.label_3.setText(_translate("CreateDialogCodeDialog", "Filter &with:", None))

