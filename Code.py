''' Author- Pranshu Vashisht'''

from pytube import YouTube
print("--------------------------------x--------------------------------")
print("YouTube Video Downloader")
print("--------------------------------x--------------------------------")
print("Download YouTube videos in High Quality!")
print("--------------------------------x--------------------------------")
link= input("Enter your link here: ")
yt = YouTube(link)
yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')[-1].download()
print("Task Performed!")
