INSERT INTO jobs (title, location) VALUES ('Data Analyst', 'Bangalore, India');

select * from careersv2.jobs;

UPDATE `careersv2`.`jobs` SET `responsibilities` = 'Design and develop a cloud based backend
Participate and produce a scalable cloud based backend system
Design and develop REST based APIs
Interact with customer directly and with other stakeholders in the organization', `requirements` = 'Hands on experience with building a web backend in Java or Golang
Knowledge of designing and building REST APIs
Proven experience in building a scalable and resilient backend
Good understanding of database schemas and using both relational (SQL) and noSQL based data stores
Strong analytical and debugging skills' WHERE (`id` = '4');