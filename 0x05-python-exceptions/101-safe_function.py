#!/usr/bin/python3
import sys


def safe_funtion(fct, *args):
    try:
        return fct(*args)
    except Exception as inst:
        print("Exception: {}".format(inst), file=stderr)
        return None
