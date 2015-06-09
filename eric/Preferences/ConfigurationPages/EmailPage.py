# -*- coding: utf-8 -*-

# Copyright (c) 2006 - 2014 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing the Email configuration page.
"""

import smtplib
import socket

from PyQt4.QtCore import pyqtSignature,  Qt
from PyQt4.QtGui import QApplication, QCursor

from KdeQt import KQMessageBox

from ConfigurationPageBase import ConfigurationPageBase
from Ui_EmailPage import Ui_EmailPage

import Preferences

class EmailPage(ConfigurationPageBase, Ui_EmailPage):
    """
    Class implementing the Email configuration page.
    """
    def __init__(self):
        """
        Constructor
        """
        ConfigurationPageBase.__init__(self)
        self.setupUi(self)
        self.setObjectName("EmailPage")
        
        # set initial values
        self.mailServerEdit.setText(Preferences.getUser("MailServer"))
        self.portSpin.setValue(Preferences.getUser("MailServerPort"))
        self.emailEdit.setText(Preferences.getUser("Email"))
        self.signatureEdit.setPlainText(Preferences.getUser("Signature"))
        self.mailAuthenticationCheckBox.setChecked(\
            Preferences.getUser("MailServerAuthentication"))
        self.mailUserEdit.setText(Preferences.getUser("MailServerUser"))
        self.mailPasswordEdit.setText(\
            Preferences.getUser("MailServerPassword"))
        self.useTlsCheckBox.setChecked(\
            Preferences.getUser("MailServerUseTLS"))
        
    def save(self):
        """
        Public slot to save the Email configuration.
        """
        Preferences.setUser("MailServer",
            self.mailServerEdit.text())
        Preferences.setUser("MailServerPort", 
            self.portSpin.value())
        Preferences.setUser("Email",
            self.emailEdit.text())
        Preferences.setUser("Signature",
            self.signatureEdit.toPlainText())
        Preferences.setUser("MailServerAuthentication",
            int(self.mailAuthenticationCheckBox.isChecked()))
        Preferences.setUser("MailServerUser",
            self.mailUserEdit.text())
        Preferences.setUser("MailServerPassword",
            self.mailPasswordEdit.text())
        Preferences.setUser("MailServerUseTLS",
            int(self.useTlsCheckBox.isChecked()))
    
    def __updateTestButton(self):
        """
        Private slot to update the enabled state of the test button.
        """
        self.testButton.setEnabled(
            self.mailAuthenticationCheckBox.isChecked() and \
            not self.mailUserEdit.text().isEmpty() and \
            not self.mailPasswordEdit.text().isEmpty() and \
            not self.mailServerEdit.text().isEmpty()
        )
    
    @pyqtSignature("bool")
    def on_mailAuthenticationCheckBox_toggled(self, checked):
        """
        Private slot to handle a change of the state of the authentication
        selector.
        
        @param checked state of the checkbox (boolean)
        """
        self.__updateTestButton()
    
    @pyqtSignature("QString")
    def on_mailUserEdit_textChanged(self, txt):
        """
        Private slot to handle a change of the text of the user edit.
        
        @param txt current text of the edit (QString)
        """
        self.__updateTestButton()
    
    @pyqtSignature("QString")
    def on_mailPasswordEdit_textChanged(self, txt):
        """
        Private slot to handle a change of the text of the user edit.
        
        @param txt current text of the edit (QString)
        """
        self.__updateTestButton()
    
    @pyqtSignature("")
    def on_testButton_clicked(self):
        """
        Private slot to test the mail server login data.
        """
        QApplication.setOverrideCursor(QCursor(Qt.WaitCursor))
        QApplication.processEvents()
        try:
            server = smtplib.SMTP(str(self.mailServerEdit.text()),
                                  self.portSpin.value(), timeout=10)
            if self.useTlsCheckBox.isChecked():
                server.starttls()
            try:
                server.login(unicode(self.mailUserEdit.text()),
                             unicode(self.mailPasswordEdit.text()))
                QApplication.restoreOverrideCursor()
                KQMessageBox.information(self,
                    self.trUtf8("Login Test"),
                    self.trUtf8("""The login test succeeded."""))
            except (smtplib.SMTPException, socket.error) as e:
                QApplication.restoreOverrideCursor()
                if isinstance(e,  smtplib.SMTPResponseException):
                    errorStr = e.smtp_error.decode()
                elif isinstance(e, socket.timeout):
                    errorStr = str(e)
                elif isinstance(e, socket.error):
                    errorStr = e[1]
                else:
                    errorStr = str(e)
                KQMessageBox.critical(self,
                    self.trUtf8("Login Test"),
                    self.trUtf8("""<p>The login test failed.<br>Reason: %1</p>""")
                        .arg(errorStr))
            server.quit()
        except (smtplib.SMTPException, socket.error) as e:
            QApplication.restoreOverrideCursor()
            if isinstance(e,  smtplib.SMTPResponseException):
                errorStr = e.smtp_error.decode()
            elif isinstance(e, socket.timeout):
                errorStr = str(e)
            elif isinstance(e, socket.error):
                errorStr = e[1]
            else:
                errorStr = str(e)
            KQMessageBox.critical(self,
                self.trUtf8("Login Test"),
                self.trUtf8("""<p>The login test failed.<br>Reason: %1</p>""")
                    .arg(errorStr))
    
def create(dlg):
    """
    Module function to create the configuration page.
    
    @param dlg reference to the configuration dialog
    """
    page = EmailPage()
    return page
