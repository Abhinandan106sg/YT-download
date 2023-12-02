from pytube import YouTube
from sys import argv
from plyer import notification

#link passed as arguement in command line
link = argv[1]

#setting download path
download_path = "C:/Users/HP/Downloads"

#Function for progress bar in command prompt
def progress(streams, chunk: bytes, bytes_remaining: int):
    contentsize = video.filesize
    size = contentsize - bytes_remaining

    print('\r' + '[Download progress]:[%s%s]%.2f%%;' % (
    '█' * int(size*20/contentsize), ' '*(20-int(size*20/contentsize)), float(size/contentsize*100)), end='')
    
try:
    
    #creating object of YouTube class
    yt=YouTube(link,on_progress_callback=progress)

    #Calculating file size
    File_size=yt.streams.get_highest_resolution().filesize_mb

    #Notifing user
    notification.notify(
        title = f"Downloading {yt.title}",
        message = f"File size : {File_size}",
        app_icon = "C:/Users/HP/OneDrive/Desktop/yt-download/pythonlogoIco.ico"
    )

    #Getting highest resolution of video
    video=yt.streams.get_highest_resolution();

    #Downloading the video
    video.download(output_path=download_path)

    #Notifing user
    notification.notify(
        title = yt.title,
        message = f"Download complete \n {download_path}",
        app_icon = "C:/Users/HP/OneDrive/Desktop/yt-download/pythonlogoIco.ico"
    )
    
except Exception as e:
    print(f"An error occured : {e}")
