import os
from pytube import YouTube
dropoff = os.path.dirname(__file__)
print("Requested videos will be downloaded to the working folder ("+dropoff+") under the orginial video title.")
requested = input("Requested video link: ")
print("Video processing...")
YouTube(requested).streams.get_highest_resolution().download(dropoff)
title = YouTube(requested).title
if os.path.exists(dropoff+"\\"+title+".mp4"):
    print("Video: "+title+".mp4"+" is now finshed downloading!")