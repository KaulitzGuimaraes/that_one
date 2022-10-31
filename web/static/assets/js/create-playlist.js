
document.getElementById("createPlaylist").addEventListener("click",
async () => {
    document.getElementById("embededPlaylistDiv").style = ""
    let track_name = document.getElementById("trackName").value;
    let artist = document.getElementById("artist").value;
    console.log(track_name)
    console.log(artist)
    let url = '/playlists' + '?' + (new URLSearchParams({
                "track_name": track_name,
                "artist": artist
            })).toString();
    const fetchPromise = fetch(url,
        {
            method: 'GET',
        });
    await fetchPromise.then(response => {
        console.log(response);
    })
    await fetchPromise.then((response => response.json())).then(
        (responseJSON) =>{
           document.getElementById("embededPlaylist").src =`https://open.spotify.com/embed/playlist/${responseJSON['id']}?utm_source=generator&theme=0`
           document.getElementById("embededPlaylistDiv").style = ""
        }
    )
}
    );