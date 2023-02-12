#!/usr/bin/env python3

#!/usr/bin/env python3
'''basic async function'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
   
    '''start with the async function
    arguments are:
        max_delay(int, optional) : default: max_delay = 10'''
    delay_rate = random.random() * max_delay
    await asyncio.sleep(delay_rate)
    return delay_rate

    

    