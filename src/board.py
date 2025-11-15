import numpy as np
from acre_state.empty_acre import EmptyAcre


class Board:
    default_size = [8, 6]

    def __init__(self):
        self.contents = np.array([[EmptyAcre()]*Board.default_size[0]]*Board.default_size[1]) # creates a 8x6 2d array of EmptyAcre's

    def set_acre_state(self, x, y, state):
        self.contents[x][y] = state


