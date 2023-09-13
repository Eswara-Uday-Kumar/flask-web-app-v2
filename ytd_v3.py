from pytube import YouTube

yt = YouTube('https://www.youtube.com/watch?v=ux1UULoflFk')

#print(yt.title)

ys = yt.streams.filter(file_extension="mp4", type="video", adaptive="True")
#print(type(ys))
for i in ys:
    print(i.resolution)
#ys.download()