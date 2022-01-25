from django.shortcuts import render
from .models import Room



# Create your views here.
def home(request):
    rooms = Room.objects.all()
    context = {'rooms':rooms} #we put our parameters into a dictionary
    return render(request,'base/home.html', context)

def room(request,id):
    room = Room.objects.get(id=id);
    
    context = {'room':room}

    return  render(request,'base/room.html',context)