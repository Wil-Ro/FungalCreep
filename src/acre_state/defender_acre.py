from acre_state.acre_state import AcreState
import curses


class DefenderAcre(AcreState):

    def __init__(self):
        super().__init__("█", curses.A_NORMAL, None)

    def update(self, board, x, y):
        """
        :param board: Copy of the board object we're updating
        :param x: x coordinate on board
        :param y: y coordinate on board
        :return:
        """
        print("I'm a defender, you don't have anything to do with me in growth phase")