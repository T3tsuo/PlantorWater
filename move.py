import pydirectinput
import time

import random_breaks
import interact


first_plant = True


def move_one(side, face):
    # move to next soil block
    pydirectinput.PAUSE = 0.03
    pydirectinput.press(side)
    time.sleep(random_breaks.input_break())
    pydirectinput.press(side)
    pydirectinput.PAUSE = 0.1
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

    
def do_section(side, face, action):
    global first_plant
    if action == "water":
        interact.water()
    # you have to manually plant your first seeds but the program will water for you
    elif action == "plant" and first_plant is True:
        interact.first_plant()
        first_plant = False
    elif action == "plant" and first_plant is False:
        interact.plant()
    for k in range(5):
        # move one plant block to the right
        move_one(side, face)
        if action == "water":
            interact.water()
        elif action == "plant":
            interact.plant()
    time.sleep(random_breaks.paying_attention_break())

    
def do_row(side, face, action):
    # does a section
    do_section(side, face, action)
    # move to next
    move_section(side, face)
    # does next section
    do_section(side, face, action)


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
