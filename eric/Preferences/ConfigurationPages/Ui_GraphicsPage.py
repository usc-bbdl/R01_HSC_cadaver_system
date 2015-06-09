# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Preferences\ConfigurationPages\GraphicsPage.ui'
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

class Ui_GraphicsPage(object):
    def setupUi(self, GraphicsPage):
        GraphicsPage.setObjectName(_fromUtf8("GraphicsPage"))
        GraphicsPage.resize(440, 334)
        self.vboxlayout = QtGui.QVBoxLayout(GraphicsPage)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.headerLabel = QtGui.QLabel(GraphicsPage)
        self.headerLabel.setObjectName(_fromUtf8("headerLabel"))
        self.vboxlayout.addWidget(self.headerLabel)
        self.line7 = QtGui.QFrame(GraphicsPage)
        self.line7.setFrameShape(QtGui.QFrame.HLine)
        self.line7.setFrameShadow(QtGui.QFrame.Sunken)
        self.line7.setFrameShape(QtGui.QFrame.HLine)
        self.line7.setFrameShadow(QtGui.QFrame.Sunken)
        self.line7.setObjectName(_fromUtf8("line7"))
        self.vboxlayout.addWidget(self.line7)
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        self.graphicsFontButton = QtGui.QPushButton(GraphicsPage)
        self.graphicsFontButton.setObjectName(_fromUtf8("graphicsFontButton"))
        self.hboxlayout.addWidget(self.graphicsFontButton)
        self.graphicsFontSample = QtGui.QLineEdit(GraphicsPage)
        self.graphicsFontSample.setFocusPolicy(QtCore.Qt.NoFocus)
        self.graphicsFontSample.setAlignment(QtCore.Qt.AlignHCenter)
        self.graphicsFontSample.setReadOnly(True)
        self.graphicsFontSample.setObjectName(_fromUtf8("graphicsFontSample"))
        self.hboxlayout.addWidget(self.graphicsFontSample)
        self.vboxlayout.addLayout(self.hboxlayout)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vboxlayout.addItem(spacerItem)

        self.retranslateUi(GraphicsPage)
        QtCore.QMetaObject.connectSlotsByName(GraphicsPage)

    def retranslateUi(self, GraphicsPage):
        self.headerLabel.setText(_translate("GraphicsPage", "<b>Configure graphics settings</b>", None))
        self.graphicsFontButton.setToolTip(_translate("GraphicsPage", "Press to select the font for the graphic items", None))
        self.graphicsFontButton.setText(_translate("GraphicsPage", "Graphics Font", None))
        self.graphicsFontSample.setText(_translate("GraphicsPage", "Graphics Font", None))

