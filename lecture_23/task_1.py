import requests
import aiohttp
import asyncio
import time


rick_morty_url = 'https://rickandmortyapi.com/api/character/{id}'


def sync_requests():

    start = time.time()

    results = []

    for i in range(1, 11):
        url = rick_morty_url.format(id=i)

        response = requests.get(url)
        response.raise_for_status()

        results.append(response.json())

    end = time.time()

    print("Synchronous execution:")
    print(f"Total time: {end - start:.2f} seconds")

    return results, end - start


async def fetch_data(session, url):

    async with session.get(url) as response:
        response.raise_for_status()
        return await response.json()


async def async_requests():

    start = time.time()

    async with aiohttp.ClientSession() as session:

        tasks = [
            fetch_data(session, rick_morty_url.format(id=i))
            for i in range(1, 11)
        ]

        results = await asyncio.gather(*tasks)

    end = time.time()

    print("\nAsynchronous execution:")
    print(f"Total time: {end - start:.2f} seconds")

    return results, end - start


async def main():

    sync_results, sync_time = sync_requests()

    async_results, async_time = await async_requests()

    difference = sync_time - async_time

    print("\nComparison:")

    if difference > 0:
        print(f"Asynchronous version was {difference:.2f} seconds faster!")

    elif difference < 0:
        print(f"Synchronous version was {abs(difference):.2f} seconds faster!")

    else:
        print("Both versions took approximately the same time.")


if __name__ == "__main__":
    asyncio.run(main())