from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
    'id': 1,
    'role': 'Data Analyst',
    'location': 'Bengaluru',
    'Salary': '10k'
}, {
    'id': 2,
    'role': 'Data Scientist',
    'location': 'Noida',
    'Salary': '12k'
}, {
    'id': 3,
    'role': 'Backend Developer',
    'location': 'Hyderabad',
    'Salary': '9k'
}]


@app.route('/')
def hello_world():
    return render_template('home.html', jobs=JOBS, name="Sudhakar")


@app.route('/api/jobs')
def jobs():
    return jsonify(JOBS)


if __name__ == "__main__":
    app.run(debug=True)
