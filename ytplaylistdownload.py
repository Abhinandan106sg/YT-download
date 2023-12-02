from pytube import Playlist
from sys import argv
from plyer import notification
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
notification.notify(
        title = f"Downloading {(p.title)}",
        app_icon = "C:/Users/HP/OneDrive/Desktop/yt-download/pythonlogoIco.ico"
        timeout = 5
    )

time.sleep(3)

for video in p.videos:
    small_title = (video.title)[:50] if (len(video.title)>50) else video.title
    print(f"Downloading {small_title}")
    notification.notify(
        title = f"Downloading {(small_title)}",
        message = f"File size : {video.streams.get_highest_resolution().filesize_mb}",
        app_icon = "C:/Users/HP/OneDrive/Desktop/yt-download/pythonlogoIco.ico"
        timeout = 5
    )
    video.register_on_progress_callback(progress)
    high_def_video = video.streams.get_highest_resolution()
    high_def_video.download(output_path=download_path)
    print(f"\n {small_title} downloaded successfully")
    notification.notify(
        title = small_title,
        message = f"Download complete \n {download_path}",
        app_icon = "C:/Users/HP/OneDrive/Desktop/yt-download/pythonlogoIco.ico"
        timeout = 5
    )
    time.sleep(3)

