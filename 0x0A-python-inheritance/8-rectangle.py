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
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height