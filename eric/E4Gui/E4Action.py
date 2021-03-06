# -*- coding: utf-8 -*-

# Copyright (c) 2006 - 2014 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing an Action class extending QAction.

This extension is necessary in order to support alternate keyboard
shortcuts.
"""

from PyQt4.QtGui import QAction, QActionGroup, QIcon, QKeySequence, qApp
from PyQt4.QtCore import QObject, QString

class ArgumentsError(RuntimeError):
    """
    Class implementing an exception, which is raised, if the wrong number of arguments
    are given.
    """
    def __init__(self, error):
        """
        Constructor
        """
        self.errorMessage = unicode(error)
        
    def __repr__(self):
        """
        Private method returning a representation of the exception.
        
        @return string representing the error message
        """
        return unicode(self.errorMessage)
        
    def __str__(self):
        """
        Private method returning a string representation of the exception.
        
        @return string representing the error message
        """
        return str(self.errorMessage)

class E4Action(QAction):
    """
    Class implementing an Action class extending QAction.
    """
    def __init__(self, *args):
        """
        Constructor
        
        @param args argument list of the constructor. This list is one of
            <ul>
            <li>text (string or QString), icon (QIcon), menu text (string or QString), 
                accelarator (QKeySequence), alternative accelerator (QKeySequence), 
                parent (QObject), name (string or QString), toggle (boolean)</li>
            <li>text (string or QString), icon (QIcon), menu text (string or QString), 
                accelarator (QKeySequence), alternative accelerator (QKeySequence), 
                parent (QObject), name (string or QString)</li>
            <li>text (string or QString), menu text (string or QString), 
                accelarator (QKeySequence), alternative accelerator (QKeySequence), 
                parent (QObject), name (string or QString), toggle (boolean)</li>
            <li>text (string or QString), menu text (string or QString), 
                accelarator (QKeySequence), alternative accelerator (QKeySequence), 
                parent (QObject), name (string or QString)</li>
            </ul>
        """
        if isinstance(args[1], QIcon):
            icon = args[1]
            incr = 1
        else:
            icon = None
            incr = 0
        if len(args) < 6+incr:
            raise ArgumentsError("Not enough arguments, %d expected, got %d" % \
                                 (6+incr, len(args)))
        elif len(args) > 7+incr:
            raise ArgumentsError("Too many arguments, max. %d expected, got %d" % \
                                 (7+incr, len(args)))
            
        parent = args[4+incr]
        QAction.__init__(self, parent)
        name = args[5+incr]
        if name:
            self.setObjectName(name)
        
        if args[1+incr]:
            self.setText(args[1+incr])
        
        if args[0]:
            self.setIconText(args[0])
        if args[2+incr]:
            self.setShortcut(QKeySequence(args[2+incr]))
        
        if args[3+incr]:
            self.setAlternateShortcut(QKeySequence(args[3+incr]))
        
        if icon:
            self.setIcon(icon)
        
        if len(args) == 7+incr:
            self.setCheckable(args[6+incr])
        
    def setAlternateShortcut(self, shortcut, removeEmpty=False):
        """
        Public slot to set the alternative keyboard shortcut.
        
        @param shortcut the alternative accelerator (QKeySequence)
        @param removeEmpty flag indicating to remove the alternate shortcut,
            if it is empty (boolean)
        """
        if not shortcut.isEmpty():
            shortcuts = self.shortcuts()
            if len(shortcuts) > 0:
                if len(shortcuts) == 1:
                    shortcuts.append(shortcut)
                else:
                    shortcuts[1] = shortcut
                self.setShortcuts(shortcuts)
        elif removeEmpty:
            shortcuts = self.shortcuts()
            if len(shortcuts) == 2:
                del shortcuts[1]
                self.setShortcuts(shortcuts)
        
    def alternateShortcut(self):
        """
        Public method to retrieve the alternative keyboard shortcut.
        
        @return the alternative accelerator (QKeySequence)
        """
        shortcuts = self.shortcuts()
        if len(shortcuts) < 2:
            return QKeySequence()
        else:
            return shortcuts[1]
        
    def setShortcut(self, shortcut):
        """
        Public slot to set the keyboard shortcut.
        
        @param shortcut the accelerator (QKeySequence)
        """
        QAction.setShortcut(self, shortcut)
        self.__ammendToolTip()
        
    def setShortcuts(self, shortcuts):
        """
        Public slot to set the list of keyboard shortcuts.
        
        @param shortcuts list of keyboard accelerators (list of QKeySequence)
            or key for a platform dependent list of accelerators 
            (QKeySequence.StandardKey)
        """
        QAction.setShortcuts(self, shortcuts)
        self.__ammendToolTip()
        
    def setIconText(self, text):
        """
        Public slot to set the icon text of the action.
        
        @param text new tool tip (string or QString)
        """
        QAction.setIconText(self, text)
        self.__ammendToolTip()
        
    def __ammendToolTip(self):
        """
        Private slot to add the primary keyboard accelerator to the tooltip.
        """
        shortcut = self.shortcut().toString(QKeySequence.NativeText)
        if not shortcut.isEmpty():
            if qApp.isLeftToRight():
                fmt = QString("%1 (%2)")
            else:
                fmt = QString("(%2) %1")
            self.setToolTip(fmt.arg(self.iconText()).arg(shortcut))

def addActions(target, actions):
    """
    Module function to add a list of actions to a widget.
    
    @param target reference to the target widget (QWidget)
    @param actions list of actions to be added to the target. A
        None indicates a separator (list of QActions)
    """
    if target is None:
        return
    
    for action in actions:
        if action is None:
            target.addSeparator()
        else:
            target.addAction(action)

def createActionGroup(parent, name = None, exclusive = False):
    """
    Module function to create an action group.
    
    @param parent parent object of the action group (QObject)
    @param name name of the action group object (string or QString)
    @param exclusive flag indicating an exclusive action group (boolean)
    @return reference to the created action group (QActionGroup)
    """
    actGrp = QActionGroup(parent)
    if name:
        actGrp.setObjectName(name)
    actGrp.setExclusive(exclusive)
    return actGrp
