from agent.scanner import ManagerFactory
from agent.scanner.common.Scanner import Scanner


class ScriptScanner(Scanner):
    def __init__(self, scriptManager):
        Scanner.__init__(scriptManager)

    def scan(self):
        taskList = ManagerFactory().taskManager.getTaskList()
        for taskConfig in taskList:
            self.manager.upgradeScript(taskConfig.taskName)


