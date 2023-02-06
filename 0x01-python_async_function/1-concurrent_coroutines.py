#!/usr/bin/env python3
'''program to execute multiple coroutines
at the same time with async
'''
import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    '''async function that inherits from basic_async_syntax
    args:
        List: sorted list of delays 
        n: number of times to spwan wait_random
        max_delay: maximum delay time'''

    '''for i in range(n):
        display = [await wait_random(max_delay)]
        lst = sorted(display)
    return lst'''


    return sorted([await wait_random(max_delay) for i in range(n)])