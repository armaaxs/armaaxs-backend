import os
import stat
import time
import shutil
import zipstream
from starlette.responses import StreamingResponse, FileResponse

from yt_search import youtube_search
from scraper import playlist_scraper
from tempfile import NamedTemporaryFile, TemporaryDirectory
import yt_dlp
from zipstream import ZipFile



def download_track_from_yt(track, folder='.'):
    print(track)
    track_name=track['Name']
    artist_string=track['Artists'][0]+(track['Artists'][1] if len(track['Artists'])>1 else "")
    query = track_name + '-' + artist_string
    results=youtube_search(query)
    filename=f'{query}.mp3'
    print(results)
    print('-----------------------------------')
    options = {
        'quiet': True,
        'format': 'bestaudio/best',
        'extract_audio': True,
        'audio_format': 'mp3',  # convert to mp3 using FFmpeg
        'outtmpl': f'{folder}\\{query}.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192'
        }]
    }
    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([results[0]])
    return FileResponse(f'{folder}\\{query}.mp3', media_type='audio/mp3')

def download_playlist(tracks, relative_file_path):
    folder_path=relative_file_path
    os.makedirs(folder_path, exist_ok=True)

    for track in tracks:
        track_name = track['Name']
        artist_string = track['Artists'][0] + (track['Artists'][1] if len(track['Artists']) > 1 else "")
        query = track_name + '-' + artist_string
        download_track_from_yt(track,folder_path)
    shutil.make_archive(folder_path, 'zip', folder_path)
    return FileResponse(f'{folder_path}.zip', media_type='application/zip')







# Create generator
# gen = generate_zip_stream([{'Name': 'GLIMPSE OF US', 'Artists': ['Joji'], 'Duration': '3 minutes, 54 seconds', 'Duration_ms': 174357}])
# # Actually run it by iterating
# for chunk in gen:
#     print(f"Chunk size: {chunk} bytes")

# download_track_from_yt({'Name': 'GLIMPSE OF US', 'Artists': ['Joji'], 'Duration': '3 minutes, 54 seconds', 'Duration_ms': 174357})
# download_track_from_yt({'Name': 'GLIMPSE OF US', 'Artists': ['Joji'], 'Duration': '3 minutes, 54 seconds', 'Duration_ms': 174357})



# ##TAKE INPUT
# if len(sys.argv)>1:
#     playlist_url= sys.argv[1]
# else:
#     playlist_url=input('ENTER PLAYLIST URL: ')
# ##
    # playlist = playlist_scraper(playlist_url)
#
#
#
# yt_urls=[] #  [{name: ,url:}...]
# for song in playlist['tracks']:
#     try:
#         name=song['Name']
#         # artists_str = f"{song['Art
#         # Lists'][0]}"+f"{' and'+song['Artists'][1] if song['Artists'][1] else ''}"
#         artists_str=song['Artists'][0]
#         query=name+'-'+artists_str
#         results=youtube_search(query)
#     except Exception as error:
#         print('Warning')
#
#     # print(dir(results))
#     print(f'NOW DOWNLOADING: {query}')
#     song['yt_url']=results[0]
#     url=song['yt_url']
#     options = {
#         'quiet':True,
#         'format': 'bestaudio/best',
#         'extract_audio': True,
#         'audio_format': 'mp3',  # convert to mp3 using FFmpeg
#         'outtmpl': f"./{playlist['playlist_name']}-{playlist['playlist_owner']}/{query}.%(ext)s",
#         'postprocessors': [{
#         'key': 'FFmpegExtractAudio',
#         'preferredcodec': 'mp3',
#         'preferredquality': '192',
#     }],
#     'postprocessors_args':['-loglevel', 'quiet', '-hide_banner'] #NO FFMPEG OUTPUT, (not working)
#     }
#     with yt_dlp.YoutubeDL(options) as ydl:
#         ydl.download([url])
#     print('DOWNLOAD COMPLETE')
