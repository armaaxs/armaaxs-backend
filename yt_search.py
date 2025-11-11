import yt_dlp

def youtube_search(query, limit=3):
    ydl_opts = {
        "quiet": True,                 # no output spam
        "skip_download": True,         # we only want search results
        "extract_flat": True,          # no extra details, just URLs
        "default_search": "ytsearch",  # search instead of direct URL
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        search_query = f"ytsearch{limit}:{query}"
        info = ydl.extract_info(search_query, download=False)
        # print(info)
        return [entry["url"] for entry in info.get("entries", [])]

