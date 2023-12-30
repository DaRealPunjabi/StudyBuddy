from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'home.html')
#    return HttpResponse('Home Page')

def room(request):
    return render(request, 'room.html')
#    return HttpResponse('Room')