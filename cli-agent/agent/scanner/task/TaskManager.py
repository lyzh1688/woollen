from agent.scanner.common.BaseManager import BaseManager


class TaskManager(BaseManager):

    def __init__(self, taskServer):
        BaseManager.__init__(taskServer)
        # 'taskList': [taskConfig]
        self.__taskConfig = {'taskList': []}

    def __addTaskConfig(self, taskConfig):
        self.__taskConfig.get('taskList').append(taskConfig)

    def pullAllTaskConfigFromRemote(self):
        # todo: remote call and update __taskConfig by invoke __addTaskConfig()
        pass

    def getTaskList(self):
        return self.__taskConfig['taskList']