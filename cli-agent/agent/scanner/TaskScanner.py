from agent.scanner.ManagerFactory import ManagerFactory
from agent.scanner.common.Scanner import Scanner
from agent.scanner.script.module.ScriptConfig import ScriptConfig


class TaskScanner(Scanner):
    def __init__(self, taskManager):
        Scanner.__init__(taskManager)

    def scan(self):
        self.manager.pullAllTaskConfigFromRemote()
        for taskConfig in self.manager.getTaskList():
            scriptConfig = ScriptConfig(taskConfig.taskName, taskConfig.taskName)
            ManagerFactory().scriptManager.addScriptConfig(scriptConfig)
