import pydirectinput
import time

import random_breaks

def water():
    pydirectinput.keyDown("z")
    time.sleep(random_breaks.water_break())
    pydirectinput.keyUp("z")
    time.sleep(random_breaks.paying_attention_break())
    print("Watered")


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
    print("Planted")


def first_plant():
    # get to the section where you have to pick your seeds
    pydirectinput.keyDown("z")
    time.sleep(random_breaks.plant_break())
    pydirectinput.keyUp("z")
    input("Hit enter once you planted your first seeds and finished the dialogue: ")
    print("Planted")
    # wait for user to switch back to game window
    time.sleep(2)
