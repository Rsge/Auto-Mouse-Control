#!/usr/bin/env python3

"""Move and click or doubleclick the specified positions."""

import mouse
import time

# Points to click
POSITIONS = [
    [1113, 263],
    [1511, 309],
    [929, 314],
    [1130, 826],
    [1132, 662],
    [81, 19],
    [1895, 20],
    ]
# Position indices to double click
DOUBLE_CLICK_INDICES = [
    0,
    ]
# Time in seconds between clicks
SLEEP_TIME = 0.8


def click_move(xy, dc = False):
    mouse.move(xy[0], xy[1])
    if dc:
        mouse.double_click()
    else:
        mouse.click()
    time.sleep(SLEEP_TIME)

while True:
    inp = input("How many times?\n")
    if not inp.isnumeric:
        exit()
    x = int(inp)
    print("This'll take appr. {} s.\nPlease don't touch the mouse...".format(int(round(len(POSITIONS) * SLEEP_TIME * x, 0))))
        
    for i in range (x):
        print("{}. run".format(i + 1))
        for j in range(len(POSITIONS)):
            click_move(POSITIONS[j], j in DOUBLE_CLICK_INDICES)
    print ("Done.\n")