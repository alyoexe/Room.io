from django.db import models

# Create your models here.


    

class Room(models.Model):
    room_name = models.CharField(max_length=100, unique=True, primary_key=True)  # Unique room identifier      # Human-friendly name
    description = models.TextField(blank=True)                 # Room description
    is_public = models.BooleanField(default=True)              # Public/private flag
    created_at = models.DateTimeField(auto_now_add=True)       # Creation timestamp
    total_count = models.PositiveIntegerField(default=0)     # Number of users (update as needed)
    owner = models.ForeignKey('RoomMemeber', on_delete=models.SET_NULL, null=True, blank=True,related_name='owned_rooms')  # Room creator
    def __str__(self):
        return self.room_name
    
class RoomMemeber(models.Model):
    room_name = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='members')
    uid = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    joined_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name