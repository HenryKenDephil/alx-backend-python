#!/usr/bin/env python3
'''returns asyncio.Task'''
import asyncio
from asyncio import create_task, Task

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """concurrency without async
    Args:
        max_delay (int): max_delay
    Returns:
        Task: createx task
    """
    return asyncio.create_task(wait_random(max_delay))