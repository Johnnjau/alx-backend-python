#!/usr/bin/env python3
"""
A coroutine that loops 10 times
every loop will wait 1 second async
yield random int (0,10)
"""
import asyncio
import random
import typing


async def async_generator() -> typing.Generator[float, None, None]:
    """
    coroutine yields a randint(0,10)
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
