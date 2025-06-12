from django.shortcuts import render
from agora_token_builder import RtcTokenBuilder
from django.http import JsonResponse
import random
import time
# Create your views here.


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