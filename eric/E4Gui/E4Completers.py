# -*- coding: utf-8 -*-

# Copyright (c) 2007 - 2014 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing various kinds of completers.
"""

from PyQt4.QtCore import QDir, QStringList, Qt
from PyQt4.QtGui import QCompleter, QFileSystemModel, QStringListModel

from Globals import isWindowsPlatform

class E4FileCompleter(QCompleter):
    """
    Class implementing a completer for file names.
    """
    def __init__(self, parent = None, 
                 completionMode = QCompleter.PopupCompletion, 
                 showHidden = False):
        """
        Constructor
        
        @param parent parent widget of the completer (QWidget)
        @keyparam completionMode completion mode of the 
            completer (QCompleter.CompletionMode)
        @keyparam showHidden flag indicating to show hidden entries as well (boolean)
        """
        QCompleter.__init__(self, parent)
        self.__model = QFileSystemModel(self)
        if showHidden:
            self.__model.setFilter(\
                QDir.Filters(QDir.Dirs | QDir.Files | QDir.Drives | \
                             QDir.AllDirs | QDir.Hidden))
        else:
            self.__model.setFilter(\
                QDir.Filters(QDir.Dirs | QDir.Files | QDir.Drives | QDir.AllDirs))
        self.setModel(self.__model)
        self.setCompletionMode(completionMode)
        if isWindowsPlatform():
            self.setCaseSensitivity(Qt.CaseInsensitive)
        if parent:
            parent.setCompleter(self)

class E4DirCompleter(QCompleter):
    """
    Class implementing a completer for directory names.
    """
    def __init__(self, parent = None, 
                 completionMode = QCompleter.PopupCompletion, 
                 showHidden = False):
        """
        Constructor
        
        @param parent parent widget of the completer (QWidget)
        @keyparam completionMode completion mode of the 
            completer (QCompleter.CompletionMode)
        @keyparam showHidden flag indicating to show hidden entries as well (boolean)
        """
        QCompleter.__init__(self, parent)
        self.__model = QFileSystemModel(self)
        if showHidden:
            self.__model.setFilter(\
                QDir.Filters(QDir.Drives | QDir.AllDirs | QDir.Hidden))
        else:
            self.__model.setFilter(\
                QDir.Filters(QDir.Drives | QDir.AllDirs))
        self.setModel(self.__model)
        self.setCompletionMode(completionMode)
        if isWindowsPlatform():
            self.setCaseSensitivity(Qt.CaseInsensitive)
        if parent:
            parent.setCompleter(self)

class E4StringListCompleter(QCompleter):
    """
    Class implementing a completer for string lists.
    """
    def __init__(self, parent = None, strings = QStringList(),
                 completionMode = QCompleter.PopupCompletion):
        """
        Constructor
        
        @param parent parent widget of the completer (QWidget)
        @param strings list of string to load into the completer (QStringList)
        @keyparam completionMode completion mode of the 
            completer (QCompleter.CompletionMode)
        """
        QCompleter.__init__(self, parent)
        self.__model = QStringListModel(strings, parent)
        self.setModel(self.__model)
        self.setCompletionMode(completionMode)
        if parent:
            parent.setCompleter(self)
