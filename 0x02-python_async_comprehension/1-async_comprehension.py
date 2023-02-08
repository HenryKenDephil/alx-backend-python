#!/usr/bin/env python3
#async comprehensions

import asyncio
from typing import Generator, List

async_generator = __import__('0-async_generator').async_generator

async def async_comprehension() -> List[float]:
    '''async function that takes no arguments
    arguments:
        async_generator: collects 10 random numbers
        
        Return: returns the 10 random numbers'''
    
    nums = [i async for i in async_generator()]
    return nums