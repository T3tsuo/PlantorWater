import pydirectinput
import time

import random_breaks

def water():
    pydirectinput.keyDown("z")
    time.sleep(random_breaks.water_break())
    pydirectinput.keyUp("z")
    time.sleep(random_breaks.paying_attention_break())
