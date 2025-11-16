from enum import Enum

class MenuOptions(str,Enum):
    play = "play\n"
    changeName1 = "changeName1\n"
    changeName2 = "changeName2\n"
    exit = "exit\n"