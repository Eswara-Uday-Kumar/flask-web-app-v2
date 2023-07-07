
from flask import Flask, render_template, jsonify, request
from pytube import YouTube

ytapp = Flask(__name__)


@ytapp.route("/", methods=['GET'])
def Home():
    return render_template('index.html')


@ytapp.route("/download", methods = ["POST"])
def download():
    resolutions = ['240p', '360p', '480p', '720p', '1080p']
    if request.method == 'POST':
        result = request.form
        video_url = request.form['yturl']
        resolution_cnt = request.form['resolution']
        resolution = resolutions[int(resolution_cnt)]
        def video_download(url):
            yt = YouTube(url)
            yd = yt.streams.get_by_resolution(resolution)
            yd.download()

        video_download(video_url)
        return render_template('result.html', result=result)



if __name__ == "__main__":
    ytapp.run(debug=True)