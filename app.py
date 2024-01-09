from flask import Flask, jsonify, render_template

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Benguluru, India',
    'salary': 'Rs. 1,000,000'
  },
  {
    'id': 2,
    'title': 'Data Scintist',
    'location': 'Delhi, India',
    'salary': 'Rs. 1,500,000'
  },
  {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'remote',
    'salary': 'Rs. 1,200,000'
  },
  {
    'id': 4,
    'title': 'backend Engeneer ',
    'location': 'San Franc, USA',
    'salary': '$120,000'
  },
]

@app.route("/")
def hello_world():
    return render_template('home.html', jobs=JOBS, company_name='Jovian')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)