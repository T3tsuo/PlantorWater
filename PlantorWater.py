import time

import mistralton, abundant_shrine


def run():
    # else then ask for input
    place = int(input("1 for Mistralton or 2 for Abundant Shrine: "))
    action = input("'water' or 'plant'?: ")
    # time for user to switch windows
    time.sleep(2)
    if place == 1:
        mistralton.do_all(action)
    elif place == 2:
        abundant_shrine.do_all(action)
