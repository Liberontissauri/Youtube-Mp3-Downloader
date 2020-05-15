import download as dw
import files
from pytube import Playlist

print("-"*30)
print("Youtube Audio Downloader")
print("-"*30)
URL = str(input("Type the URL of the video/playlist: "))
print("-"*30)
print("")
print("Creating Folder structure if not existent...")
files.create_folder_structure()
print("Folder Structure Ready!!")
print("")

if "playlist" in URL:

    playlist = Playlist(URL)
    playlist = playlist.populate_video_urls()
    
    for url in playlist:
        dw.mp3(url)

else:
    dw.mp3(URL)

files.deletetmpfiles()