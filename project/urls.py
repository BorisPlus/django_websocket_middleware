# project_name/urls.py


from django.urls import path
from ws.urls import websocket
from app import views


urlpatterns = [
    path("", views.IndexView.as_view()),
    websocket("websocket/", views.websocket_view),
]
