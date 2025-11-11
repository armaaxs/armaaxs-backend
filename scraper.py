from spotify_scraper import SpotifyClient
def convert_ms_to_minute(ms):
    # print(type(ms))
    if type(ms) is  int or ms is float:
        # print (True)
        s=ms/1000
        return f"{int(round(s/60))} minutes, {int(round(s%60))} seconds"
    else:
        # print(False)
        return 0
def playlist_scraper(playlist_URL):
    client= SpotifyClient()
    playlist = client.get_playlist_info(playlist_URL)
    print(playlist)
    playlist_name=playlist.get('name', 'Unknown')
    playlist_owner=playlist.get('owner', {}).get('name', playlist.get('owner', {}).get('id', 'Unknown'))
    playlist_count=playlist.get('track_count', 0)
    playlist_cover=''
    print('IMAGES:', playlist.get('images', []))
    if playlist.get('images', []):
        print('EXECUTED')
        for image in playlist.get('images', []):
            if image['height']==300:
                playlist_cover=image['url']
        if not playlist_cover:
            playlist_cover=playlist.get('images', {})[0]['url']
        print(playlist_cover)
    else:
        playlist_cover=''
    # print(f"Playlist: {playlist_name}")
    # print(f"Owner: {playlist_owner}")
    # print(f"Tracks: {playlist_count}")
    # print(f"Followers: {playlist.get('followers', {}).get('total', 'N/A'):,}")


    # Get all tracks
    # print(playlist)

    filtered_playlist=[]
    # TAKING WHATS NEEDED, TO RETURN
    # EACH SONG IS A LIST OF DICTS(TRACK) CONTAINING KEYS-name="", artists={'',''...}, duration= 0
    print('TRACKS IN PLAYLIST: \n')
    for track in playlist['tracks']:
        track_name=track.get('name', 'Unknown')
        track_artists=track.get('artists')
        artists=[]
        for i,artist in enumerate(track_artists):
            artists.append(artist['name'])
        filtered_playlist.append({'Name':track_name,"Artists":artists,"Duration":convert_ms_to_minute(int(track.get("duration_ms","Unknown"))), "Duration_ms":track.get("duration_ms","Unknown")})
        print(f"  - {track.get('name', 'Unknown')} by {(track.get('artists', [{}])[0].get('name', 'Unknown') if track.get('artists')[0] else 'Unknown')}")

    return {'playlist_name':playlist_name,
            'playlist_owner':playlist_owner,
            'playlist_count':playlist_count,
            'playlist_url':playlist_URL,
            'playlist_cover':playlist_cover,
            'tracks':filtered_playlist
            }
# playlist_scraper('https://open.spotify.com/playlist/5EN7iSaC6eVZajdwLC4WOk?si=cfa8bb07d15a4417')