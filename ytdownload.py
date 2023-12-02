from pytube import YouTube
from sys import argv
from plyer import notification

link = argv[1]

download_path = "C:/Users/HP/Downloads"


def progress(streams, chunk: bytes, bytes_remaining: int):
    contentsize = video.filesize
    size = contentsize - bytes_remaining

    print('\r' + '[Download progress]:[%s%s]%.2f%%;' % (
    '█' * int(size*20/contentsize), ' '*(20-int(size*20/contentsize)), float(size/contentsize*100)), end='')
    
try:
    
    yt=YouTube(link,on_progress_callback=progress)

    File_size=yt.streams.get_highest_resolution().filesize_mb
    notification.notify(
        title = f"Downloading {yt.title}",
        message = f"File size : {File_size}"
    )

    video=yt.streams.get_highest_resolution();
    video.download(output_path=download_path)

    notification.notify(
        title = yt.title,
        message = f"Download complete \n {download_path}"
    )
    
except Exception as e:
    print(f"An error occured : {e}")
