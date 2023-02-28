from random import random

def plant_break():
    # 1.5 to 2 seconds
    return random() * 0.5 + 1.5


def water_break():
    # random number from 2.5 to 3 seconds
    return random() * 0.5 + 2.5


def paying_attention_break():
    # timer between 0.25 seconds to 0.50 seconds
    return random() * 0.25 + 0.25


def next_section_break():
    # break between 0.28 to 0.3 seconds
    return random() * 0.02 + 0.28


def change_row_break():
    # 0.2 seconds to 0.225 seconds
    return random() * 0.025 + 0.2

def input_break():
    # 0.1 - 0.25 seconds
    return random() * 0.15 + 0.1

