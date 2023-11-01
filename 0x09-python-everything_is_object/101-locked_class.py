#!/usr/bin/python3
"""
This satistisfy task 101


"""


class LockedClass:
    """
    a class with no class
    or object atribute
    prevents user form dynamiclaly creating new instance attributes
    """

    __slots__ = ["first_name"]
