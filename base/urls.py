from django.urls import path
from base.views import *

urlpatterns = [
    path("", home , name="home"),
    path("room/<int:pk>", room , name="room"),
    path("create-room/", create_room ,name="create-room" ),
    path("send-message/",send_message ,name='send-message')
]