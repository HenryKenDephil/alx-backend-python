#!/usr/bin/env python3
'''
    run time for paralle comprehensions
'''

import asyncio
import time
from time import perf_counter

async_comprehension = __import__('1-async_comprehension').async_comprehension

async def measure_runtime():
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
    result = await asyncio.gather(*[async_comprehension()] * 4)
    #print(result)
    return total_run_time
    


