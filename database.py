from sqlalchemy import create_engine, text
import os

my_secret = os.environ['DB_CONNECTION_STRING']
db_connection_string = my_secret

engine = create_engine(db_connection_string,
              connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem"
                }
              })

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
  
    jobs = []
    for row in result:
      jobs.append(row._mapping)
  return jobs