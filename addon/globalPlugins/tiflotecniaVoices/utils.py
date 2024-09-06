import addonHandler

addonHandler.initTranslation()
addonInst = addonHandler.getCodeAddon()
addonName = addonInst.name
addonVersion = addonInst.version
addonSummary = _(addonInst.manifest["summary"])
menuEntryName = "&{name}".format(name=addonSummary)
