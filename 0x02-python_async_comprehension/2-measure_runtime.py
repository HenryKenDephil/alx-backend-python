#!/usr/bin/env python3
'''
    run time for paralle comprehensions
'''

import asyncio
from time import time
from time import perf_counter
from asyncio import gather 

async_comprehension = __import__('1-async_comprehension').async_comprehension

async def measure_runtime() -> float:
    '''
    function that measure run time for 
    four times parallel asyncio.gather
    args:
        async_comprehension: imported function whose run time to be
        measured
        Returns: return the total run time
    total run time is about 10 seconds    
    '''
    time_before = perf_counter()
    total_run_time = perf_counter() - time_before
    await asyncio.gather(*[async_comprehension() for i in range(4)])
    return total_run_time

   


