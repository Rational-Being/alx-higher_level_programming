#!/usr/bin/python3

""""
created by:knowlede seeker
"""


def inherits_from(obj, a_class):
    """
    returns true object of an obj is an instance
    """
    if not isinstnace(a_class, type):
        raise TypeError("not correct type")
    return issubclass(type(obj), a_class) and type(obj) is not a_class
