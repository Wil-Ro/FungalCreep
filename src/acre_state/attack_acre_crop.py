from acre_state import AcreState
from attack_acre_seed import AttackAcreSeed
from empty_acre import EmptyAcre
from acre_state.acre_state import AcreState
import curses


class AttackAcreCrop(AcreState):

    def __init__(self):
        super().__init__("▓", curses.A_NORMAL, None)

    def update(self, board, x, y):
        """
        if adjacent non-diagonal spaces are empty, places sprouts
        :param board: Copy of the board object we're updating
        :param x: x coordinate on board
        :param y: y coordinate on board
        :return:
        """
        print("Crop spread to their neighbours")
        self.growSprouts(board, x, y)

    @staticmethod
    def growSprouts(board, x, y):
        """

        :param board: board we're referencing
        :param x: coordinate on board
        :param y: coordinate on board
        :return:
        """

        if isinstance(board[x - 1][y], EmptyAcre):
            board[x - 1][y] = AttackAcreSeed()
        elif isinstance(board[x + 1][y], EmptyAcre):
            board[x + 1][y] = AttackAcreSeed
        elif isinstance(board[x][y - 1], EmptyAcre):
            board[x][y - 1] = AttackAcreSeed
        elif isinstance(board[x][y + 1], EmptyAcre):
            board[x][y + 1] = AttackAcreSeed