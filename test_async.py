import asyncio
from socket import MsgFlag
from time import perf_counter
import time


async def counter(name, number):
    for i in range(0, number+2):
        print(f'{name} : {i}')
        time.sleep(1)


async def hasil():
    start_launch = perf_counter()
    counter("indra", 8)
    msg = "done"
    # await asyncio.gather(
    #     counter("cita", 1), counter("nanta", 2), counter("indra", 3)
    # )
    print(f'total time : {perf_counter() - start_launch}.')
    return await asyncio.to_thread(counter, "indra", 8) 

# asyncio.run(main())
