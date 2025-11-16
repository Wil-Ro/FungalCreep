from enum import Enum

class GameState(Enum):
    menu = 0
    main_loop = 1
    options = 2
    score = 3
    exit = 4