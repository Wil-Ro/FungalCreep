from abc import ABC, abstractmethod

class AcreState(ABC):

    @abstractmethod
    def __init__(self, symbol, style, colour):
        self.symbol = symbol
        self.style = style
        self.colour = colour

    @abstractmethod
    def update(self):
        pass
