-- script that creates a database and table
CREATE DATABASE hbtn_0d_usa;
CREATE TABLE states (
    id INT NOT NULL AUTO_INCREMENT UNIQUE,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);