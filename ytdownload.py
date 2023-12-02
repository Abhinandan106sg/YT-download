from pytube import YouTube
from sys import argv
from plyer import notification

link = argv[1]

def alert(video_title,video_size):
    notification.notify(
        title = f"Downloading {video_title}",
        messege = f"File size : {video_size} mb "
    )


def progress(streams, chunk: bytes, bytes_remaining: int):
    contentsize = video.filesize
    size = contentsize - bytes_remaining

    print('\r' + '[Download progress]:[%s%s]%.2f%%;' % (
    '█' * int(size*20/contentsize), ' '*(20-int(size*20/contentsize)), float(size/contentsize*100)), end='')
    
try:
    notification.notify(
        title = "notification",
        message = "this is a messege"
    )
    yt=YouTube(link,on_progress_callback=progress)

    File_size=yt.streams.get_highest_resolution().filesize_mb
    print(type(File_size))
    # alert(yt.title,str(File_size))

    video=yt.streams.get_highest_resolution();
    video.download(output_path="C:/Users/HP/Downloads")

    # alert("Download Complete",yt.title)
    
except Exception as e:
    print(f"An error occured : {e}")
