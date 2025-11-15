from acre_state import AcreState

class AttackAcreSeed(AcreState):

    def __init__(self, symbol):
        super.__init__(symbol)

    def update(self, board, x, y):
        """
        checks if it still has a neighbouring crop supporting
        if it does, replaces self with a sprout object
        :param board: Copy of the board object we're updating
        :param x: x coordinate on board
        :param y: y coordinate on board
        :return:
        """
        print("Attack seeds become sprouts")