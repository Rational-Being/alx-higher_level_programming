#!/usr/bin/python3
"""

This module satisfies the task which name the file is named

@author: knowledge seeker

"""

def add_integer(a, b=98):
    """
    Return the sum of two integers
    Args: 
        a: takes int
        b: takes int
    Raises:
        TypeError: if arg not int
    """
    
    if not (type(a) is float or type(a) is int):
       raise TypeError("a must be an integer")
    if not (type(b) is float or type(b) is int):
       raise TypeError("b must be an integer")
    return int(a) + int(b)
    
