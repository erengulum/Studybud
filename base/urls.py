
from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("room/<str:pk>/",views.room,name="room"),  #name is not necessary but it is important. Even though you can path, if the name stays same then there won't be any problem on other py files
    
    path("create-room/",views.createRoom, name="create-room"),
    path("update-room/<str:pk>",views.updateRoom, name="update-room"),
    path("delete-room/<str:pk>",views.deleteRoom, name="delete-room"),


]
