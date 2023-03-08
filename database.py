from sqlalchemy import create_engine, text
import os
from flask import render_template

my_secret = os.environ['DB_CONNECTION_STRING']
db_connection_string = my_secret

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))

    jobs = []
    for row in result:
      jobs.append(row._mapping)
  return jobs


#query = "select * from jobs where id = " + '10'

#with engine.connect() as conn:
#result = conn.execute(text(query))
#job = []

#for row in result:
#job.append(row._mapping)

#if not job: #Se estiver vazio
#print(None)
#else:
#print(job)


def load_job_from_db(id):
  query = "select * from jobs where id = " + id

  with engine.connect() as conn:
    result = conn.execute(text(query))

  job = []
  for row in result:
    job.append(row._mapping)
  if not job:  #Se estiver vazio
    return 'None'
  else:
    return job


def add_application_to_db(job_id, data):
  with engine.connect() as conn:
    '''
    query = text("INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)")
    '''
    query = text("INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES ("+job_id+", '"+data['full_name']+"', '"+data['email']+"', '"+data['linkedin_url']+"', '"+ data['education']+"', '"+ data['work_experience']+"', '"+data['resumelink']+"')")
    conn.execute(query)
                 
'''                 
                 :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)")
    conn.execute(query,
         1,
         full_name = data['full_name'],
         email = data['email'],
         linkedin = data['linkedin_url'],
         education = data['education'],
         work_experience = data['work_experience'],
         resume_url = data['resumelink'])
'''
    