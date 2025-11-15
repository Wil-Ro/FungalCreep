
from .acre_state import AcreState
import curses


class EmptyAcre(AcreState):

    def __init__(self):
        super().__init__("▒", curses.A_NORMAL, None)

    def update(self):
        pass


    def update(self, board, x, y):
        """
        :param board: Copy of the board object we're updating
        :param x: x coordinate on board
        :param y: y coordinate on board
        :return:
        """
        print("This acre is empty")