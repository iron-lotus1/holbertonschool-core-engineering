#!/usr/bin/env python3

import asyncio
import websockets
from websockets import ConnectionClosed


connected_clients = set()


async def handler(websocket):
    connected_clients.add(websocket)

    try:
        async for message in websocket:
            await broadcast("B:{0}".format(message))

    finally:
        connected_clients.remove(websocket)


async def broadcast(message):
    for websocket in connected_clients.copy():
        try:
            await websocket.send(message)
        except ConnectionClosed:
            connected_clients.remove(websocket)


async def main():
    async with websockets.serve(handler, "127.0.0.1", 8765):
        await broadcast()

if __name__ == "__main__":
    asyncio.run(main())
