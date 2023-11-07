#!/usr/bin/python3

"""
Creattes myint
"""


class MyInt(int):

    """
    Creattes myint
    """

    def __eq__(self, value):
        return super().__ne__(value)

    def __ne__(self, value):
        return super().__eq__(value)
