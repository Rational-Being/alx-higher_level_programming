#!/usr/bin/python3

""""
created by:knowlede seeker
"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Square(BaseGeometry):
    """
    calculates square
    """

    def __init__(self, width, height):
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        return "[Square]" + str(self.__size) + "/" + str(self.__size)

    def area(self):
        return self.__size**2
