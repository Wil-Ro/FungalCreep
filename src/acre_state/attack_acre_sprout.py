
import logging
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
        logging.info("Attack sprouts become crop")
        from .cropType import CropType
        newCrop = CropType.crop.value()
        logging.debug(newCrop)
        board[x][y] = newCrop