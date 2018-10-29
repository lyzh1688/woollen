import schedule
import time


class Scanner(object):
    def __init__(self, manager):
        self.__manager = manager

    @property
    def manager(self):
        return self.__manager

    def scan(self):
        print ' %s do %...' % (self.__class__.__name__, 'scan')

    def run(self):
        schedule.every(1).minutes.do(self.scan)
        while True:
            schedule.run_pending()
            time.sleep(1)
