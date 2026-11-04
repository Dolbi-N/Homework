# ##############
# Task 1
# ##############

import multiprocessing
import time
import threading
import requests
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor


def calculate_factorial_part(numbers):
    result = 1

    for number in numbers:
        result *= number

    return result


if __name__ == '__main__':

    n = 100000

    # Single Process
    start = time.time()

    single_factorial = calculate_factorial_part(range(1, n + 1))

    end = time.time()
    single_time = end - start

    print(f"Single-process time: {single_time:.4f} seconds")


    # Multiprocessing
    start = time.time()

    numbers = list(range(1, n + 1))

    chunks = [
        numbers[i::4]
        for i in range(4)
    ]

    with ProcessPoolExecutor(max_workers=4) as executor:
        results = list(executor.map(calculate_factorial_part, chunks))

    factorial = 1

    for result in results:
        factorial *= result

    end = time.time()
    multi_time = end - start

    print(f"Multiprocessing time: {multi_time:.4f} seconds")

    print(f"Results are equal: {factorial == single_factorial}")


# #########
# Task2
# #########


def get_post(post_id):
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"

    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()

        data = response.json()
        print(f"Post {post_id}: {data['title']}")

    except requests.exceptions.RequestException as e:
        print(f"Post {post_id} failed: {e}")


threads = []

start = time.time()

for i in range(1, 101):
    thread = threading.Thread(target=get_post, args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

end = time.time()

print(f"\nTotal execution time: {end - start:.4f} seconds")


# #############
# Task3
# #############

def get_post(post_id):
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"

    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()

        data = response.json()
        print(f"Post {post_id}: {data['title']}")

    except requests.exceptions.RequestException as e:
        print(f"Post {post_id} failed: {e}")


start = time.time()

with ThreadPoolExecutor(max_workers=10) as executor:
    results = list(executor.map(get_post, range(1, 101)))

end = time.time()

print(f"\nTotal execution time: {end - start:.4f} seconds")