# interface.py
# Copyright (C) 2024 AccessMind
#This file is covered by the GNU General Public License.
#See the file COPYING for more details.

import addonHandler
import gui
import languageHandler
import os
import synthDriverHandler
import wx

from .ActivationDialog import MainActivationDialog
from .utils import *

addonHandler.initTranslation()
ABOUT_TEXT = _("""{name} version {version}.

This product is based on AccessMind Runa TTS technology, and Cerence embedded TTS voices. License conditions for each component are as follows:

Cerence Embedded TTS, 

Copyright © 2024 Cerence, Inc. All rights reserved.

Runa TTS technology, including engine, NVDA interface, and license management:

Copyright © 2024 AccessMind, LLC. All rights reserved.
""").format(name=addonSummary, version=addonVersion)


class Interface():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

    def __init__(self, gpInstance, licenseManager):
        self.gpInstance = gpInstance
        self.licenseManager = licenseManager

    def showActivationDialog(self):
        wx.CallLater(2000, self.onShowDialog)

    def onShowDialog(self):
        activationDlg = MainActivationDialog(self, gui.mainFrame)
        ans = activationDlg.ShowModal()
        if ans == wx.ID_OK:
            activationDlg.Destroy()
            activationDlg = None
            if not self.gpInstance.checkData():
                self.onManageVoices()
            else:
                if gui.messageBox(_("Do you want to switch to {name} speech synthesizer?").format(name=addonSummary), _("Switch speech synthesizer"),wx.YES|wx.NO|wx.ICON_INFORMATION,gui.mainFrame) == wx.YES:
                    self.setSynth(addonName)
            self.reinitializeMenu()

    def onLicenseImport(self, evt):
        self.onShowDialog()

    def onLicenseRemove(self, evt):
        confirmationMsg = _("Are you sure you want to remove the license from this computer? The license will be transfered back to the server and the {name} will stop working.").format(name=addonSummary)
        offlineActivationMsg = _(" Because you have an offline activated license, you will need to save the file which will be created after this dialog and pass it to the activation portal or your distributer to get the activation back.")
        if self.licenseManager.isActivationOffline():
            confirmationMsg += offlineActivationMsg
        result = gui.messageBox(confirmationMsg, _("Remove license"), style=wx.YES|wx.NO|wx.ICON_INFORMATION, parent=gui.mainFrame)
        if result == wx.NO:
            return
        if self.licenseManager.isActivationOffline():
            fileName = wx.FileSelector(_("Save machine identification file"), default_filename="info.req", flags=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT, parent=gui.mainFrame)
            if not fileName:
                gui.messageBox(_("File was not saved."), _("Error"), style=wx.OK | wx.ICON_ERROR, parent=gui.mainFrame)
                return
            res = self.licenseManager.unregisterLicense(fileName)
        else:
            res = self.licenseManager.unregisterLicense()
        if not res:
            errorMsg = self.licenseManager.errorMsg
            gui.messageBox(_("Error removing license: {0}.").format(errorMsg), _("Error"), style=wx.OK | wx.ICON_ERROR, parent=gui.mainFrame)
            return
        gui.messageBox(_("The license has been removed successfully."), _("Success"), style=wx.OK | wx.ICON_INFORMATION, parent=gui.mainFrame)
        if synthDriverHandler.getSynth().name == addonName:
            self.setSynth("espeak")
        self.reinitializeMenu()

    def setSynth(self, synthName):
                synthList = synthDriverHandler.getSynthList()
                ttsEngine = [engine[0] for engine in synthList if engine[0] == synthName][0]
                synthDriverHandler.setSynth(ttsEngine)  

    def onManageVoices(self, evt=None):
        if evt is None:
            if not gui.messageBox(_("Do you want to run voice manager tool to download voices?"), _("No installed voices"), wx.YES|wx.NO|wx.ICON_INFORMATION, gui.mainFrame) == wx.YES:
                return
        self.runVoiceManager()

    def onAbout(self, evt):
        gui.messageBox(_(ABOUT_TEXT), _("About {name}").format(name=addonSummary), wx.OK)

    def onDocumentation(self, evt):
        from documentationUtils import getDocFilePath
        getDocFilePath.rootPath = os.path.join(self.BASE_DIR, "doc")
        os.startfile(getDocFilePath("readme.html"))

    def createMenu(self):
        self.menu = gui.mainFrame.sysTrayIcon.menu
        mainMenu = wx.Menu()
        self.addonMenu = self.menu.Insert(2, wx.ID_ANY, _(menuEntryName), mainMenu, _("{name} management options").format(name=addonSummary))
        self.manageVoicesItem = self.addMenuItem(mainMenu, _("Manage &voices..."), _("Manages voices installations and removals"), self.onManageVoices)
        if self.licenseManager.checkLicenseValidity():
            self.removeLicenseItem = self.addMenuItem(mainMenu, _("&Remove license"), _("Removes the license from this computer"), self.onLicenseRemove)
        else:
            self.activateLicenseItem = self.addMenuItem(mainMenu, _("&activate license"), _("Opens license activation dialog"), self.onLicenseImport)
        self.documentationItem = self.addMenuItem(mainMenu, _("Open &documentation..."), _("Opens documentation"), self.onDocumentation)
        self.aboutItem = self.addMenuItem(mainMenu, _("&About {name}...").format(name=addonSummary), _("Shows about dialog"), self.onAbout)

    def addMenuItem(self, menu, title, tooltip, callback):
        item = menu.Append(wx.ID_ANY, title, tooltip)
        gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, callback, item)
        return item

    def removeMenu(self):
        try:
            self.menu.Remove(self.addonMenu)
        except Exception:
            pass

    def reinitializeMenu(self):
        self.removeMenu()
        self.createMenu()

    def runVoiceManager(self):
        lang = languageHandler.getLanguage()
        voiceManagerPath = os.path.join(self.BASE_DIR, "voiceManager")
        voiceManagerExecutablePath = os.path.join(voiceManagerPath, "voiceManager.exe")
        command = [voiceManagerExecutablePath, "--language", lang]
        import subprocess
        subprocess.Popen(command)
