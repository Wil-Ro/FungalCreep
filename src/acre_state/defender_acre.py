from acre_state.acre_state import AcreState
import curses


class DefenderAcre(AcreState):

    def __init__(self):
        super().__init__("█", curses.A_NORMAL, None)

    def update(self):
        """

        :return:
        """
        pass
