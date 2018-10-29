import requests
import json

from agent.scanner.common.BaseManager import BaseManager


class ScriptManager(BaseManager):

    def __init__(self, dispatchServer):
        BaseManager.__init__(dispatchServer)
        self.__scriptConfigMapper = {}

    def addScriptConfig(self, scriptConfig):
        self.__scriptConfigMapper[scriptConfig.taskName] = scriptConfig

    # 脚本升级
    def upgradeScript(self, taskName):
        if taskName not in self.____scriptConfigMapper:
            return
        checkRet = self.__checkLatestScript(taskName)
        if checkRet['isExpire']:
            scriptConfig = self.____scriptConfigMapper[taskName]
            self.____downloadLatestScript(scriptConfig.scriptNameList, checkRet['latestScriptVersion'])

    # 获取任务当前脚本版本
    def __getLocalScriptVersion(self, taskName):
        # todo:
        return '1.0.0.1'

    # 检查是否需要更新
    def __checkLatestScript(self, taskName):
        # todo:
        ret = {'isExpire': True, 'latestScriptVersion': '1.0.0.1'}
        return ret

    def __downloadLatestScriptGroup(self,targetScriptNameList, targetScriptVersion):
        for targetScriptName in targetScriptNameList:
            self.__downloadLatestScript(targetScriptName, targetScriptVersion)

    def __downloadLatestScript(self, targetScriptName, targetScriptVersion):
        request = {'targetScriptVersion': targetScriptVersion, 'targetScriptName': targetScriptName}
        headers = {'content-type': "application/json"}
        response = requests.post(self.serverAddress, data=json.dumps(request), headers=headers)
        script_file = open(targetScriptName, 'wb')
        for chunk in response.iter_content(100000):
            script_file.write(chunk)
        script_file.close()
        # todo: check complete by checksum
