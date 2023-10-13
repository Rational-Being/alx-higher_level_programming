#!/usr/bin/python3


def complex_delete(a_dictionary, value):
    to_del = a_dictionary.copy()
    for key, v in to_del.items():
        if value in v:
            del a_dictionary[key]
    return a_dictionary
