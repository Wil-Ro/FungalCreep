from curses import wrapper
from display import Display
from input import Input
from board import Board
from player import Player
from interactive_display import InteractiveDisplay

# have a peek here https://docs.python.org/3/howto/curses.html
# to get the vibe of how curses works

'''
Represents the game
'''


class Game:
    def __init__(self, window):
        self.disp = Display(window)
        self.inp = Input(window)
        self.inter = InteractiveDisplay(self.disp, self.inp)
        self.players = [Player("player 1", None), Player("player 2", None)]
        self.turn_index = 0

    def run(self):
        while True:
            self.inter.basic_input_window()
            self.disp.draw_board(0, 0, board)
            self.disp.update_screen()
            if self.inp.wait_on_key("q"):
                break

        # we eventually want:
        # call method to check for inputs
        # call a method to draw screen
        # loop through those, when enter is hit:
        # call method to recalculate players boards
        # repeat


'''
We create a method called run which sets up the game and runs it, we then
give this to the curses wrapper to run.

Curses has a method called "wrapper()" which cleans up after itself if the
program crashes or errors out. You give it a method to run and it runs it, 
passing it a window object (we give this to Display and Input, see their files
for more details). If that method crashes itll keep things tidy.
'''
if __name__ == '__main__':
    def run(scr):
        game = Game(scr)
        game.run()

    wrapper(run)

