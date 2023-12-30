from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

rooms = [
    {'id':1, 'name':'Lets learn python1!'},
    {'id':2, 'name':'Design with me'},
    {'id':3, 'name':'Frontend developers'},
]

def home(request):
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)
#    return HttpResponse('Home Page')

def room(request):
    return render(request, 'base/room.html')
#    return HttpResponse('Room')