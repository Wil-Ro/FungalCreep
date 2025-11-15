from curses import wrapper
from display import Display

# have a peek here https://docs.python.org/3/howto/curses.html
# to get the vibe of how curses works


class Game:
    def __init__(self, window):
        self.disp = Display(window)
        # players are stored here, they store their boards

    def run(self):
        while True:
            # call a method to draw screen
            # call method to check for inputs
            # call method to recalculate players boards
            self.disp.hello_world()
            self.disp.update_screen()


if __name__ == '__main__':
    def run(scr):
        game = Game(scr)
        game.run()

    wrapper(run)

