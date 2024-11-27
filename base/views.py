from django.shortcuts import render
from base.models import *

def home(request):
    return render(request, 'index/home.html' )

def room(request):
    rooms = Room.objects.all()
    context = {'rooms':rooms}
    return render(request , 'index/room.html' , context)

