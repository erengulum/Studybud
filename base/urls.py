
from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("room/<str:id>/",views.room,name="room"),  #name is not necessary but it is important. Even though you can path, if the name stays same then there won't be any problem on other py files
    

]
