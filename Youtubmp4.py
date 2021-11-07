import os
from pytube import YouTube
print("Requested videos will be downloaded to a target dropoff location under the orginial video title.")
dropoff = input("Targeted dropoff: ")
requested = input("Requested video link: ")
print("Video processing...")
YouTube(requested).streams.get_highest_resolution().download(dropoff)
title = YouTube(requested).title
if os.path.exists(dropoff+"\\"+title+".mp4"):
    print("Video: "+title+".mp4"+" is now finshed downloading!")