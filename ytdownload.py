from pytube import YouTube
from sys import argv

link = argv[1]

def progress(streams, chunk: bytes, bytes_remaining: int):
    contentsize = video.filesize
    size = contentsize - bytes_remaining

    print('\r' + '[Download progress]:[%s%s]%.2f%%;' % (
    '█' * int(size*20/contentsize), ' '*(20-int(size*20/contentsize)), float(size/contentsize*100)), end='')
    
try:
    yt=YouTube(link,on_progress_callback=progress)

    print("Title:",yt.title)
    File_size=yt.streams.get_highest_resolution().filesize_mb
    print(f"File size : {File_size} mb")

    video=yt.streams.get_highest_resolution();
    video.download(output_path="C:/Users/HP/Downloads")

    print("\n DOWNLOAD COMPLETE")
    
except Exception as e:
    print(f"An error occured : {e}")
