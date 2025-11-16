import numpy as np
from board import Board
from acre_state.defender_acre import DefenderAcre
from acre_state.empty_acre import EmptyAcre
from acre_state.attack_acre import AttackAcre
import logging


class GameplayUpdate:
    def __init__(self):
        """

        """

    def OthelloUpdate(self, board, x, y):
        # Dave time
        # x and y is the most recent played piece - the one that initiates the flips
        """
        Updates board state for othello rules
        :return:
        """
        # board_width = Board.default_size[0]
        # board_height = Board.default_size[1]
        board_width = 6
        board_height = 6
        # remember to update these if I find something that makes that easy


        
        # making 8 lists of the directions going away from the piece that's going to do the othelloing
        x_before =[]
        xy_before_above = []
        y_above = []
        xy_after_above = []
        x_after = []
        xy_after_below = []
        y_below = []
        xy_before_below = []
        directions = [x_before, xy_before_above, y_above, xy_after_above, x_after, xy_after_below, y_below, xy_before_below]
        for i in range (x):
            x_before.append(board.contents[i,y])
            x_before.reverse()
        for i in range (min(x, y)):
            xy_before_above.append(board.contents[x-i-1, y-i-1])
        for i in range (y):
            y_above.append(board.contents[x,i])
            y_above.reverse()
        for i in range (min(board_width-x-1, y)):
            xy_after_above.append(board.contents[x+i+1, y-i-1])
        for i in range (board_width-x-1):
            x_after.append(board.contents[x+i+1,y])
        for i in range (min(board_width-x-1, board_height-y-1)):
            xy_after_below.append(board.contents[x+i+1, y+i+1])
        for i in range (board_height-y-1):
            y_below.append(board.contents[x,y+i+1])
        for i in range (min(x, board_height-y-1)):
            xy_before_below.append(board.contents[x-i-1, y+i+1])
        logging.debug(directions)


        # goes through and puts any acres that should be claimed in to_flip
        to_flip = []
        for direction in directions:
            attack_possible = True
            # for cell in direction:
            #     if isinstance(cell, DefenderAcre):
            #         attack_possible = True
            potential_flips = []
            for cell in direction:
                if attack_possible and isinstance(cell, AttackAcre):
                    potential_flips.append(cell)
                elif attack_possible and isinstance(cell, DefenderAcre):
                    attack_possible = False
                    to_flip.append(potential_flips)
                elif attack_possible and isinstance(cell, EmptyAcre):
                    attack_possible = False
                    potential_flips = []

        for cell in to_flip:
            cell = DefenderAcre

        return board
    # oats


    def GrowthUpdate(self, board):
        """
        Updates board state for growth rules
        :return:
        """
        logging.debug("growth update")
        # logging.debug(board.contents)

        # iterates over the rows and colums of board
        # updating contents for each acreState object contained in each index
        for x, row in enumerate(board.contents):
            for y, acre in enumerate(row):
                logging.debug("Updating cell: %s,%s", x,y)
                acre.update(board.contents, x, y)

        # logging.debug(board.contents)

        logging.debug("finished growth update")
        # logging.debug(board)
        return board