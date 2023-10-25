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
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
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
