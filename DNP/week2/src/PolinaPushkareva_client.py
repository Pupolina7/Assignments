import os
import socket
import time
import threading
from multiprocessing import Pool, cpu_count

SERVER_URL = '127.0.0.1:12345'
CLIENT_BUFFER = 1024
UNSORTED_FILES_COUNT = 100


def create_directories():
    if not os.path.exists('unsorted_files'):
        os.mkdir('unsorted_files')

    if not os.path.exists('sorted_files'):
        os.mkdir('sorted_files')


def download_unsorted_files(i):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            ip, port = SERVER_URL.split(':')
            s.connect((ip, int(port)))
            file = b''
            while True:
                packet = s.recv(CLIENT_BUFFER)
                if not packet:
                    break
                file += packet
            with open(f'unsorted_files/{i}.txt', 'wb') as f:
                f.write(file)
    except Exception as e:
        print(f"Error downloading file {i}: {e}")


def optimize_unsorted_download():
    threads = []  # Create an empty list to keep track of threads
    for file_id in range(UNSORTED_FILES_COUNT):
        thread = threading.Thread(target=download_unsorted_files, args=(file_id,))
        threads.append(thread)  # Add the thread to the list
        thread.start()

    for t in threads:
        t.join()


def create_sorted_file(unsorted_id):
    with open(f"unsorted_files/{unsorted_id}.txt", "r") as unsorted_file:
        unsorted_list = [int(number)
                         for number in unsorted_file.read().split(',')]

        sorted_list = sorted(unsorted_list)

        with open(f"sorted_files/{unsorted_id}.txt", "w") as sorted_file:
            sorted_file.write(','.join(map(str, sorted_list)))


def optimize_sorted_create():
    with Pool(processes=min(UNSORTED_FILES_COUNT, cpu_count())) as pool:
        pool.map(create_sorted_file, range(UNSORTED_FILES_COUNT))


if __name__ == '__main__':
    create_directories()
    tdownload0 = time.monotonic()
    optimize_unsorted_download()
    tdownload = time.monotonic() - tdownload0
    print(f"Files download time: {tdownload}")
    tsort0 = time.monotonic()
    optimize_sorted_create()
    tsort = time.monotonic() - tsort0
    print(f"Sorting time: {tsort}")
