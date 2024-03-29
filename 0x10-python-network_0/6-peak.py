#!/usr/bin/python3
"""Defines a peak-finding algorithm."""


def find_peak(list_of_integers):
    """Finds the peak in a list of integers."""
    length = len(list_of_integers)

    if length == 0:
        return None

    down, up = 0, length - 1

    while down < up:
        mid = (down + up) // 2

        if list_of_integers[mid] < list_of_integers[mid + 1]:
            down = mid + 1
        else:
            up = mid

    return list_of_integers[down]
