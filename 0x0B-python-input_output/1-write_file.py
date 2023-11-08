#!/usr/bin/python3
"""

created by: knowlegde seeker

"""

def write_file(filename="", text=""):
    """
    prints a text file
    """
    with open(filename, "w", encoding="utf-8") as f:
       print(f.write(text))
