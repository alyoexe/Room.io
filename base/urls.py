from django.urls import path, include
from . import views
urlpatterns = [
    path("", views.lobby, name="lobby"),
    path("room/", views.room, name="room"),
    path("getToken/", views.getToken, name="getToken"),
    path('create_member/', views.createMember, name='create_member'),
    path('get_member/', views.getMember, name='get_member'),



]