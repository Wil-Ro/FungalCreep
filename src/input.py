import curses
from curses import *

'''
Curses gives us a single "window" object that does input and output,
it does this with weird quirks because its a c program under the hood.

This takes that object and wraps up its input methods things into 
something nicer
'''


class Input:
    KEY_UP = curses.KEY_UP
    KEY_DOWN = curses.KEY_DOWN
    KEY_ENTER = 10

    def __init__(self, window):
        self.window = window
        curses.halfdelay(10)  # set default timeout when waiting for keypress
        window.keypad(True)

    # waits a lil' while for a key then moves on
    def wait_on_any_key(self):
        try:
            key_given = self.window.getkey()
            return key_given
        except curses.error:
            pass

    # waits a lil while for a specific key then moves on
    def wait_on_key(self, key):
        try:
            key_given = self.window.getkey()
            if key_given is None:
                return False
            if key_given == ord(key):
                return True
        except curses.error:
            pass

        return False

    # waits forver till a key
    def wait_indefinitely_for_any_key(self):
        curses.nocbreak()  # no timeout
        key_given = self.window.getch()
        curses.halfdelay(20)  # timeout back on
        return key_given

    def get_key_now(self):
        inp = None
        self.window.nodelay(True)
        try:
            inp = self.window.getkey()
        except curses.error:
            pass
        self.window.nodelay(False)
        return inp
