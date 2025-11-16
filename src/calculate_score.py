import logging
from acre_state.cropType import CropType

class CalculateScore:
    def __init__(self, players):
        """

        """
        self.players = players

    def calculate(self):
        """
        Calculates score based on all boards
        :return: list of values for score for each player
        """
        return