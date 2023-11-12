#!/usr/bin/python3
"""

created by: knowlegde seeker

"""

def append_write(filename="", text=""):
    """
    prints a text file
    """
    if filename == "":
        return
    with open(filename, "a", encoding="utf-8") as f:
       f.write(text)
    return len(text)
