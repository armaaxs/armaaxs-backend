import sys
from yt_search import youtube_search
from scraper import playlist_scraper
import yt_dlp

##TAKE INPUT
if len(sys.argv)>1:
    playlist_url= sys.argv[1]
else:
    playlist_url=input('ENTER PLAYLIST URL: ')
##
playlist = playlist_scraper(playlist_url)



yt_urls=[] #  [{name: ,url:}...]
for song in playlist['tracks']:
    try:
        name=song['Name']
        # artists_str = f"{song['Art
        # Lists'][0]}"+f"{' and'+song['Artists'][1] if song['Artists'][1] else ''}"
        artists_str=song['Artists'][0]
        query=name+'-'+artists_str
        results=youtube_search(query)
    except Exception as error:
        print('Warning')

    # print(dir(results))
    print(f'NOW DOWNLOADING: {query}')
    song['yt_url']=results[0]
    url=song['yt_url']
    options = {
        'quiet':True,
        'format': 'bestaudio/best',
        'extract_audio': True,
        'audio_format': 'mp3',  # convert to mp3 using FFmpeg
        'outtmpl': f"./{playlist['playlist_name']}-{playlist['playlist_owner']}/{query}.%(ext)s",
        'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'postprocessors_args':['-loglevel', 'quiet', '-hide_banner'] #NO FFMPEG OUTPUT, (not working)
    }
    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([url])
    print('DOWNLOAD COMPLETE')
