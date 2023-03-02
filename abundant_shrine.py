import pydirectinput
import time

import random_breaks
import move


def do_block(side, face, action):
    move.do_section(side, face, action)
    move.other_side(side, face)
    move.do_section(move.opposite_direction[side], move.opposite_direction[face], action)


def move_first_second():
    # leave first soil to the left
    pydirectinput.keyDown("left")
    time.sleep(random_breaks.three_blocks())
    pydirectinput.keyUp("left")
    time.sleep(random_breaks.input_break())
    # go up the stairs
    pydirectinput.keyDown("up")
    time.sleep(random_breaks.three_blocks())
    pydirectinput.keyUp("up")
    time.sleep(random_breaks.input_break())
    # head towards soil
    pydirectinput.keyDown("right")
    time.sleep(random_breaks.two_blocks())
    pydirectinput.keyUp("right")
    time.sleep(random_breaks.input_break())
    # head up near it
    pydirectinput.keyDown("up")
    time.sleep(random_breaks.two_blocks())
    pydirectinput.keyUp("up")
    time.sleep(random_breaks.input_break())
    # adjust by one and face it
    move.move_one("right", "up")
    print("Next block")


def move_second_third():
    # leave second soil to the left
    pydirectinput.keyDown("left")
    time.sleep(random_breaks.second_to_third_break())
    pydirectinput.keyUp("left")
    time.sleep(random_breaks.input_break())
    pydirectinput.press("down")
    time.sleep(random_breaks.paying_attention_break())
    print("Next block")


def move_third_fourth():
    pydirectinput.keyDown("down")
    time.sleep(random_breaks.two_blocks())
    pydirectinput.keyUp("down")
    time.sleep(random_breaks.input_break())
    pydirectinput.keyDown("left")
    time.sleep(random_breaks.eleven_blocks())
    pydirectinput.keyUp("left")
    time.sleep(random_breaks.input_break())
    pydirectinput.keyDown("down")
    time.sleep(random_breaks.four_blocks())
    pydirectinput.keyUp("down")
    time.sleep(random_breaks.input_break())
    pydirectinput.keyDown("left")
    time.sleep(random_breaks.six_blocks())
    pydirectinput.keyUp("left")
    time.sleep(random_breaks.input_break())
    pydirectinput.press("up")
    time.sleep(random_breaks.paying_attention_break())
    print("Next block")


def move_fourth_fifth():
    move.move_one("left", "up")
    pydirectinput.keyDown("up")
    time.sleep(random_breaks.six_blocks())
    pydirectinput.keyUp("up")
    time.sleep(random_breaks.input_break())
    print("Next block")


def move_fifth_sixth():
    pydirectinput.keyDown("up")
    time.sleep(random_breaks.four_blocks())
    pydirectinput.keyUp("up")
    time.sleep(random_breaks.input_break())
    move.move_one("right", "up")
    print("Next block")


def move_sixth_seventh():
    pydirectinput.keyDown("up")
    time.sleep(random_breaks.seven_blocks())
    pydirectinput.keyUp("up")
    time.sleep(random_breaks.input_break())
    pydirectinput.keyDown("right")
    time.sleep(random_breaks.seven_blocks())
    pydirectinput.keyUp("right")
    time.sleep(random_breaks.input_break())
    pydirectinput.keyDown("up")
    time.sleep(random_breaks.four_blocks())
    pydirectinput.keyUp("up")
    time.sleep(random_breaks.input_break())
    pydirectinput.keyDown("right")
    time.sleep(random_breaks.six_blocks())
    pydirectinput.keyUp("right")
    time.sleep(random_breaks.input_break())
    pydirectinput.keyDown("z")
    time.sleep(random_breaks.use_surf_break())
    pydirectinput.keyUp("z")
    time.sleep(random_breaks.input_break())
    pydirectinput.keyDown("right")
    time.sleep(random_breaks.cross_water())
    pydirectinput.keyUp("right")
    time.sleep(random_breaks.cross_water())
    # hop on bike
    pydirectinput.press("1")
    # go to soil
    pydirectinput.keyDown("right")
    time.sleep(random_breaks.three_blocks())
    pydirectinput.keyUp("right")
    time.sleep(random_breaks.input_break())
    pydirectinput.keyDown("down")
    time.sleep(random_breaks.three_blocks())
    pydirectinput.keyUp("down")
    time.sleep(random_breaks.input_break())
    move.move_one("right", "down")
    print("Last Block")


def do_all(action):
    do_block("right", "up", action)
    move_first_second()
    do_block("right", "up", action)
    move_second_third()
    do_block("right", "down", action)
    move_third_fourth()
    do_block("right", "up", action)
    move_fourth_fifth()
    do_block("right", "up", action)
    move_fifth_sixth()
    do_block("left", "up", action)
    move_sixth_seventh()
    do_block("right", "down", action)
