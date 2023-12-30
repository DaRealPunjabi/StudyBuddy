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

def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = {'room': room}        
    return render(request, 'base/room.html', context)
#    return HttpResponse('Room')

