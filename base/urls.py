from django.urls import path, include
from . import views
urlpatterns = [
    path("", views.lobby, name="lobby"),
    path("room/", views.room, name="room"),
    path("getToken/", views.getToken, name="getToken"),

]