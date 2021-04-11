import random
from game import *
from key_input import *
from display import *

if __name__ == "__main__":
    print("Hello Sequence\n")

    print("####### Game Setup #######")
    total_player: int = input_total_player()
    player_idx: int = input_player_index()

    card, board, players = game_init(total_player, player_idx)

    turn: int = 0
    while True:
        print(f"####### Player {turn:02}'s turn: ({players[turn]['color']})\n")

        game_check_card(board, card, players[turn]["hand"])
        if players[turn]["type"] == "PLAYER":
            display_board(board)
            print()
            display_hand(players[turn]["hand"])

            card_idx: int = input_card_index(len(players[turn]["hand"]))
            played_card = players[turn]["hand"].pop(card_idx)
            if played_card == "CJ" or played_card == "DJ":
                row, col = input_board_front_position(board)
                game_play_add_card(board, players[turn]["color"], row, col)
            elif played_card == "SJ" or played_card == "HJ":
                row, col = input_board_side_position(board, players[turn]["color"])
                game_play_remove_card(board, row, col)
            else:
                row, col = input_board_normal_position(board, played_card)
                game_play_add_card(board, players[turn]["color"], row, col)
        else:
            card_idx: int = random.randint(0, len(players[turn]["hand"]) - 1)
            played_card = players[turn]["hand"].pop(card_idx)
            if played_card == "CJ" or played_card == "DJ":
                row, col = input_board_front_position_random(board)
                game_play_add_card(board, players[turn]["color"], row, col)
            elif played_card == "SJ" or played_card == "HJ":
                row, col = input_board_side_position_random(
                    board, players[turn]["color"]
                )
                game_play_remove_card(board, row, col)
            else:
                row, col = input_board_normal_position_random(board, played_card)
                game_play_add_card(board, players[turn]["color"], row, col)
        players[turn]["hand"].append(card.pop())
        print(f"# Played {played_card} into ({row}, {col})\n")

        turn += 1
        turn %= total_player