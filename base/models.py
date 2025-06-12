from django.db import models

# Create your models here.

class RoomMemeber(models.Model):
    room_name = models.CharField(max_length=100)
    uid = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    joined_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name