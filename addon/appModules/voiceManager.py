import appModuleHandler
import winUser


class AppModule(appModuleHandler.AppModule):

    def isGoodUIAWindow(self, hwnd):
        windowClass = winUser.getClassName(hwnd)
        return "SysListView32" in windowClass
