# -*- coding: utf-8 -*-

# Copyright (c) 2008 - 2014 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing the Multi Project configuration page.
"""

from PyQt4.QtCore import pyqtSignature
from PyQt4.QtGui import QFileDialog

from ConfigurationPageBase import ConfigurationPageBase
from Ui_MultiProjectPage import Ui_MultiProjectPage

from KdeQt import KQFileDialog

import Preferences
import Utilities

class MultiProjectPage(ConfigurationPageBase, Ui_MultiProjectPage):
    """
    Class implementing the Multi Project configuration page.
    """
    def __init__(self):
        """
        Constructor
        """
        ConfigurationPageBase.__init__(self)
        self.setupUi(self)
        self.setObjectName("MultiProjectPage")
        
        # set initial values
        self.openMasterAutomaticallyCheckBox.setChecked(\
            Preferences.getMultiProject("OpenMasterAutomatically"))
        self.multiProjectTimestampCheckBox.setChecked(\
            Preferences.getMultiProject("XMLTimestamp"))
        self.multiProjectRecentSpinBox.setValue(
            Preferences.getMultiProject("RecentNumber"))
        self.workspaceEdit.setText(
            Utilities.toNativeSeparators(
                Preferences.getMultiProject("Workspace") or Utilities.getHomeDir()))
        
    def save(self):
        """
        Public slot to save the Project configuration.
        """
        Preferences.setMultiProject("OpenMasterAutomatically",
            int(self.openMasterAutomaticallyCheckBox.isChecked()))
        Preferences.setMultiProject("XMLTimestamp",
            int(self.multiProjectTimestampCheckBox.isChecked()))
        Preferences.setMultiProject("RecentNumber", 
            self.multiProjectRecentSpinBox.value())
        Preferences.setMultiProject("Workspace",
            self.workspaceEdit.text())
        
    @pyqtSignature("")
    def on_workspaceButton_clicked(self):
        """
        Private slot to display a directory selection dialog.
        """
        default = self.workspaceEdit.text()
        if default.isEmpty():
            default = Utilities.getHomeDir()
        directory = KQFileDialog.getExistingDirectory(
            self,
            self.trUtf8("Select Workspace Directory"),
            default,
            QFileDialog.Options(0))
        
        if not directory.isEmpty():
            self.workspaceEdit.setText(Utilities.toNativeSeparators(directory))
    
def create(dlg):
    """
    Module function to create the configuration page.
    
    @param dlg reference to the configuration dialog
    """
    page = MultiProjectPage()
    return page
