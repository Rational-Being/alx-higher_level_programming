#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    if my_list == 0:
        return None
    new_list = []
    for c in my_list:
        if c % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
    return new_list
