import asyncio
import time

import websockets


async def handle_connection(websocket, path):
    outFileName = f"recording_{time.time()}.csv"
    with open(outFileName, "w") as f:
        async for message in websocket:
            print(f"Received: {message}")  # Print the received message
            f.writelines([f"{time.time()},{message}\n"])


async def main(link):
    async with websockets.connect(link) as websocket:
        await handle_connection(websocket, path="")  # No path needed for client


if __name__ == "__main__":

    link = input("what websocket")
    if len(link) < 1:
        link = "ws://localhost:8765"
    asyncio.run(main(link))
