from abc import ABC, abstractmethod

class AcreState(ABC):

    @abstractmethod
    def __init__(self):
        self.symbol
        self.style
        self.colour

    @abstractmethod
    def update(self):
        pass
