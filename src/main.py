import logging

logging.basicConfig(
    filename="app.log",
    encoding="utf-8",
    filemode="a",
    format="{asctime} - {levelname} - {message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M",
)

logging.warning("Save me!")

from curses import wrapper
from display import Display
from input import Input
from board import Board
from player import Player
from interactive_display import InteractiveDisplay
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
        self.inter = InteractiveDisplay(self.disp, self.inp)
        self.players = [Player("player 1", None), Player("player 2", None)]
        self.turn_index = 0
        self.updater = GameplayUpdate()
        # we eventually want:
        # players are stored here, they store their boards

    def process_input(self, input):
        # player number | item placing | x | y
        opts = {"a": DefenderAcre, "b": AttackAcreCrop}
        player =int(input[0])
        item = opts[input[1]]
        x =int(input[2])
        y =int(input[3])

        self.players[player].board.set_acre_state(x, y, item())
        self.players[player].board = self.updater.OthelloUpdate(self.players[0].board, y, x)

    def run(self):
        while True:
            self.disp.clear_screen()
            self.disp.draw_board(0, 0, self.players[0].board)
            self.disp.draw_board(0, 7, self.players[1].board)
            input = self.inter.input_box(0, 14, "enter move")
            if input is not None:
                self.process_input(input)
            self.disp.update_screen()
            
            

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

