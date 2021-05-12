from pytube import YouTube, streams
from pytube.request import stream

class VideoDownloder():
    link = float(input("Enter the url here:"))
    video = YouTube(link)
    stream = video.streams.get_highest_resolution()
    stream.download()