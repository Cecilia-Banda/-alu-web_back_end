#!/usr/bin/env python3

""" Async Generator """

from asyncio import asyncio
from random import uniform
from typing import AsyncGenerator, Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Coroutine that loop 10 times, each time asynchronously wait 1 second,
    then yield a random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)


if __name__ == "__main__":
    asyncio.run(async_generator)