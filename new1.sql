INSERT INTO jobs (title, location) VALUES ('Data Analyst', 'Bangalore, India');

select * from careersv2.applications;

UPDATE `careersv2`.`jobs` SET `responsibilities` = 'Design and develop a cloud based backend
Participate and produce a scalable cloud based backend system
Design and develop REST based APIs
Interact with customer directly and with other stakeholders in the organization', `requirements` = 'Hands on experience with building a web backend in Java or Golang
Knowledge of designing and building REST APIs
Proven experience in building a scalable and resilient backend
Good understanding of database schemas and using both relational (SQL) and noSQL based data stores
Strong analytical and debugging skills' WHERE (`id` = '4');


CREATE TABLE applications (
  id INT NOT NULL AUTO_INCREMENT,
  job_id INT NOT NULL,
  full_name VARCHAR(250) NOT NULL,
  email VARCHAR(250) NOT NULL,
  linkedin_url VARCHAR(500),
  education VARCHAR(2000),
  work_experience VARCHAR(2000),
  resume_url VARCHAR(500),
  PRIMARY KEY (id)
);

show tables;