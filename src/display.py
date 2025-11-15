import curses


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

    def hello_world(self):
        # w,h = self.get_window_size()
        # text_x, text_y = int(w/2)-6, int(h/2)
        # self.window.addstr(text_x, text_y, "hello world")
        self.window.addstr(10, 10, "hello world")

