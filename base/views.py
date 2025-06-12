from django.shortcuts import render
from django.http import JsonResponse
import random
import time
from agora_token_builder import RtcTokenBuilder
from .models import RoomMemeber
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
    member, created = RoomMemeber.objects.get_or_create(
        name=data['name'],
        uid=data['UID'],
        room_name=data['room_name']
    )

    return JsonResponse({'name':data['name']}, safe=False)


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
    return JsonResponse('Member deleted', safe=False)