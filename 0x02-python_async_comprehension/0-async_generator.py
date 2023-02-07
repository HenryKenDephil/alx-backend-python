#!/usr/bin/env python3
# coroutine function that takes no arguments
import asyncio
import random
from typing import Generator

async def async_generator():
    '''
    a function that takes no arguments
    yield a random number between 0 and 10
    '''
    
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0,10)
     

    


