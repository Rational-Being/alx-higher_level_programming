#!/usr/bin/python3
"""

created by: knowlegde seeker

"""

def read_file(filename=""):
    """
    prints a text file
    """
    with open(filename, encoding="utf-8") as f:
       print(f.read(), end="")
