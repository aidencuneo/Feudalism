import contextlib
import os
import platform
import sys
import threading

import key_class


def getinput(p=''):
    return raw_input(p) if sys.version_info[0] < 3 else input(p)


def prompt():
    return get_input('\n-- Enter to continue --\n')


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_platform():
    return platform.system()


def thread(target, daemon=True):
    t = threading.Thread(target=target)
    t.setDaemon(daemon)
    t.start()
    return t


key = key_class.Key(get_platform())


def getkey():
    return key.getkey()
