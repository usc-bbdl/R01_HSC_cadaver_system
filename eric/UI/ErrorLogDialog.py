# -*- coding: utf-8 -*-

# Copyright (c) 2012 - 2014 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing a dialog to display an error log.
"""

import os

from PyQt4.QtCore import pyqtSignature
from PyQt4.QtGui import QDialog, QStyle

from .Ui_ErrorLogDialog import Ui_ErrorLogDialog


class ErrorLogDialog(QDialog, Ui_ErrorLogDialog):
    """
    Class implementing a dialog to display an error log.
    """
    def __init__(self, logFile, parent=None):
        """
        Constructor
        
        @param logFile name of the log file containing the error info (string)
        @param parent reference to the parent widget (QWidget)
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)
        
        pixmap = self.style().standardIcon(QStyle.SP_MessageBoxQuestion).pixmap(32, 32)
        self.icon.setPixmap(pixmap)
        
        self.__ui = parent
        self.__logFile = logFile
        
        try:
            f = open(logFile, "r")
            txt = f.read()
            f.close()
            self.logEdit.setPlainText(txt)
        except IOError:
            pass
    
    @pyqtSignature("")
    def on_emailButton_clicked(self):
        """
        Private slot to send an email.
        """
        self.__ui.showEmailDialog("bug",
            attachFile=self.__logFile, deleteAttachFile=True)
        self.accept()
    
    @pyqtSignature("")
    def on_deleteButton_clicked(self):
        """
        Private slot to delete the log file.
        """
        if os.path.exists(self.__logFile):
            os.remove(self.__logFile)
        self.accept()
    
    @pyqtSignature("")
    def on_keepButton_clicked(self):
        """
        Private slot to just do nothing.
        """
        self.accept()
