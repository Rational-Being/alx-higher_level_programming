#!/usr/bin/python3

"""
tis is supposed to be a comment
"""

def add_attribute(obj, name, other):
    """
    tis is supposed to be a comment
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, other)
