import asyncio
import aiofiles
import os
import time
import aiohttp

urls = [
    'https://mykaleidoscope.ru/uploads/posts/2021-03/1616732502_43-p-kvartirnii-interer-46.jpg',
    'https://mykaleidoscope.ru/uploads/posts/2021-03/1616609828_38-p-trendi-v-interere-41.jpg',
    'https://dekormyhome.ru/wp-content/uploads/2019/10/07-26.jpg',
]


async def download(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                content = await response.read()
    dir_name = 'async'
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    filename = dir_name + '/' + url.split('/')[-1]
    async with aiofiles.open(filename, 'wb') as f:
        await f.write(content)
    print(f"Downloaded {url} in {time.time() - start_time:.2f} seconds")


folder = 'async'
start_time = time.time()


async def main():
    tasks = []
    for url in urls:
        task = asyncio.create_task(download(url))
        tasks.append(task)
    # запустить одновременно все задачи из tasks
    await asyncio.gather(*tasks)
    print(f"Посчитано за {time.time() - start_time} секунд")


if __name__ == '__main__':
    asyncio.run(main())
