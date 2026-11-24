#!/usr/bin/env python3

import asyncio
import websockets


connected_clients = set()


async def handler(websocket):
    connected_clients.add(websocket)

    try:
        async for m in websocket:
            await websocket.send("U:{}".format(m))

    finally:
        connected_clients.remove(websocket)


async def main():
    async with websockets.serve(handler, "127.0.0.1", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
