from django.urls import path
from base.views import *

urlpatterns = [
    path("", home , name="home"),
    path("room/<int:pk>", room , name="room")
]