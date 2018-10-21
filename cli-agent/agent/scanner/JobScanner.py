#!/usr/bin/env python3
import time


class JobScanner(object):
    def __init__(self):
        pass

    def scan_from_remote(self):
        time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        print(time_str)
