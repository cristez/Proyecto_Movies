CREATE_DW =  '''

CREATE TABLE IF NOT EXISTS custumer (
  id_client int PRIMARY KEY,
  name varchar(50) DEFAULT NULL,
  gender varchar(50)  DEFAULT NULL,
  custumer_type varchar(50) DEFAULT NULL
);

CREATE TABLE IF NOT EXISTS movies (
  id_movies INT PRIMARY KEY,
  show_type TEXT NULL DEFAULT NULL,
  title TEXT NULL DEFAULT NULL,
  director TEXT NULL DEFAULT NULL,
  casting TEXT NULL DEFAULT NULL,
  country_name TEXT NULL DEFAULT NULL,
  date_added DATE NULL DEFAULT NULL,
  release_year BIGINT NULL DEFAULT NULL,
  rating TEXT NULL DEFAULT NULL,
  duration TEXT NULL DEFAULT NULL,
  listed_in TEXT NULL DEFAULT NULL,
  description TEXT NULL DEFAULT NULL,
  price INT NULL DEFAULT NULL
);

CREATE TABLE IF NOT EXISTS payment_methods (
  id_payment INT PRIMARY KEY,
  name varchar(50)
);

CREATE TABLE IF NOT EXISTS fact_table (
   id_fact INT PRIMARY KEY,
   id_movies INT NOT NULL,
   id_client INT NOT NULL,
   id_payment INT NOT NULL,
   total INT,
   id_fecha DATE,
   
 CONSTRAINT fk_fact_dim_movies
	FOREIGN KEY (id_movies)
	REFERENCES movies(id_movies),
			
 CONSTRAINT fk_fact_dim_custumer
	FOREIGN KEY (id_client)
	REFERENCES custumer(id_client),
			
 CONSTRAINT fk_fact_dim_payment_methods
	FOREIGN KEY (id_payment)
	REFERENCES payment_methods(id_payment)

); '''