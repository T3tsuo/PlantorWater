import pydirectinput
import time
from random import random

def adjust_to_side_break():
    # 0.02 to 0.07 seconds
    return random() * 0.05 + 0.02


def paying_attention_break():
    # timer between 0.25 seconds to 0.50 seconds
    return random() * 0.25 + 0.25


def next_section_break():
    # break between 0.275 to 0.3 seconds
    return random() * 0.025 + 0.275


def change_row_break():
    # 0.2 seconds to 0.225 seconds
    return random() * 0.025 + 0.2


def fake_water():
    print("watered")
    return 2

def move_one(side, face):
    pydirectinput.keyDown(side)
    time.sleep(adjust_to_side_break())
    pydirectinput.keyUp(side)
    time.sleep(paying_attention_break())
    pydirectinput.press(face)
    time.sleep(paying_attention_break())


def move_section(side, face):
    pydirectinput.keyDown(side)
    time.sleep(next_section_break())
    pydirectinput.keyUp(side)
    time.sleep(paying_attention_break())
    pydirectinput.press(face)
    time.sleep(paying_attention_break())

def one_section(side, face):
    time.sleep(fake_water())
    for k in range(5):
        move_one(side, face)
        time.sleep(fake_water())
    time.sleep(paying_attention_break())

def do_row(side, face):
    one_section(side, face)
    move_section(side, face)
    one_section(side, face)


def up_row(side):
    if side == "right":
        pydirectinput.keyDown("right")
        time.sleep(adjust_to_side_break())
        pydirectinput.keyUp("right")
        time.sleep(paying_attention_break())
        # go up
        pydirectinput.keyDown("up")
        time.sleep(change_row_break())
        pydirectinput.keyUp("up")
        time.sleep(paying_attention_break())
        # go left
        pydirectinput.keyDown("left")
        time.sleep(adjust_to_side_break())
        pydirectinput.keyUp("left")
        time.sleep(paying_attention_break())
        pydirectinput.press("down")
        time.sleep(paying_attention_break())
    elif side == "left":
        pydirectinput.keyDown("up")
        time.sleep(change_row_break())
        pydirectinput.keyUp("up")
        time.sleep(paying_attention_break())


def do_block():
    do_row("right", "up")
    up_row("right")
    do_row("left", "down")


def water_all():
    for i in range(2):
        do_block()
        up_row("left")
    do_block()


water_all()
