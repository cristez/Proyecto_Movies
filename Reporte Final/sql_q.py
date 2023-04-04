DDL_QUERY =  '''

CREATE TABLE categories (
  Id_Category SERIAL PRIMARY KEY,
  Name TEXT COLLATE "ucs_basic"
);


-- -----------------------------------------------------
-- Table  `countries`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS countries (
  Id_Country INT NOT NULL,
  Name TEXT COLLATE "ucs_basic",
  PRIMARY KEY (Id_Country)
);


-- -----------------------------------------------------
-- Table  `custumer`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS custumer (
  Id_Client SERIAL PRIMARY KEY,
  Name TEXT COLLATE "ucs_basic" DEFAULT NULL,
  Gender TEXT COLLATE "ucs_basic" DEFAULT NULL,
  "Custumer type" TEXT COLLATE "ucs_basic" DEFAULT NULL
);


-- -----------------------------------------------------
-- Table  `movie_type`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS movie_type (
  Id_type INT NOT NULL,
  Name TEXT NULL DEFAULT NULL,
  PRIMARY KEY (Id_type)
);

-- -----------------------------------------------------
-- Table  `movies`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS movies (
  show_id INT NOT NULL,
  type INT NULL DEFAULT NULL,
  title TEXT NULL DEFAULT NULL,
  director TEXT NULL DEFAULT NULL,
  casting TEXT NULL DEFAULT NULL,
  country INT NULL DEFAULT NULL,
  date_added DATE NULL DEFAULT NULL,
  release_year BIGINT NULL DEFAULT NULL,
  rating TEXT NULL DEFAULT NULL,
  duration TEXT NULL DEFAULT NULL,
  listed_in INT NULL DEFAULT NULL,
  description TEXT NULL DEFAULT NULL,
  price BIGINT NULL DEFAULT NULL,
  PRIMARY KEY (show_id),
  CONSTRAINT country_fk FOREIGN KEY (country) REFERENCES countries (id_country) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT listed_in_fk FOREIGN KEY (listed_in) REFERENCES categories (id_category) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT type_fk FOREIGN KEY (type) REFERENCES movie_type (id_type) ON DELETE NO ACTION ON UPDATE NO ACTION
);


-- -----------------------------------------------------
-- Table  `payment_methods`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS payment_methods (
  Id_Payment INT NOT NULL,
  Name TEXT COLLATE "ucs_basic" NULL DEFAULT NULL,
  PRIMARY KEY (Id_Payment)
);

-- -----------------------------------------------------
-- Table  `Ventas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS Ventas (
   Id_ventas SERIAL PRIMARY KEY,
   movies_show_id INT NOT NULL,
   custumer_Id_Client INT NOT NULL,
   payment_methods_Id_Payment INT NOT NULL,
   Total INT NOT NULL,
   Fecha DATE NOT NULL,
   CONSTRAINT fk_Ventas_movies1
      FOREIGN KEY (movies_show_id)
      REFERENCES movies (show_id)
      ON DELETE NO ACTION
      ON UPDATE NO ACTION,
   CONSTRAINT fk_Ventas_custumer1
      FOREIGN KEY (custumer_Id_Client)
      REFERENCES custumer (Id_Client)
      ON DELETE NO ACTION
      ON UPDATE NO ACTION,
   CONSTRAINT fk_Ventas_payment_methods1
      FOREIGN KEY (payment_methods_Id_Payment)
      REFERENCES payment_methods (Id_Payment)
      ON DELETE NO ACTION
      ON UPDATE NO ACTION
);


 '''