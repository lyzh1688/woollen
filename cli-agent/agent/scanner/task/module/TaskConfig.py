class TaskConfig(object):
    def __init__(self, taskName, mainScriptName, version, order):
        self.__taskName = taskName
        self.__mainScriptName = mainScriptName
        self.__version = version
        self.__order = order

    @property
    def taskName(self):
        return self.__taskName

    @taskName.setter
    def taskName(self, taskName):
        self.__taskName = taskName

    @property
    def mainScriptName(self):
        return self.__mainScriptName

    @mainScriptName.setter
    def mainScriptName(self, mainScriptName):
        self.__mainScriptName = mainScriptName

    @property
    def version(self):
        return self.__version

    @version.setter
    def version(self, version):
        self.__version = version

    @property
    def order(self):
        return self.__order

    @order.setter
    def order(self, order):
        self.__order = order

