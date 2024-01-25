#!/usr/bin/python3
"""funtion finds the peak of an iterable
passed to it"""

def find_peak(list_of_integers):
    """
    the function that performs the task in commant above above
    """
    list_of_integers.sort()
    return list_of_integers[-1]
   