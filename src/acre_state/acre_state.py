from abc import ABC, abstractmethod
import logging
"""
Acre State Class Abstract
See Class Diagram.svg for relations to children

"""
class AcreState(ABC):

    @abstractmethod
    def __init__(self, symbol= None, style = None, colour = None):
        """

        :param symbol:
        :param style:
        :param colour:
        """
        self.symbol = symbol
        self.style = style
        self.colour = colour


    @abstractmethod
    def update(self, board, x, y):
        """

        :param board: Copy of the board object we're updating
        :param x: x coordinate on board
        :param y: y coordinate on board
        :return: nothing
        """
        #logging.info("You shouldn't be able to call this Acre State Update as it's abstract")
