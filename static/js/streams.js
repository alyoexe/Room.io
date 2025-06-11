const APP_ID = 'f23030188c0d4de3b69056854f7079c7';
const CHANNEL = 'main';
const TOKEN = '007eJxTYJhfvy7RSeHD3IPPgmuXb3zHoK2yk8XY+d52OYPlinYSvicUGNKMjA2MDQwtLJINUkxSUo2TzCwNTM0sTE3SzA3MLZPNJzN4ZjQEMjIs42JkYmSAQBCfhSE3MTOPgQEAuMQcBA==';
let UID;


const client = AgoraRTC.createClient({ mode: 'rtc', codec: 'vp8' })
let localTracks = []
let remoteUsers = {}


let joinAndDisplayLocalStream = async () => {

    client.on('user-published', handleUserJoined)
    UID = await client.join(APP_ID, CHANNEL, TOKEN, null);
    localTracks = await AgoraRTC.createMicrophoneAndCameraTracks();
    let player = `<div class="video-container" id="user-container-${UID}">
                    <div class="username-wrapper"><span class="user-name">User 1</span></div>
                    <div class="video-player" id="user-${UID}"></div>
                  </div>`;
    document.getElementById('video-streams').insertAdjacentHTML('beforeend', player);

    localTracks[1].play(`user-${UID}`);
    await client.publish([ localTracks[0], localTracks[1] ]);

}

let handleUserJoined = async (user, mediaType) => {
    remoteUsers[user.uid] = user
    await client.subscribe(user, mediaType)
    if (mediaType === 'video') {
        let player = document.getElementById('user-container-${user.uid}');
        if (player!= null) {
            player.remove();
        }
        player = `<div class="video-container" id="user-container-${user.uid}">
                    <div class="username-wrapper"><span class="user-name">User ${user.uid}</span></div>
                    <div class="video-player" id="user-${user.uid}"></div>
                  </div>`;
        document.getElementById('video-streams').insertAdjacentHTML('beforeend', player);
        user.videoTrack.play(`user-${user.uid}`);
    }
    if(mediaType=== 'audio') {
        user.audioTrack.play();
    }
    
}
