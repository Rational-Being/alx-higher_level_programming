#!/usr/bin/python3
"""

created by: knowlegde seeker

"""

def append_after(filename="", search_string="", new_string=""):
    """
    prints a text file
    """
    with open(filename) as f:
        for line in f:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as f:
        w.write(text)
