#!/usr/bin/env python

"""Move mouse to and click or doubleclick the specified positions."""

# Imports
import time

# Points to click
POSITIONS = [
    [0, 0],
    [100, 100],
    [200, 200],
    ]
# Position indices to double click
DOUBLE_CLICK_INDICES = [
    0,
    ]
# Time in seconds between clicks
SLEEP_TIME = 0.8

# String constants
IMPORT_ERROR = "Error: Module \"{0}\" not installed.\nInstall using \"pip install {0}\" in console."
INPUT_QUESTION = "How many times?\n"
WAIT_TIME_MSG = "This will take appr. {} s.\nPlease don't touch the mouse..."
RUN_COUNTER = "\t{}. run"
DONE_MSG = "Done.\n"

# Import non-default package.
try:
    import mouse
except ModuleNotFoundError:
    input(IMPORT_ERROR.format("mouse"))
    exit(1)


# Move and (double)click function
def click_move(xy, dc=False):
    mouse.move(xy[0], xy[1])
    if dc:
        mouse.double_click()
    else:
        mouse.click()
    time.sleep(SLEEP_TIME)

# Run through the defined positions an input number of times, then ask again
# Exit if not provided with number
while True:
    inp = input(INPUT_QUESTION)
    if not inp.isnumeric:
        exit()
    x = int(inp)
    print(WAIT_TIME_MSG.format(int(round(len(POSITIONS) * SLEEP_TIME * x, 0))))
        
    for i in range (x):
        print(RUN_COUNTER.format(i + 1))
        for j in range(len(POSITIONS)):
            click_move(POSITIONS[j], j in DOUBLE_CLICK_INDICES)
    print(DONE_MSG)