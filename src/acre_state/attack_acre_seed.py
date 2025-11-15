
import logging
from .acre_state import AcreState

import curses

"""
Attack Acre Seed Class
Inherits from attack acre class

"""
class AttackAcreSeed(AcreState):

    def __init__(self, symbol, style, colour):
        """

        :param symbol:
        :param style:
        :param colour:
        """
        super().__init__("▁", curses.A_NORMAL, None)

    def update(self, board, x, y):
        """
        checks if it still has a neighbouring attack crop supporting
        if it does, replaces self with a sprout object
        else replaces with an empty acre object
        :param board: Copy of the board object we're updating
        :param x: x coordinate on board
        :param y: y coordinate on board
        :return:
        """
        logging.info("Attack seeds become sprouts")
        from .cropType import CropType
        if self.doesSurroundingContainCrop(board, x, y):
            newCrop = CropType.sprout.value()
            logging.info("This seed sprouted")
        else:
            newCrop = CropType.empty.value()
            logging.debug("This seed not sprouted")
        logging.debug(newCrop)
        board[x][y] = newCrop

    @staticmethod
    def doesSurroundingContainCrop(board, x, y):
        """
        Checks if any non-diagonal cells are of type attack crop
        :param board: board we're referencing
        :param x: coordinate on board
        :param y: coordinate on board
        :return: if any non-diagonal adjacent cell is of type attack acre crop
        """

        from .cropType import CropType
        try:
            if isinstance(board[x - 1][y], CropType.crop.value):
                return True
        except IndexError:
            pass
        try:
            if isinstance(board[x + 1][y], CropType.crop.value):
                return True
        except IndexError:
            pass
        try:
            if isinstance(board[x][y - 1], CropType.crop.value):
                return True
        except IndexError:
            pass
        try:
            if isinstance(board[x][y + 1], CropType.crop.value):
                return True
        except IndexError:
            pass


        return False