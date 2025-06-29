-- script that creates a database and table
CREATE DATABASE hbtn_0d_usa;
CREATE TABLE states (
    id INT UNIQUE, AUTO_INCREMENT PRIMARY KEY NOT NULL,
    name VARCHAR(256) NOT NULL
);