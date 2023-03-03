import pydirectinput
import time

import random_breaks
import move


def move_section(side, face):
    # keep moving to next section
    pydirectinput.keyDown(side)
    time.sleep(random_breaks.four_blocks())
    pydirectinput.keyUp(side)
    time.sleep(random_breaks.paying_attention_break())
    # face direction to plant/water
    pydirectinput.press(face)
    time.sleep(random_breaks.paying_attention_break())
    print("Moved Section")


def up_row(face):
    pydirectinput.keyDown(face)
    time.sleep(random_breaks.change_row_break())
    pydirectinput.keyUp(face)
    time.sleep(random_breaks.paying_attention_break())
    print("Changed Row")


def do_row(side, face, action):
    # does a section
    move.do_section(side, face, action)
    # move to next
    move_section(side, face)
    # does next section
    move.do_section(side, face, action)


def do_block(action):
    # do entire row
    do_row("right", "up", action)
    # go to next row of block
    move.other_side("right", "up")
    # do that row
    do_row("left", "down", action)


def do_all(action):
    for i in range(2):
        # do a whole block
        do_block(action)
        # then go to next block
        up_row("up")
    # do final block
    do_block(action)
