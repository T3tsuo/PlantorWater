import sys
import time

import move

try:
    # try to grab input from command-line
    x = sys.argv[1]
except IndexError:
    # else then ask for input
    x = input("'water' or 'plant'?: ")
# time for user to switch windows
time.sleep(2)
# do all
move.do_all(x)
