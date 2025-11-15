from acre_state import AcreState
from attack_acre_sprout import AttackAcreSprout
from attack_acre_crop import AttackAcreCrop
from empty_acre import EmptyAcre

class AttackAcreSeed(AcreState):

    def __init__(self, symbol):
        super.__init__(symbol)

    def update(self, board, x, y):
        """
        checks if it still has a neighbouring attack crop supporting
        if it does, replaces self with a sprout object
        else replaces with an empty acre object
        :param board: Copy of the board object we're updating
        :param x: x coordinate on board
        :param y: y coordinate on board
        :return:
        """
        print("Attack seeds become sprouts")
        if self.doesSurroundingContainCrop(board, x, y):
            board[x][y] = AttackAcreSprout()
        else:
            board[x][y] = EmptyAcre()

    @staticmethod
    def doesSurroundingContainCrop(board, x, y):
        """
        Checks if any non-diagonal cells are of type attack crop
        :param board: board we're referencing
        :param x: coordinate on board
        :param y: coordinate on board
        :return: if any non-diagonal adjacent cell is of type attack acre crop
        """
        if isinstance(board[x - 1][y],AttackAcreCrop):
            return True
        elif isinstance(board[x + 1][y],AttackAcreCrop):
            return True
        elif isinstance(board[x][y - 1],AttackAcreCrop):
            return True
        elif isinstance(board[x][y + 1],AttackAcreCrop):
            return True
        else:
            return False