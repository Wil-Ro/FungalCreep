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
from player import Player
from interactive_display import InteractiveDisplay
from gameplay_update import GameplayUpdate
from calculate_score import CalculateScore
from acre_state.cropType import CropType
from game_state import GameState
from menu_options import MenuOptions


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
        self.game_state = GameState.menu
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
        self.get_current_player().board = self.updater.OthelloUpdate(self.get_current_player().board, x, y)
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
        """
        Handles main game screen
        :return:
        """
        game_over = False
        user_input = None

        player_1_move = self.players[0].name + ":" + str(user_input)
        player_2_move = self.players[1].name + ":" + str(user_input)
        while not game_over:



            self.disp.clear_screen()
            self.disp.draw_board(0, 0, self.players[0].board)
            self.disp.write_string(20, 0, player_1_move)
            self.disp.draw_board(0, 7, self.players[1].board)
            self.disp.write_string(20, 7, player_2_move)
            self.disp.write_string(0, 13, f"{self.get_current_player().name}'s turn'")
            user_input = self.inter.input_box(0, 15, "enter move (expected format: boardNumber x y  (no spaces)")




            if user_input is not None:
                if self.process_player_game_input(user_input):

                    if self.turn_index == 0:
                        player_1_move = self.players[0].name + ":" + str(user_input)
                    elif self.turn_index == 1:
                        player_2_move = self.players[1].name + ":" + str(user_input)

                    self.increment_player()


            if self.get_current_player() == 0:
                pass
            elif self.get_current_player() == 1:
               pass

            self.disp.update_screen()

    def process_player_menu_input(self, user_input):
        menu_direction = 0
        if user_input == self.inp.KEY_UP:
            menu_direction -= 1
        if user_input == self.inp.KEY_DOWN:
            menu_direction += 1
        return menu_direction

    def menu(self):
        """
        Handles menu screen
        :return:
        """
        current_option = 0
        while True:
            self.disp.clear_screen()
            self.disp.draw_menu(self.players, current_option)

            user_input = self.inp.window.getch()
            #logging.debug("User input: %s",user_input)

            if user_input is not -1:

                current_option += self.process_player_menu_input(user_input)

                if current_option < 0:
                    current_option = len(MenuOptions)-1
                elif current_option >= len(MenuOptions):
                    current_option = 0


                """
                TODO refactor this to use menu option enum
                """
                if current_option == 0 and user_input == self.inp.KEY_ENTER:
                    #logging.debug("Running main game loop")
                    self.game_state = GameState.main_loop
                    break
                if current_option == 1 and user_input == self.inp.KEY_ENTER:
                    pass
                if current_option == 2 and user_input == self.inp.KEY_ENTER:
                    pass
                if current_option == 3 and user_input == self.inp.KEY_ENTER:
                    self.game_state = GameState.exit
                    break



            #logging.debug("currentOption: %s", current_option)
            self.disp.update_screen()


    def score(self):
        """
        Handles score screen
        :return:
        """
        score = CalculateScore(self.players)
        self.disp.draw_score(score.calculate())

    def run(self):
        """
        Main state machine
        :return:
        """

        while True:

            if self.game_state == GameState.menu:
                self.menu()

            elif self.game_state == GameState.options:
                pass
            elif self.game_state == GameState.main_loop:
                self.primary_game_loop()

            elif self.game_state == GameState.score:
                self.score()
            elif self.game_state == GameState.exit:
                #logging.debug("Qutting")
                break





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

