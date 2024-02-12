import requests
import time
import threading
from multiprocessing import Process
import asyncio
import aiohttp


urls = ['https://www.google.ru/',
'https://gb.ru/',
'https://ya.ru/',
'https://www.python.org/',
'https://habr.com/ru/all/',
]


# threading
def download(url):
    response = requests.get(url)
    filename = f"threading_{url.replace('/', '').replace(':', '').replace('.', '')}.html"
    with open(f"threading_files/{filename}", 'w', encoding='utf-8') as file:
        file.write(response.text)
    print(f"{time.time() - start_time}")



threads = []
start_time = time.time()

for url in urls:
    thread = threading.Thread(target=download, args=(url, ))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()




# multiprocessing
def download(url):
    response = requests.get(url)
    filename = f"multiproc_{url.replace('/', '').replace(':', '').replace('.', '')}.html"
    with open(f"multiproc_files/{filename}", 'w', encoding='utf-8') as file:
        file.write(response.text)


if __name__ == '__main__':
    processes = []
    start_time = time.time()

    for url in urls:
        process = Process(target=download, args=(url, ))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    print(f"{time.time() - start_time}")



# async 
async def download(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            filename = f"async_{url.replace('/', '').replace(':', '').replace('.', '')}.html"
            with open(filename, 'w', encoding='utf-8') as file:
                text = await response.text()
                file.write(text)


async def main():
    tasks = []
    for url in urls:
        task = asyncio.ensure_future(download(url))
        tasks.append(task)
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    start_time = time.time()
    asyncio.run(main())

    print(f"{time.time() - start_time}")