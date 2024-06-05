from pytube import YouTube
from sys import argv

if len(argv) < 2:
    print("Usage: python ytDownloader.py <YouTube URL>")
    exit(1)

link = argv[1]
yt = YouTube(link)

print("Title:", yt.title)
print("Views:", yt.views)
print("Length:", yt.length, "seconds")
print("Rating:", yt.rating)

video = yt.streams.get_highest_resolution()

video.download("/Users/annietran/Desktop")