#!/usr/bin/python3

""""
created by:knowlede seeker
"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    calculates square
    """

    def __init__(self, size):
        """
        inializwes square
        """
        super().__init__(size, size)
