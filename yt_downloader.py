
from pytube import YouTube

def get_quality(yt):

    video_stream = yt.streams.filter(file_extension="mp4", type="video", adaptive="True")
    video_res = []
    for res in video_stream:
        video_res.append(res.resolution)
    print(video_res)
    return video_res


def video_download(url, selected_res):

    option_res = {'360p': "Low", '480p':"Medium480", '720p':"Medium720", '1080p':"High"}
    yt = YouTube(url)
    title = yt.title
    video_res = get_quality(yt)
    res_used = ""
    res_available = False
    print(selected_res)
    for res, option in option_res.items():
        if res in video_res:
            if selected_res == option:
                res_used = res
                res_available = True
                break
    if res_used == "":
        res_used = "360p"
    yd = yt.streams.get_by_resolution(res_used)
    yd.download()
                
    return res_used, title, res_available

