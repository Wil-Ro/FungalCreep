from abc import ABC, abstractmethod

class AcreState(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def x(self):
        pass

    @abstractmethod
    def y(self):
        pass