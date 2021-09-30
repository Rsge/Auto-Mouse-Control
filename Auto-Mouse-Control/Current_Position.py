#!/usr/bin/env python3

import mouse, time

while True:
    print("Current mouse position: {}".format(mouse.get_position()))
    time.sleep(1)