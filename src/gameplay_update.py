from acre_state.cropType import CropType
import logging


class GameplayUpdate:
    def __init__(self):
        """

        """

    def OthelloUpdate(self, board, y, x):
        logging.debug("fuck me sideways")
        # Dave time
        # x and y is the most recent played piece - the one that initiates the flips
        """
        Updates board state for othello rules
        :return:
        """
        #board_width = Board.default_size[0]
        #board_height = Board.default_size[1]
        board_width = 6
        board_height = 6
        # remember to update these if I find something that makes that easy


        
        # making 8 lists of the directions going away from the piece that's going to do the othelloing
        x_before = []
        xy_before_above = []
        y_above = []
        xy_after_above = []
        x_after = []
        xy_after_below = []
        y_below = []
        xy_before_below = []
        directions = [x_before, xy_before_above, y_above, xy_after_above, x_after, xy_after_below, y_below, xy_before_below]

        # adds the coordinates of each cell into its relevant direction
        for i in range (x):
            x_before.append([x-1-i,y])
        for i in range (min(x, y)):
            xy_before_above.append([x-i-1, y-i-1])
        for i in range (y):
            y_above.append([x,y-i-1])
        for i in range (min(board_width-x-1, y)):
            xy_after_above.append([x+i+1, y-i-1])
        for i in range (board_width-x-1):
            x_after.append([x+i+1,y])
        for i in range (min(board_width-x-1, board_height-y-1)):
            xy_after_below.append([x+i+1, y+i+1])
        for i in range (board_height-y-1):
            y_below.append([x,y+i+1])
        for i in range (min(x, board_height-y-1)):
            xy_before_below.append([x-i-1, y+i+1])
        # logging.debug("directions: %s", directions)
        logging.debug("x_before: %s", x_before)
        logging.debug("xy_before_above: %s", xy_before_above)
        logging.debug("y_above: %s", y_above)
        logging.debug("xy_after_above: %s", xy_after_above)
        logging.debug("x_after: %s", x_after)
        logging.debug("xy_after_below: %s", xy_after_below)
        logging.debug("y_below: %s", y_below)
        logging.debug("xy_before_below: %s", xy_before_below)



        # goes through and puts any acres that should be claimed in to_flip
        to_flip = []
        for direction in directions:
            attack_possible = True
            # for cell in direction:
            #     if isinstance(cell, DefenderAcre):
            #         attack_possible = True
            potential_flips = []
            for cell in direction:
                logging.debug("cell checking: %s", cell)
                logging.debug("WHAT IS YOUR FUCKING TYPE %s", type(board.contents[cell[0]][cell[1]]))

                # next cell an attacking one? we can eat that :3
                if attack_possible and isinstance(board.contents[cell[0]][cell[1]], CropType.crop.value):
                    logging.debug("cell checking attack: %s", cell)
                    potential_flips.append(cell)

                # next cell a defending one? we can eat everything before it :3 (BUT EATING STOPS HERE  )
                elif attack_possible and isinstance(board.contents[cell[0]][cell[1]], CropType.defender.value):
                    logging.debug("cell checking defender: %s", cell)
                    attack_possible = False
                    for fuck in potential_flips:
                        to_flip.append(fuck)

                # empty cell? no snack for you :(
                elif attack_possible and isinstance(board.contents[cell[0]][cell[1]], CropType.empty.value):
                    logging.debug("cell checking empty: %s", cell)
                    attack_possible = False
                    potential_flips = []
            logging.debug("potential flips: %s", potential_flips)

        # goes through consumed cells and eats them (turns them into defenders)
        for cell in to_flip:
            board.contents[cell[0]][cell[1]] = CropType.defender.value()
            logging.debug("cunt: %s", [x,y])

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

        for x, row in enumerate(board.contents):
            for y, acre in enumerate(row):
                if isinstance(acre, CropType.crop.value):
                    acre.new_seed = False

        logging.debug("finished growth update")
        logging.debug(board.contents)
        # logging.debug(board)
        return board