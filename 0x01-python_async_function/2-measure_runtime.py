#!/usr/bin/env python3
#program to measure the runtime of a function 

import asyncio
from asyncio import run
import time 

wait_n = __import__('1-concurrent_coroutines').wait_n

#!/usr/bin/env python3
#measure the runtime of a function

import asyncio, time 

wait_n = __import__('1-concurrent_coroutines').wait_n

def measure_time(n: int, max_delay: int) -> float:
    '''
    function to measure execution time
    args:
    n: number of times to spawn wait_n
    max_delay: maximum delay to wait for
    Returns: run time in float form'''


    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    return(time.time() - start_time)
