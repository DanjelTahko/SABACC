WIDTH   = 1280
HEIGHT  = 720
FPS     = 60
CARD_BG = '#b5651d'

UI_FONT = "graphic/Pixeled.ttf"
UI_FONT_SIZE = 35
UI_FONT_COLOR = "black"
UI_BG_COLOR = "grey"

GAME_SETTINGS = {
    'rounds' : 4
}

CARD_CONFIG = {
    'numbers': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'symbols': ["square", "circle", "triangle"],
    'status': ["positive", "negative"]
}

WINNING_HANDS = {

    "PURE SABACC": 11,
    "FULL SABACC": 10,
    "FLEET": 9,
    "YEE-HAA": 8,
    "RHYLET": 7,
    "SQUADRON": 6,
    "GEE WHIZ": 5,
    "STRAIGHT KHYRON": 4,
    "BANTHAS WILD": 3,
    "RULE OF TWO": 2,
    "SABACC": 1,
    "ZERO": 0
}


BOARD = [
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'S'],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', '-', ' ', '|', '-', '-', '-', '-', '|', ' ', ' ', ' '],
    [' ', '-', ' ', '|', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' '],
    [' ', '-', ' ', '|', ' ', 'J', 'B', ' ', '|', ' ', ' ', ' '],
    [' ', '-', ' ', '|', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' '],
    [' ', '-', ' ', '|', '-', '-', '-', '-', '|', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', 'X', 'X', 'X', 'X', 'X', ' ', 'B', 'D', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
]

"""
X = 12
Y = 10

//-> 106,6666, 72


"""

