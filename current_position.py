#!/usr/bin/env python

"""Print the current X and Y of the mouse every second."""

# Imports
import time

# String constant
IMPORT_ERROR = "Error: Module \"{0}\" not installed.\nInstall using \"pip install {0}\" in console."
OUTPUT = "Current mouse position: {}"

# Import non-default package.
try:
    import mouse
except ModuleNotFoundError:
    input(IMPORT_ERROR.format("mouse"))
    exit(1)


# Print current position every second
while True:
    print(OUTPUT.format(mouse.get_position()))
    time.sleep(1)