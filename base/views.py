from django.shortcuts import render
from django.http import JsonResponse
import random
import time
from agora_token_builder import RtcTokenBuilder
from .models import RoomMemeber , Room
import json
from django.views.decorators.csrf import csrf_exempt


def getToken(request):
    appId = 'f23030188c0d4de3b69056854f7079c7'
    appCertificate = 'f2f0e4a220c04e4c8a8ad3cb25e3cf42'
    channelName = request.GET.get('channel')
    uid = random.randint(1,230)
    expirationTimeInSeconds = 3600 * 24
    currentTimeStamp = time.time()
    role = 1
    privilegeExpiredTs = currentTimeStamp + expirationTimeInSeconds
    token = RtcTokenBuilder.buildTokenWithUid(appId, appCertificate, channelName, uid, role, privilegeExpiredTs)
    return JsonResponse({'token': token , 'uid':uid },safe=False)





def lobby(request):

    return render(request, "base/lobby.html")

def room(request):

    return render(request, "base/room.html")

@csrf_exempt
def createMember(request):
    data = json.loads(request.body)
    # Safely get is_public, default to True if not provided
    is_public = data.get('is_public', True)
    # If coming as string (from JS), convert to boolean
    if isinstance(is_public, str):
        is_public = is_public == 'True'

    # Get or create the Room instance
    room, createdd = Room.objects.get_or_create(
        room_name=data['room_name'],
        defaults={
            'description': data.get('description', ''),
            'is_public': is_public,
        }
    )
    room.total_count += 1
    room.save()
    # Create or get the RoomMemeber, using the Room instance for ForeignKey
    member, created = RoomMemeber.objects.get_or_create(
        name=data['name'],
        uid=data['UID'],
        room_name=room  # Use the Room instance, not room_name string
    )
    if createdd:
        room.owner = member
        room.save()
    return JsonResponse({'name': data['name']}, safe=False)




def getMember(request):
    uid = request.GET.get('UID')
    room_name = request.GET.get('room_name')

    member = RoomMemeber.objects.get(
        uid=uid,
        room_name=room_name,
    )
    name = member.name
    return JsonResponse({'name':member.name}, safe=False)

@csrf_exempt
def deleteMember(request):
    data = json.loads(request.body)
    member = RoomMemeber.objects.get(
        name=data['name'],
        uid=data['UID'],
        room_name=data['room_name']
    )
    member.delete()
    room = Room.objects.get(room_name=data['room_name'])
    room.total_count = max(0, room.total_count - 1)
    room.save()
    return JsonResponse('Member deleted', safe=False)


def public_rooms(request):
    rooms = Room.objects.filter(is_public=True)
    return render(request, 'base/public_rooms.html', {'rooms': rooms})