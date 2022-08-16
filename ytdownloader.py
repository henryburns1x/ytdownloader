
from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)

print("Views", yt.views)
print("Title ", yt.title)
yd = yt.streams.get_highest_resolution()

#input link
yd.download('/Users/henryburns/Desktop/YoutubeVideos')

#Type in commoand "python3 ytdownloader "Link"