class ScriptConfig(object):
    def __init__(self, downloadPath, taskName):
        self.__downloadPath = downloadPath
        self.__taskName = taskName

    @property
    def downloadPath(self):
        return self.__downloadPath

    @downloadPath.setter
    def downloadPath(self, downloadPath):
        self.__downloadPath = downloadPath

    @property
    def taskName(self):
        return self.__taskName

    @taskName.setter
    def taskName(self, taskName):
        self.__taskName = taskName


