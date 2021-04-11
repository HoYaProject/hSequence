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


def _get_int_number(msg: str) -> int:
    try:
        return int(input(msg))
    except:
        raise Exception("Not available")