import numpy as np

class Board:
    default_size = [8, 6]
    def __init__(self):
        self.contents = np.array([[None]*Board.default_size[0]]*Board.default_size[1])


test = Board()
        
