#!/usr/bin/env python3

from pathlib import Path

from starlette.applications import Starlette
from starlette.responses import FileResponse
from starlette.routing import Route, WebSocketRoute
from starlette.websockets import WebSocketDisconnect


BASE_DIR = Path(__file__).resolve().parent


async def homepage(request):
    return FileResponse(BASE_DIR / "index.html")


async def css_file(request):
    return FileResponse(BASE_DIR / "styles.css")


async def javascript_file(request):
    return FileResponse(BASE_DIR / "chat.js")


async def websocket_endpoint(websocket):
    await websocket.accept()

    try:
        while True:
            message = await websocket.receive_text()
            await websocket.send_text(message)

    except WebSocketDisconnect:
        pass


app = Starlette(routes=[
    Route("/", homepage),
    Route("/styles.css", css_file),
    Route("/chat.js", javascript_file),
    WebSocketRoute("/ws", websocket_endpoint),
])
