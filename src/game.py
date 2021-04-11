import random
from defines import *


def game_init(total_player: int, player_idx: int):
    card: [int] = CARD_SET * 2
    random.shuffle(card)

    board: dict = {
        "base": [
            ["J", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9", "J"],
            ["C6", "C5", "C4", "C3", "C2", "HA", "HK", "HQ", "H10", "S10"],
            ["C7", "SA", "D2", "D3", "D4", "D5", "D6", "D7", "H9", "SQ"],
            ["C8", "SK", "C6", "C5", "C4", "C3", "C2", "D8", "H8", "SK"],
            ["C9", "SQ", "C7", "H6", "H5", "H4", "HA", "D9", "H7", "SA"],
            ["C10", "S10", "C8", "H7", "H2", "H3", "HK", "D10", "H6", "D2"],
            ["CQ", "S9", "C9", "H8", "H9", "H10", "HQ", "DQ", "H5", "D3"],
            ["CK", "S8", "C10", "CQ", "CK", "CA", "DA", "DK", "H4", "D4"],
            ["CA", "S7", "S6", "S5", "S4", "S3", "S2", "H2", "H3", "D5"],
            ["J", "DA", "DK", "DQ", "D10", "D9", "D8", "D7", "D6", "J"],
        ],
        "played": [[None for _ in range(BOARD_COL)] for _ in range(BOARD_ROW)],
    }

    color: [str] = [COLOR_RED, COLOR_GREEN, COLOR_BLUE]
    if total_player == 2:
        max_cards = 7
    elif total_player == 3 or total_player == 4:
        max_cards = 6
    elif total_player == 6:
        max_cards = 5
    elif total_player == 8 or total_player == 9:
        max_cards = 4
    elif total_player == 10 or total_player == 12:
        max_cards = 3
    players: [dict] = []
    for i in range(total_player):
        player: dict = {}
        if i < 2 or total_player != 4:
            color_idx: int = random.randint(0, len(color) - 1)
            player["color"] = color.pop(color_idx)
        else:
            player["color"] = players[i - 2]["color"]
        if i == player_idx:
            player["type"] = "PLAYER"
        else:
            player["type"] = "COM"
        player["hand"] = [card.pop() for _ in range(max_cards)]
        players.append(player)

    return card, board, players


def game_check_card(board: dict, card: [str], hand: [str]):
    for r in range(BOARD_ROW):
        for c in range(BOARD_COL):
            for elem in hand:
                if board["base"][r][c] == elem and board["played"][r][c] == None:
                    hand.remove(elem)
                    hand.append(card.pop())


# Clova, Diamond: Front
def game_play_add_card(board: dict, color: str, row: int, col: int):
    board["played"][row][col] = f"{color}F"


# Spade, Heart: Side
def game_play_remove_card(board: dict, row: int, col: int):
    board["played"][row][col] = None