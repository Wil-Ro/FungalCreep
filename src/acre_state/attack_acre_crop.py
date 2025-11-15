
import logging
from .acre_state import AcreState
import curses

"""
Attack Acre Crop class
Inherits from attack acre class

"""
class AttackAcreCrop(AcreState):

    def __init__(self):
        """

        :param symbol:
        :param style:
        :param colour:
        """
        super().__init__("▓", curses.A_NORMAL, None)

    def update(self, board, x, y):
        """
        if adjacent non-diagonal spaces are empty, places sprouts
        :param board: Copy of the board object we're updating
        :param x: x coordinate on board
        :param y: y coordinate on board
        :return:
        """
        logging.info("Crop spread to their neighbours")
        self.growSprouts(board, x, y)

    @staticmethod
    def growSprouts(board, x, y):
        """
        Places Seed Crops in empty adjacent non-diagonal spaces
        :param board: board we're referencing
        :param x: coordinate on board
        :param y: coordinate on board
        :return:
        """

        from .cropType import CropType
        try:
            if isinstance(board[x - 1][y], CropType.empty.value):
                board[x - 1][y] = CropType.seed.value()
                logging.debug("planting Seed at %n",board[x - 1][y])
        except IndexError:
            pass
        try:
            if isinstance(board[x + 1][y], CropType.empty.value):
                board[x + 1][y] = CropType.seed.value()
                logging.debug("planting Seed at %n",board[x + 1][y])
        except IndexError:
            pass
        try:
            if isinstance(board[x][y - 1], CropType.empty.value):
                board[x][y - 1] = CropType.seed.value()
                logging.debug("planting Seed at %n",board[x][y - 1])
        except IndexError:
            pass
        try:
            if isinstance(board[x][y + 1], CropType.empty.value):
                board[x][y + 1] = CropType.seed.value()
                logging.debug("planting Seed at %n",board[x][y + 1])
        except IndexError:
            pass
