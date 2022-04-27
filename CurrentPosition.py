#!/usr/bin/env python3

"""Print the current X and Y of the mouse every second."""

import mouse
import time

while True:
    print("Current mouse position: {}".format(mouse.get_position()))
    time.sleep(1)