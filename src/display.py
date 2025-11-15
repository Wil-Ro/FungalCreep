import curses
import logging
'''
Curses gives us a single "window" object that does input and output,
it does this with weird quirks because its a c program under the hood.

This takes that object and wraps up its display methods things into
something nicer

its also in charge of displaying specific screens e.g. the input screen
and menu
'''


class Display:
    def __init__(self, window):
        self.window = window
        curses.noecho()
        curses.cbreak()
        curses.curs_set(0)

    def __del__(self):
        curses.nocbreak()
        curses.echo()
        curses.endwin()

    def clear_screen(self):
        self.window.clear()

    def update_screen(self):
        self.window.refresh()

    def get_window_size(self):
        return curses.COLS, curses.LINES

    def write_string(self, x, y, text):
        self.window.addstr(y, x, text)
    
    def draw_board(self, x, y, board):
        for column in board.contents:
            for acre in column:
                # replace acre.style with acre.style|acre.colour to let them
                # control their own colour
                # logging.debug(acre)
                self.window.addstr(y, x*2, f"{acre.symbol}{acre.symbol}", acre.style)
                x += 1
            y += 1
            x = 0
