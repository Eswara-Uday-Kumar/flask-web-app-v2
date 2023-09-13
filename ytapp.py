from yt_downloader import video_download
from flask import Flask, render_template, jsonify, request
from pytube import YouTube

ytapp = Flask(__name__)


@ytapp.route("/", methods=['GET'])
def Home():
    return render_template('index.html')
    

@ytapp.route("/download", methods = ["POST"])
def download():
    if request.method == 'POST':
        option_res = ["Low", "Medium480", "Medium720", "High"]
        video_url = request.form['yturl']
        selected_val = int(request.form['resolution'])
        selected_res = option_res[selected_val]
        downloaded_res, title, available_res = video_download(video_url, selected_res)
        return render_template('result.html', url = video_url, resolution = downloaded_res, title = title, available_res = available_res)



if __name__ == "__main__":
    ytapp.run(debug=True)