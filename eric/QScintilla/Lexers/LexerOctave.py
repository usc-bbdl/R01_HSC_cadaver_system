# -*- coding: utf-8 -*-

# Copyright (c) 2010 - 2014 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing a Octave lexer with some additional methods.
"""

from PyQt4.Qsci import QsciLexerOctave
from PyQt4.QtCore import QString

from Lexer import Lexer

class LexerOctave(QsciLexerOctave, Lexer):
    """
    Subclass to implement some additional lexer dependent methods.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent parent widget of this lexer
        """
        QsciLexerOctave.__init__(self, parent)
        Lexer.__init__(self)
        
        self.commentString = QString("#")
    
    def isCommentStyle(self, style):
        """
        Public method to check, if a style is a comment style.
        
        @return flag indicating a comment style (boolean)
        """
        return style in [QsciLexerOctave.Comment]
    
    def isStringStyle(self, style):
        """
        Public method to check, if a style is a string style.
        
        @return flag indicating a string style (boolean)
        """
        return style in [QsciLexerOctave.DoubleQuotedString,
                         QsciLexerOctave.SingleQuotedString]
    
    def defaultKeywords(self, kwSet):
        """
        Public method to get the default keywords.
        
        @param kwSet number of the keyword set (integer)
        @return string giving the keywords (string) or None
        """
        return QsciLexerOctave.keywords(self, kwSet)
