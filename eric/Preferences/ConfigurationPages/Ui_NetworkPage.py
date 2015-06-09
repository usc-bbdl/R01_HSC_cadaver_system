# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Preferences\ConfigurationPages\NetworkPage.ui'
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

class Ui_NetworkPage(object):
    def setupUi(self, NetworkPage):
        NetworkPage.setObjectName(_fromUtf8("NetworkPage"))
        NetworkPage.resize(589, 563)
        self.verticalLayout_2 = QtGui.QVBoxLayout(NetworkPage)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.headerLabel = QtGui.QLabel(NetworkPage)
        self.headerLabel.setObjectName(_fromUtf8("headerLabel"))
        self.verticalLayout_2.addWidget(self.headerLabel)
        self.line9_3 = QtGui.QFrame(NetworkPage)
        self.line9_3.setFrameShape(QtGui.QFrame.HLine)
        self.line9_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line9_3.setFrameShape(QtGui.QFrame.HLine)
        self.line9_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line9_3.setObjectName(_fromUtf8("line9_3"))
        self.verticalLayout_2.addWidget(self.line9_3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_6 = QtGui.QLabel(NetworkPage)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout.addWidget(self.label_6)
        self.downloadDirEdit = QtGui.QLineEdit(NetworkPage)
        self.downloadDirEdit.setObjectName(_fromUtf8("downloadDirEdit"))
        self.horizontalLayout.addWidget(self.downloadDirEdit)
        self.downloadDirButton = QtGui.QPushButton(NetworkPage)
        self.downloadDirButton.setObjectName(_fromUtf8("downloadDirButton"))
        self.horizontalLayout.addWidget(self.downloadDirButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.requestFilenameCheckBox = QtGui.QCheckBox(NetworkPage)
        self.requestFilenameCheckBox.setObjectName(_fromUtf8("requestFilenameCheckBox"))
        self.verticalLayout_2.addWidget(self.requestFilenameCheckBox)
        self.proxyGroup = QtGui.QGroupBox(NetworkPage)
        self.proxyGroup.setCheckable(True)
        self.proxyGroup.setChecked(True)
        self.proxyGroup.setObjectName(_fromUtf8("proxyGroup"))
        self.verticalLayout = QtGui.QVBoxLayout(self.proxyGroup)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.systemProxyButton = QtGui.QRadioButton(self.proxyGroup)
        self.systemProxyButton.setChecked(True)
        self.systemProxyButton.setObjectName(_fromUtf8("systemProxyButton"))
        self.verticalLayout.addWidget(self.systemProxyButton)
        self.manualProxyButton = QtGui.QRadioButton(self.proxyGroup)
        self.manualProxyButton.setObjectName(_fromUtf8("manualProxyButton"))
        self.verticalLayout.addWidget(self.manualProxyButton)
        self.groupBox = QtGui.QGroupBox(self.proxyGroup)
        self.groupBox.setEnabled(False)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)
        self.proxyTypeCombo = QtGui.QComboBox(self.groupBox)
        self.proxyTypeCombo.setObjectName(_fromUtf8("proxyTypeCombo"))
        self.gridLayout.addWidget(self.proxyTypeCombo, 0, 1, 1, 2)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.proxyHostEdit = QtGui.QLineEdit(self.groupBox)
        self.proxyHostEdit.setObjectName(_fromUtf8("proxyHostEdit"))
        self.gridLayout.addWidget(self.proxyHostEdit, 1, 1, 1, 2)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.proxyPortSpin = QtGui.QSpinBox(self.groupBox)
        self.proxyPortSpin.setAlignment(QtCore.Qt.AlignRight)
        self.proxyPortSpin.setMinimum(1)
        self.proxyPortSpin.setMaximum(65535)
        self.proxyPortSpin.setProperty("value", 80)
        self.proxyPortSpin.setObjectName(_fromUtf8("proxyPortSpin"))
        self.gridLayout.addWidget(self.proxyPortSpin, 2, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 2, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.proxyUserEdit = QtGui.QLineEdit(self.groupBox)
        self.proxyUserEdit.setObjectName(_fromUtf8("proxyUserEdit"))
        self.gridLayout.addWidget(self.proxyUserEdit, 3, 1, 1, 2)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.proxyPasswordEdit = QtGui.QLineEdit(self.groupBox)
        self.proxyPasswordEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.proxyPasswordEdit.setObjectName(_fromUtf8("proxyPasswordEdit"))
        self.gridLayout.addWidget(self.proxyPasswordEdit, 4, 1, 1, 2)
        self.verticalLayout.addWidget(self.groupBox)
        self.verticalLayout_2.addWidget(self.proxyGroup)
        spacerItem1 = QtGui.QSpacerItem(571, 21, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)

        self.retranslateUi(NetworkPage)
        QtCore.QObject.connect(self.manualProxyButton, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.groupBox.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(NetworkPage)
        NetworkPage.setTabOrder(self.downloadDirEdit, self.downloadDirButton)
        NetworkPage.setTabOrder(self.downloadDirButton, self.requestFilenameCheckBox)

    def retranslateUi(self, NetworkPage):
        self.headerLabel.setText(_translate("NetworkPage", "<b>Configure Network</b>", None))
        self.label_6.setText(_translate("NetworkPage", "Download directory:", None))
        self.downloadDirEdit.setToolTip(_translate("NetworkPage", "Enter the download directory (leave empty to use the default location)", None))
        self.downloadDirButton.setToolTip(_translate("NetworkPage", "Select the download directory via a directory selection dialog", None))
        self.downloadDirButton.setText(_translate("NetworkPage", "...", None))
        self.requestFilenameCheckBox.setToolTip(_translate("NetworkPage", "Select to ask the user for a download filename", None))
        self.requestFilenameCheckBox.setText(_translate("NetworkPage", "Request name of downloaded file", None))
        self.proxyGroup.setToolTip(_translate("NetworkPage", "Select to use a web proxy", None))
        self.proxyGroup.setTitle(_translate("NetworkPage", "Use network proxy", None))
        self.systemProxyButton.setToolTip(_translate("NetworkPage", "Select to use the system proxy configuration", None))
        self.systemProxyButton.setText(_translate("NetworkPage", "Use system proxy configuration", None))
        self.manualProxyButton.setToolTip(_translate("NetworkPage", "Select to use an application specific proxy configuration", None))
        self.manualProxyButton.setText(_translate("NetworkPage", "Manual proxy configuration:", None))
        self.groupBox.setTitle(_translate("NetworkPage", "Manual proxy settings", None))
        self.label_5.setText(_translate("NetworkPage", "Proxy-Type:", None))
        self.proxyTypeCombo.setToolTip(_translate("NetworkPage", "Select the type of the proxy", None))
        self.label.setText(_translate("NetworkPage", "Proxy-Host:", None))
        self.proxyHostEdit.setToolTip(_translate("NetworkPage", "Enter the name of the proxy host", None))
        self.label_2.setText(_translate("NetworkPage", "Proxy-Port:", None))
        self.proxyPortSpin.setToolTip(_translate("NetworkPage", "Enter the proxy port", None))
        self.label_3.setText(_translate("NetworkPage", "Username:", None))
        self.proxyUserEdit.setToolTip(_translate("NetworkPage", "Enter the username for the proxy", None))
        self.label_4.setText(_translate("NetworkPage", "Password:", None))
        self.proxyPasswordEdit.setToolTip(_translate("NetworkPage", "Enter the password for the proxy", None))

