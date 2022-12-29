import os
import re
from pytube import YouTube
from time import perf_counter

def downloadYtMp4(ytURL, dlDir=os.getcwd()):
    yt = YouTube(ytURL)
    hqMp4 = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')[-1].download()
    m = re.search("- (\d\d\dp) -", str(hqMp4))
    quality = m.group(1)
    video = yt.get('mp4', quality)
    #download and save video to specified dir
    video.download(dlDir)

downloadYtMp4("https://www.youtube.com/watch?v=hwNWx1GTSKo")
