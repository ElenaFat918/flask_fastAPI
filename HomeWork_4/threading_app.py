import requests
import threading
import os
import time


urls = [
    'https://mykaleidoscope.ru/uploads/posts/2021-03/1616732502_43-p-kvartirnii-interer-46.jpg',
    'https://mykaleidoscope.ru/uploads/posts/2021-03/1616609828_38-p-trendi-v-interere-41.jpg',
    'https://dekormyhome.ru/wp-content/uploads/2019/10/07-26.jpg',
]


def download(url):
    response = requests.get(url).content
    dir_name = 'thread'
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    filename = dir_name + '/' + url.split('/')[-1]
    with open(filename, 'wb') as f:
        f.write(response)
    print(f"Downloaded {url} in {time.time() - start_time:.2f} seconds")


threads = []
start_time = time.time()

for url in urls:
    thread = threading.Thread(target=download, args=[url])
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
