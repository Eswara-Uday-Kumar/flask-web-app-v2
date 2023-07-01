
from flask import Flask, render_template, jsonify

app = Flask(__name__)


JOBS = [
    {
        "id": 1,
        'title': 'Data Analyst',
        'Location': 'Bangalore, India',
        'Salary': 'Rs. 10,00,000'
    },
    {
        "id": 2,
        'title': 'Data Scientist',
        'Location': 'Chennai, India',
        'Salary': 'Rs. 15,00,000'
    },
    {
        "id": 3,
        'title': 'Frontend Engineer',
        'Location': 'Remote',
        'Salary': 'Rs. 12,00,000'
    },
    {
        "id": 4,
        'title': 'Backend Engineer',
        'Location': 'San Fransico, USA',
        'Salary': '$. 120,000'
    }
]


@app.route("/")
def hello_world():
    return render_template('home.html', jobs=JOBS)


@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)


if __name__ == "__main__":
    app.run(debug = True)