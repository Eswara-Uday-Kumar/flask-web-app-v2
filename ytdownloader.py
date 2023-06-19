
from pytube import YouTube

def get_filename():
    filename = yd.default_filename
    names = filename.split(" ")
    lst = [name for name in names if name.isalpha()]
    title =  '_'.join(lst)+'.mp4'
    return title


yt = YouTube('https://www.youtube.com/watch?v=ux1UULoflFk')
        #     on_progress_callback=Stream.on_progress,
        #on_complete_callback=Stream.on_complete)

print(yt.title)

print(yt.views)

yd = yt.streams.get_by_resolution('360p')

filename = get_filename()

print(yd.download('E:\BlogPrograms', filename))

print(yd.filesize_mb, "mb")