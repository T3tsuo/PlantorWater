from random import random

def plant_break():
    # 1.5 to 2 seconds
    return random() * 0.5 + 1.5


def water_break():
    # random number from 2.5 to 3 seconds
    return random() * 0.5 + 2.5


def adjust_to_side_break():
    # 0.02 to 0.05 seconds
    return random() * 0.03 + 0.02


def paying_attention_break():
    # timer between 0.25 seconds to 0.50 seconds
    return random() * 0.25 + 0.25


def next_section_break():
    # break between 0.275 to 0.3 seconds
    return random() * 0.025 + 0.275


def change_row_break():
    # 0.2 seconds to 0.225 seconds
    return random() * 0.025 + 0.2

