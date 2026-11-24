#!/usr/bin/env python3


from starlette.applications import Starlette
from starlette.responses import HTMLResponse
from starlette.routing import Route, WebSocketRoute


async def homepage(request):
    return HTMLResponse("<h1>WebSocket Echo</h1>")


async def websocket_endpoint(websocket):
    await websocket.accept()

    try:
        while True:
            message = await websocket.receive_text()
            await websocket.send_text(message)

    except Exception:
        pass

app = Starlette(routes=[
    Route("/", homepage),
    WebSocketRoute("/ws", websocket_endpoint),
])
