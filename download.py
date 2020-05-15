from pytube import YouTube
import os
import time
from moviepy.editor import VideoFileClip
import eyed3
import requests
import files

special_char = "~#%&{*}\\:<>?/+|\""

def mp3(URL):
    video = YouTube(URL)
    stream = video.streams.get_lowest_resolution()

    stream.download(os.getcwd()+"/tmp",filename="video")

    audio = VideoFileClip(os.getcwd()+"/tmp/"+"video.mp4")
    audio.audio.write_audiofile(os.getcwd()+"/tmp/"+"audio.mp3")
    audio.close()

    os.rename(os.getcwd()+"/tmp/"+"audio.mp3",os.getcwd()+"/tmp/"+ stream.default_filename[:-4] +".mp3")
    
    audio = eyed3.load("tmp/"+ stream.default_filename[:-4] +".mp3")
    if (audio.tag == None):
        audio.initTag()

    thumb = video.thumbnail_url
    thumb = requests.get(thumb)
    with open("tmp/cover.jpg", "wb") as f:
        f.write(thumb.content)


    audio.tag.images.set(3, open('./tmp/cover.jpg','rb').read(), 'image/jpeg')
    print("writting Data...")
    audio.tag.save()

    
    os.rename(os.getcwd()+"/tmp/"+ stream.default_filename[:-4] +".mp3",os.getcwd()+"/mp3/"+ stream.default_filename[:-4] +".mp3")
