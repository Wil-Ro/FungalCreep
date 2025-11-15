from curses import wrapper
from display import Display
from input import Input
from board import Board
from gameplay_update import GameplayUpdate
from acre_state.defender_acre import DefenderAcre
from acre_state.attack_acre_sprout import AttackAcreSprout
from acre_state.attack_acre_seed import AttackAcreSeed
from acre_state.attack_acre_crop import AttackAcreCrop

# have a peek here https://docs.python.org/3/howto/curses.html
# to get the vibe of how curses works

'''
Represents the game
'''


class Game:
    def __init__(self, window):
        self.disp = Display(window)
        self.inp = Input(window)
        self.updater = GameplayUpdate()
        # we eventually want:
        # players are stored here, they store their boards

    def run(self):
        b = Board()
        b.set_acre_state(3, 3, DefenderAcre())
        b.set_acre_state(3, 4, AttackAcreSeed())
        b.set_acre_state(3, 5, AttackAcreSprout())
        b.set_acre_state(3, 1, AttackAcreCrop())
        b.set_acre_state(5, 4, AttackAcreSeed())
        b.set_acre_state(5, 5, AttackAcreSprout())
        b.set_acre_state(5, 1, AttackAcreCrop())
        b.set_acre_state(3, 6, DefenderAcre())
        b.set_acre_state(5, 0, DefenderAcre())
        while True:
            self.disp.draw_board(0, 0, b)
            self.disp.update_screen()
            self.inp.wait_on_key("q")
            b = self.updater.OthelloUpdate(b,1,2)
            self.disp.draw_board(0, 0, b)
            self.disp.update_screen()
            self.inp.wait_on_key("q")

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

