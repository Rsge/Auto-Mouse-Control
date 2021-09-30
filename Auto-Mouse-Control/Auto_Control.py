#!/usr/bin/env python3

import mouse, time

poss = [[1113, 263], [1511, 309], [929, 314], [1130, 826], [1132, 662], [81, 19], [1895, 20]]
dcs = [0]
sleep_time = 0.8

while True:
    inp = input("How often?\n")
    if not inp.isnumeric:
        exit()
    x = int(inp)
    print("This'll take appr. {} s.\nPlease don't touch the mouse...".format(int(round(len(poss)) * sleep_time * x, 0)))

    def click_move(xy, dc = False):
        mouse.move(xy[0], xy[1])
        if dc:
            mouse.double_click()
        else:
            mouse.click()
        time.sleep(sleep_time)
        
    for i in range (x):
        print("{}. run".format(i + 1))
        for j in range(len(poss)):
            click_move(poss[j], j in dcs)
    print ("Done.\n")