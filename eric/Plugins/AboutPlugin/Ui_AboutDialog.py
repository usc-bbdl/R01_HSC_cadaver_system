# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric\Plugins\AboutPlugin\AboutDialog.ui'
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

class Ui_AboutDialog(object):
    def setupUi(self, AboutDialog):
        AboutDialog.setObjectName(_fromUtf8("AboutDialog"))
        AboutDialog.resize(580, 450)
        self.vboxlayout = QtGui.QVBoxLayout(AboutDialog)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        self.ericPixmap = QtGui.QLabel(AboutDialog)
        self.ericPixmap.setScaledContents(False)
        self.ericPixmap.setObjectName(_fromUtf8("ericPixmap"))
        self.hboxlayout.addWidget(self.ericPixmap)
        self.ericLabel = QtGui.QLabel(AboutDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ericLabel.sizePolicy().hasHeightForWidth())
        self.ericLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.ericLabel.setFont(font)
        self.ericLabel.setObjectName(_fromUtf8("ericLabel"))
        self.hboxlayout.addWidget(self.ericLabel)
        self.vboxlayout.addLayout(self.hboxlayout)
        self.aboutTabWidget = QtGui.QTabWidget(AboutDialog)
        self.aboutTabWidget.setObjectName(_fromUtf8("aboutTabWidget"))
        self.about = QtGui.QWidget()
        self.about.setObjectName(_fromUtf8("about"))
        self.vboxlayout1 = QtGui.QVBoxLayout(self.about)
        self.vboxlayout1.setObjectName(_fromUtf8("vboxlayout1"))
        self.aboutEdit = QtGui.QTextBrowser(self.about)
        self.aboutEdit.setFrameShape(QtGui.QFrame.NoFrame)
        self.aboutEdit.setOpenExternalLinks(True)
        self.aboutEdit.setObjectName(_fromUtf8("aboutEdit"))
        self.vboxlayout1.addWidget(self.aboutEdit)
        self.aboutTabWidget.addTab(self.about, _fromUtf8(""))
        self.authors = QtGui.QWidget()
        self.authors.setObjectName(_fromUtf8("authors"))
        self.vboxlayout2 = QtGui.QVBoxLayout(self.authors)
        self.vboxlayout2.setObjectName(_fromUtf8("vboxlayout2"))
        self.authorsEdit = QtGui.QTextEdit(self.authors)
        self.authorsEdit.setFrameShape(QtGui.QFrame.NoFrame)
        self.authorsEdit.setReadOnly(True)
        self.authorsEdit.setObjectName(_fromUtf8("authorsEdit"))
        self.vboxlayout2.addWidget(self.authorsEdit)
        self.aboutTabWidget.addTab(self.authors, _fromUtf8(""))
        self.thanks = QtGui.QWidget()
        self.thanks.setObjectName(_fromUtf8("thanks"))
        self.vboxlayout3 = QtGui.QVBoxLayout(self.thanks)
        self.vboxlayout3.setObjectName(_fromUtf8("vboxlayout3"))
        self.thanksEdit = QtGui.QTextEdit(self.thanks)
        self.thanksEdit.setFrameShape(QtGui.QFrame.NoFrame)
        self.thanksEdit.setReadOnly(True)
        self.thanksEdit.setObjectName(_fromUtf8("thanksEdit"))
        self.vboxlayout3.addWidget(self.thanksEdit)
        self.aboutTabWidget.addTab(self.thanks, _fromUtf8(""))
        self.license = QtGui.QWidget()
        self.license.setObjectName(_fromUtf8("license"))
        self.vboxlayout4 = QtGui.QVBoxLayout(self.license)
        self.vboxlayout4.setObjectName(_fromUtf8("vboxlayout4"))
        self.licenseEdit = QtGui.QTextEdit(self.license)
        self.licenseEdit.setFrameShape(QtGui.QFrame.NoFrame)
        self.licenseEdit.setLineWrapMode(QtGui.QTextEdit.FixedColumnWidth)
        self.licenseEdit.setLineWrapColumnOrWidth(80)
        self.licenseEdit.setReadOnly(True)
        self.licenseEdit.setAcceptRichText(False)
        self.licenseEdit.setObjectName(_fromUtf8("licenseEdit"))
        self.vboxlayout4.addWidget(self.licenseEdit)
        self.aboutTabWidget.addTab(self.license, _fromUtf8(""))
        self.vboxlayout.addWidget(self.aboutTabWidget)
        self.buttonBox = QtGui.QDialogButtonBox(AboutDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(AboutDialog)
        self.aboutTabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), AboutDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), AboutDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(AboutDialog)
        AboutDialog.setTabOrder(self.aboutTabWidget, self.aboutEdit)
        AboutDialog.setTabOrder(self.aboutEdit, self.authorsEdit)
        AboutDialog.setTabOrder(self.authorsEdit, self.thanksEdit)
        AboutDialog.setTabOrder(self.thanksEdit, self.licenseEdit)

    def retranslateUi(self, AboutDialog):
        AboutDialog.setWindowTitle(_translate("AboutDialog", "About Eric", None))
        self.aboutTabWidget.setTabText(self.aboutTabWidget.indexOf(self.about), _translate("AboutDialog", "&About", None))
        self.aboutTabWidget.setTabText(self.aboutTabWidget.indexOf(self.authors), _translate("AboutDialog", "A&uthors", None))
        self.aboutTabWidget.setTabText(self.aboutTabWidget.indexOf(self.thanks), _translate("AboutDialog", "&Thanks To", None))
        self.aboutTabWidget.setTabText(self.aboutTabWidget.indexOf(self.license), _translate("AboutDialog", "&License Agreement", None))

