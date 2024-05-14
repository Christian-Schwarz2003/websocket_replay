import asyncio
import os
import time

import websockets
from wakepy import keep


async def send_heartbeat(websocket):
    while True:
        await websocket.send("heartbeat")
        await asyncio.sleep(300)  # Send heartbeat every 5 minutes


async def handle_connection(websocket, path, name):
    print(name, "Connected!")
    if not os.path.exists('recordings'):
        os.makedirs('recordings')
    outFileName = f"recordings/recording_{time.time()}.csv"
    with open(outFileName, "w") as f:
        async for message in websocket:
            print(name, f"Received: {message}")  # Print the received message
            f.writelines([f"{time.time()},{message}\n"])


async def main(link, heartbeat, name=""):
    try:
        async with websockets.connect(link) as websocket:
            if heartbeat:
                heartbeat_task = asyncio.create_task(send_heartbeat(websocket))
                await asyncio.gather(handle_connection(websocket, "", name), heartbeat_task)
            else:
                await handle_connection(websocket, "", name)  # No path needed for client
    except websockets.ConnectionClosed as e:
        print(name, f'Terminated', e)


if __name__ == "__main__":
    with keep.presenting():
        link = input("what websocket: ")
        heartbeatRes = input("5 min heartbeat (Y/n): ")
        heartbeat = heartbeatRes == "Y" or heartbeatRes == "y"
        if len(link) < 1:
            link = "ws://localhost:8765"
        asyncio.run(main(link, heartbeat))
