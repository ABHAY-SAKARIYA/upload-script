const client_id = "9FL2NniMLtVzQAQFV9VO1mMplWaGgXO0";
const client_secret = "cqBoChypSkfOVLshMwhPDQPmcQxxbjPL";
const credentials = btoa(`${client_id}:${client_secret}`);

const getAccessToken = async () => {
    const response = await fetch('https://secure.soundcloud.com/oauth/token', {
        method: 'POST',
        headers: {
            'Accept': 'application/json; charset=utf-8',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': `Basic ${credentials}`,
        },
        body: new URLSearchParams({
            grant_type: 'client_credentials',
        }),
    });

    const data = await response.json()
    console.log(data);
}


const getTrackDetails = async (trackId, token) => {
    const trackUrl = `https://api.soundcloud.com/tracks/${trackId}`;

    const response = await fetch(trackUrl, {
        headers: {
            'Authorization': `OAuth ${token}`,
        },
    });

    const data = await response.json();
    console.log(data.user.subscriptions);
    if (data.streamable) {
        const streamUrl = `${data.stream_url}?client_id=${client_id}`;
        console.log('Stream URL:', streamUrl);
    } else {
        console.log('Track is not streamable');
    }
}


// getAccessToken()
// getTrackDetails("1608721632","2-294530--VhpjB0J48WGOVjSSSr9zLiJ");