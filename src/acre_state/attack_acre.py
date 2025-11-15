from abc import abstractmethod
import acre_state

class AttackAcre(acre_state):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def x(self):
        pass

    @abstractmethod
    def y(self):
        pass