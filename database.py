
from sqlalchemy import create_engine, text
import os

connector_str = os.environ["DB_PlanetScale_CareerDB_ConnectionString"]

engine = create_engine(connector_str, 
                       connect_args= {
                           "ssl":{
                               "ssl_ca": "/etc/ssl/cert.pem"
                           }
                       })

def load_jobs_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
    
        jobs = []
        for row in result.all():
            jobs.append(row._asdict())
        return jobs
    