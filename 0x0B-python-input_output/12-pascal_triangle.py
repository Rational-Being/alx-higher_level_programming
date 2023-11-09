#!/usr/bin/python3
"""

created by: knowlegde seeker

"""

def pascal_triangle(n):
    """
    creates pascal tringle
    """
    p = []
    tri = []

    for i in range(int(n)):    
        buf = p[:]
        buf.append(1)
        for i in range(1, len(p)):
            buf[i] = p[i - 1] + p[i]
        p = buf[:]
        tri.append(p)
    return tri
