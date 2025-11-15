from abc import ABC, abstractmethod

class AcreState(ABC):

    @abstractmethod
    def __init__(self, symbol):
        self.symbol = symbol

    @abstractmethod
    def update(self):
        pass
