from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import is_valid_path
from django.db.models import Q
from .models import Room, Topic
from .forms import RoomForm

# Create your views here.

rooms = [
    {'id':1, 'name':'Lets learn python1!'},
    {'id':2, 'name':'Design with me'},
    {'id':3, 'name':'Frontend developers'},
]

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    # rooms = Room.objects.filter(
    #     topic__name__icontains=q
    # )

    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
    )


    #rooms = Room.objects.all()

    topics = Topic.objects.all()[0:5]
    room_count = rooms.count()
    context = {'rooms': rooms, 'topics': topics, 'room_count':room_count}
    return render(request, 'base/home.html', context)
#    return HttpResponse('Home Page')

def room(request, pk):
    room = None
    room = Room.objects.get(id=pk)
    # for i in rooms:
    #     if i['id'] == int(pk):
    #         room = i
    context = {'room': room}        
    return render(request, 'base/room.html', context)
#    return HttpResponse('Room')

def createRoom(request):
    form = RoomForm

    if request.method == 'POST':
        print(request.POST)
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/room_form.html', context)

def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/room_form.html', context)

def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)

    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': room})