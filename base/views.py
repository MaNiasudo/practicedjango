from django.shortcuts import render , redirect
from base.models import *
from base.forms import *

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


def create_room(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form':form}
    return render(request, 'index/room_form.html', context)


def send_message(request):
    form = MessageForm()
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form}
    return render(request,'index/send_message.html',context)