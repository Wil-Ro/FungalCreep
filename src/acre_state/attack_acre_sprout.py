from acre_state import AcreState
from attack_acre_crop import AttackAcreCrop

class AttackAcreSprout(AcreState):

    def __init__(self, symbol):
        super.__init__(symbol)

    def update(self, board, x, y):
        """
        replaces self with a crop object
        :param board: Copy of the board object we're updating
        :param x: x coordinate on board
        :param y: y coordinate on board
        :return:
        """
        print("Attack sprouts become crop")
        board[x][y] = AttackAcreCrop()