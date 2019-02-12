from __future__ import unicode_literals
import youtube_dl
from youtube_dl import YoutubeDL
from subprocess import call

ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '128',
        }],
    }
ch=input("Is the file in location where you want to donwload(Y/N)")
if ch == 'Y' or 'y' or 'yes':
    video=input("Enter link to dowload")
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video])
else:
    print("Please put in the directory where you want to donwload the files")