#!/usr/bin/env python3
import time
import schedule
from agent.scanner.script.ScriptManager import ScriptManager


class MetaScanner(object):
    def __init__(self):
        pass

    def scanFromRemote(self):
        timeStr = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        print timeStr
        ScriptManager('http://192.168.1.2:8080/woollen/dispatch/scriptDownload').downloadLatestScript('1.0.0.1')
        print 'download script'

    def run(self):
        schedule.every(1).minutes.do(self.__jobScanner.scanFromRemote)
        while True:
            schedule.run_pending()
            time.sleep(1)