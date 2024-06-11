#!/usr/bin/env python3
"""
    coroutine collect 10 random numbers
    using an async comprehensing over
    async_generator, then return the
    10 random numbers
"""
import asyncio
import typing
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> typing.List[float]:
    """
    coroutine return random int
    """
    return [i async for i in async_generator()]
