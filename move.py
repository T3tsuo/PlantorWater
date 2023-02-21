import pydirectinput
import time

import random_breaks
import interact

def move_one(side, face):
    # move to next soil block
    pydirectinput.keyDown(side)
    time.sleep(random_breaks.adjust_to_side_break())
    pydirectinput.keyUp(side)
    time.sleep(random_breaks.paying_attention_break())
    # face the block
    pydirectinput.press(face)
    time.sleep(random_breaks.paying_attention_break())


def move_section(side, face):
    # keep moving to next section
    pydirectinput.keyDown(side)
    time.sleep(random_breaks.next_section_break())
    pydirectinput.keyUp(side)
    time.sleep(random_breaks.paying_attention_break())
    # face direction to plant/water
    pydirectinput.press(face)
    time.sleep(random_breaks.paying_attention_break())

def one_section(side, face, action):
    if action == "water":
        interact.water()
    for k in range(5):
        # move one plant block to the right
        move_one(side, face)
        if action == "water":
            interact.water()
    time.sleep(random_breaks.paying_attention_break())

def do_row(side, face, action):
    # does a section
    one_section(side, face, action)
    # move to next
    move_section(side, face)
    # does next section
    one_section(side, face, action)


def up_row(side):
    if side == "right":
        pydirectinput.keyDown("right")
        time.sleep(random_breaks.adjust_to_side_break())
        pydirectinput.keyUp("right")
        time.sleep(random_breaks.paying_attention_break())
        # go up
        pydirectinput.keyDown("up")
        time.sleep(random_breaks.change_row_break())
        pydirectinput.keyUp("up")
        time.sleep(random_breaks.paying_attention_break())
        # go left
        pydirectinput.keyDown("left")
        time.sleep(random_breaks.adjust_to_side_break())
        pydirectinput.keyUp("left")
        time.sleep(random_breaks.paying_attention_break())
        pydirectinput.press("down")
        time.sleep(random_breaks.paying_attention_break())
    elif side == "left":
        pydirectinput.keyDown("up")
        time.sleep(random_breaks.change_row_break())
        pydirectinput.keyUp("up")
        time.sleep(random_breaks.paying_attention_break())


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

# wait for user to switch windows
time.sleep(2)
do_all("water")
