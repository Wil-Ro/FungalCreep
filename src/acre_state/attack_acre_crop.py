from acre_state import AcreState

class AttackAcreCrop(AcreState):

    def __init__(self, symbol):
        super.__init__(symbol)

    def update(self, board, x, y):
        """
        if adjacent non-diagonal spaces are empty, places sprouts
        :param board: Copy of the board object we're updating
        :param x: x coordinate on board
        :param y: y coordinate on board
        :return:
        """
        print("Crop spread to their neighbours")