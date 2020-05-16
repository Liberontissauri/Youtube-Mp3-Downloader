# Youtube-Mp3-Downloader:
A program that downloads videos/playlists from youtube, converts them to Mp3 and attaches the thumbnails to the album-arts

## Dependencies:
- pytube3
- moviepy
- requests
- eyed3
- os
- time

## Functions:
- download.py - mp3(URL)
  - Downloads the mp3 of a video/all the videos on the playlist.
- files.py - create_folder_structure()
  - Generates the folders needed in order to make the program function correctly.
- files.py - deletetmpfiles()
  - Deletes all files on tmp folder of the program.