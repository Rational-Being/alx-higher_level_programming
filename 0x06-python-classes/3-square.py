#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: knowledge seeker
"""


class Square:
    """
    a class that defines a sqaure
    """

    def __init__(self, size=0):
        """
        Initailizes the square class
        Args:
            size: the size of the square
        Raises:
           TypeError: if size not int
           ValueError: if size less than zero
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size * self.__size
