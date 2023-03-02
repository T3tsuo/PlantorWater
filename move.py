import pydirectinput
import time

import random_breaks
import interact


first_plant = True
opposite_direction = {'right': 'left',
                      'left': 'right',
                      'up': 'down',
                      'down': 'up'}


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

def other_side(side, face):
    # go right/left
    pydirectinput.PAUSE = 0.03
    pydirectinput.press(side)
    time.sleep(random_breaks.input_break())
    pydirectinput.press(side)
    pydirectinput.PAUSE = 0.1
    time.sleep(random_breaks.paying_attention_break())
    # go up/down
    pydirectinput.keyDown(face)
    time.sleep(random_breaks.change_row_break())
    pydirectinput.keyUp(face)
    time.sleep(random_breaks.paying_attention_break())
    # go right/left
    pydirectinput.PAUSE = 0.03
    pydirectinput.press(opposite_direction[side])
    time.sleep(random_breaks.input_break())
    pydirectinput.press(opposite_direction[side])
    pydirectinput.PAUSE = 0.1
    time.sleep(random_breaks.paying_attention_break())
    pydirectinput.press(opposite_direction[face])
    time.sleep(random_breaks.paying_attention_break())
    print("Other Side")
