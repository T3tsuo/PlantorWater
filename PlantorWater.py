import sys
import time

import mistralton, abundant_shrine

try:
    # try to grab input from command-line
    place = int(sys.argv[1])
    action = sys.argv[2]
except IndexError:
    # else then ask for input
    place = int(input("1 for Mistralton or 2 for Abundant Shrine: "))
    action = input("'water' or 'plant'?: ")

# time for user to switch windows
time.sleep(2)
if place == 1:
    mistralton.do_all(action)
elif place == 2:
    abundant_shrine.do_all(action)