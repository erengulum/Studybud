from django.shortcuts import render, redirect
from .models import Room
from .forms import RoomForm


# Create your views here.
def home(request):
    rooms = Room.objects.all()
    context = {'rooms':rooms} #we put our parameters into a dictionary
    return render(request,'base/home.html', context)

def room(request,pk):
    room = Room.objects.get(id=pk);
    
    context = {'room':room}

    return  render(request,'base/room.html',context)



def createRoom(request):
    form = RoomForm()

    if request.method=="POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save() #it will automatically save the model in DB
            return redirect('home') #we use name value of url here

    context = {'form':form}
    return render(request, 'base/room_form.html',context)



def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room) #pre filled with the room that given by id

    if request.method=="POST":
        form = RoomForm(request.POST,instance=room)
        if form.is_valid:
            form.save()
            return redirect("home")

    context = {'form': form}
    return render(request, 'base/room_form.html',context)


def deleteRoom(request,pk):
    room = Room.objects.get(id=pk)

    if request.method=="POST":
        room.delete()
        return redirect('home')

    return render(request, "base/delete.html",{'obj':room})