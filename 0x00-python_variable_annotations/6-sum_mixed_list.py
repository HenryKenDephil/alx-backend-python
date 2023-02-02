#!/usr/bin/env python3
'''a type-annotated function sum_mixed_list
which takes a list of integers
'''
from typing import List


mxd_lst: list = [int, float]


def sum_mixed_list(mxd_lst: list) -> float:
    ''' a function that takes a list mxd_lst of integers
    and floats, and returns their sum as a float
    '''

    return sum(mxd_lst)
