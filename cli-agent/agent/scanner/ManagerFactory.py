from agent.scanner.common.Singleton import Singleton
from agent.scanner.script.ScriptManager import ScriptManager
from agent.scanner.task.TaskManager import TaskManager


@Singleton
class ManagerFactory(object):
    def __init__(self):
        self.__scriptManager = None
        self.__taskManager = None

    def createTaskManager(self, taskServer):
        self.__taskManager = TaskManager(taskServer)

    def createScriptManager(self, dispatchServer):
        self.__scriptManager = ScriptManager(dispatchServer)

    @property
    def scriptManager(self):
        if self.__scriptManager is None:
            raise Exception("scriptManager not init")
        return self.__scriptManager

    @property
    def taskManager(self):
        if self.__taskManager is None:
            raise Exception("taskManager not init")
        return self.__taskManager
