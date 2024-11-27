from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def blogs(request):
    return HttpResponse("Welcome to blogs lets see what we have")

def blogsingle(request):
    return HttpResponse("This is blog single")