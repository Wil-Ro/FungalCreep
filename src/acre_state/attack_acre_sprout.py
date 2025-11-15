

from .acre_state import AcreState
import curses


class AttackAcreSprout(AcreState):

    def __init__(self):
        super().__init__("▄", curses.A_NORMAL, None)

    def update(self, board, x, y):
        """
        replaces self with a crop object
        :param board: Copy of the board object we're updating
        :param x: x coordinate on board
        :param y: y coordinate on board
        :return:
        """
        print("Attack sprouts become crop")
        return CropType.crop.value()