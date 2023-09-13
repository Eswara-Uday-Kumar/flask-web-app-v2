
from pytube import YouTube

p = "240p"

yt = YouTube('https://www.youtube.com/watch?v=ux1UULoflFk')

if p == '240p':
    yd = yt.streams.get_by_resolution("360p")
    yd.download(filename="untitled1", filename_prefix="mp4")

#ytStream = yt.streams.filter(file_extension='mp4').get_by_itag(133)
#ytStream.download()
#mp4stream = ytStream.filter(file_extension='mp4')
#res_stream = mp4stream.filter(resolution=resolution)

#res_stream.download('E:/blog')
