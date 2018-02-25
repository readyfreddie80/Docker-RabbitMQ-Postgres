CREATE DATABASE my_db;
CREATE USER ninja;
GRANT ALL ON DATABASE my_db TO ninja;

\connect my_db

CREATE TABLE IF NOT EXISTS strings(
	id serial PRIMARY KEY,
	data varchar(500)
);



