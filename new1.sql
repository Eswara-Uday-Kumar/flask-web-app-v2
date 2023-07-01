INSERT INTO jobs (title, location) VALUES ('Data Analyst', 'Bangalore, India');

select * from careersv2.jobs;

UPDATE `careersv2`.`jobs` SET `responsibilities` = 'Translate designs and wireframes into high quality JS, CSS, HTML templates
Design, build, and maintain high performance, reusable, and reliable UI components and products
Ensure the best possible performance, quality, and optimize for maximum speed and scalability
Identify and correct bottlenecks and fix bugs.
Help maintain code quality, organization, and automatization', `requirements` = 'Strong knowledge of programming skills in JS, CSS and HTML
Familiarity with responsive and adaptive web design, and good knowledge of JS libraries such as JQuery
Strong knowledge of about atleast one of the JS frameworks (e.g. VueJS, Angular JS, NodeJS, ReactJS)
Experience with building websites, ability to handle cross browser compatibility issues' WHERE (`id` = '3');