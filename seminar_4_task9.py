import requests
import time
import threading
from multiprocessing import Process
import asyncio
import aiohttp


urls = ['https://unsplash.com/photos/a-snow-covered-mountain-with-a-lake-in-front-of-it-6X8QuPSr2UE',
    'https://unsplash.com/photos/a-close-up-of-a-snow-covered-hill-htMfQCwKrro',
    'https://unsplash.com/photos/waterfall-and-trees-under-white-sky-KGM5q3dePFw'
    ]


# threading
def download(url):
    response = requests.get(url)
    filename = 'threading_' + url.replace('https://unsplash.com/photos/', '').replace('-', '_') + '.jpg'
    with open(filename, "w", encoding='utf-8') as f:
        f.write(response.text)
    print(f"Downloaded {url} in {time.time()-start_time:.2f} seconds")
        
        
threads = []
start_time = time.time()

for url in urls:
    thread = threading.Thread(target=download, args=[url])
    threads.append(thread)
    thread.start()
    
for thread in threads:
    thread.join()
    
    
    
# multiprocessing
def download(url):
    response = requests.get(url)
    filename = 'multiprocessing_' + url.replace('https://unsplash.com/photos/', '').replace('-', '_') + '.jpg'
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(response.text)
    print(f"Downloaded {url} in {time.time()-start_time:.2f} seconds")
    
    
processes = []
start_time = time.time()


if __name__ == '__main__':
    for url in urls:
        process = Process(target=download, args=(url, ))
        processes.append(process)
        process.start()
        
    for process in processes:
        process.join()



# a-sync
async def download(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            text = await response.text()
            filename = 'a-sync_' + url.replace('https://unsplash.com/photos/', '').replace('-', '_') + '.jpg'
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(text)
     
            
async def main():
    tasks = []
    for url in urls:
        task = asyncio.ensure_future(download(url))
        tasks.append(task)
    await asyncio.gather(*tasks)
            
            
if __name__ == '__main__':
    start_time = time.time()
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(main())
    asyncio.run(main())
    print(f"Downloaded {time.time()-start_time:.2f} seconds")