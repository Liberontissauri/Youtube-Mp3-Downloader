import download as dw
from pytube import Playlist

print("-"*30)
print("Youtube Audio Downloader")
print("-"*30)
URL = str(input("Type the URL of the video/playlist: "))
print("-"*30)

if "playlist" in URL:

    playlist = Playlist(URL)
    playlist = playlist.populate_video_urls()
    
    for url in playlist:
        dw.mp3(url)

else:
    dw.mp3(URL)