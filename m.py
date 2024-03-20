from pytube import YouTube
DOWNLOAD_PATH = "C:/Users/r/3D Objects/youtube downloader/videos/new" #to_do
#List of links of the video to be downloaded
video_link=["https://www.youtube.com/watch?v=hwNWx1GTSKo"]
for i in video_link:
    try:
        yt = YouTube(i)
    except:
        #to handle exception
        print("Connection Error")
    mp4files = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')[-1].download()
    d_video = yt.streams.get(mp4files[-1].extension,mp4files[-1].resolution)
    try:
        # downloading the video
        d_video.download(DOWNLOAD_PATH)
    except:
        print("There is some Error!")
print('Videos Download Successfully!')
