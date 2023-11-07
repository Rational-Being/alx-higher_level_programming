#!/usr/bin/python3

""""
created by:knowlede seeker
"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    calculates area
    """

    def __init__(self, width, height):
    """
    calculates area
    """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
    """
    calculates area
    """
        return "[Rectangle]" + str(self.__width) + "/" + str(self.__height)

    def area(self):
    """
    calculates area
    """
        return self.__width * self.__height
