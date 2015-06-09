# -*- coding: utf-8 -*-

# Copyright (c) 2007 - 2014 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing the Ericapi plugin.
"""

import os
import sys
import copy

from PyQt4.QtCore import QObject, SIGNAL, QString
from PyQt4.QtGui import QDialog, QApplication

from KdeQt.KQApplication import e4App

from E4Gui.E4Action import E4Action

from DocumentationPlugins.Ericapi.EricapiConfigDialog import EricapiConfigDialog
from DocumentationPlugins.Ericapi.EricapiExecDialog import EricapiExecDialog

import Utilities

from eric4config import getConfig

# Start-Of-Header
name = "Ericapi Plugin"
author = "Detlev Offenbach <detlev@die-offenbachs.de>"
autoactivate = True
deactivateable = True
version = "4.4.0"
className = "EricapiPlugin"
packageName = "__core__"
shortDescription = "Show the Ericapi dialogs."
longDescription = """This plugin implements the Ericapi dialogs.""" \
 """ Ericapi is used to generate a QScintilla API file for Python and Ruby projects."""
# End-Of-Header

error = QString("")

def exeDisplayData():
    """
    Public method to support the display of some executable info.
    
    @return dictionary containing the data to query the presence of
        the executable
    """
    exe = 'eric4_api'
    if Utilities.isWindowsPlatform():
        exe = os.path.join(getConfig("bindir"), exe +'.bat')
    
    data = {
        "programEntry"      : True, 
        "header"            : QApplication.translate("EricapiPlugin",
                                "Eric4 API File Generator"), 
        "exe"               : exe, 
        "versionCommand"    : '--version', 
        "versionStartsWith" : 'eric4_', 
        "versionPosition"   : -2, 
        "version"           : "", 
        "versionCleanup"    : None, 
    }
    
    return data

class EricapiPlugin(QObject):
    """
    Class implementing the Ericapi plugin.
    """
    def __init__(self, ui):
        """
        Constructor
        
        @param ui reference to the user interface object (UI.UserInterface)
        """
        QObject.__init__(self, ui)
        self.__ui = ui
        self.__initialize()
        
    def __initialize(self):
        """
        Private slot to (re)initialize the plugin.
        """
        self.__projectAct = None

    def activate(self):
        """
        Public method to activate this plugin.
        
        @return tuple of None and activation status (boolean)
        """
        menu = e4App().getObject("Project").getMenu("Apidoc")
        if menu:
            self.__projectAct = E4Action(self.trUtf8('Generate API file (eric4_api)'),
                    self.trUtf8('Generate &API file (eric4_api)'), 0, 0,
                    self, 'doc_eric4_api')
            self.__projectAct.setStatusTip(\
                self.trUtf8('Generate an API file using eric4_api'))
            self.__projectAct.setWhatsThis(self.trUtf8(
                """<b>Generate API file</b>"""
                """<p>Generate an API file using eric4_api.</p>"""
            ))
            self.connect(self.__projectAct, SIGNAL('triggered()'), self.__doEricapi)
            e4App().getObject("Project").addE4Actions([self.__projectAct])
            menu.addAction(self.__projectAct)
        
        self.connect(e4App().getObject("Project"), SIGNAL("showMenu"), 
                     self.__projectShowMenu)
        
        return None, True

    def deactivate(self):
        """
        Public method to deactivate this plugin.
        """
        self.disconnect(e4App().getObject("Project"), SIGNAL("showMenu"), 
                        self.__projectShowMenu)
        
        menu = e4App().getObject("Project").getMenu("Apidoc")
        if menu:
            menu.removeAction(self.__projectAct)
            e4App().getObject("Project").removeE4Actions([self.__projectAct])
        self.__initialize()
    
    def __projectShowMenu(self, menuName, menu):
        """
        Private slot called, when the the project menu or a submenu is 
        about to be shown.
        
        @param menuName name of the menu to be shown (string)
        @param menu reference to the menu (QMenu)
        """
        if menuName == "Apidoc":
            if self.__projectAct is not None:
                self.__projectAct.setEnabled(\
                    e4App().getObject("Project").getProjectLanguage() in \
                        ["Python", "Python3", "Ruby"])
    
    def __doEricapi(self):
        """
        Private slot to perform the eric4_api api generation.
        """
        project = e4App().getObject("Project")
        parms = project.getData('DOCUMENTATIONPARMS', "ERIC4API")
        dlg = EricapiConfigDialog(project, parms)
        if dlg.exec_() == QDialog.Accepted:
            args, parms = dlg.generateParameters()
            project.setData('DOCUMENTATIONPARMS', "ERIC4API", parms)
            
            # now do the call
            dia = EricapiExecDialog("Ericapi")
            res = dia.start(args, project.ppath)
            if res:
                dia.exec_()
                
            outputFileName = parms['outputFile']
                
            # add output files to the project data, if they aren't in already
            for progLanguage in parms['languages']:
                if "%L" in outputFileName:
                    outfile = outputFileName.replace("%L", progLanguage)
                else:
                    if len(parms['languages']) == 1:
                        outfile = outputFileName
                    else:
                        root, ext = os.path.splitext(outputFileName)
                        outfile = "%s-%s%s" % (root, progLanguage.lower(), ext)
                
                outfile = project.getRelativePath(outfile)
                if outfile not in project.pdata['OTHERS']:
                    project.pdata['OTHERS'].append(outfile)
                    project.setDirty(True)
                    project.othersAdded(outfile)
