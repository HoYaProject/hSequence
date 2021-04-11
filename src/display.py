from defines import *


def display_board(board: dict):
    print("   0   1   2   3   4   5   6   7   8   9 ")
    print("  -----------------------------------------")
    for r in range(BOARD_ROW):
        print(f"{r} |", end="")
        for c in range(BOARD_COL):
            cell = (
                board["played"][r][c] if board["played"][r][c] else board["base"][r][c]
            )
            print(f"{cell:3}", end="")
            if c != (BOARD_COL - 1):
                print("|", end="")
            else:
                print("|")
        print("  -----------------------------------------")


def display_hand(hand: [str]):
    print(hand)
