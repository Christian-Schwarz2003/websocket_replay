import asyncio

from wakepy import keep

import receive


async def main(link):
    tasks = []
    tasks.append(asyncio.create_task(receive.main(link, False, "1")))
    tasks.append(asyncio.create_task(receive.main(link, True, "2")))
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    with keep.presenting():
        link = input("what websocket: ")
        if len(link) < 1:
            link = "ws://localhost:8765"
        asyncio.run(main(link))
