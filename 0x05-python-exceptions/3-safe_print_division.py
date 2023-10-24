#!/usr/bin/python3


def safe_print_division(a, b):
    try:
        int = a / b
    except:
        int = None
    finally:
        print("Inside result: {}".format(int))
    return int
