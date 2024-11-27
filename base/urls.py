from django.urls import path
from base.views import *

urlpatterns = [
    path("", home , name="home"),
    path("room/", room , name="room")
]