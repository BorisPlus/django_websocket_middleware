from django.urls import resolve
from .connection import WebSocket


def websockets(app):
    async def asgi(scope, receive, send):
        if scope["type"] == "websocket":
            print(scope)
            # match = resolve(scope["raw_path"])
            match = resolve(scope["path"])
            await match.func(WebSocket(scope, receive, send), *match.args, **match.kwargs)
            return

        await app(scope, receive, send)
    return asgi
