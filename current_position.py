#!/usr/bin/env python

"""Print the current X and Y of the mouse every second."""

# Imports
import mouse
import time

# String constant
OUTPUT = "Current mouse position: {}"


# Print current position every second
while True:
    print(OUTPUT.format(mouse.get_position()))
    time.sleep(1)