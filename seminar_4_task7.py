import threading
import asyncio
from multiprocessing import Process, Pool
from random import randint
import time


numbers = [randint(1, 100) for _ in range(1_000_000)]

counter = 0

#    threads
def increment():
    global counter
    for i in range(0, 500_000):
        counter += numbers[i]
    print(counter)


if __name__ == '__main__':
    threads = []
    thread = threading.Thread(target=increment)
    start_time = time.time()
    thread.start()

    for thread in threads:
        thread.join()

    print(f"{time.time() - start_time}")
    
    

#    processes
def increment():
    global counter
    for i in range(500_000, 1_000_000):
        counter += numbers[i]
    print(counter)


if __name__ == '__main__':
    processes = []
    process = Process(target=increment)
    start_time = time.time()
    process.start()

    for process in processes:
        process.join()

    print(f"{time.time() - start_time}")
    


# # async



async def increment():
    global counter
    for i in range(len(numbers)):
        counter += numbers[i]
    print(counter)


if __name__ == '__main__':
    start_time = time.time()
    asyncio.run(increment())

    print(f"{time.time() - start_time}")