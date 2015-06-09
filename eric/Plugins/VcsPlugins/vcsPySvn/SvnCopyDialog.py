# -*- coding: utf-8 -*-

# Copyright (c) 2003 - 2014 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing a dialog to enter the data for a copy operation.
"""

import os.path

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from KdeQt import KQFileDialog

from E4Gui.E4Completers import E4FileCompleter, E4DirCompleter

from Ui_SvnCopyDialog import Ui_SvnCopyDialog

import Utilities

class SvnCopyDialog(QDialog, Ui_SvnCopyDialog):
    """
    Class implementing a dialog to enter the data for a copy or rename operation.
    """
    def __init__(self, source, parent = None, move = False, force = False):
        """
        Constructor
        
        @param source name of the source file/directory (QString)
        @param parent parent widget (QWidget)
        @param move flag indicating a move operation (boolean)
        @param force flag indicating a forced operation (boolean)
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)
        
        self.source = source
        if os.path.isdir(self.source):
            self.targetCompleter = E4DirCompleter(self.targetEdit)
        else:
            self.targetCompleter = E4FileCompleter(self.targetEdit)
        
        if move:
            self.setWindowTitle(self.trUtf8('Subversion Move'))
        else:
            self.forceCheckBox.setEnabled(False)
        self.forceCheckBox.setChecked(force)
        
        self.sourceEdit.setText(source)
        
        self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)
        
    def getData(self):
        """
        Public method to retrieve the copy data.
        
        @return the target name (QString) and a flag indicating
            the operation should be enforced (boolean)
        """
        target = unicode(self.targetEdit.text())
        if not os.path.isabs(target):
            sourceDir = os.path.dirname(unicode(self.sourceEdit.text()))
            target = os.path.join(sourceDir, target)
        return (QString(Utilities.toNativeSeparators(target)),
                self.forceCheckBox.isChecked())
        
    @pyqtSignature("")
    def on_dirButton_clicked(self):
        """
        Private slot to handle the button press for selecting the target via a 
        selection dialog.
        """
        if os.path.isdir(self.source):
            target = KQFileDialog.getExistingDirectory(\
                None,
                self.trUtf8("Select target"),
                self.targetEdit.text(),
                QFileDialog.Options(QFileDialog.ShowDirsOnly))
        else:
            target = KQFileDialog.getSaveFileName(\
                None,
                self.trUtf8("Select target"),
                self.targetEdit.text(),
                QString(),
                None,
                QFileDialog.Options(QFileDialog.DontConfirmOverwrite))
        
        if not target.isEmpty():
            self.targetEdit.setText(Utilities.toNativeSeparators(target))
    
    @pyqtSignature("QString")
    def on_targetEdit_textChanged(self, txt):
        """
        Private slot to handle changes of the target.
        
        @param txt contents of the target edit (QString)
        """
        txt = unicode(txt)
        self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(
            os.path.isabs(txt) or os.path.dirname(txt) == "")
