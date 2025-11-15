
from .acre_state import AcreState
import curses
import logging

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
        logging.info("I'm a defender, you don't have anything to do with me in growth phase")