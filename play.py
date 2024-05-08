import asyncio
from time import sleep

import websockets
import json


def parseJson():
    with open("websocket.json", "r") as f:
        data = json.load(f)
    return data


async def printAndSend(websocket, data):
    await websocket.send(data)
    print(data)


async def handle_connection(websocket):
    data = parseJson()
    for message in data:
        await asyncio.sleep(message['dt'])
        res = message['data']
        await printAndSend(websocket, res)


async def main():
    async with websockets.serve(handle_connection, "localhost", 8765):
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())
