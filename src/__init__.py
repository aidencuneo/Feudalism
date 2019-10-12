import time

import var


def getkeyloop():
    while True:
        var.getkey()
        if var.key == 'x':
            break


gklthread = var.thread(getkeyloop)

while True:
    if str(var.key):
        # handle the key presses.
        var.key.clear()
