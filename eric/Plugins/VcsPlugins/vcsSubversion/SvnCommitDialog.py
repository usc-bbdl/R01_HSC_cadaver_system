# -*- coding: utf-8 -*-

# Copyright (c) 2003 - 2014 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing a dialog to enter the commit message.
"""

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from Ui_SvnCommitDialog import Ui_SvnCommitDialog

import Preferences

class SvnCommitDialog(QWidget, Ui_SvnCommitDialog):
    """
    Class implementing a dialog to enter the commit message.
    
    @signal accepted() emitted, if the dialog was accepted
    @signal rejected() emitted, if the dialog was rejected
    """
    def __init__(self, vcs, parent = None):
        """
        Constructor
        
        @param vcs reference to the vcs object
        @param parent parent widget (QWidget)
        """
        QWidget.__init__(self, parent, Qt.WindowFlags(Qt.Window))
        self.setupUi(self)
        
        if vcs.versionStr < '1.5.0':
            self.changeListsGroup.hide()
        else:
            self.changeLists.addItems(sorted(vcs.svnGetChangelists()))
        
    def showEvent(self, evt):
        """
        Public method called when the dialog is about to be shown.
        
        @param evt the event (QShowEvent)
        """
        self.recentCommitMessages = \
            Preferences.Prefs.settings.value('Subversion/Commits').toStringList()
        self.recentComboBox.clear()
        self.recentComboBox.addItem("")
        self.recentComboBox.addItems(self.recentCommitMessages)
        
    def logMessage(self):
        """
        Public method to retrieve the log message.
        
        @return the log message (QString)
        """
        msg = self.logEdit.toPlainText()
        if not msg.isEmpty():
            self.recentCommitMessages.removeAll(msg)
            self.recentCommitMessages.prepend(msg)
            no = Preferences.Prefs.settings\
                .value('Subversion/CommitMessages', QVariant(20)).toInt()[0]
            del self.recentCommitMessages[no:]
            Preferences.Prefs.settings.setValue('Subversion/Commits', 
                QVariant(self.recentCommitMessages))
        return msg
        
    def hasChangelists(self):
        """
        Public method to check, if the user entered some changelists.
        
        @return flag indicating availability of changelists (boolean)
        """
        return len(self.changeLists.selectedItems()) > 0
        
    def changelistsData(self):
        """
        Public method to retrieve the changelists data.
        
        @return tuple containing the changelists (list of strings) and a flag
            indicating to keep changelists (boolean)
        """
        slists = [unicode(l.text()).strip() for l in self.changeLists.selectedItems()
                  if unicode(l.text()).strip() != ""]
        
        if len(slists) == 0:
            return [], False
        
        return slists, self.keepChangeListsCheckBox.isChecked()
        
    def on_buttonBox_clicked(self, button):
        """
        Private slot called by a button of the button box clicked.
        
        @param button button that was clicked (QAbstractButton)
        """
        if button == self.buttonBox.button(QDialogButtonBox.Cancel):
            self.logEdit.clear()
        
    def on_buttonBox_accepted(self):
        """
        Private slot called by the buttonBox accepted signal.
        """
        self.close()
        self.emit(SIGNAL("accepted()"))
        
    def on_buttonBox_rejected(self):
        """
        Private slot called by the buttonBox rejected signal.
        """
        self.close()
        self.emit(SIGNAL("rejected()"))
    
    @pyqtSignature("QString")
    def on_recentComboBox_activated(self, txt):
        """
        Private slot to select a commit message from recent ones.
        """
        if not txt.isEmpty():
            self.logEdit.setPlainText(txt)
