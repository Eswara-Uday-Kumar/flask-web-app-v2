
from flask import Flask, render_template, jsonify, request
from pytube import YouTube

ytapp = Flask(__name__)


@ytapp.route("/", methods=['GET'])
def Home():
    return render_template('index.html')


@ytapp.route("/download", methods = ["POST"])
def download():
    if request.method == 'POST':
        result = request.form
        video_url = request.form['yturl']
        resolution = request.form['resolution']
        def video_download(url):
            video = YouTube(url)
            yd = video.streams.get_by_resolution(resolution)
            yd.download()

        video_download(video_url)
        return render_template("result.html", result=result)


if __name__ == "__main__":
    ytapp.run(debug=True)