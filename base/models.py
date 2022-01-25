from statistics import mode
from django.db import models
from django.contrib.auth.models import User
# Create your models here.




class Topic(models.Model):
    name = models.CharField(max_length=200)


    def __str__(self):
        return self.name




class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL,null=True) #one to many
    topic = models.ForeignKey(Topic,on_delete=models.SET_NULL,null=True) #one to many
    name = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True) #null=True can't be empty
    #participants
    updated = models.DateTimeField(auto_now=True) #snaphost of the item ->timestamp
    created = models.DateTimeField(auto_now_add=True) #initial time stamp. 


    def __str__(self):
        return self.name


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True) #snaphost of the item ->timestamp
    created = models.DateTimeField(auto_now_add=True) #initial time stamp. 


    def __str__(self):
        return self.body[0:50] #return first 50 char of the long message bodies
