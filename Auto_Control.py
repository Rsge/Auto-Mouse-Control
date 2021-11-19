#!/usr/bin/env python3

import mouse, time

# Points to click
poss = [[1113, 263], [1511, 309], [929, 314], [1130, 826], [1132, 662], [81, 19], [1895, 20]]
# Position indexes to double click
dcs = [0]
# Time in seconds between clicks
sleep_time = 0.8

def click_move(xy, dc = False):
    mouse.move(xy[0], xy[1])
    if dc:
        mouse.double_click()
    else:
        mouse.click()
    time.sleep(sleep_time)

while True:
    inp = input("How many times?\n")
    if not inp.isnumeric:
        exit()
    x = int(inp)
    print("This'll take appr. {} s.\nPlease don't touch the mouse...".format(int(round(len(poss) * sleep_time * x, 0))))
        
    for i in range (x):
        print("{}. run".format(i + 1))
        for j in range(len(poss)):
            click_move(poss[j], j in dcs)
    print ("Done.\n")