# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Tasks\TaskPropertiesDialog.ui'
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

class Ui_TaskPropertiesDialog(object):
    def setupUi(self, TaskPropertiesDialog):
        TaskPropertiesDialog.setObjectName(_fromUtf8("TaskPropertiesDialog"))
        TaskPropertiesDialog.resize(579, 297)
        TaskPropertiesDialog.setSizeGripEnabled(True)
        self.gridlayout = QtGui.QGridLayout(TaskPropertiesDialog)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.label = QtGui.QLabel(TaskPropertiesDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridlayout.addWidget(self.label, 0, 0, 1, 1)
        self.descriptionEdit = QtGui.QLineEdit(TaskPropertiesDialog)
        self.descriptionEdit.setObjectName(_fromUtf8("descriptionEdit"))
        self.gridlayout.addWidget(self.descriptionEdit, 0, 1, 1, 3)
        self.textLabel1 = QtGui.QLabel(TaskPropertiesDialog)
        self.textLabel1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.textLabel1.setObjectName(_fromUtf8("textLabel1"))
        self.gridlayout.addWidget(self.textLabel1, 1, 0, 1, 1)
        self.longtextEdit = QtGui.QTextEdit(TaskPropertiesDialog)
        self.longtextEdit.setObjectName(_fromUtf8("longtextEdit"))
        self.gridlayout.addWidget(self.longtextEdit, 1, 1, 1, 3)
        self.textLabel2 = QtGui.QLabel(TaskPropertiesDialog)
        self.textLabel2.setObjectName(_fromUtf8("textLabel2"))
        self.gridlayout.addWidget(self.textLabel2, 2, 0, 1, 1)
        self.creationLabel = QtGui.QLabel(TaskPropertiesDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.creationLabel.sizePolicy().hasHeightForWidth())
        self.creationLabel.setSizePolicy(sizePolicy)
        self.creationLabel.setObjectName(_fromUtf8("creationLabel"))
        self.gridlayout.addWidget(self.creationLabel, 2, 1, 1, 3)
        self.textLabel4 = QtGui.QLabel(TaskPropertiesDialog)
        self.textLabel4.setObjectName(_fromUtf8("textLabel4"))
        self.gridlayout.addWidget(self.textLabel4, 3, 0, 1, 1)
        self.priorityCombo = QtGui.QComboBox(TaskPropertiesDialog)
        self.priorityCombo.setObjectName(_fromUtf8("priorityCombo"))
        self.priorityCombo.addItem(_fromUtf8(""))
        self.priorityCombo.addItem(_fromUtf8(""))
        self.priorityCombo.addItem(_fromUtf8(""))
        self.gridlayout.addWidget(self.priorityCombo, 3, 1, 1, 1)
        self.projectCheckBox = QtGui.QCheckBox(TaskPropertiesDialog)
        self.projectCheckBox.setObjectName(_fromUtf8("projectCheckBox"))
        self.gridlayout.addWidget(self.projectCheckBox, 3, 2, 1, 1)
        self.completedCheckBox = QtGui.QCheckBox(TaskPropertiesDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.completedCheckBox.sizePolicy().hasHeightForWidth())
        self.completedCheckBox.setSizePolicy(sizePolicy)
        self.completedCheckBox.setObjectName(_fromUtf8("completedCheckBox"))
        self.gridlayout.addWidget(self.completedCheckBox, 3, 3, 1, 1)
        self.textLabel5 = QtGui.QLabel(TaskPropertiesDialog)
        self.textLabel5.setObjectName(_fromUtf8("textLabel5"))
        self.gridlayout.addWidget(self.textLabel5, 4, 0, 1, 1)
        self.filenameEdit = QtGui.QLineEdit(TaskPropertiesDialog)
        self.filenameEdit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.filenameEdit.setReadOnly(True)
        self.filenameEdit.setObjectName(_fromUtf8("filenameEdit"))
        self.gridlayout.addWidget(self.filenameEdit, 4, 1, 1, 3)
        self.textLabel6 = QtGui.QLabel(TaskPropertiesDialog)
        self.textLabel6.setObjectName(_fromUtf8("textLabel6"))
        self.gridlayout.addWidget(self.textLabel6, 5, 0, 1, 1)
        self.linenoEdit = QtGui.QLineEdit(TaskPropertiesDialog)
        self.linenoEdit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.linenoEdit.setReadOnly(True)
        self.linenoEdit.setObjectName(_fromUtf8("linenoEdit"))
        self.gridlayout.addWidget(self.linenoEdit, 5, 1, 1, 3)
        self.buttonBox = QtGui.QDialogButtonBox(TaskPropertiesDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridlayout.addWidget(self.buttonBox, 6, 0, 1, 4)
        self.label.setBuddy(self.descriptionEdit)
        self.textLabel1.setBuddy(self.longtextEdit)
        self.textLabel4.setBuddy(self.priorityCombo)

        self.retranslateUi(TaskPropertiesDialog)
        self.priorityCombo.setCurrentIndex(1)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), TaskPropertiesDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), TaskPropertiesDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(TaskPropertiesDialog)
        TaskPropertiesDialog.setTabOrder(self.descriptionEdit, self.longtextEdit)
        TaskPropertiesDialog.setTabOrder(self.longtextEdit, self.priorityCombo)
        TaskPropertiesDialog.setTabOrder(self.priorityCombo, self.projectCheckBox)
        TaskPropertiesDialog.setTabOrder(self.projectCheckBox, self.completedCheckBox)
        TaskPropertiesDialog.setTabOrder(self.completedCheckBox, self.buttonBox)

    def retranslateUi(self, TaskPropertiesDialog):
        TaskPropertiesDialog.setWindowTitle(_translate("TaskPropertiesDialog", "Task Properties", None))
        self.label.setText(_translate("TaskPropertiesDialog", "&Summary:", None))
        self.descriptionEdit.setToolTip(_translate("TaskPropertiesDialog", "Enter the task summary", None))
        self.textLabel1.setText(_translate("TaskPropertiesDialog", "&Description:", None))
        self.longtextEdit.setToolTip(_translate("TaskPropertiesDialog", "Enter the task description", None))
        self.textLabel2.setText(_translate("TaskPropertiesDialog", "Creation Time:", None))
        self.textLabel4.setText(_translate("TaskPropertiesDialog", "&Priority:", None))
        self.priorityCombo.setToolTip(_translate("TaskPropertiesDialog", "Select the task priority", None))
        self.priorityCombo.setItemText(0, _translate("TaskPropertiesDialog", "High", None))
        self.priorityCombo.setItemText(1, _translate("TaskPropertiesDialog", "Normal", None))
        self.priorityCombo.setItemText(2, _translate("TaskPropertiesDialog", "Low", None))
        self.projectCheckBox.setToolTip(_translate("TaskPropertiesDialog", "Select to indicate a task related to the current project", None))
        self.projectCheckBox.setText(_translate("TaskPropertiesDialog", "Project &Task", None))
        self.completedCheckBox.setToolTip(_translate("TaskPropertiesDialog", "Select to mark this task as completed", None))
        self.completedCheckBox.setText(_translate("TaskPropertiesDialog", "T&ask completed", None))
        self.textLabel5.setText(_translate("TaskPropertiesDialog", "Filename:", None))
        self.textLabel6.setText(_translate("TaskPropertiesDialog", "Line:", None))

