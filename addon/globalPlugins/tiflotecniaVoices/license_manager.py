# license_manager.py
# Copyright (C) 2024 AccessMind
#This file is covered by the GNU General Public License.
#See the file COPYING for more details.

from contextlib import contextmanager
import synthDrivers.tiflotecniaVoices.lowLevel as ttsEngine


class LicenseManager():
    def __init__(self):
        self.engineInitialized = False
        self.errorMsg = None

    def _initialize(self):
        if ttsEngine.ttsEngineLib is None:
            ttsEngine.preinitialize()
            res = ttsEngine.startAuthorization()
            if not res:
                return False
        else:
            self.engineInitialized = True
        return True

    def _terminate(self):
        if not self.engineInitialized:
            ttsEngine.terminate()

    @contextmanager
    def _engineInit(self):
        try:
            if not self._initialize(): return
            yield
        finally:
            self._terminate()

    def checkLicenseValidity(self):
        with self._engineInit():
            res = ttsEngine.setLicenseKey("")
            if not res: return False
            res = ttsEngine.queryLicense()
            if not res:
                self.errorMsg = ttsEngine.getLastErrorMessage()
                return False
            return True

    def registerLicense(self, licenseKey, path="", offline=False):
        with self._engineInit():
            if not licenseKey:
                res = ttsEngine.setLicenseKey("")
            else:
                res = ttsEngine.setLicenseKey(licenseKey.encode())
            if not res:
                self.errorMsg = ttsEngine.getLastErrorMessage()
                return False
            res = ttsEngine.registerLicense(path, offline)
            if not res:
                self.errorMsg = ttsEngine.getLastErrorMessage()
                return False
            return True

    def generateAuthorizationData(self, licenseKey, path):
        with self._engineInit():
            res = ttsEngine.setLicenseKey(licenseKey.encode())
            if not res: return False
            res = ttsEngine.generateAuthorizationData(path)
            if not res:
                self.errorMsg = ttsEngine.getLastErrorMessage()
                return False
            return True

    def unregisterLicense(self, path=""):
        with self._engineInit():
            res = ttsEngine.setLicenseKey("")
            if not res: return False
            res = ttsEngine.queryLicense()
            if not res:
                self.errorMsg = ttsEngine.getLastErrorMessage()
                return False
            res = ttsEngine.unregisterLicense(path)
            if not res:
                self.errorMsg = ttsEngine.getLastErrorMessage()
                return False
            return True

    def isActivationOffline(self):
        with self._engineInit():
            res = ttsEngine.setLicenseKey("")
            if not res: return False
            res = ttsEngine.queryLicense()
            if not res:
                self.errorMsg = ttsEngine.getLastErrorMessage()
                return False
            res = ttsEngine.isActivationOffline()
            return res
