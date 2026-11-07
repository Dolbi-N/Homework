import aiohttp
import asyncio

url = 'https://jsonplaceholder.typicode.com/posts'


async def fetch_data(session, post_id):

    async with session.get(f'{url}/{post_id}') as response:
        response.raise_for_status()
        return await response.json()


async def main():

    async with aiohttp.ClientSession() as session:

        tasks = [
            fetch_data(session, i)
            for i in range(1, 21)
        ]

        responses = await asyncio.gather(*tasks)

        filtered_posts = [
            post for post in responses
            if post['userId'] == 1
        ]

        print("Posts with userId = 1:")
        print("-" * 40)

        for post in filtered_posts:
            print(post['title'])


if __name__ == '__main__':
    asyncio.run(main())
