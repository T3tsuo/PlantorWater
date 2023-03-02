import sys
import time

import mistralton

try:
    # try to grab input from command-line
    place = int(sys.argv[1])
    x = sys.argv[2]
except IndexError:
    # else then ask for input
    place = int(input("1 for Mistralton or 2 for Abundant Shrine: "))
    x = input("'water' or 'plant'?: ")

# time for user to switch windows
time.sleep(2)
if place == 1:
    mistralton.do_all(x)
