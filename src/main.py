import random
from game import *
from key_input import *

if __name__ == "__main__":
    print("Hello Sequence\n")

    print("####### Game Setup #######")
    total_player: int = input_total_player()
    player_idx: int = input_player_index()

    card, board, players = game_init(total_player, player_idx)
