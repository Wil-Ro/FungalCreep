from board import Board


class Player:
    def __init__(self, name, colour):
        self.board = Board()
        self.name = name
        self.colour = colour

    def get_colour(self):
        return self.colour

    def set_colour(self, colour):
        self.colour = colour

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name