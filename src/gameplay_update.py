import numpy as np



class GameplayUpdate:
    def __init__(self):
        """

        """

    def OthelloUpdate(self, board):
        """
        Updates board state for othello rules
        :return:
        """





    def GrowthUpdate(self, board):
        """
        Updates board state for growth rules
        :return:
        """

        for x, row in enumerate(board):
            for y, acre in enumerate(row):
                acre.update(board, x, y)
