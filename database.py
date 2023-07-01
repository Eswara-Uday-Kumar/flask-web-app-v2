
from sqlalchemy import create_engine, text

connector_str = "mysql+pymysql://g5qu6m9h6kis6ocnpiy1:pscale_pw_LQR8kpHj5yXDGe4hmgBibnwSTV0i9R9kXlepqmFCpzW@aws.connect.psdb.cloud/careersv2?charset=utf8mb4"

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