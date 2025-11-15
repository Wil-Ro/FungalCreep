from abc import ABC, abstractmethod

class AcreState(ABC):

    @abstractmethod
    def __init__(self, symbol, coordinate):
        self.symbol = symbol
        self.coordinate = coordinate

    @abstractmethod
    def update(self):
        pass
