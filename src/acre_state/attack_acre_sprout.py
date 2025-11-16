
import logging
from .acre_state import AcreState
import curses

"""
Attack Acre Sprout
Inherits from attack acre class
"""
class AttackAcreSprout(AcreState):

    def __init__(self):
        """

        :param symbol:
        :param style:
        :param colour:
        """
        super().__init__("▄", curses.A_NORMAL, None)

    def update(self, board, x, y):
        """
        replaces self with a crop object
        :param board: Copy of the board object we're updating
        :param x: x coordinate on board
        :param y: y coordinate on board
        :return:
        """
        from .cropType import CropType
        newCrop = CropType.crop.value()
        logging.debug("Attack sprouts become crop %s %s,%s ", newCrop, x,y)
        board[x][y] = newCrop