

#!/usr/bin/env python3
"""alter the function wait_n to make task_wait_n"""
import random
#!/usr/bin/env python3
#tasks

import asyncio
from typing import List
import asyncio 
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """execute concurrent coroutines
    Args:
        n (int): number of times to spawn task_wait_random
        max_delay (int): max delay
    Returns:
        list: sorted list of all delays (float values)
    """
    wait_times = await asyncio.gather(
        *tuple(map(lambda _: task_wait_random(max_delay), range(n)))
    )

    #return sorted([await task_wait_random(max_delay) for num in range(n)])
    return sorted(wait_times)