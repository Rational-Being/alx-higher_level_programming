#!/usr/bin/python3

"""
This module satisifies the name of the task it is named after
"""


def read_file(filename=""):
    """
    prints a file content
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
