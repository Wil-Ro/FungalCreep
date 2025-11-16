from abc import abstractmethod
import logging

from .acre_state import AcreState

"""
Acre State Class Abstract 
Inherits from acre state class

"""
class AttackAcre(AcreState):

    def __init__(self):

        super.__init__()

    @abstractmethod
    def update(self, board, x, y):
        """
        :param board: Copy of the board object we're updating
        :param x: x coordinate on board
        :param y: y coordinate on board
        :return:
        """

        logging.info("You shouldn't be able to call this attack acre")


