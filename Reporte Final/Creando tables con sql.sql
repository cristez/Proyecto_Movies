select * from ventas order by show_id
CREATE SCHEMA IF NOT EXISTS `my_moviestore` DEFAULT CHARACTER SET latin1 ;
USE `my_moviestore` ;


CREATE TABLE IF NOT EXISTS `categories` (
  `id_Category` INT NOT NULL,
  `name` TEXT CHARACTER SET 'utf8' COLLATE 'utf8_roman_ci' NULL DEFAULT NULL,
  PRIMARY KEY (`id_category`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table  `countries`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS  `countries` (
  `id_country` INT NOT NULL,
  `name` TEXT CHARACTER SET 'utf8' COLLATE 'utf8_roman_ci' NULL DEFAULT NULL,
  PRIMARY KEY (`id_country`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table  `custumer`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS  `custumer` (
  `Id_Client` INT NOT NULL AUTO_INCREMENT,
  `Name` TEXT CHARACTER SET 'utf8' COLLATE 'utf8_roman_ci' NULL DEFAULT NULL,
  `Gender` TEXT CHARACTER SET 'utf8' COLLATE 'utf8_roman_ci' NULL DEFAULT NULL,
  `Custumer type` TEXT CHARACTER SET 'utf8' COLLATE 'utf8_roman_ci' NULL DEFAULT NULL,
  PRIMARY KEY (`Id_Client`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table  `movie_type`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS  `movie_type` (
  `id_type` INT NOT NULL,
  `name` TEXT CHARACTER SET 'utf8' COLLATE 'utf8_roman_ci' NULL DEFAULT NULL,
  PRIMARY KEY (`id_type`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table  `movies`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS  `movies` (
  
  `show_id` INT NOT NULL,
  `type` INT NULL DEFAULT NULL,
  `title` TEXT CHARACTER SET 'utf8' COLLATE 'utf8_roman_ci' NULL DEFAULT NULL,
  `director` TEXT CHARACTER SET 'utf8' COLLATE 'utf8_roman_ci' NULL DEFAULT NULL,
  `cast` TEXT CHARACTER SET 'utf8' COLLATE 'utf8_roman_ci' NULL DEFAULT NULL,
  `country` INT NULL DEFAULT NULL,
  `date_added` DATE NULL DEFAULT NULL,
  `release_year` BIGINT(20) NULL DEFAULT NULL,
  `rating` TEXT CHARACTER SET 'utf8' COLLATE 'utf8_roman_ci' NULL DEFAULT NULL,
  `duration` TEXT CHARACTER SET 'utf8' COLLATE 'utf8_roman_ci' NULL DEFAULT NULL,
  `listed_in` INT NULL DEFAULT NULL,
  `description` TEXT CHARACTER SET 'utf8' COLLATE 'utf8_roman_ci' NULL DEFAULT NULL,
  `price` BIGINT(20) NULL DEFAULT NULL,
  PRIMARY KEY (`show_id`))
  
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table  `payment_methods`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS  `payment_methods` (
  `id_payment` INT NOT NULL,
  `name` TEXT CHARACTER SET 'utf8' COLLATE 'utf8_roman_ci' NULL DEFAULT NULL,
  PRIMARY KEY (`id_payment`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table  `Ventas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS  `Ventas` (
  `id_ventas` INT NOT NULL AUTO_INCREMENT,
  `movies_show_id` INT NOT NULL,
  `custumer_id_Client` INT NOT NULL,
  `payment_methods_id_payment` INT NOT NULL,
  `total` INT NOT NULL,
  `fecha` DATE NOT NULL,
  PRIMARY KEY (`id_ventas`))
ENGINE = InnoDB;





