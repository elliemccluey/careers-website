from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
  {
  'id': 1,
  'title': 'Data Analyst',
  'location': 'New York, NY, USA',
  'salary': '$25/hr'
  },
  {
  'id': 2,
  'title': 'Data Scientist',
  'location': 'Philadelphia, PA, USA',
  'salary': '$28/hr'
  },
  {
  'id': 3,
  'title': 'Frontend Engineer',
  'location': 'Remote',
  'salary': '$30/hr'
  },
  {
  'id': 1,
  'title': 'Backend Engineer',
  'location': 'San Francisco, CA, USA',
  'salary': '$28/hr'
  }
]

@app.route("/")
def hello_world():
  return render_template('home.html', 
                        jobs=JOBS,
                        company_name='AXLE')

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)