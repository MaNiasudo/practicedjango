from django.shortcuts import render
from base.models import *

def home(request):
    rooms = Room.objects.all()
    context = {'rooms':rooms}

    return render(request, 'index/home.html' , context )

def room(request,pk):
    room = Room.objects.get(id=pk)
    message = Message.objects.filter()
    context = {'room':room}
    return render(request , 'index/room.html' , context)

