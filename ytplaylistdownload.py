from pytube import Playlist
from pytube.exceptions import VideoUnavailable
from sys import argv
from plyer import notification
import time

#Function for progress bar in command prompt
def progress(streams, chunk: bytes, bytes_remaining: int):
    contentsize = high_def_video.filesize
    size = contentsize - bytes_remaining

    print('\r' + '[Download progress]:[%s%s]%.2f%%;' % (
    '█' * int(size*20/contentsize), ' '*(20-int(size*20/contentsize)), float(size/contentsize*100)), end='')

#link passed as arguement in command line
link = argv[1]

#setting download path
download_path = "C:/Users/HP/Downloads"

#creating object of playlist class
p = Playlist(link)

#Notifing user
print(f"Title : {p.title}")
notification.notify(
        title = f"Downloading {(p.title)}",
        message = f"{len(p)} videos",
        app_icon = "pythonlogoIco.ico",
        timeout = 5
    )

time.sleep(3)

#Iterating over each video in playlist
for video in p.videos:

    #Slicing video title into small title of length 50 for notification
    small_title = (video.title)[:50] if (len(video.title)>50) else video.title

    print(f"Downloading {video.title}")

    #Calling progress function
    video.register_on_progress_callback(progress)

    try:

        #Getting highest resolution of video
        high_def_video = video.streams.get_highest_resolution()
    
    except VideoUnavailable:
        print(f"{video.title} unavailable ......... skipping ")

    else:

        #Downloading the video
        high_def_video.download(output_path=download_path)

        #Notifing user
        print(f"\n {video.title} downloaded successfully")
        notification.notify(
            title = small_title,
            message = f"Download complete \n {download_path}",
            app_icon = "pythonlogoIco.ico",
            timeout = 5
        )

        #Pause for 3 seconds
        time.sleep(3)

