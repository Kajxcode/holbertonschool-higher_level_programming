#!/usr/bin/python3'
def add_tuple(tuple_a=(), tuple_b=()):
    length = max(len(tuple_a), len(tuple_b))
    tuple_a = tuple_a + (0,) * (length - len(tuple_a))
    tuple_b = tuple_b + (0,) * (length - len(tuple_b))

    return tuple(a + b for a, b in zip (tuple_a, tuple_b))
