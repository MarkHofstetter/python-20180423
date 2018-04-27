import asyncio
import time

# execute with -u so output is not buffered

async def hello_world():
    print("Hello World!")
    await asyncio.sleep(10)
    print('hello over')    

async def some_loop():
    for i in range(15):
        print(i)
        await asyncio.sleep(1)
        # time.sleep(1)  ## blocked

async def ainput():
    a = input("iiii")
        
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.gather(
    hello_world(),
    some_loop(),
))
# loop.close()# Blocking call which returns when the hello_world() coroutine is done


# loop.run_until_complete(hello_world())
    
loop.close()