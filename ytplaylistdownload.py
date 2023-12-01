from pytube import Playlist
from sys import argv

link = argv[1]

p = Playlist(link)

for video in p.videos:
    yt=video.streams.get_highest_resolution()
    yt.download("C:/Users/HP/Downloads")
    print(f"Downloaded {video.title}")

