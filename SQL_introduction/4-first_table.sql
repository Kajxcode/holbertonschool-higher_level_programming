-- script that creates a table
CREATE DATABASE IF NOT EXISTS hbtn_test_db_4;
USE hbtn_test_db_4;

CREATE TABLE first_table (
    id INT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
