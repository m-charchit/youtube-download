from pytube import YouTube

def downloadVideo(link):
	yt = YouTube(link)
	video = yt.streams.filter(res="720p").first()
	stream = video.download(filename="video.mp4")
