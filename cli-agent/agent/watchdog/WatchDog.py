#!/usr/bin/env python3

import schedule
import time
from agent.scanner import MetaScanner


class WatchDog(object):
    def __init__(self):
        self.__jobScanner = MetaScanner.MetaScanner()

    def run(self):
        schedule.every(1).minutes.do(self.__jobScanner.scanFromRemote)
        while True:
            schedule.run_pending()
            time.sleep(1)


def main():
    WatchDog().run()


if __name__ == '__main__':
    main()
