import pydirectinput
import time

import random_breaks

def water():
    pydirectinput.keyDown("z")
    time.sleep(random_breaks.water_break())
    pydirectinput.keyUp("z")
    time.sleep(random_breaks.paying_attention_break())


def plant():
    # select which seeds
    pydirectinput.keyDown("z")
    time.sleep(random_breaks.plant_break())
    pydirectinput.keyUp("z")
    time.sleep(random_breaks.paying_attention_break())
    # plant them
    pydirectinput.keyDown("z")
    time.sleep(random_breaks.plant_break())
    pydirectinput.keyUp("z")
    time.sleep(random_breaks.paying_attention_break())


def first_plant():
    # get to the section where you have to pick your seeds
    pydirectinput.keyDown("z")
    time.sleep(random_breaks.plant_break())
    pydirectinput.keyUp("z")
    input("Hit anything once you have manually added the seeds you want to plant and hit 'plant seeds'")
    # wait for user to switch back to game window
    time.sleep(2)
    pydirectinput.keyDown("z")
    time.sleep(random_breaks.plant_break())
    pydirectinput.keyUp("z")
