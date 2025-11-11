# 🎵 Downloadify

**Downloadify** is a powerful, lightweight CLI tool that lets you download songs or playlists directly from Spotify using a URL or name. It’s perfect for users who want to archive, organize, or listen offline — without needing the Spotify app.

---

## 🚀 Features

- 🔍 Search and download by **Spotify URL** or **track/playlist name**
- 🎧 Supports individual tracks, albums, and entire playlists
- 🧠 Intelligent metadata tagging (title, artist, album, cover art)
- 💽 Output as high-quality MP3 (configurable bitrate)
- 📁 Custom output templates for file naming and folder organization
- ⚡ Fast and minimal — perfect for power users and scripts

---

## 📦 Installation

Make sure you have **Python 3.7+** and **FFmpeg** installed.

```bash
git clone https://github.com/yourusername/downloadify.git
cd downloadify
pip install -r requirements.txt
Or install globally:
```
```bash
pip install git+https://github.com/yourusername/downloadify
```
## 🛠️ Usage
Basic Usage
```bash
downloadify "https://open.spotify.com/track/4uLU6hMCjMI75M1A2tKUQC"   
```
Or by name:
```bash
Copy
Edit
downloadify "Bohemian Rhapsody by Queen"
```
```bash
Download a Playlist
bash
Copy
Edit
downloadify "https://open.spotify.com/playlist/37i9dQZF1DXcBWIGoYBM5M"
```
Options
bash
Copy
Edit
downloadify [OPTIONS] <query or URL>
Option	Description
--format mp3	Output format (mp3, wav, etc.)
--bitrate 192	Set audio bitrate (default: 192kbps)
--output "%(title)s"	Custom output filename template
--no-metadata	Skip metadata tagging
--dry-run	Show what will be downloaded without downloading
--help	Show help message

🧩 How It Works
Downloadify uses the Spotify Web API to fetch metadata and then searches YouTube (or another backend) for matching audio. Once found, it downloads the best-quality audio stream and converts it to MP3 using FFmpeg.

📝 Output Template Variables
You can customize filenames using template keys like:

%(title)s – Track title

%(artist)s – Artist name

%(album)s – Album name

%(ext)s – File extension

%(track_number)s – Track number in album/playlist

Example:

bash
Copy
Edit
--output "downloads/%(artist)s - %(title)s.%(ext)s"
🔧 Requirements
Python 3.7+

FFmpeg (must be in your system PATH)

yt-dlp (installed via requirements)

📚 License
MIT License

🙌 Contributing
Pull requests are welcome! Please open an issue first to discuss any major changes. Bug reports, feature requests, and improvement ideas are appreciated.

📫 Contact
Made with ❤️ by YourName
Issues or suggestions? Open an issue

yaml
Copy
Edit

---

Would you like me to generate this as a downloadable file for you (`README.md`), or edi