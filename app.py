from flask import Flask, render_template, jsonify
from database import load_jobs_from_db, load_job_from_db

app = Flask(__name__)

@app.route("/")
def hello_jovian():
  JOBS = load_jobs_from_db()
  return render_template("home.html", jobs=JOBS, company_name='Jovian')


@app.route("/api/jobs")
def list_jobs():
  JOBS = load_jobs_from_db()
  jobs_dict = []
  for job in JOBS:
    jobs_dict.append(dict(job))
  return (jobs_dict)

@app.route("/job/<id>")
def show_job(id):
  
  job = load_job_from_db(id)
  if not job: #Nenhum linha foi retornada
    return "Not found", 404
  else:
    job_dict = []
    for job_details in job:
      job_dict.append(dict(job_details))
      
    return render_template("jobpage.html", job=job_details)
    #return (job_dict)
    
  
if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
  

