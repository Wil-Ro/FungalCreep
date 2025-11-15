from abc import ABC, abstractmethod

class AcreState(ABC):

    @abstractmethod
    def __init__(self, symbol, style, colour):
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
        print("You shouldn't be able to call this Acre State Update")
