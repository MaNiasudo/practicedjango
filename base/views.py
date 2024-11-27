from django.shortcuts import render

def home(request):
    return render(request, 'index/home.html' )

def room(request):
    return render(request , 'index/room.html')

