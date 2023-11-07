#!/usr/bin/python3

"""
Creattes myint
"""


def add_attribute(obj, name, other):
    """
    Creattes myint
    """
    if not hasattr(obj, "__dict__"):
       raise TypeError("can't add new attribute")
    setattr(obj, name, other)
