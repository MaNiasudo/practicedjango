from django.shortcuts import render
from base.models import *

def home(request):
    rooms = Room.objects.all()
    context = {'rooms':rooms}

    return render(request, 'index/home.html' , context )

def room(request,pk):
    room = Room.objects.get(id=pk)
    messages = Message.objects.filter(room=room).order_by('updated')
    context = {
        'room':room , 
        'messages':messages
        }
    return render(request , 'index/room.html' , context)

