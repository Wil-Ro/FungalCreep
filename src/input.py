import curses
from curses import *

'''
Curses gives us a single "window" object that does input and output,
it does this with weird quirks because its a c program under the hood.

This takes that object and wraps up its input methods things into 
something nicer
'''


class Input:
    def __init__(self, window):
        self.window = window
        curses.halfdelay(10)  # set default timeout when waiting for keypress

    # waits a lil' while for a key then moves on
    def wait_on_any_key(self):
        try:
            key_given = self.window.getch()
            return key_given
        except curses.error:
            pass

    # waits a lil while for a specific key then moves on
    def wait_on_key(self, key):
        try:
            key_given = self.window.getch()
            if key_given is None:
                return False
            if key_given == ord(key):
                return True
        except curses.error:
            pass

        return False

    # waits forver till a key
    def wait_indefinitely_for_key(self):
        curses.nocbreak()  # no timeout
        self.window.getch()
        curses.halfdelay(20)  # timeout back on
