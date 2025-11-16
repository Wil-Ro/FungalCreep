# FungalCreep
Game for ascii game jam

## Setup instructions
1. clone repo
2. go into repo folder and run command ``python3 -m venv venv``
3. activate venv with `venv\Scripts\activate.bat` for windows or `source venv/bin/activate` for linux
4. run ``pip install -r requirements.txt`` to install the packages
5. set up code in src!

## TODO
1. User Input
    * Able to attack and defend, specify grid index and board
    * Able to set player name, color
    * Menu system
    * ### Bounds validation
2. Display Board
    * Display unique symbols for each tile type
    * ### Color and player names displayed 
    * Display two boards
3. Growth Behaviour
    * growth cycle of crop from seed to sprout
    * seeds die if crop dies
    * Mature crops spread seeds
    * ### some crops growing faster than others
4. Othello Behaviour
    *
5. State Machine program 
    * Basic game behaviour
    * Menu
    * Player customization
    * Options menu
    * Post game score screen