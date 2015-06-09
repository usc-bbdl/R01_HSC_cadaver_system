# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Preferences\ConfigurationPages\TasksPage.ui'
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

class Ui_TasksPage(object):
    def setupUi(self, TasksPage):
        TasksPage.setObjectName(_fromUtf8("TasksPage"))
        TasksPage.resize(586, 433)
        self.verticalLayout = QtGui.QVBoxLayout(TasksPage)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.headerLabel = QtGui.QLabel(TasksPage)
        self.headerLabel.setObjectName(_fromUtf8("headerLabel"))
        self.verticalLayout.addWidget(self.headerLabel)
        self.line11_2_2_2 = QtGui.QFrame(TasksPage)
        self.line11_2_2_2.setFrameShape(QtGui.QFrame.HLine)
        self.line11_2_2_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line11_2_2_2.setFrameShape(QtGui.QFrame.HLine)
        self.line11_2_2_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line11_2_2_2.setObjectName(_fromUtf8("line11_2_2_2"))
        self.verticalLayout.addWidget(self.line11_2_2_2)
        self.groupBox = QtGui.QGroupBox(TasksPage)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridlayout = QtGui.QGridLayout(self.groupBox)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.tasksMarkerEdit = QtGui.QLineEdit(self.groupBox)
        self.tasksMarkerEdit.setObjectName(_fromUtf8("tasksMarkerEdit"))
        self.gridlayout.addWidget(self.tasksMarkerEdit, 0, 1, 1, 1)
        self.textLabel4_3 = QtGui.QLabel(self.groupBox)
        self.textLabel4_3.setObjectName(_fromUtf8("textLabel4_3"))
        self.gridlayout.addWidget(self.textLabel4_3, 0, 0, 1, 1)
        self.tasksMarkerBugfixEdit = QtGui.QLineEdit(self.groupBox)
        self.tasksMarkerBugfixEdit.setText(_fromUtf8(""))
        self.tasksMarkerBugfixEdit.setObjectName(_fromUtf8("tasksMarkerBugfixEdit"))
        self.gridlayout.addWidget(self.tasksMarkerBugfixEdit, 1, 1, 1, 1)
        self.textLabel5_3 = QtGui.QLabel(self.groupBox)
        self.textLabel5_3.setObjectName(_fromUtf8("textLabel5_3"))
        self.gridlayout.addWidget(self.textLabel5_3, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(TasksPage)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridlayout1 = QtGui.QGridLayout(self.groupBox_2)
        self.gridlayout1.setObjectName(_fromUtf8("gridlayout1"))
        self.tasksProjectBgColourButton = QtGui.QPushButton(self.groupBox_2)
        self.tasksProjectBgColourButton.setMinimumSize(QtCore.QSize(100, 0))
        self.tasksProjectBgColourButton.setText(_fromUtf8(""))
        self.tasksProjectBgColourButton.setObjectName(_fromUtf8("tasksProjectBgColourButton"))
        self.gridlayout1.addWidget(self.tasksProjectBgColourButton, 3, 1, 1, 1)
        self.tasksBgColourButton = QtGui.QPushButton(self.groupBox_2)
        self.tasksBgColourButton.setMinimumSize(QtCore.QSize(100, 0))
        self.tasksBgColourButton.setText(_fromUtf8(""))
        self.tasksBgColourButton.setObjectName(_fromUtf8("tasksBgColourButton"))
        self.gridlayout1.addWidget(self.tasksBgColourButton, 2, 1, 1, 1)
        self.tasksBugfixColourButton = QtGui.QPushButton(self.groupBox_2)
        self.tasksBugfixColourButton.setMinimumSize(QtCore.QSize(100, 0))
        self.tasksBugfixColourButton.setText(_fromUtf8(""))
        self.tasksBugfixColourButton.setObjectName(_fromUtf8("tasksBugfixColourButton"))
        self.gridlayout1.addWidget(self.tasksBugfixColourButton, 1, 1, 1, 1)
        self.tasksColourButton = QtGui.QPushButton(self.groupBox_2)
        self.tasksColourButton.setMinimumSize(QtCore.QSize(100, 0))
        self.tasksColourButton.setText(_fromUtf8(""))
        self.tasksColourButton.setObjectName(_fromUtf8("tasksColourButton"))
        self.gridlayout1.addWidget(self.tasksColourButton, 0, 1, 1, 1)
        self.textLabel2_8 = QtGui.QLabel(self.groupBox_2)
        self.textLabel2_8.setObjectName(_fromUtf8("textLabel2_8"))
        self.gridlayout1.addWidget(self.textLabel2_8, 1, 0, 1, 1)
        self.textLabel6_3 = QtGui.QLabel(self.groupBox_2)
        self.textLabel6_3.setObjectName(_fromUtf8("textLabel6_3"))
        self.gridlayout1.addWidget(self.textLabel6_3, 2, 0, 1, 1)
        self.textLabel3_4 = QtGui.QLabel(self.groupBox_2)
        self.textLabel3_4.setObjectName(_fromUtf8("textLabel3_4"))
        self.gridlayout1.addWidget(self.textLabel3_4, 3, 0, 1, 1)
        self.textLabel1_3 = QtGui.QLabel(self.groupBox_2)
        self.textLabel1_3.setObjectName(_fromUtf8("textLabel1_3"))
        self.gridlayout1.addWidget(self.textLabel1_3, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridlayout1.addItem(spacerItem, 1, 2, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox_3 = QtGui.QGroupBox(TasksPage)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.clearCheckBox = QtGui.QCheckBox(self.groupBox_3)
        self.clearCheckBox.setObjectName(_fromUtf8("clearCheckBox"))
        self.horizontalLayout.addWidget(self.clearCheckBox)
        self.verticalLayout.addWidget(self.groupBox_3)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)

        self.retranslateUi(TasksPage)
        QtCore.QMetaObject.connectSlotsByName(TasksPage)
        TasksPage.setTabOrder(self.tasksMarkerEdit, self.tasksMarkerBugfixEdit)
        TasksPage.setTabOrder(self.tasksMarkerBugfixEdit, self.tasksColourButton)
        TasksPage.setTabOrder(self.tasksColourButton, self.tasksBugfixColourButton)
        TasksPage.setTabOrder(self.tasksBugfixColourButton, self.tasksBgColourButton)
        TasksPage.setTabOrder(self.tasksBgColourButton, self.tasksProjectBgColourButton)

    def retranslateUi(self, TasksPage):
        self.headerLabel.setText(_translate("TasksPage", "<b>Configure Tasks</b>", None))
        self.groupBox.setTitle(_translate("TasksPage", "Tasks Markers", None))
        self.tasksMarkerEdit.setToolTip(_translate("TasksPage", "Enter the tasks markers separated by a space character.", None))
        self.textLabel4_3.setText(_translate("TasksPage", "Standard tasks:", None))
        self.tasksMarkerBugfixEdit.setToolTip(_translate("TasksPage", "Enter the tasks markers separated by a space character.", None))
        self.textLabel5_3.setText(_translate("TasksPage", "Bugfix tasks:", None))
        self.groupBox_2.setTitle(_translate("TasksPage", "Tasks Colours", None))
        self.tasksProjectBgColourButton.setToolTip(_translate("TasksPage", "Select the background colour for project tasks.", None))
        self.tasksBgColourButton.setToolTip(_translate("TasksPage", "Select the background colour for global tasks.", None))
        self.tasksBugfixColourButton.setToolTip(_translate("TasksPage", "Select the colour for bugfix tasks.", None))
        self.tasksColourButton.setToolTip(_translate("TasksPage", "Select the colour for standard tasks.", None))
        self.textLabel2_8.setText(_translate("TasksPage", "Bugfix tasks foreground colour:", None))
        self.textLabel6_3.setText(_translate("TasksPage", "Global tasks background colour:", None))
        self.textLabel3_4.setText(_translate("TasksPage", "Project tasks background colour:", None))
        self.textLabel1_3.setText(_translate("TasksPage", "Standard tasks foreground colour:", None))
        self.groupBox_3.setTitle(_translate("TasksPage", "Tasks Handling", None))
        self.clearCheckBox.setToolTip(_translate("TasksPage", "Select to clear global file tasks when the file is closed", None))
        self.clearCheckBox.setText(_translate("TasksPage", "Clear global file task when file is closed", None))

