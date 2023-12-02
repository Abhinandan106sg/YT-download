from pytube import Playlist
from sys import argv
import time

def progress(streams, chunk: bytes, bytes_remaining: int):
    contentsize = high_def_video.filesize
    size = contentsize - bytes_remaining

    print('\r' + '[Download progress]:[%s%s]%.2f%%;' % (
    '█' * int(size*20/contentsize), ' '*(20-int(size*20/contentsize)), float(size/contentsize*100)), end='')

link = argv[1]

download_path = "C:/Users/HP/Downloads"

p = Playlist(link)

print(f"Title : {p.title}")
for video in p.videos:
    print(f"video title : {video.title}")
    video.register_on_progress_callback(progress)
    high_def_video = video.streams.get_highest_resolution()
    high_def_video.download(output_path=download_path)
    print(f"{video.title} downloaded successfully")

