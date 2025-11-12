from os.path import exists

from fastapi import FastAPI,BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from spotify_scraper.core.types import TrackData
from track_downloader import download_track_from_yt, download_playlist
from scraper import playlist_scraper
from yt_search import youtube_search
from tempfile import TemporaryFile
from file_cleaner import delete_file
api = FastAPI()
# Configure CORS
api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Next.js dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
#GET, POST, PUT, DELETE
linky='https://open.spotify.com/playlist/07er8cd8GSKhYywUWcYK62?si=182cf45991b8450b'
@api.get('/')
def index():
    return {'message': 'Hello World'}

# @api.get('/playlist/{playlist_url}')
# def get_data(playlist_url):
#     print('HI')
#     print('playlist_url', playlist_url)       CANNOT ACCEPT URL AS PATH PARAMETER
#     try:
#         playlistJSON = playlist_scraper(playlist_url)
#     except:
#         playlistJSON={'ERROR'}
#     return playlistJSON

@api.get('/playlist')
def get_spotify_playlist(url=''):
    if url:
        print(url)
        try:
            playlistJSON = playlist_scraper(url)
        except:
            playlistJSON={'ERROR'}
        return playlistJSON
    else:
        return{'No url mentioned'}
@api.get('/track/{yt_search_string}')
def get_yt_url(yt_search_string):
    print(yt_search_string)
    return youtube_search(yt_search_string)

@api.post('/download')
def download_song(track:dict,background_tasks:BackgroundTasks):
    print(track)
    if  'playlist_name' not in track:  # IF ITS A TRACK INSTEAD OF A PLAYLIST
        track_name = track['Name']
        artist_string = track['Artists'][0] + (track['Artists'][1] if len(track['Artists']) > 1 else "")
        query = track_name + '-' + artist_string
        background_tasks.add_task(delete_file,query+'.mp3',type='file')  # NAME OF SAVED FILE ON DISK
        return download_track_from_yt(track)
    else:
        tracks=track['tracks']
        background_tasks.add_task(delete_file, track['playlist_name'], type='')
        background_tasks.add_task(delete_file, track['playlist_name']+'.zip', type='')
        return download_playlist(tracks, track['playlist_name'])

