import random
from defines import *


def input_total_player() -> int:
    while True:
        try:
            num: int = _get_int_number(f"Input Total Players (2-4): ")
            if 2 <= num <= 4:
                return num
        except:
            continue


def input_player_index() -> bool:
    while True:
        try:
            idx: int = _get_int_number(
                f"Input Player Index (If you don't input the available index, COM only play): "
            )
            return idx
        except:
            continue


def input_card_index(len: int) -> int:
    while True:
        try:
            idx: int = _get_int_number(f"Input Card Index (0 - {len - 1}): ")
            if 0 <= idx < len:
                return idx
        except:
            continue


def input_board_front_position(board: dict):
    while True:
        try:
            row = _get_int_number("Input Position to Play (Row): ")
            col = _get_int_number("Input Position to Play (Col): ")
            if 0 <= row <= 9 and 0 <= col <= 9:
                if board["base"][row][col] != "J" and board["played"][row][col] == None:
                    return row, col
        except:
            continue


def input_board_side_position(board: dict, color: str):
    while True:
        try:
            row = _get_int_number("Input Position to Play (Row): ")
            col = _get_int_number("Input Position to Play (Col): ")
            if 0 <= row <= 9 and 0 <= col <= 9:
                if (
                    board["base"][row][col] != "J"
                    and board["played"][row][col] != None
                    and board["played"][row][col][0] != color
                    and board["played"][row][col][1] == "F"
                ):
                    return row, col
        except:
            continue


def input_board_normal_position(board: dict, played_card: str):
    while True:
        try:
            row = _get_int_number("Input Position to Play (Row): ")
            col = _get_int_number("Input Position to Play (Col): ")
            if 0 <= row <= 9 and 0 <= col <= 9:
                if (
                    board["base"][row][col] == played_card
                    and board["played"][row][col] == None
                ):
                    return row, col
        except:
            continue


def input_board_front_position_random(board: dict):
    row: [int] = []
    col: [int] = []
    for r in range(BOARD_ROW):
        for c in range(BOARD_COL):
            if board["base"][r][c] == "J" and board["played"][r][c] == None:
                row.append(r)
                col.append(c)
    idx: int = random.randint(0, len(row) - 1)
    return row[idx], col[idx]


def input_board_side_position_random(board: dict, color: str):
    row: [int] = []
    col: [int] = []
    for r in range(BOARD_ROW):
        for c in range(BOARD_COL):
            if (
                board["base"][row][col] != "J"
                and board["played"][row][col] != None
                and board["played"][row][col][0] != color
                and board["played"][row][col][1] == "F"
            ):
                row.append(r)
                col.append(c)
    idx: int = random.randint(0, len(row) - 1)
    return row[idx], col[idx]


def input_board_normal_position_random(board: dict, played_card: str):
    row: [int] = []
    col: [int] = []
    for r in range(BOARD_ROW):
        for c in range(BOARD_COL):
            if board["base"][r][c] == played_card and board["played"][r][c] == None:
                row.append(r)
                col.append(c)
    idx: int = random.randint(0, len(row) - 1)
    return row[idx], col[idx]


def _get_int_number(msg: str) -> int:
    try:
        return int(input(msg))
    except:
        raise Exception("Not available")