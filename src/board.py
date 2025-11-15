import numpy as np
from acre_state import empty_acre

class Board:
    default_size = [8, 6]
    def __init__(self):
        self.contents = np.array([[empty_acre]*Board.default_size[0]]*Board.default_size[1])

        def set_acre_state(self, x, y, state):
            self.contents[x][y] = state


