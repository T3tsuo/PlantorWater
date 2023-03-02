from random import random


def cross_water():
    # 1 - 1.02 seconds
    return random() * 0.02 + 1


def use_surf_break():
    # 4 - 5 seconds
    return random() * 1 + 4

def seven_blocks():
    # 0.53 - 0.55 seconds
    return random() * 0.02 + 0.53

def six_blocks():
    # 0.48 - 0.5
    return random() * 0.02 + 0.48

def four_blocks():
    # 0.28 - 0.3
    return random() * 0.02 + 0.28


def eleven_blocks():
    # from 0.89 to 0.91 seconds
    return random() * 0.02 + 0.89

def second_to_third_break():
    # from 0.96 seconds to 0.98 second
    return random() * 0.02 + 0.96


def three_blocks():
    # from 0.21 to 0.23 seconds
    return random() * 0.02 + 0.21


def two_blocks():
    # from 0.11 to 0.13 seconds
    return random() * 0.02 + 0.11

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

