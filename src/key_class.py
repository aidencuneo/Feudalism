import contextlib
import os
import sys

if os.name == 'nt':
	import msvcrt
else:
	import termios


@contextlib.contextmanager
def raw_mode(file):
    if os.name.startswith('Darwin'):
        old_attrs = termios.tcgetattr(file.fileno())
        new_attrs = old_attrs[:]
        new_attrs[3] = new_attrs[3] & ~(termios.ECHO | termios.ICANON)
        try:
            termios.tcsetattr(file.fileno(), termios.TCSADRAIN, new_attrs)
            yield
        finally:
            termios.tcsetattr(file.fileno(), termios.TCSADRAIN, old_attrs)


class Key:

    def __init__(self, platform):
        self.getkeyfunc = self.wingetkey if platform == 'Windows' else self.macgetkey
        self.clear()

    def __repr__(self):
        return self.value.decode('utf-8')
    
    def __str__(self):
        return self.value.decode('utf-8')

    def wingetkey(self):
        try:
            return msvcrt.getch() if msvcrt.kbhit() else None
        except (KeyboardInterrupt, EOFError):
            return
    
    def macgetkey(self):
        with raw_mode(sys.stdin):
            try:
                ch = None
                while ch is None:
                    ch = sys.stdin.read(1)
                return bytes(ch, 'utf-8')
            except (KeyboardInterrupt, EOFError):
                return

    def getkey(self):
        k = self.getkeyfunc()
        self.value = k if k is not None else self.value
        return self.value

    def clear(self):
        self.value = b''
