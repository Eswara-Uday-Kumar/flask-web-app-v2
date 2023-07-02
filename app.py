
from flask import Flask, render_template, jsonify
from database import load_jobs_from_db, load_job_from_db

app = Flask(__name__)


@app.route("/")
def hello_world():
    jobs = load_jobs_from_db()
    return render_template('home.html', jobs=jobs)


@app.route("/api/job/<id>")
def show_job(id):
    job = load_job_from_db(id)
    return jsonify(job)


@app.route("/job/<id>")
def return_job(id):
    job = load_job_from_db(id)
    if not job:
        return "Page Not Found", 404 
    return render_template('jobpage.html', job=job)


@app.route("/api/jobs")
def list_jobs():
    return jsonify(load_jobs_from_db())


if __name__ == "__main__":
    app.run(debug = True)