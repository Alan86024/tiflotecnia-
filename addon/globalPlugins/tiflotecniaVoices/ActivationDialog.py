# ActivationDialog.py
# Copyright (C) 2024 AccessMind
#This file is covered by the GNU General Public License.
#See the file COPYING for more details.

import addonHandler
import gui
import wx

from .utils import *

addonHandler.initTranslation()


class BaseActivationDialog(wx.Dialog):
    def __init__(self, parent, title, size=(250, 150)):
        super().__init__(parent, title=title, size=size)
        self.parent = parent
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.panel = wx.Panel(self)
        messageLabel = wx.StaticText(self.panel, label=self.description)
        licenseLabel = wx.StaticText(self.panel, label=_("Enter the license key you have received after purchasing the software:"))
        self.licenseEdit = wx.TextCtrl(self.panel, style=wx.TE_LEFT)
        self.generateAuthorizationIDButton = wx.Button(self.panel, label=_("&Generate identification file"))
        self.activateButton = wx.Button(self.panel, label=_("&Activate license"))
        closeButton = wx.Button(self.panel, label=_("Close"))
        self.generateAuthorizationIDButton.Bind(wx.EVT_BUTTON, self.onGenerateID)
        self.activateButton.Bind(wx.EVT_BUTTON, self.onActivate)
        closeButton.Bind(wx.EVT_BUTTON, self.onClose)
        sizer.Add(messageLabel, 0, wx.EXPAND | wx.ALL, 5)
        sizer.Add(licenseLabel, 0, wx.EXPAND | wx.ALL, 5)
        sizer.Add(self.licenseEdit, 0, wx.EXPAND | wx.ALL, 5)
        sizer.Add(self.generateAuthorizationIDButton, 0, wx.EXPAND | wx.ALL, 5)
        sizer.Add(self.activateButton, 0, wx.EXPAND | wx.ALL, 5)
        sizer.Add(closeButton, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        self.panel.SetSizer(sizer)
        sizer.Fit(self)
        self.Layout()

    def onClose(self, evt):
        self.Close()


class OnlineActivationDialog(BaseActivationDialog):
    title = _("Online activation")
    description = _("This method will allow you to activate the software using a license key and an internet connection.")

    def __init__(self, parent):
        super().__init__(parent, title=self.title)
        self.generateAuthorizationIDButton.Hide()
        self.activateButton.SetDefault()

    def onGenerateID(self):
        pass

    def onActivate(self, evt):
        licenseKey = self.licenseEdit.GetValue()
        if not licenseKey:
            self.parent.errorMessage(_("No license key entered."))
            self.Raise()
            return
        res = self.parent.gpInstance.licenseManager.registerLicense(licenseKey, "", False)
        if not res:
            errorMsg = self.parent.gpInstance.licenseManager.errorMsg
            msg = _("An error occurred while activating license: {0}.").format(errorMsg)
            self.parent.success = False
            self.parent.message = msg
            self.EndModal(wx.ID_CANCEL)
            return
        self.parent.shouldTerminate = True
        self.parent.success = True
        self.parent.message = _("Product activation has been successfully completed. Thank you.")
        self.EndModal(wx.ID_OK)


class OfflineActivationDialog(BaseActivationDialog):
    ACTIVATION_URL = "https:///activate.accessmind.net"
    title = _("Offline activation")
    description = _("This method will allow you to activate a license without an internet connection. To perform this action, enter the license key you have received after purchasing the software, generate a machine identification file, and import a license file received from the offline activation portal which can be accessed at: {url}.").format(url=ACTIVATION_URL)

    def __init__(self, parent):
        super().__init__(parent, title=self.title)
        self.generateAuthorizationIDButton.SetDefault()

    def onGenerateID(self, evt):
        licenseKey = self.licenseEdit.GetValue()
        if not licenseKey:
            self.parent.errorMessage(_("No license key entered."))
            self.Raise()
            return
        fileName = wx.FileSelector(_("Save machine identification file"), default_filename="info.req", flags=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT, parent=self)
        if fileName:
            res = self.parent.gpInstance.licenseManager.generateAuthorizationData(licenseKey, fileName)
            if not res:
                errorMsg = self.parent.gpInstance.licenseManager.errorMsg
                self.parent.success = False
                self.parent.message = _("Error saving identification data: {0}.").format(errorMsg)
                self.EndModal(wx.ID_CANCEL)
                return
            self.parent.successMessage(_("Identification data has been saved successfully."))
            self.Raise()

    def onActivate(self, evt):
        licenseKey = self.licenseEdit.GetValue()
        if not licenseKey:
            self.parent.errorMessage(_("No license key entered."))
            self.Raise()
            return
        fileName = wx.FileSelector(_("Import license file"), default_filename="license.lic", flags=wx.FD_OPEN, parent=self)
        if fileName:
            res = self.parent.gpInstance.licenseManager.registerLicense(licenseKey, fileName, True)
            if not res:
                errorMsg = self.parent.gpInstance.licenseManager.errorMsg
                self.parent.success = False
                self.parent.message = _("Error activating license: {0}.").format(errorMsg)
                self.EndModal(wx.ID_CANCEL)
                return
            self.parent.success = True
            self.parent.shouldTerminate = True
            self.parent.message = _("Offline license has been successfully activated.")
            self.EndModal(wx.ID_OK)


class MainActivationDialog(wx.Dialog):
    def __init__(self, gpInstance, parent):
        super().__init__(parent, title=_("{name} product activation system").format(name=addonSummary), size=(250, 150))
        self.gpInstance = gpInstance
        self.success = False
        self.message = None
        self.shouldTerminate = False
        self.panel = wx.Panel(self)
        self.dlgDesc = wx.StaticText(self.panel, label=_("This program will allow you to activate your {name} software.").format(name=addonSummary))
        self.radioBox = wx.RadioBox(self.panel, label=_("Choose an activation method:"), choices=[_("Using the internet (recommended)"), _("Offline activation (for places without an internet connection)"), _("I want to try the product for 7 days")])
        self.nextButton = wx.Button(self.panel, label=_("&Next"))
        self.activateButton = wx.Button(self.panel, label=_("Try the product for &7 days"))
        self.activateButton.Hide()
        self.closeButton = wx.Button(self.panel, label=_("Close"))
        self.radioBox.Bind(wx.EVT_RADIOBOX, self.onRadioSelect)
        self.nextButton.Bind(wx.EVT_BUTTON, self.onNext)
        self.activateButton.Bind(wx.EVT_BUTTON, self.onActivateTrial)
        self.closeButton.Bind(wx.EVT_BUTTON, self.onClose)
        self.radioBox.SetSelection(0)
        self.onRadioSelect(None)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.dlgDesc, 0, wx.EXPAND | wx.ALL, 5)
        self.sizer.Add(self.radioBox, 1, wx.EXPAND | wx.ALL, 5)
        self.sizer.Add(self.nextButton, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        self.sizer.Add(self.activateButton, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        self.sizer.Add(self.closeButton, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        self.panel.SetSizer(self.sizer)
        self.sizer.Fit(self)
        self.Layout()
        self.Raise()

    def onRadioSelect(self, evt):
        selection = self.radioBox.GetSelection()
        if selection == 2:
            self.activateButton.Show()
            self.activateButton.SetDefault()
            self.nextButton.Hide()
        else:
            self.activateButton.Hide()
            self.nextButton.Show()
            self.nextButton.SetDefault()
        self.Layout()

    def onNext(self, evt):
        selection = self.radioBox.GetSelection()
        if selection == 0:
            dlg = OnlineActivationDialog(self)
        elif selection == 1:
            dlg = OfflineActivationDialog(self)
        res = dlg.ShowModal()
        if res == wx.ID_OK and self.success:
            self.successMessage(self.message, endModal=self.shouldTerminate)
        elif self.message is not None:
            self.errorMessage(self.message)

    def onActivateTrial(self, evt):
        res = self.gpInstance.licenseManager.registerLicense("", "", False)
        if not res:
            errorMsg = self.gpInstance.licenseManager.errorMsg
            self.errorMessage(_("An error occurred while activating a trial license: {0}.").format(errorMsg), endModal=True)
            return
        self.successMessage(_("Trial activation successful"), endModal=True)

    def onClose(self, evt):
        self.Close()

    def successMessage(self, text, caption=_("Success"), caller=None, endModal=False):
        gui.messageBox(text, caption, style=wx.OK | wx.ICON_INFORMATION, parent=self)
        if endModal:
            self.EndModal(wx.ID_OK)

    def errorMessage(self, text, caption=_("Error"), endModal=False):
        gui.messageBox(text, caption, style=wx.OK | wx.ICON_ERROR, parent=self)
        if endModal:
            self.EndModal(wx.ID_CANCEL)
