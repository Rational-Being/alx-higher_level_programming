#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: knowledge seeker
"""


class Square:
    """
    a class that defines a sqaure
    """

    def __init__(self, size=0, position=(0, 0)):
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
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        msg = TypeError("position must be a tuple of 2 positive integers")
        if type(value) is not tuple or len(value) != 2:
            raise msg
        elif type(value[0]) is not int or type(value[1]) is not int:
            raise msg
        elif value[0] < 0 or value[1] < 0:
            raise msg
        self.__position = value

    def area(self):
        return self.__size**2

    def my_print(self):
        SS = self.__size  # self.__size
        SP = self.position
        if SS == 0:
            print()
        else:
            for i in range(SP[1]):
                print()
            for i in range(SS):
                for j in range(SP[0]):
                    print(end="")
                for k in range(SS):
                    print("#", end="")
                print()
