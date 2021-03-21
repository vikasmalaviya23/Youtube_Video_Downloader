import pafy

# enter the url of the video you want to download
url = "https://www.youtube.com/watch?v=iIkJrwVUl1c&t=1s"
video = pafy.new(url)

#best resolution in required format
best = video.getbest(preftype="mp4")

# if you want to specify a particular path for the video
filename = best.download(filepath="E:\movie And Video")