import logging
from datetime import datetime

logging.basicConfig(
    filename="Logs/" + datetime.now().strftime('mylogfile_%H_%M_%d_%m_%Y.log'),
    encoding="utf-8",
    filemode="a",
    format="{asctime} - {levelname} - {message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M",
    level=logging.DEBUG
)


from curses import wrapper
from display import Display
from input import Input
from board import Board
from player import Player
from interactive_display import InteractiveDisplay
from gameplay_update import GameplayUpdate
from acre_state.cropType import CropType


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

    # def process_dev_input(self, userInput):
    #     # player number | item placing | x | y
    #     opts = {"a": DefenderAcre, "b": AttackAcreCrop}
    #     try:
    #         player =int(userInput[0])
    #         item = opts[userInput[1]]
    #         x =int(userInput[2])
    #         y =int(userInput[3])
    #     except (IndexError, ValueError) as e:
    #         logging.debug(f"missing some user input: {userInput} {e}")
    #         return
    #
    #     self.players[player].board.set_acre_state(x, y, item())
    #     self.players[player].board = self.updater.OthelloUpdate(self.players[0].board, y, x)

    def process_player_game_input(self, userInput):
        """
        Proccess player input for which board to act upon
        :param userInput: expected format BoardNumber,x,y
        :return: if user input handled succesfully
        """
        # board (1-2) | x | y
        try:
            player = int(userInput[0])-1
            x = int(userInput[1])
            y = int(userInput[2])
        except (IndexError, ValueError) as e:
            logging.debug(f"missing some user input: {userInput} {e}")
            return False

        if player == self.turn_index:
            item = CropType.defender.value
        else:
            item = CropType.crop.value

        self.players[player].board.set_acre_state(x, y, item())
        # self.get_current_player().board = self.updater.OthelloUpdate(self.get_current_player().board, x, y)
        self.get_current_player().board = self.updater.GrowthUpdate(self.get_current_player().board)

        return True

    def get_current_player(self):
        """
        Whose turn it is
        :return:
        """
        return self.players[self.turn_index]

    def increment_player(self):
        """
        Increments the player's turn
        :return:
        """
        self.turn_index = (self.turn_index+1) % len(self.players)

    def primary_game_loop(self):
        game_over = False
        while not game_over:
            self.disp.clear_screen()
            self.disp.draw_board(0, 0, self.players[0].board)
            self.disp.draw_board(0, 7, self.players[1].board)
            self.disp.write_string(0, 13, f"{self.get_current_player().name}'s turn'")
            user_input = self.inter.input_box(0, 15, "enter move (expected format: boardNumber x y  (no spaces)")
            if user_input is not None:
                if self.process_player_game_input(user_input):
                    self.increment_player()

            self.disp.update_screen()

    def run(self):
        """
        Main state machine
        :return:
        """


        self.primary_game_loop()



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

