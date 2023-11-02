#!/usr/bin/python3
"""

This code helps me learn more about classes

@author: knowledge seeker

"""


class Rectangle:
    """
    class rectangle that defines a rectangle
    """

    def __init__(self, width=0, height=0):
        """
        Initailizes the rectangle class
        Args:
            width and height
        Raises:
           Nothing
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
