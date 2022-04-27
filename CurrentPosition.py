#!/usr/bin/env python3

import mouse
import time

while True:
    print("Current mouse position: {}".format(mouse.get_position()))
    time.sleep(1)