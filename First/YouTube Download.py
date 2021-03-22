import pytube
url = "https://youtu.be/9a6UaCBEV6o"

video = pytube.YouTube(url)
youtube = video.streams.first()
youtube.download(r'D:\Anime')