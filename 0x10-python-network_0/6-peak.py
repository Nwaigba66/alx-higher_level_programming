#!/usr/bin/python3
"""This module defines a function that finds a peak in unsorted list"""


def find_peak(list_of_integers):
    """ Find peak in an unsorted list """

    # return None if not list or if empty
    if not list_of_integers:
        return
    left_index = 0
    right_index = len(list_of_integers) - 1

    # keep the search going until left index == right index
    while left_index != right_index:
        middle_index = int((left_index+right_index)/2)

        if list_of_integers[middle_index] < list_of_integers[middle_index + 1]:
            left_index = middle_index + 1
        else:  
            right_index = middle_index
    # return the number (peak) at the convergent left and right index
    return list_of_integers[right_index]
