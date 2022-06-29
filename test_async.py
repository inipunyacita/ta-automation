import asyncio
from time import perf_counter
import time


async def counter(name, number):
    for i in range(0, number+2):
        print(f'{name} : {i}')


async def main():
    start_launch = perf_counter()
    await asyncio.gather(
        counter("cita", 1), counter("nanta", 2), counter("indra", 3)
    )
    print(f'total time : {perf_counter() - start_launch}.')

asyncio.run(main())
