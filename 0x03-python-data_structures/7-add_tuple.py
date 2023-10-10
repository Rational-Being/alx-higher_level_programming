#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    tuple_c = list(tuple_a) + [0] * 2
    tuple_d = list(tuple_b) + [0] * 2
    tuple_f = [x + y for x, y in zip(a, b)]
    return tuple(tuple_f[0:2])
