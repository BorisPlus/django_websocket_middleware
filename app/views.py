from django.views.generic.base import TemplateView
from ws.connection import WebSocket


class IndexView(TemplateView):
    template_name = "index.html"


# async def websocket_view(socket):
#     await socket.accept()
#     await socket.send_text('hello')
#     await socket.close()


# async def websocket_view(socket: WebSocket):
async def websocket_view(socket: WebSocket):
    await socket.accept()
    while True:
        message = await socket.receive_text()
        await socket.send_text(f'Server answer to message: {message}')
