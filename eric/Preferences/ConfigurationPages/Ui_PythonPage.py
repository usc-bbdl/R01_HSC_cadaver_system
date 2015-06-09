# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Preferences\ConfigurationPages\PythonPage.ui'
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

class Ui_PythonPage(object):
    def setupUi(self, PythonPage):
        PythonPage.setObjectName(_fromUtf8("PythonPage"))
        PythonPage.resize(482, 473)
        self.verticalLayout = QtGui.QVBoxLayout(PythonPage)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.headerLabel = QtGui.QLabel(PythonPage)
        self.headerLabel.setObjectName(_fromUtf8("headerLabel"))
        self.verticalLayout.addWidget(self.headerLabel)
        self.line11_2_2_2_2 = QtGui.QFrame(PythonPage)
        self.line11_2_2_2_2.setFrameShape(QtGui.QFrame.HLine)
        self.line11_2_2_2_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line11_2_2_2_2.setFrameShape(QtGui.QFrame.HLine)
        self.line11_2_2_2_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line11_2_2_2_2.setObjectName(_fromUtf8("line11_2_2_2_2"))
        self.verticalLayout.addWidget(self.line11_2_2_2_2)
        self.groupBox = QtGui.QGroupBox(PythonPage)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.stringEncodingComboBox = QtGui.QComboBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stringEncodingComboBox.sizePolicy().hasHeightForWidth())
        self.stringEncodingComboBox.setSizePolicy(sizePolicy)
        self.stringEncodingComboBox.setObjectName(_fromUtf8("stringEncodingComboBox"))
        self.gridLayout.addWidget(self.stringEncodingComboBox, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.ioEncodingComboBox = QtGui.QComboBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ioEncodingComboBox.sizePolicy().hasHeightForWidth())
        self.ioEncodingComboBox.setSizePolicy(sizePolicy)
        self.ioEncodingComboBox.setObjectName(_fromUtf8("ioEncodingComboBox"))
        self.gridLayout.addWidget(self.ioEncodingComboBox, 1, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_3 = QtGui.QGroupBox(PythonPage)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_3 = QtGui.QLabel(self.groupBox_3)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 2)
        self.label_4 = QtGui.QLabel(self.groupBox_3)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)
        self.py2ExtensionsEdit = QtGui.QLineEdit(self.groupBox_3)
        self.py2ExtensionsEdit.setObjectName(_fromUtf8("py2ExtensionsEdit"))
        self.gridLayout_2.addWidget(self.py2ExtensionsEdit, 1, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.groupBox_3)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 2, 0, 1, 1)
        self.py3ExtensionsEdit = QtGui.QLineEdit(self.groupBox_3)
        self.py3ExtensionsEdit.setObjectName(_fromUtf8("py3ExtensionsEdit"))
        self.gridLayout_2.addWidget(self.py3ExtensionsEdit, 2, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_3)
        spacerItem = QtGui.QSpacerItem(464, 41, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(PythonPage)
        QtCore.QMetaObject.connectSlotsByName(PythonPage)

    def retranslateUi(self, PythonPage):
        self.headerLabel.setText(_translate("PythonPage", "<b>Configure Python</b>", None))
        self.groupBox.setTitle(_translate("PythonPage", "Encoding", None))
        self.label.setText(_translate("PythonPage", "String Encoding:", None))
        self.stringEncodingComboBox.setToolTip(_translate("PythonPage", "Select the string encoding to be used.", None))
        self.label_2.setText(_translate("PythonPage", "I/O Encoding:", None))
        self.ioEncodingComboBox.setToolTip(_translate("PythonPage", "Select the string encoding used by commandline tools.", None))
        self.groupBox_3.setTitle(_translate("PythonPage", "Source association", None))
        self.label_3.setText(_translate("PythonPage", "Enter the file extensions to be associated with the Python versions separated by a space. They must not overlap with each other.", None))
        self.label_4.setText(_translate("PythonPage", "Python 2:", None))
        self.label_5.setText(_translate("PythonPage", "Python 3:", None))

