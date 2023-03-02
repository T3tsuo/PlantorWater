import pydirectinput
import time

import random_breaks
import move


def move_section(side, face):
    # keep moving to next section
    pydirectinput.keyDown(side)
    time.sleep(random_breaks.next_section_break())
    pydirectinput.keyUp(side)
    time.sleep(random_breaks.paying_attention_break())
    # face direction to plant/water
    pydirectinput.press(face)
    time.sleep(random_breaks.paying_attention_break())
    print("Moved Section")


def up_row(side):
    if side == "right":
        pydirectinput.PAUSE = 0.03
        pydirectinput.press("right")
        time.sleep(random_breaks.input_break())
        pydirectinput.press("right")
        pydirectinput.PAUSE = 0.1
        time.sleep(random_breaks.paying_attention_break())
        # go up
        pydirectinput.keyDown("up")
        time.sleep(random_breaks.change_row_break())
        pydirectinput.keyUp("up")
        time.sleep(random_breaks.paying_attention_break())
        # go left
        pydirectinput.PAUSE = 0.03
        pydirectinput.press("left")
        time.sleep(random_breaks.input_break())
        pydirectinput.press("left")
        pydirectinput.PAUSE = 0.1
        time.sleep(random_breaks.paying_attention_break())
        pydirectinput.press("down")
        time.sleep(random_breaks.paying_attention_break())
    elif side == "left":
        pydirectinput.keyDown("up")
        time.sleep(random_breaks.change_row_break())
        pydirectinput.keyUp("up")
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
    up_row("right")
    # do that row
    do_row("left", "down", action)


def do_all(action):
    for i in range(2):
        # do a whole block
        do_block(action)
        # then go to next block
        up_row("left")
    # do final block
    do_block(action)
