

from .acre_state import AcreState
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
        from .cropType import CropType
        if isinstance(board[x - 1][y], CropType.empty.value):
            board[x - 1][y] = CropType.seed.value()
        elif isinstance(board[x + 1][y], CropType.empty.value):
            board[x + 1][y] = CropType.seed.value()
        elif isinstance(board[x][y - 1], CropType.empty.value):
            board[x][y - 1] = CropType.seed.value()
        elif isinstance(board[x][y + 1], CropType.empty.value):
            board[x][y + 1] = CropType.seed.value()