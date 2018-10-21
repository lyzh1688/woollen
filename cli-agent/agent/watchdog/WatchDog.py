#!/usr/bin/env python3

import schedule
import time
from agent.scanner import JobScanner


class WatchDog(object):
    def __init__(self):
        self.__job_scanner = JobScanner.JobScanner()

    def run(self):
        schedule.every(1).minutes.do(self.__job_scanner.scan_from_remote)
        while True:
            schedule.run_pending()
            time.sleep(1)


def main():
    WatchDog().run()


if __name__ == '__main__':
    main()
