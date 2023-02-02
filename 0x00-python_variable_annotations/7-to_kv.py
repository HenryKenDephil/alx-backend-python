#!/usr/bin/env python3
'''
a typed-annotated function to_kv that takes string
k and an int or float v and returs a tuple
'''
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''
    function that takes string k and an int or float
    as arguments and returns a tuple

    keyword arguments:
    k --str variable
    v --int or float variable
    Return:  a tuple
    '''
    return (k, v**2)
