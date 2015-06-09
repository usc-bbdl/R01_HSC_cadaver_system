# -*- coding: utf-8 -*-

# Copyright (c) 2010 - 2014 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing the editor highlighter keywords configuration page.
"""

from PyQt4.QtCore import pyqtSignature, QStringList, QString
from PyQt4.QtGui import QWidget

from ConfigurationPageBase import ConfigurationPageBase
from Ui_EditorKeywordsPage import Ui_EditorKeywordsPage

import QScintilla.Lexers
from QScintilla.Lexers.LexerContainer import LexerContainer

import Preferences

class EditorKeywordsPage(ConfigurationPageBase, Ui_EditorKeywordsPage):
    """
    Class implementing the editor highlighter keywords configuration page.
    """
    def __init__(self):
        """
        Constructor
        """
        ConfigurationPageBase.__init__(self)
        self.setupUi(self)
        self.setObjectName("EditorKeywordsPage")
        
        # set initial values
        self.__keywords = {
            "": QStringList(["", "", "", "", "", "", "", "", "", ""])
        }
        languages = [''] + QScintilla.Lexers.getSupportedLanguages().keys()
        languages.sort()
        for lang in languages:
            if lang:
                lex = QScintilla.Lexers.getLexer(lang)
                if isinstance(lex, LexerContainer):
                    continue
                keywords = Preferences.getEditorKeywords(lang)[:]
                if keywords.isEmpty():
                    keywords = QStringList("")
                    for kwSet in range(1, 10):
                        kw = lex.keywords(kwSet)
                        if kw is None:
                            kw = ""
                        keywords.append(kw)
                self.__keywords[lang] = keywords
            self.languageCombo.addItem(lang)
        
        self.currentLanguage = QString()
        self.currentSet = 1
        self.on_languageCombo_activated(self.currentLanguage)
    
    def save(self):
        """
        Public slot to save the editor highlighter keywords configuration.
        """
        lang = unicode(self.languageCombo.currentText())
        kwSet = self.setSpinBox.value()
        self.__keywords[lang][kwSet] = self.keywordsEdit.toPlainText()
        
        for lang, keywords in self.__keywords.items():
            Preferences.setEditorKeywords(lang, keywords)
    
    @pyqtSignature("QString")
    def on_languageCombo_activated(self, language):
        """
        Private slot to fill the keywords edit.
        
        @param language selected language (QString)
        """
        if self.currentLanguage == language:
            return
        
        if self.setSpinBox.value() == 1:
            self.on_setSpinBox_valueChanged(1)
        first, last = 10, 0
        for kwSet in range(1, 10):
            if not self.__keywords[unicode(language)][kwSet].isEmpty():
                first = min(first, kwSet)
                last = max(last, kwSet)
        if language in ["Python", "Python2", "Python3"] and last < 2:
            last = 2    # support for keyword set 2 as of QScintilla 2.6.0
        self.setSpinBox.setEnabled((not language.isEmpty()) and first < 10)
        self.keywordsEdit.setEnabled((not language.isEmpty()) and first < 10)
        if first < 10:
            self.setSpinBox.setMinimum(first)
            self.setSpinBox.setMaximum(last)
            self.setSpinBox.setValue(first)
        else:
            self.setSpinBox.setMinimum(0)
            self.setSpinBox.setMaximum(0)
            self.setSpinBox.setValue(0)
    
    @pyqtSignature("int")
    def on_setSpinBox_valueChanged(self, kwSet):
        """
        Private slot to fill the keywords edit.
        
        @param kwSet number of the selected keyword set (integer)
        """
        language = self.languageCombo.currentText()
        if self.currentLanguage == language and self.currentSet == kwSet:
            return
        
        self.__keywords[unicode(self.currentLanguage)][self.currentSet] = \
            self.keywordsEdit.toPlainText()
        
        self.currentLanguage = language
        self.currentSet = kwSet
        self.keywordsEdit.setPlainText(self.__keywords[unicode(language)][kwSet])

def create(dlg):
    """
    Module function to create the configuration page.
    
    @param dlg reference to the configuration dialog
    """
    page = EditorKeywordsPage()
    return page
