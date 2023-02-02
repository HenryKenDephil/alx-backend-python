#!/usr/bin/env python3
# program that takes a list input of floats
from typing import List, Optional

input_list = List[float]


def sum_list(lst: input_list) -> float:
    '''
    a function that takes input_list of floats as argument
    and returns their sum as a float
    '''
    return sum(lst)


# sum_list(3.14, 1.11, 2.22)
